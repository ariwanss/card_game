class Card:
    suits = ['diamonds', 'clubs', 'hearts', 'spades']
    values = [None, None, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King', 'Ace']

    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __lt__(self, other):
        if self.value < other.value:
            return True
        if self.value == other.value:
            if self.suit < other.suit:
                return True
        return False

    def __gt__(self, other):
        if self.value > other.value:
            return True
        if self.value == other.value:
            if self.suit > other.suit:
                return True
        return False

    def __repr__(self):
        return str(values[self.value]) + ' of ' + suits[self.suit]