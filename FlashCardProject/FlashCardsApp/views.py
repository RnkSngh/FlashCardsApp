from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from FlashCardsApp.models import Card
from FlashCardsApp.serializers import CardSerializer
from rest_framework import status
from datetime import datetime, timedelta
from django.contrib.auth.decorators import login_required
from .Variables import bin_dict

# Create your views here.
def practice(request):
    return render(request, "FlashCardsApp/practice.html")

def addCardView(request):
    return render(request, "FlashCardsApp/addCard.html")

def getCardsView(request):
    return render(request, "FlashCardsApp/getCards.html")

@api_view(['GET'])
def get_all_cards(request):
    if request.method == 'GET':
        user_cards = Card.objects.filter(owner=request.user)
        serializer = CardSerializer(user_cards, many=True)
        return Response(serializer.data)


@api_view(['POST'])
def add_card(request):
    if request.method == 'POST':
        #send 400 error if word already exists
        if Card.objects.filter(owner=request.user).filter(word=request.data.get('word')):
            raise ValidationError("Word Already Exists")
        data = {
            'word': request.data.get('word'), 
            'definition': request.data.get('definition'), 
            'wordBin':0,
            'lastShowed':datetime.utcnow(),
            'showAt':datetime.max-timedelta(hours=5),   #save as datetime.max when first initializing time                     
            'owner': request.user.pk,
            "incorrect":0}
        serializer = CardSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_word(request):
    if request.method == 'GET':
        user_cards = Card.objects.filter(owner=request.user)
        #get cards which are not in bin 0 or -1 and which are due for review
        active_cards = user_cards.filter(wordBin__range=[1,10]).order_by("wordBin")
        due_cards = active_cards.filter(showAt__lte=datetime.utcnow())
        if len(due_cards)>0:
            next_card = due_cards.first()
        else: #if no active cards, take a new unseen card from bin 0 if there are any
            new_cards = user_cards.filter(wordBin = 0)
            if len(new_cards)>0:
                next_card = new_cards.first()
            else: #if no new cards either, check if there are cards remaining in other bins
                if len(active_cards)>0:
                    return Response("Come back later")
                else:
                    return Response("No Cards Remaining - All Done!")

        serializer = CardSerializer(next_card)
        return Response(serializer.data)

@api_view(['POST'])
def mark_correct(request):
    if request.method == 'POST':
        user_cards = Card.objects.filter(owner=request.user.pk)
        word_card = user_cards.get(word=request.data.get('word'))
        if request.data.get('correct'):
            if word_card.wordBin<11:
                new_bin = word_card.wordBin + 1
        else: #mark incorrect
            incorrect = word_card.incorrect + 1
            if incorrect>=10: #move card to bin -1 if incorrect more than 10 times. 
                word_card.incorrect = 10
                new_bin=-1
            else:
                word_card.incorrect = incorrect
                if word_card.wordBin==0 or word_card.wordBin==1:
                    new_bin = 1
                else:
                    new_bin = word_card.wordBin - 1
        t_delta = timedelta(seconds=bin_dict[new_bin])
        word_card.wordBin = new_bin
        word_card.showAt = datetime.utcnow() + t_delta
        word_card.lastShowed = datetime.utcnow()
        word_card.save()

        serializer = CardSerializer(word_card)
        return Response(serializer.data)