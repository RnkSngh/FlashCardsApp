from rest_framework import serializers
from FlashCardsApp.models import Card
from datetime import datetime, timezone

from django.utils import timezone


class CardSerializer(serializers.ModelSerializer):
    timeRemaining = serializers.SerializerMethodField() # add time remaining field
    class Meta:
        model = Card
        fields = ('word', 'definition', 'lastShowed', 'showAt', 'wordBin', 'owner', 'incorrect', 'timeRemaining')

    def get_timeRemaining(self, obj):
        #NEED TO FIX - ONLY CALCULATES TIME WINDOW
        if obj.wordBin>0 and obj.wordBin<=10:
            try:
                now = timezone.now()
                diff = obj.showAt - now
                diff_seconds = diff.days*86400 + diff.seconds

                if diff_seconds>0:
                    return diff_seconds
                else:
                    return "due"
            except Exception as e:
                print(str(e))
        else:
            return "Not in Stack"
