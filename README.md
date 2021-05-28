# FlashCards
A barebones flashcard app in Django that uses spaced repetition for vocabulary practice. Each word is put in one of 12 bins that represent increasing levels of mastery. 
When first added, a word goes in bin 0. During practice, the word is shown, and you can turn over the word to see if you got the definition right or not (and mark the corresponding option of correct/incorrect). When marked correct, a card is moved to a higher bin. If marked incorrect, the word goes back to the 1st bin (bin 0 is only for cards not yet shown). The higher a word's bin is, the longer time it will be before the card is shown during practice. Words gotten incorrect more than 10 times will be put in bin 12, and will not be shown again. 


# Quickstart
1. Create a virtual env in the root directory using ```python -m venv venv```. Start the venv using ```venv\Scripts\Activate``` (if on windows), and install requirements using ```pip install -r requirements.txt```
2. From the FlashCardProject/ folder, run ```python manage.py makemigrations```
3. From the same folder run ```python manage.py migrate``` to create the cards database
4. From the same folder start the server using ```python manage.py runserver```

# Using the App
1. Register a user account at http://localhost:8000/register. 
2. Login at http://localhost:8000/login
3. Add cards and definitions that you want to study at http://localhost:8000/app/addCard
4. Practice learning your cards at http://localhost:8000/app/practice
The status of all added definitions can be viewed at http://localhost:8000/app/getAllCards.

# Backend Structure
There are a few backend endpoints used in constructing the front-end that are defined in ```FlashCardsApp/FlashCardProject/FlashCardsApp/views.py```: 
* ```get_all_cards``` returns info for all cards
* ```add_card``` adds a card and a definition for the logged in user. Note: each word must be unique. (Basic Auth Required) 
* ```get_word``` gets the next word for the logged in user. To find which cards are due for showing, the current timestamp is compared to the showAT field for each word. (Basic Auth Required) 
* ```mark_correct``` mark a word as correct/incorrect. This updates the wordBin and showAT fields for a particular word using the spaced repetition model. (Basic Auth Required) 
