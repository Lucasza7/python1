import random

# Card constants
SUITS = ('Spades', 'Hearts', 'Clubs', 'Diamonds')
RANKS = ('Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King')
NCARDS = 8

class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        self.value = RANKS.index(rank) + 1

    def __str__(self):
        return f"{self.rank} of {self.suit}"

class Deck:
    def __init__(self):
        self.cards = [Card(rank, suit) for suit in SUITS for rank in RANKS]

    def shuffle(self):
        random.shuffle(self.cards)

    def draw_card(self):
        return self.cards.pop()

class HigherOrLowerGame:
    def __init__(self):
        self.deck = Deck()
        self.score = 50
        self.current_card = None

    def start_game(self):
        print('Welcome to Higher or Lower.')
        print('You have to choose whether the next card to be shown will be higher or lower than the current card.')
        print('Getting it right adds 20 points; get it wrong and you lose 15 points.')
        print('You have 50 points to start.')
        print()

        while True:
            self.play_round()
            go_again = input('To play again, press ENTER, or "q" to quit: ')
            if go_again.lower() == 'q':
                break

        print('OK bye')

    def play_round(self):
        self.deck = Deck()
        self.deck.shuffle()
        self.current_card = self.deck.draw_card()
        print(f"Starting card is: {self.current_card}")
        print()

        for _ in range(NCARDS):
            self.make_guess()

    def make_guess(self):
        guess = input(f"Will the next card be higher or lower than the {self.current_card}? (enter h or l): ").casefold()
        next_card = self.deck.draw_card()
        print(f"Next card is: {next_card}")

        if (guess == 'h' and next_card.value > self.current_card.value) or (guess == 'l' and next_card.value < self.current_card.value):
            print(f"You got it right, it was {'higher' if guess == 'h' else 'lower'}")
            self.score += 20
        else:
            print(f"Sorry, it was not {'higher' if guess == 'h' else 'lower'}")
            self.score -= 15

        print(f"Your score is: {self.score}")
        print()
        self.current_card = next_card

if __name__ == "__main__":
    game = HigherOrLowerGame()
    game.start_game()
