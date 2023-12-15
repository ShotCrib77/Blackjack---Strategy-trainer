import random
with open("deckofcards.txt", "r", encoding="utf-8") as deck_of_cards:
  deck_cards = [line.strip() for line in deck_of_cards]

CARDS = [item for item in deck_cards if item != ""]

amount_of_decks = 1
# Impliment a way to be able to choose how many decks the shoe of cards will contain.

shoe_of_cards = CARDS * amount_of_decks

deck = {
  "2 spades": {"value": 2, "color": "spades", "image": "2S.png"},
  "3 spades": {"value": 3, "color": "spades", "image": "3S.png"},
  "4 spades": {"value": 4, "color": "spades", "image": "4S.png"},
  "5 spades": {"value": 5, "color": "spades", "image": "5S.png"},
  "6 spades": {"value": 6, "color": "spades", "image": "6S.png"},
  "7 spades": {"value": 7, "color": "spades", "image": "7S.png"},
  "8 spades": {"value": 8, "color": "spades", "image": "8S.png"},
  "9 spades": {"value": 9, "color": "spades", "image": "9S.png"},
  "10 spades": {"value": 10, "color": "spades", "image": "10S.png"},
  "J spades": {"value": 10, "color": "spades", "image": "JS.png"},
  "Q spades": {"value": 10, "color": "spades", "image": "QS.png"},
  "K spades": {"value": 10, "color": "spades", "image": "KS.png"},
  "A spades": {"value": 11, "color": "spades", "image": "AS.png"},
  
  "2 hearts": {"value": 2, "color": "hearts", "image": "2H.png"},
  "3 hearts": {"value": 3, "color": "hearts", "image": "3H.png"},
  "4 hearts": {"value": 4, "color": "hearts", "image": "4H.png"},
  "5 hearts": {"value": 5, "color": "hearts", "image": "5H.png"},
  "6 hearts": {"value": 6, "color": "hearts", "image": "6H.png"},
  "7 hearts": {"value": 7, "color": "hearts", "image": "7H.png"},
  "8 hearts": {"value": 8, "color": "hearts", "image": "8H.png"},
  "9 hearts": {"value": 9, "color": "hearts", "image": "9H.png"},
  "10 hearts": {"value": 10, "color": "hearts", "image": "10H.png"},
  "J hearts": {"value": 10, "color": "hearts", "image": "JH.png"},
  "Q hearts": {"value": 10, "color": "hearts", "image": "QH.png"},
  "K hearts": {"value": 10, "color": "hearts", "image": "KH.png"},
  "A hearts": {"value": 11, "color": "hearts", "image": "AH.png"},
  
  "2 diamonds": {"value": 2, "color": "diamonds", "image": "2D.png"},
  "3 diamonds": {"value": 3, "color": "diamonds", "image": "3D.png"},
  "4 diamonds": {"value": 4, "color": "diamonds", "image": "4D.png"},
  "5 diamonds": {"value": 5, "color": "diamonds", "image": "5D.png"},
  "6 diamonds": {"value": 6, "color": "diamonds", "image": "6D.png"},
  "7 diamonds": {"value": 7, "color": "diamonds", "image": "7D.png"},
  "8 diamonds": {"value": 8, "color": "diamonds", "image": "8D.png"},
  "9 diamonds": {"value": 9, "color": "diamonds", "image": "9D.png"},
  "10 diamonds": {"value": 10, "color": "diamonds", "image": "10D.png"},
  "J diamonds": {"value": 10, "color": "diamonds", "image": "JD.png"},
  "Q diamonds": {"value": 10, "color": "diamonds", "image": "QD.png"},
  "K diamonds": {"value": 10, "color": "diamonds", "image": "KD.png"},
  "A diamonds": {"value": 11, "color": "diamonds", "image": "AD.png"},
  
  "2 clubs": {"value": 2, "color": "clubs", "image": "2C.png"},
  "3 clubs": {"value": 3, "color": "clubs", "image": "3C.png"},
  "4 clubs": {"value": 4, "color": "clubs", "image": "4C.png"},
  "5 clubs": {"value": 5, "color": "clubs", "image": "5C.png"},
  "6 clubs": {"value": 6, "color": "clubs", "image": "6C.png"},
  "7 clubs": {"value": 7, "color": "clubs", "image": "7C.png"},
  "8 clubs": {"value": 8, "color": "clubs", "image": "8C.png"},
  "9 clubs": {"value": 9, "color": "clubs", "image": "9C.png"},
  "10 clubs": {"value": 10, "color": "clubs", "image": "10C.png"},
  "J clubs": {"value": 10, "color": "clubs", "image": "JC.png"},
  "Q clubs": {"value": 10, "color": "clubs", "image": "QC.png"},
  "K clubs": {"value": 10, "color": "clubs", "image": "KC.png"},
  "A clubs": {"value": 11, "color": "clubs", "image": "AC.png"}
}

class Card:
  def __init__(self, value, color, image):
    self.value = value
    self.color = color
    self.image = image

def draw_card():
  drawn_card = random.choice(shoe_of_cards)
  print(drawn_card)
  shoe_of_cards.remove(drawn_card)
  card_values = deck[drawn_card]
  card_instance = Card(card_values["value"], card_values["color"], card_values["image"])
  print(card_values["value"], card_values["color"], card_values["image"])
  
def shoe_reset():
  shoe_of_cards = CARDS * amount_of_decks
  
draw_card()