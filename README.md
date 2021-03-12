# FlashCards
A barebones flashcard app in Django that uses spaced repetition

# Using the App
The app is hosted using an AWS EC2 instance at http://54.148.90.25:8000/. To use the app:
1. Register a user account at http://54.148.90.25:8000/register. 
2. Login at http://54.148.90.25:8000/login
3. Add cards and definitions that you want to study at http://54.148.90.25:8000/app/addCard
4. Practice learning your cards at http://54.148.90.25:8000/app/practice
The status of all added definitions can be viewed at http://54.148.90.25:8000/app/getAllCards.
# Backend Structure
There are a few backend endpoints used in constructing the front-end that are defined in ```FlashCardsApp/FlashCardProject/FlashCardsApp/views.py```: 
* ```get_all_cards``` returns info for all cards
* ```add_card``` adds a card and a definition for the logged in user. Note: each word must be unique. (Basic Auth Required) 
* ```get_word``` gets the next word for the logged in user. To find which cards are due for showing, the current timestamp is compared to the showAT field for each word. (Basic Auth Required) 
* ```mark_correct``` mark a word as correct/incorrect. This updates the wordBin and showAT fields for a particular word using the spaced repetition model. (Basic Auth Required) 
