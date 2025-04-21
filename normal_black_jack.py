import random

# Constants
CARD_VALUES = {
    'A': (1, 11),
    '2': 2, '3': 3, '4': 4, '5': 5,
    '6': 6, '7': 7, '8': 8, '9': 9, '10': 10,
    'J': 10, 'Q': 10, 'K': 10
}

SUITS = ['h', 'c', 's', 'd']
RANKS = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

def create_deck():
    return [rank + suit for suit in SUITS for rank in RANKS]

def calculate_total(cards):
    total = 0
    aces = 0

    for card in cards:
        rank = card[:-1]
        value = CARD_VALUES[rank]

        if rank == 'A':
            total += 11
            aces += 1
        else:
            total += value

    # Adjust for Aces if total is over 21
    while total > 21 and aces > 0:
        total -= 10
        aces -= 1

    return total


class NormalBlackJackGame:
    def __init__(self):
        self.deck = create_deck()
        random.shuffle(self.deck)

    def get_a_card(self):
        if self.deck:
            return self.deck.pop()
        return None  # Deck is empty

    def deal_initial_hands(self):
        return [self.get_a_card(), self.get_a_card()]

    def reset_deck(self):
        self.deck = create_deck()
        random.shuffle(self.deck)
