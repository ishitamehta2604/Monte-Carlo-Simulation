import numpy as np
import random

class Player():
    '''
    This class defines the player and dealer,  and stores their cards and calculate the cards score. And also taken into account when a player should take stand

    >>> random.seed(1)
    >>> player1 = Player([('\u2663', 'K', 10), ('\u2660', 'J', 10)])
    >>> player1.stand()
    True

    >>> player1.card_score()
    20

    >>> player1.update_cards_in_hand(('\u2663', 'A', 1))
    >>> player1.card_score()
    21
    >>> player1.stand()
    True

    '''
    def __init__(self, dealt_card, dealer= False):
        '''
        This function take the necessary inputs required for the class Player and creates the necessary variable
        :param dealt_card: list of cards
        :param dealer: if the Player is d dealer
        '''
        self.dealer = dealer
        self.cards_in_hand = dealt_card
        self.cards_score = []
        self.flag_Ace = False
        self.dealt_card = dealt_card

        if not dealer:
            self.bet = random.randint(1, 10)*10

    def card_score(self):
        score =0
        for i in self.cards_in_hand:
            if i[2] == 1:
                score += i[2]
                self.flag_Ace = True
            else:
                score += i[2]
        return score

    def update_cards_in_hand(self, card):
        self.cards_in_hand.append(card)

    def stand(self):
        player_score = self.card_score()
        # true means terminal_state has reached
        ############################################## ace value
        if self.flag_Ace == False:
            return player_score > 15
        else:
            ## Ace value is stored as 1 in the card_score
            if player_score > (7 + 10) & player_score < (11 + 10):
                return True
            else:
                self.flag_Ace = False
                self.stand(self)


    # def double:
    ## compulory add a card
    # and terminal_state
    # def split():
    ## A K
    ## K 1
    ## Insurance taken




class Cards():
    '''
    This call generate the deck, dealt the cards in the start of the game and allows player to draw a card from deck

    >>> random.seed(100)
    >>> card = Cards(7)
    >>> test_cards = card.dealt_cards()
    >>> len(test_cards)
    8
    >>> len(test_cards[0])
    3


    '''
    def __init__(self, number_of_player: int):
        '''
        This function take the necessary inputs required for the class Cards and creates the necessary variable
        :param number_of_player: self explainatory
        '''
        ## try combing both
        self.deck = [i for i in range(1,52 + 1)]
        random.shuffle(self.deck)
        self.number_of_player = number_of_player

    def dealt_cards(self) -> list:
        '''
        This function dealt the cards to player and dealer, based on there turn
        :return: list of list containing tuples with card and suit
        '''
        ## each player and deal are dealt with 2 cards_score
        player_dealer_cards = [[] for i in range(self.number_of_player + 1)]

        # Number of cards to be dealt
        for _ in range(2):
            # Number of player
            for i in range(self.number_of_player + 1):
                player_dealer_cards[i].append(self.remove_card_from_deck())

        return player_dealer_cards

    def remove_card_from_deck(self) -> tuple:
        '''
        This functions removes the top card from deck
        :return: list of tuple with card and suit
        '''
        top_card_on_deck = self.deck[0]

        ## Exact card
        if top_card_on_deck % 13 == 1:
             card = 'A'
             card_score = 1
        elif top_card_on_deck % 13 == 11:
            card = 'J'
            card_score = 10
        elif top_card_on_deck % 13 == 12:
            card = 'Q'
            card_score = 10
        elif top_card_on_deck % 13 == 0:
            card = 'K'
            card_score = 10
        else:
            card = str(top_card_on_deck)
            card_score = top_card_on_deck

        ## Suit of the card
        # Reference: https://www.youtube.com/watch?v=IsklrLQE88Y&ab_channel=AllTech
        # Club - \u2663
        # Spades - \u2660
        # Diamond - \u2666
        # Heart - \u2665
        if top_card_on_deck < 14:
            suit = '\u2663'
        elif top_card_on_deck < 27:
            suit = '\u2660'
        elif top_card_on_deck < 40:
            suit = '\u2666'
        else:
            suit = '\u2665'

        # Removing the card from the deck
        self.deck.remove(top_card_on_deck)

        return (suit, card, card_score)

### remove head cards


#
#
# class Game():
#     def __init__(self):
#         self.number_of_player = random(2,7)
#         self.deck = Cards(number_of_player)
#         self.player_cards = deck.dealt_cards()
#         self.final_score = []
#             self.all_players_bet = []
#     # def creating_player_instance(self):
#         for i in range(1, self.number_of_player + 2):
#             if i <= self.number_of_player + 1:
#                 # Reference :https://stackoverflow.com/questions/6181935/how-do-you-create-different-variable-names-while-in-a-loop
#                 exec(f'self.contender{i} = Player(self.player_cards[i])')
#
#
#             # defining dealer
#             elif i ==  self.number_of_player + 2:
#                 self.dealer = Player(self.player_cards[i], dealer= True)
#
#     def contender_game(self):
#         for i in range(1, self.number_of_player + 1):
#             while !(eval('self.contender'+ i + '.stand')):
#                 card = self.deck.remove_card_from_deck()
#                 eval('self.contender' + i + '.update_cards_in_hand(card)')
#             self.final_score.append(eval('self.contender' + i + '.card_score()'))
#             self.all_players_bet.append('self.contender' + i + '.bet')
#         # Score more than 21 than player lose
#         self.final_score = np.tolist(np.where(np.asarray(self.final_score) <= 21, np.asarray(self.final_score), 0))
#
#
#     def dealer_game(self):
#         ## Check if the dealer is winning the majority bet, then stand
#         ### else pick a cards
#         ### Also consider extreme case like where total should be less than 20
#         while np.where(self.dealer.card_score() > (np.asarray(self.final_score)) == True, self.all_players_bet, 0).sum() > (sum(self.all_players_bet) / 2):
#             if self.dealer.card_score() >= 20:
#                 break
#             else:
#                 card = self.deck.remove_card_from_deck()
#                 self.dealer.update_cards_in_hand(card)
#
#     def win_loss:
#         ## Win-loss for Dealer
#         ## Draw
#         if self.dealer.card_score() > 21:
#             return np.where((np.asarray(self.final_score) == 0, 'Draw', 'Lose')
#         else:
#             return np.where(self.dealer.card_score() > (np.asarray(self.final_score), 'Win', 'Lose')


    # def summary(self, print = True):
        # For Each
        # for i in range(1, self.number_of_player + 1):
            # Cards_in_hands

            # bet
            # Win/Lose
        # Total Win/Loss




if __name__ == '__main__':
    card = Cards(2)
