import pandas as pd
import numpy as np
import random


class Player():
    '''
    This class defines the player and dealer,  and stores their cards and calculate the cards score. And also taken into account when a player should take stand

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

    >>> player2 = Player([('\U0001F4A3','EXPLODE',100), ('\u2660', 'J', 5)], 21)
    >>> player2.player_stand()
    True

    >>> player2.card_score()
    (100, False)

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


    def __init__(self, dealt_card: list, target_score:int  =21, dealer: bool =False):
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
        self.target_score = target_score


        if not self.dealer:
            self.bet = random.randint(1, 10) * 10

    def card_score(self) -> tuple:
        '''
        Card Score helps to calculates the score for the player instance and whether they have a Blackjack or not
        '''
        score = 0
        Ace_count = 0
        BlackJack = False
        count = 2


        for i in self.cards_in_hand:
            count -= 1
            if "EXPLODE" == i[1]:
                score = 100
                return score, BlackJack

            elif i[2] == 11:
                score += i[2]
                self.flag_Ace = True
                Ace_count += 1
            else:
                score += i[2]

        ## Accounting for Ace score
        while Ace_count >= 1:
            if score > self.target_score:
                Ace_count -= 1
                score -= 10
                if Ace_count == 0:
                    self.flag_Ace = False
            else:
                break


        ## BlackJack Condition
        if score == self.target_score:
            if count == 0:
                BlackJack = True
        return score, BlackJack

    def update_cards_in_hand(self, card: tuple):
        '''
        Updated the player's cards in hand
        :param card: The new card drawn from the deck
        '''
        self.cards_in_hand.append(card)

    def dealer_stand(self, player_score: list, player_bet: list) -> bool:
        '''
        The conditions where the dealer decides to take a stand on whether to pick another card or not

        :player_score: The list
        :player_bet: Amount bet by the player
        :return whether dealer should take a stand or not
        '''
        # print(np.asarray(player_score) < 19)
        # print(np.where(self.card_score() >= 1 ,1, 0).sum())

        if np.where(self.card_score()[0] >= (np.asarray(player_score)), np.asarray(player_bet), 0).sum() >= (
                sum(player_bet) / 2):
            return True

        if self.card_score()[0] >= self.target_score - 4:
            return True

        else:
            return False

    def player_stand(self) -> bool:
        '''
        This function checks if the player should take a stand or not

        :return boolean value whether player should take a stand or not
        '''
        player_score = self.card_score()[0]
        # true means terminal_state has reached
        ############################################## ace value
        if self.flag_Ace == False:
            return player_score >= self.target_score - 6
        else:
            ## Ace value is stored as 11 in the card_score
            if player_score >= self.target_score - 3:
                return True



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

        :param number_of_player: number of players in the game
        :param head_cards: deck should have head cards or not
        :param head_card_value: Value of the head cards should be
        :param explosion: deck contains explosion cards
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


class Game():
    '''
    This class interacts the with Player and Cards class and makes the game workable

    >>> random.seed(1)
    >>> game1 = Game()
    >>> game1.creating_player_instance()
    >>> game1.contender_game()
    >>> game1.dealer_game(dealer_advantage = True)
    >>> game1.win_loss(BJ_reward = 1.5)
    [array(['Win', 'Draw', 'Win'], dtype='<U4'), 110.0]


    '''

    def __init__(self, target_score:int = 21, head_cards: bool = True, head_card_value: int = 10, explosion: bool = False):
        '''
        Defining required variable for game class

        :param target_score: target score for Blackjack
        :param head_cards: whether game should contain head cards or not
        :param head_card_value: what should be the value of head cards
        :param explosion: whether game should contain explosion card
        '''

        self.number_of_player = random.randint(2, 7)
        self.deck = Cards(self.number_of_player, head_cards, head_card_value, explosion)
        self.player_cards = self.deck.dealt_cards()
        self.final_score = []
        self.BJ = []
        self.all_players_bet = []
        self.target_score = target_score
        self.dealer = Player(self.player_cards[-1], self.target_score, dealer=True)

    def creating_player_instance(self):
        '''
        This function define players/contenders using player class
        '''
        for i in range(1, self.number_of_player + 1):
            if i <= self.number_of_player + 1:
                # Reference :https://stackoverflow.com/questions/6181935/how-do-you-create-different-variable-names-while-in-a-loop
                exec(f'self.contender{i} = Player(self.player_cards[{i - 1}], self.target_score)')

    def contender_game(self):
        '''
        This function check when should player hit and take a stand. Also checks if the player got a Blackjack or not
        '''
        for i in range(1, self.number_of_player + 1):
            while not (eval(f'self.contender{i}.player_stand()')):
                card = self.deck.remove_card_from_deck()
                eval(f'self.contender{i}.update_cards_in_hand({card})')
            self.final_score.append(eval(f'self.contender{i}.card_score()[0]'))
            self.BJ.append(eval(f'self.contender{i}.card_score()[1]'))
            self.all_players_bet.append(eval(f'self.contender{i}.bet'))
        # Score more than 21 than player lose
        self.final_score = (
            np.where(np.asarray(self.final_score) <= self.target_score, np.asarray(self.final_score), 100)).tolist()

    def dealer_game(self, dealer_advantage: bool =True):
        '''
        This function check when should dealer hit and take a stand. Also checks if the dealer got a Blackjack or not
        '''
        if dealer_advantage:
            while not self.dealer.dealer_stand(self.final_score, self.all_players_bet):
                card = self.deck.remove_card_from_deck()
                self.dealer.update_cards_in_hand(card)
        else:
            while not self.dealer.player_stand():
                card = self.deck.remove_card_from_deck()
                self.dealer.update_cards_in_hand(card)

    def win_loss(self, BJ_reward: float =1.5) -> list:
        '''
        This function check if dealer won or loss and the amount won by him (against each player)

        :param BJ_reward: how much times the player should get the reward incase of black jack
        :return a list of lists that contains. The first list contains whether dealer won or loss and the second list contain the amount won or lost by the dealer
        '''
        if self.dealer.card_score()[1] == True:
            deal_win =np.where(np.asarray(self.BJ) == True, 'Draw', 'Win')
            amount_win = np.where(deal_win == 'Win', np.asarray(self.all_players_bet), 0).sum()
        else:
            temp_score = self.dealer.card_score()[0]
            if temp_score > self.target_score:
                deal_win = np.where(np.asarray(self.final_score) <= self.target_score, 'Lose', 'Draw')
            else:
                self.final_score = (np.where(np.asarray(self.final_score) == 100, 0, np.asarray(self.final_score))).tolist()
                deal_win = np.where(temp_score > (np.asarray(self.final_score)), 'Win', np.where(temp_score == (np.asarray(self.final_score)), 'Draw', 'Lose'))

            amount_win = np.where(deal_win == 'Win', np.asarray(self.all_players_bet), np.where(deal_win == 'Lose', 0-np.asarray(self.all_players_bet), 0))
            ## Player blackJack Payoff
            amount_win = np.where(np.asarray(self.BJ) == True, (BJ_reward * amount_win), amount_win)
            amount_win = amount_win.sum()

        return [deal_win, amount_win]

    def summary(self, detail_summary: bool =True):
        '''
        This function prints the summary

        :param detail_summary: whether to print detail summary or not
        '''
        dealer_won = self.win_loss()

        if detail_summary:
            print("Dealer Cards: ", end='')
            for dealer_c in self.dealer.cards_in_hand:
                print(f"{dealer_c[0]}", end='')
                print(f"{dealer_c[1]}", end=' |')
            print(f"\nDealer Score {self.dealer.card_score()[0]}\n")

            Winner = np.asarray(dealer_won[0])
            Player_won = (np.where(Winner == 'Draw', 'Draw', np.where(Winner == 'Lose', 'Win', 'Lose'))).tolist()

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
                print(f"Player: {Player_won[i-1]}", end='\n\n')


'''
Variations:
Target - 21
Head_card or not
There will be no change in the dealer’s winning chance, if the cards of both the player and dealer are disclosed at the end of the game.
head_card_value
Black Jack Reward
explosion card
'''


def simulation(number_of_simulations: int, target_score: int=21, head_cards:bool =True, head_card_value: int =10, dealer_advantage: bool=True,
               BJ_reward:float=1.5,explosion:bool =False, Summary:bool =True, detail_summary: bool =True) -> 'DataFrame':
    '''
    This functions generates multiple game simulation

    :param number_of_simulations: Number of time the simulation should run
    :param cumulative_win: total winning of previous games
    :param target_score: Target score for game of Blackjack
    :param head_cards: whether game should have head cards or not
    :param head_card_value: What should be the value of head cards
    :param dealer_advantage: Should dealer be given advantage/ should dealer know players cards.
    :param BJ_reward: Amound of rewards players should earn was getting perfect Blackjack
    :param explosion: Should deck contain explosion card
    :param Summary: Print summary or not
    :param detail_summary: Print detail summary or not
    :return a dataframe with 3 column (game number, win for the game, and cumulative winning )


    >>> random.seed(1)
    >>> df = simulation(2, target_score=21, head_cards= True, head_card_value=10, dealer_advantage = True,BJ_reward = 1.5, explosion = False, Summary = False, detail_summary = False)
    >>> df.columns
    Index(['Game', 'Won', 'Cumulative'], dtype='object')
    >>> len(df)
    2

    >>> df1 = simulation(4, target_score=21, head_cards =True, head_card_value=10,dealer_advantage = True,BJ_reward = 1.5, explosion = False, Summary = False, detail_summary = False  )
    >>> df1.columns
    Index(['Game', 'Won', 'Cumulative'], dtype='object')
    >>> len(df1)
    4

    >>> df2 = simulation(4, target_score=21, head_cards =True, head_card_value=10, dealer_advantage = True,BJ_reward = 1, explosion = True, Summary = False, detail_summary = False )
    >>> df2.columns
    Index(['Game', 'Won', 'Cumulative'], dtype='object')

    >>> simulation('Four', target_score=21, head_cards =True, head_card_value=10, dealer_advantage = True, BJ_reward = 1, explosion = True, Summary = False, detail_summary = False )
    Traceback (most recent call last):
    ...
    ValueError: Check the input datatype

    >>> simulation(4, target_score=21, head_cards =True, head_card_value=10, dealer_advantage = True,BJ_reward = 1, explosion = True, Summary = False, detail_summary = True )
    Traceback (most recent call last):
    ...
    ValueError: Summary should be True to print detail Summary

    '''
    ## Error Checking
    if not (isinstance(number_of_simulations, int) & isinstance(target_score, int) & \
             isinstance(head_cards, bool) & isinstance(head_card_value, int) & isinstance(dealer_advantage, bool) & \
            (isinstance(BJ_reward, float) | isinstance(BJ_reward, int)) & isinstance(explosion, bool) & \
            isinstance(Summary, bool) & isinstance(detail_summary, bool)):
        raise ValueError("Check the input datatype")


    if not Summary:
        if detail_summary:
            raise ValueError("Summary should be True to print detail Summary")


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
        cumulative_win = instance_call[1]
    Result = pd.DataFrame({'Game': Game, 'Won': Dealer_Won})
    Result['Cumulative'] = Result['Won'].cumsum(axis=0)
    return Result


def Generate_one_simulation(cumulative_win: float, target_score:int = 21, head_cards:bool = True, head_card_value:int = 10, dealer_advantage: bool = True,
                            BJ_reward: float = 1.5, explosion: bool=False, Summary: bool=True, detail_summary: bool=True) -> tuple:
    '''
    This functions generates one game simulation

    :param cumulative_win: total winning of previous games
    :param target_score: Target score for game of Blackjack
    :param head_cards: whether game should have head cards or not
    :param head_card_value: What should be the value of head cards
    :param dealer_advantage: Should dealer be given advantage/ should dealer know players cards.
    :param BJ_reward: Amound of rewards players should earn was getting perfect Blackjack
    :param explosion: Should deck contain explosion card
    :param Summary: Print summary or not
    :param detail_summary: Print detail summary or not
    :return a tuple with 2 elements, first with current game winning, and second with cumulative winnings

    >>> Generate_one_simulation(0 , target_score = 100, head_cards = True, head_card_value = 10, dealer_advantage = True, BJ_reward = 1.5, explosion=False, Summary=True, detail_summary=True)
    Traceback (most recent call last):
    ...
    ValueError: Target Score should be in range 0 to  100 (not inclusive 0 and 100)

    >>> Generate_one_simulation(0 , target_score = 0, head_cards = True, head_card_value = 10, dealer_advantage = True, BJ_reward = 1.5, explosion=False, Summary=True, detail_summary=True)
    Traceback (most recent call last):
    ...
    ValueError: Target Score should be in range 0 to  100 (not inclusive 0 and 100)


    >>> Generate_one_simulation(0 , target_score = 100, head_cards = 1, head_card_value = 10, dealer_advantage = True, BJ_reward = 1.5, explosion=False, Summary=True, detail_summary=True)
    Traceback (most recent call last):
    ...
    ValueError: Check the input datatype

    >>> Generate_one_simulation(0 , target_score = 27, head_cards = False, head_card_value = 10, dealer_advantage = True, BJ_reward = 1.5, explosion=False, Summary=True, detail_summary=True)
    Traceback (most recent call last):
    ...
    ValueError: Target Score should be less than 25, if the game has no head cards

    >>> Generate_one_simulation(0 , target_score = 42, head_cards = True, head_card_value = 10, dealer_advantage = True, BJ_reward = 1.5, explosion=False, Summary=True, detail_summary=True)
    Traceback (most recent call last):
    ...
    ValueError: Target Score should take in account the head cards value

    >>> Generate_one_simulation(0 , target_score = 21, head_cards = True, head_card_value = 10, dealer_advantage = True, BJ_reward = 1, explosion=True, Summary=False, detail_summary=True)
    Traceback (most recent call last):
    ...
    ValueError: Summary should be True to print detail Summary
    '''
    ## Error Checking
    if not (isinstance(target_score, int) & \
            isinstance(head_cards, bool) & isinstance(head_card_value, int) & isinstance(dealer_advantage, bool) & \
            (isinstance(BJ_reward, float) | isinstance(BJ_reward, int)) & isinstance(explosion, bool) & \
            isinstance(Summary, bool) & isinstance(detail_summary, bool)):
        raise ValueError("Check the input datatype")

    # if not (isinstance(cumulative_win,float) | isinstance(cumulative_win, int) | isinstance(cumulative_win, np.int32)):
    #     raise ValueError("cumulative_win datatype wrong")

    if ((target_score <= 0 ) | (target_score >= 100)):
        raise ValueError("Target Score should be in range 0 to  100 (not inclusive 0 and 100)")

    if head_cards == False:
        ## Without head card the total score for 7 players and one dealer be  will be 220/8 = 27.5
        ## But some players will be above the total score and some will be below, so we assume 25 is good
        if target_score > 25:
            raise ValueError("Target Score should be less than 25, if the game has no head cards")
    else:
        ## There are 12 head cards in a game
        ## 7 Player and 1 dealer
        if target_score > 25 + ((head_card_value*12)/8):
            raise ValueError("Target Score should take in account the head cards value")

    if not Summary:
        if detail_summary:
            raise ValueError("Summary should be True to print detail Summary")



    game_instance = Game(target_score, head_cards, head_card_value, explosion)
    game_instance.creating_player_instance()
    game_instance.contender_game()
    game_instance.dealer_game(dealer_advantage)
    dealer_winning = game_instance.win_loss(BJ_reward)[1]
    cumulative_win += dealer_winning
    if Summary:
        print(f"Dealers cumulative winning: ${cumulative_win}")
        print(f"Dealer Won: ${dealer_winning}")

        game_instance.summary(detail_summary)
    return dealer_winning, cumulative_win


if __name__ == '__main__':
    df = simulation(2, target_score=21, head_cards= True, head_card_value=10, dealer_advantage = True,BJ_reward = 1.5, explosion = False, Summary = False, detail_summary = False)
    print(df)