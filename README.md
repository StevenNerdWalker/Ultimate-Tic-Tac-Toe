
# **ULTIMATE TIC TAC TOE**

This project aims to recreate the game 'Ultimate Tic Tac Toe', originally proposed by Ben Orlin at [Math With Bad Drawings](https://mathwithbaddrawings.com/ultimate-tic-tac-toe-original-post/), who later [updated](https://mathwithbaddrawings.com/2013/06/16/ultimate-tic-tac-toe/) some of the original rules to make the game more balanced. This game is a more interesting, entertaining, and strategic version of the old classic Tic-Tac-Toe.

## **The game**

In regular tic-tac-toe, we have a 3x3 board with a total of 9 squares, but in this version, we draw a smaller board in each square of the tic-tac-toe board, which looks something like this:

![Board template](https://i0.wp.com/mathwithbaddrawings.com/wp-content/uploads/2013/06/2-blank-board.jpg 'Board template')

Here are the main rules:

### **The rules**

1.Each turn, you mark one of the small squares
2.When you get three in a row on a small board, you’ve won that board
3.To win the game, you need to win three small boards in a row

And the most important rule of the game:

**You don’t get to pick which of the nine boards to play on.** That’s determined by your opponent’s previous move. **Whichever ***square*** he picks, that’s the ***board*** you must play in next.** (And whichever square you pick will determine which board he plays on next)

For example, if I go here…

![First move](https://i0.wp.com/mathwithbaddrawings.com/wp-content/uploads/2013/06/3-first-move.jpg 'First move')

Then your next move must be here…

![Second move](https://i0.wp.com/mathwithbaddrawings.com/wp-content/uploads/2013/06/4-second-move.jpg 'Second move')

This lends the game a strategic element. You can’t just focus on the little board. You’ve got to consider where your move will send your opponent, and where his next move will send you, and so on.

The resulting scenarios look bizarre. Players seem to move randomly, missing easy two- and three-in-a-rows. But there’s a method to the madness – they’re thinking ahead to future moves, wary of setting up their opponent on prime real estate. It is, in short, vastly more interesting than regular tic-tac-toe.

Still, A few clarifying rules are necessary:

1-*What if my opponent sends me to a board that’s already been won?*
In that case, congratulations – you get to go anywhere you like, on any of the other boards. (This means you should avoid sending your opponent to an already-won board!)

2-*What if one of the small boards results in a tie?*
In this version, the board counts for neither X nor O. But, if you feel like a crazy variant, you could change the code to count a tied board for both X and O
