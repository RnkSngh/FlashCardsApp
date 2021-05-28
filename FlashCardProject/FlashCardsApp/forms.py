from .models import Card
from django.forms import ModelForm

class CardForm(ModelForm):
    class Meta:
        model = Card
        fields = ['word', 'definition']