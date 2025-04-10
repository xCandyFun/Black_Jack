import random

card_values = {
    'A': (1, 11),
    '2': 2, '3': 3, '4': 4, '5': 5,
    '6': 6, '7': 7, '8': 8, '9': 9, '10': 10,
    'J': 10, 'Q': 10, 'K': 10
}

suits = ['h', 'c', 's', 'd']
ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

deck = [rank + suit for suit in suits for rank in ranks]



class normal_game:
    
    #to remove cards:
    # drawn_card = deck.pop()
    
    @staticmethod
    def getACard():
        #random_card = random.choice(deck)
        random.shuffle(deck)
        if deck:
            drawn_card = deck.pop()
            print(drawn_card)
            return drawn_card
        else:
            return "Deck empty"

    
