from random import shuffle

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
        return str(self.values[self.value]) + ' of ' + self.suits[self.suit]

class Deck:
    def __init__(self):
        self.cards = []
        for i in range(4):
            for j in range(2, 15):
                self.cards.append(Card(i, j))
        shuffle(self.cards)

    def remove_card(self):
        return self.cards.pop()

class Player:
    def __init__(self, name):
        self.name = name
        self.card = None
        self.wins = 0

class Game:
    def __init__(self):
        name1 = input('player 1 name: ')
        name2 = input('player 2 name: ')
        self.player1 = Player(name1)
        self.player2 = Player(name2)
        self.deck = Deck()

    def play_game(self):
        print('lets begin')
        print('q to quit\n')
        print('_' * 40)
        print('\n')
        while len(self.deck.cards) >= 2:
            resp1 = input(f'{self.player1.name} press any key to draw a card')
            if resp1 == 'q':
                break
            self.player1.card = self.deck.remove_card()
            resp2 = input(f'{self.player2.name} press any key to draw a card')
            if resp2 == 'q':
                break
            self.player2.card = self.deck.remove_card()
            print(f'{self.player1.name} drew {self.player1.card}, {self.player2.name} drew {self.player2.card}\n')

            if self.player1.card > self.player2.card:
                self.player1.wins += 1
                print(f'{self.player1.name} wins')
            elif self.player1.card < self.player2.card:
                self.player2.wins += 1
                print(f'{self.player2.name} wins')
            
            if len(self.deck.cards) != 0:
                print('\n')
                print('_' * 40)
                print('next round')
                print('_' * 40)
                
        print('_' * 40)
        print('game over')
        if self.player1.wins != self.player2.wins:
            print(self.winner() + ' won')
        else:
            print(self.winner())


    def winner(self):
        if self.player1.wins > self.player2.wins:
            return self.player1.name
        elif self.player1.wins < self.player2.wins:
            return self.player2.name
        else:
            return 'it\'s a tie'
            

