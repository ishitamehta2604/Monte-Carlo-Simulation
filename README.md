Team Members:
Ishita Mehta, Karan Chhabra

# Monte Carlo Simulation: Variations of Blackjack
The aim of the project was to design a game which is equally profitable to club as Black jack and give the player decent chance of winning.

[![Blackjack Rules](https://github.com/ishitamehta2604/Monte-Carlo-Simulation/blob/main/Images%20of%20Graphs/Rules.jpg)]( https://www.youtube.com/watch?v=5bWpnABkU-Y&ab_channel=CrazyVegasOnlineCasino)

Assumptions:

•	Player decides to takes a stand at a score greater than or equal to 15 <br>
•	Dealer decides to take a stand at a score greater than or equal to 17 or he is currently winning more than or equal to half his bets against the players<br>
•	No Split in the game <br>
•	No Double in the game <br>
•	No Insurance around the bet

Random Variables:

•	Number of Players: Discrete Uniform Distribution <br>
•	Cards distributed to players: Discrete Uniform Distribution <br>
•	Players Bet: Discrete Uniform Distribution <br>

Variations:
•	Variable Target Score <BR>
This help to change the target score of the game from 21 to something else.  <BR>

•	If Game Should have Head Cards or not  <BR>
It help to determine if the game should have head face cards or not.  <BR>

•	Variable Value of Head Cards <BR>
Define the value of head cards other than 10. <BR>

•	Player cards are disclosed at the end of the game <BR>
Dealer can't know the cards of player till the end of the game. <BR>

•	Blackjack Reward <BR>
Changing the perfect black jack reward from 3:2(1.5 times) to something else.  <BR>

•	Explosion Card <BR>
The player or dealer who get this card losses <BR>

Hypothesis:

Blue line represents the basic black jack game
Orange line represents the game with the specific variations

1 - There will be no change in the dealer’s chances of winning, if the cards of both the player and dealer are disclosed at the end of the game.<br>
![Hypothesis 1](https://github.com/ishitamehta2604/Monte-Carlo-Simulation/blob/main/Images%20of%20Graphs/Hypothesis%201.png)

We reject the null hypothesis.


2 - There will be no change in the dealer’s chances of winning, if the player loses by receiving a Blackjack in the first two dealt cards.
![Hypothesis 2](https://github.com/ishitamehta2604/Monte-Carlo-Simulation/blob/main/Images%20of%20Graphs/Hypothesis%202.jpg)

We reject the null hypothesis.

3 - The players chances of winning does not change when the chosen head card value comes closer to the target score.
![Hypothesis 3](https://github.com/ishitamehta2604/Monte-Carlo-Simulation/blob/main/Images%20of%20Graphs/hypothesis3.jpg)
We reject the null hypothesis.

4 -There will be no change in the player’s chances of winning, When the target is increased or decreased over the default value of 21, keeping the other parameters constant
![Hypothesis 4](https://github.com/ishitamehta2604/Monte-Carlo-Simulation/blob/main/Images%20of%20Graphs/Hypothesis%204.jpg)

We reject the null hypothesis.


NEW GAME:
A game created with different combination of parameters which is a potentially good game to be played in a club along with black jack

Number of simulations: 100000 <br>
Target Score: 32 <br>
Head Card: True <br>
Head Card Value: 12 <br>
Should the Dealer be given the advantage: True <br>
Perfect Blackjack Reward: 200 <br>
Explosion card: True <br>

![NEW GAME](https://github.com/ishitamehta2604/Monte-Carlo-Simulation/blob/main/Images%20of%20Graphs/NEW%20GAME%20Variation.jpg)




References:

https://www.youtube.com/watch?v=5bWpnABkU-Y&ab_channel=CrazyVegasOnlineCasino <br>
https://www.247blackjack.com/ <br>
https://en.wikipedia.org/wiki/Blackjack <br>
http://www.bestonlinegambling.com/blackjack/variations/ <br>
https://uiuc-ischool-dataviz.github.io/is445AOG_fall2020/week05/ <br>
https://github.com/UIUC-iSchool-DataViz/fall2019 <br>
http://datagenetics.com/blog/march62020/index.html <br>
https://www.888casino.com/blog/blackjack-strategy-guide/how-to-play-blackjack  <br>
https://www.youtube.com/watch?v=5bWpnABkU-Y&ab_channel=CrazyVegasOnlineCasino  <br>
https://stackoverflow.com/questions/6181935/how-do-you-create-different-variable-names-while-in-a-loop  <br>
https://www.geeksforgeeks.org/print-without-newline-python/  <br>
https://www.compart.com/en/unicode/U+1F4A3  <br>
https://www.youtube.com/watch?v=IsklrLQE88Y&ab_channel=AllTech  <br>
https://www.bowl.com/rules/Rules_Home/USBC_Playing_Rules/ <br>
https://github.com/iSchool-597PR/2020Fall_A5
