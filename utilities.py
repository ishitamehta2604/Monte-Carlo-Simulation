import numpy as np

class Player():
    def __init__(self, dealt_card, dealer= False):
        self.dealer = dealer
        self.cards_in_hand = dealt_card
        # self.draw = update_cards_in_hand()
        self.cards_score = []

        ## Dealer
        self.dealt_card = dealt_card
        if dealer == False:
            self.bet = random(1, 10)*10
    def card_score(self):

    def update_cards_in_hand(self, card):
        ## ('K', 'Heart')
        self.cards_in_hand.append(card)

    def stand(self):
        # true means terminal_state has reached
        ############################################## ace value

        if self.dealer == False:
            return sum(self.cards_score) > 17
        else:
            # score more than majority

    # def double:
    ## compulory add a card
    # and terminal_state
    # def split():
    ## A K
    ## K 1
    ## Insurance taken




class Cards():
    def __init__(self, number_of_player):
        ## try combing both
        self.deck = [1 to 52]
        self.shuffle
        self.number_of_player = number_of_player

    def dealt_cards(self):
        ## each player and deal are dealt with 2 cards_score
        self.deck.remove()
        return [[], [], []]

    def remove_card_from_deck(self):
        self.deck.remove()

### remove head cards




class Game():
    def __init__(self):
        self.number_of_player = random(2,7)
        self.deck = Cards(number_of_player)
        self.player_cards = deck.dealt_cards()
        self.final_score = []
            self.all_players_bet = []
    # def creating_player_instance(self):
        for i in range(1, self.number_of_player + 2):
            if i <= self.number_of_player + 1:
                # Reference :https://stackoverflow.com/questions/6181935/how-do-you-create-different-variable-names-while-in-a-loop
                exec(f'self.contender{i} = Player(self.player_cards[i])')


            # defining dealer
            elif i ==  self.number_of_player + 2:
                self.dealer = Player(self.player_cards[i], dealer= True)

    def contender_game(self):
        for i in range(1, self.number_of_player + 1):
            while !(eval('self.contender'+ i + '.stand')):
                card = self.deck.remove_card_from_deck()
                eval('self.contender' + i + '.update_cards_in_hand(card)')
            self.final_score.append(eval('self.contender' + i + '.card_score()'))
            self.all_players_bet.append('self.contender' + i + '.bet')
        # Score more than 21 than player lose
        self.final_score = np.tolist(np.where(np.asarray(self.final_score) <= 21, np.asarray(self.final_score), 0))


    def dealer_game(self):
        ## Check if the dealer is winning the majority bet, then stand
        ### else pick a cards
        ### Also consider extreme case like where total should be less than 20
        while np.where(self.dealer.card_score() > (np.asarray(self.final_score)) == True, self.all_players_bet, 0).sum() > (sum(self.all_players_bet) / 2):
            if self.dealer.card_score() >= 20:
                break
            else:
                card = self.deck.remove_card_from_deck()
                self.dealer.update_cards_in_hand(card)
                
    def win_loss:
        ## Win-loss for Dealer
        ## Draw
        if self.dealer.card_score() > 21:
            return np.where((np.asarray(self.final_score) == 0, 'Draw', 'Lose')
        else:
            return np.where(self.dealer.card_score() > (np.asarray(self.final_score), 'Win', 'Lose')


    # def summary(self, print = True):
        # For Each
        # for i in range(1, self.number_of_player + 1):
            # Cards_in_hands

            # bet
            # Win/Lose
        # Total Win/Loss




if __name__ == '__main__':
    game()
