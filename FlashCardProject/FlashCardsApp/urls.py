from django.urls import path

from . import views

urlpatterns = [
    path('practice', views.practice, name='practice'),
    path('addCard', views.addCardView, name='add'),   
    path('getAllCards', views.getCardsView, name='getCards'),  
    path('api/addNewCard', views.add_card),
    path('api/getCards', views.get_all_cards),
    path('api/getWord', views.get_word),
    path('api/markCorrect', views.mark_correct),
]


