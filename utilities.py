import pandas as pd
import numpy as np
import random


class Player():
    '''
    This class defines the player and dealer,  and stores their cards and calculate the cards score. And also taken into account when a player should take stand

    >>> player2 = Player([('\U0001F4A3','EXPLODE',100), ('\u2660', 'J', 5)], 21)
    >>> player2.player_stand()
    True

    >>> player2.card_score()
    (100, False)

    >>> random.seed(1)
    >>> player1 = Player([('\u2663', 'K', 10), ('\u2660', 'J', 10)], 21)
    >>> player1.player_stand()
    True

    >>> player1.card_score()
    (20, False)

    >>> player1.update_cards_in_hand(('\u2663', 'A', 1))
    >>> player1.card_score()
    (21, False)
    >>> player1.player_stand()
    True



    >>> random.seed(1)
    >>> dealer = Player([('\u2663', 'K', 10), ('\u2660', 'A', 11)], 21, True)
    >>> dealer.dealer_stand([20,18], [50,60])
    True

    >>> dealer.card_score()
    (21, True)

    >>> dealer.update_cards_in_hand(('\u2663', 'A', 11))
    >>> dealer.card_score()
    (12, False)
    >>> dealer.dealer_stand([20,18], [50,60])
    False

    '''


    def __init__(self, dealt_card, target_score=21, dealer=False):
        '''
        This function take the necessary inputs required for the class Player and creates the necessary variable

        :param dealt_card: list of cards
        :param target_score: Score needed to get a black jack
        :param dealer: if the Player is a dealer
        '''
        self.dealer = dealer
        self.cards_in_hand = dealt_card
        self.cards_score = []
        self.flag_Ace = False
        self.dealt_card = dealt_card
        self.Ace_count = 0
        self.target_score = target_score


        if not self.dealer:
            self.bet = random.randint(1, 10) * 10

    def card_score(self):
        '''
        Card Score helps to calculates the score for the player instance
        '''
        score = 0
        BlackJack = False
        count = 2
        # Explode = False


        ## Explode Condition
        if "EXPLODE" in (self.cards_in_hand[0][1] or self.cards_in_hand[1][1]):
            score = 100
            return score, BlackJack


        for i in self.cards_in_hand:
            count -= 1
            if i[2] == 11:
                score += i[2]
                self.flag_Ace = True
                self.Ace_count += 1
            else:
                score += i[2]

        ## Accounting for Ace score
        while self.Ace_count >= 1:
            if score > self.target_score:
                self.Ace_count -= 1
                score -= 10
                if self.Ace_count == 0:
                    self.flag_Ace = False
            else:
                break


        ## BlackJack Condition
        if score == self.target_score:
            if count == 0:
                BlackJack = True
        return score, BlackJack

    def update_cards_in_hand(self, card):
        '''
        Updated the player's cards in hand
        :param card: The new card drawn from the deck
        '''
        self.cards_in_hand.append(card)

    def dealer_stand(self, player_score: list, player_bet: list):
        '''
        The conditions where the dealer decides to take a stand on whether to pick another card or not
        :player_score: The list
        :player_bet:
        '''
        # print(np.asarray(player_score) < 19)
        # print(np.where(self.card_score() >= 1 ,1, 0).sum())

        if np.where(self.card_score()[0] >= (np.asarray(player_score)), np.asarray(player_bet), 0).sum() >= (
                sum(player_bet) / 2):
            return True

        if self.card_score()[0] >= self.target_score - 3:
            return True

        else:
            return False

    def player_stand(self):
        player_score = self.card_score()[0]
        # true means terminal_state has reached
        ############################################## ace value
        if self.flag_Ace == False:
            return player_score >= self.target_score - 6
        else:
            ## Ace value is stored as 11 in the card_score
            if player_score >= (6 + 11):
                return True

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
    2
    >>> len(test_cards[0][0])
    3

    >>> random.seed(100)
    >>> card = Cards(7, False, head_card_value = 10)
    >>> test_cards = card.dealt_cards()
    >>> len(test_cards)
    8
    >>> test_cards[1][0]
    ('♣', 'A', 11)


    '''

    def __init__(self, number_of_player: int, head_cards: bool = True, head_card_value: int = 10, explosion=False):
        '''
        This function take the necessary inputs required for the class Cards and creates the necessary variable
        :param number_of_player: self explainatory
        '''
        ## try combing both
        self.head_cards = head_cards
        if self.head_cards:
            self.deck = [i for i in range(1, 52 + 1)]
        else:
            self.deck = [i for i in range(1, 40 + 1)]
        if explosion:
            self.deck.append(100)
        random.shuffle(self.deck)

        self.head_card_value = head_card_value
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
        if self.head_cards:
            temp = 13
        else:
            temp = 10

        if top_card_on_deck == 100:
            card = 'EXPLODE'
            card_score = 100

        elif top_card_on_deck % temp == 1:
            card = 'A'
            card_score = 11

        else:
            card = str(top_card_on_deck % temp)
            card_score = top_card_on_deck % temp

        ## Checking if head cards are need or not
        if self.head_cards:
            if top_card_on_deck % temp == 11:
                card = 'J'
                card_score = self.head_card_value
            elif top_card_on_deck % temp == 12:
                card = 'Q'
                card_score = self.head_card_value
            elif top_card_on_deck % temp == 0:
                card = 'K'
                card_score = self.head_card_value

        else:
            if top_card_on_deck % temp == 0:
                card = '10'
                card_score = 10

        ## Suit of the card
        # Reference: https://www.youtube.com/watch?v=IsklrLQE88Y&ab_channel=AllTech
        # Reference link for Bomb : https://www.compart.com/en/unicode/U+1F4A3
        # Club - \u2663
        # Spades - \u2660
        # Diamond - \u2666
        # Heart - \u2665
        # Bomb - '\U0001F4A3'

        if top_card_on_deck == 100:
            suit = '\U0001F4A3'
        elif top_card_on_deck < temp + 1:
            suit = '\u2663'
        elif top_card_on_deck < (2 * temp) + 1:
            suit = '\u2660'
        elif top_card_on_deck < (3 * temp) + 1:
            suit = '\u2666'
        else:
            suit = '\u2665'

        # Removing the card from the deck
        self.deck.remove(top_card_on_deck)

        return (suit, card, card_score)


### remove head cards


class Game():
    '''
    This class interacts the with Player and Cards class and makes the game workable

    >>> random.seed(1)
    >>> game1 = Game()
    >>> game1.creating_player_instance()
    >>> game1.contender_game()
    >>> game1.dealer_game(dealer_advantage = True)
    >>> game1.win_loss(BJ_reward = 1.5)
    [array(['Win', 'Draw', 'Win'], dtype='<U4'), array(110.)]

    >>> game1.summary(detail_summary= True)
    Dealer Won: $110.0
    Dealer Cards: ♠K |♥J |
    Dealer Score 20
    <BLANKLINE>
    Player1:
    Cards ♣3 |♠7 |♠3 |♦4 |
    Player Score: 17
    Player Bet: 20
    Player: Lose
    <BLANKLINE>
    Player2:
    Cards ♦K |♣10 |
    Player Score: 20
    Player Bet: 60
    Player: Draw
    <BLANKLINE>
    Player3:
    Cards ♣Q |♠6 |
    Player Score: 16
    Player Bet: 90
    Player: Lose
    <BLANKLINE>


    '''

    def __init__(self, target_score=21, head_cards=True, head_card_value=10, explosion=False):
        self.number_of_player = random.randint(2, 7)
        self.deck = Cards(self.number_of_player, head_cards, head_card_value, explosion)
        self.player_cards = self.deck.dealt_cards()
        self.final_score = []
        self.BJ = []
        self.all_players_bet = []
        self.target_score = target_score
        self.dealer = Player(self.player_cards[-1], self.target_score, dealer=True)

    def creating_player_instance(self):
        for i in range(1, self.number_of_player + 1):
            if i <= self.number_of_player + 1:
                # Reference :https://stackoverflow.com/questions/6181935/how-do-you-create-different-variable-names-while-in-a-loop
                exec(f'self.contender{i} = Player(self.player_cards[{i - 1}], self.target_score)')

    def contender_game(self):
        for i in range(1, self.number_of_player + 1):
            while not (eval(f'self.contender{i}.player_stand()')):
                card = self.deck.remove_card_from_deck()
                eval(f'self.contender{i}.update_cards_in_hand({card})')
            self.final_score.append(eval(f'self.contender{i}.card_score()[0]'))
            self.BJ.append(eval(f'self.contender{i}.card_score()[1]'))
            self.all_players_bet.append(eval(f'self.contender{i}.bet'))
        # Score more than 21 than player lose
        self.final_score = (
            np.where(np.asarray(self.final_score) <= self.target_score, np.asarray(self.final_score), 0)).tolist()

    def dealer_game(self, dealer_advantage=True):
        if dealer_advantage:
            while not self.dealer.dealer_stand(self.final_score, self.all_players_bet):
                card = self.deck.remove_card_from_deck()
                self.dealer.update_cards_in_hand(card)
        else:
            while not self.dealer.player_stand():
                card = self.deck.remove_card_from_deck()
                self.dealer.update_cards_in_hand(card)

    def win_loss(self, BJ_reward=1.5):
        ## Win-loss for Dealer
        ## Draw
        ## If dealer get Black Jack
        if self.dealer.card_score()[1] == True:
            deal_win = np.where(self.BJ == True, 'Draw', 'Win')
            amount_win = np.where(deal_win == 'Win', np.asarray(self.all_players_bet), 0).sum()
        else:
            deal_win = np.where(self.dealer.card_score()[0] > (np.asarray(self.final_score)), 'Win',
                                np.where(self.dealer.card_score()[0] == (np.asarray(self.final_score)), 'Draw', 'Lose'))
            amount_win = np.where(deal_win == 'Win', np.asarray(self.all_players_bet),
                                  np.where(deal_win == 'Lose', 0 - np.asarray(self.all_players_bet), 0)).sum()

            ## Player blackJack Payoff
            amount_win = np.where(self.BJ == True, (BJ_reward * amount_win), amount_win)
        return [deal_win, amount_win]

    def summary(self, detail_summary=True):
        dealer_won = self.win_loss()
        print(f"Dealer Won: ${dealer_won[1]}")

        if detail_summary:
            print("Dealer Cards: ", end='')
            for dealer_c in self.dealer.cards_in_hand:
                print(f"{dealer_c[0]}", end='')
                print(f"{dealer_c[1]}", end=' |')
            print(f"\nDealer Score {self.dealer.card_score()[0]}\n")

            Winner = dealer_won[0]
            Player_won = np.where(Winner == 'Draw', 'Draw', np.where(Winner == 'Lose', 'Win', 'Lose'))

            for i in range(1, self.number_of_player + 1):
                print(f"Player{i}:")
                # Reference: https://www.geeksforgeeks.org/print-without-newline-python/
                print("Cards", end=" ")
                for c in eval(f"self.contender{i}.cards_in_hand"):
                    print(f"{c[0]}", end='')
                    print(f"{c[1]}", end=' |')

                score = eval(f'self.contender{i}.card_score()')
                print(f"\nPlayer Score: {score[0]}")
                bet = eval(f'self.contender{i}.bet')
                print(f"Player Bet: {bet}")
                print(f"Player: {Player_won[i - 1]}", end='\n\n')


'''
Variations:
Target - 21
Head_card or not
There will be no change in the dealer’s winning chance, if the cards of both the player and dealer are disclosed at the end of the game.
head_card_value

'''


def Generate_one_simulation(cumulative_win, target_score=21, head_cards=True, head_card_value=10, dealer_advantage=True,
                            BJ_reward=1.5, explosion=False, Summary=True, detail_summary=True):
    game_instance = Game(target_score, head_cards, head_card_value, explosion)
    game_instance.creating_player_instance()
    game_instance.contender_game()
    game_instance.dealer_game(dealer_advantage)
    dealer_winning = game_instance.win_loss(BJ_reward)[1]
    cumulative_win += dealer_winning
    if Summary:
        print(f"Dealers cumulative winning: ${cumulative_win}")
        game_instance.summary(detail_summary)
    return dealer_winning, cumulative_win


def simulation(number_of_simulations, target_score=21, head_cards=True, head_card_value=10, dealer_advantage=True,
               BJ_reward=1.5,explosion=False, Summary=True, detail_summary=True ):
    '''

    >>> random.seed(1)
    >>> df = simulation(2, target_score=21, head_cards= True, dealer_advantage = True,BJ_reward = 1.5, explosion = False, Summary = True, detail_summary = False)
    Game 0
    Dealers cumulative winning: $110.0
    Dealer Won: $110.0
    Game 1
    Dealers cumulative winning: $380.0
    Dealer Won: $270.0

    >>> df.columns
    Index(['Game', 'Won', 'Cumulative'], dtype='object')
    >>> len(df)
    2

    >>> df1 = simulation(4, target_score=21, head_cards =True, dealer_advantage = True,BJ_reward = 1.5, explosion = False, Summary = False, detail_summary = False  )
    >>> df1.columns
    Index(['Game', 'Won', 'Cumulative'], dtype='object')
    >>> len(df1)
    4

    >>> df2 = simulation(4, target_score=21, head_cards =True, dealer_advantage = True,BJ_reward = 1.5, explosion = True, Summary = False, detail_summary = False )
    >>> df2.columns
    Index(['Game', 'Won', 'Cumulative'], dtype='object')
    '''
    Game = []
    Dealer_Won = []
    cumulative_win = 0
    for i in range(number_of_simulations):
        Game.append(i)
        if Summary:
            print(f"Game {i}")
        instance_call = Generate_one_simulation(cumulative_win, target_score, head_cards, head_card_value,
                                                dealer_advantage, BJ_reward, explosion, Summary, detail_summary )
        Dealer_Won.append(instance_call[0])
        cumulative_win += instance_call[1]
    Result = pd.DataFrame({'Game': Game, 'Won': Dealer_Won})
    Result['Cumulative'] = Result['Won'].cumsum(axis=0)
    return Result


if __name__ == '__main__':
    #card = Cards(2)
    player2 = Player([('\U0001F4A3', 'EXPLODE', 100), ('\u2660', 'J', 10)], 21)
    player2.player_stand()
