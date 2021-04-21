# FlashCards
A barebones flashcard app in Django that uses spaced repetition

# Backend Structure
There are a few backend endpoints used in constructing the front-end that are defined in ```FlashCardsApp/FlashCardProject/FlashCardsApp/views.py```: 
* ```get_all_cards``` returns info for all cards
* ```add_card``` adds a card and a definition for the logged in user. Note: each word must be unique. (Basic Auth Required) 
* ```get_word``` gets the next word for the logged in user. To find which cards are due for showing, the current timestamp is compared to the showAT field for each word. (Basic Auth Required) 
* ```mark_correct``` mark a word as correct/incorrect. This updates the wordBin and showAT fields for a particular word using the spaced repetition model. (Basic Auth Required) 
