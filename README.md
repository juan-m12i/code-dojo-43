# Code-Dojo-43

Code for the 43rd London Code Dojo meetup in July 2018, Go Fish! kata. 

Write a simple terminal app to allow two players to play the card game ‘Go Fish!’. The rules are:

* Each player is dealt seven cards from an ordinary shuffled 52-card deck;
* Each player takes a turn to ask the other player for all the cards they have of a certain value e.g. ‘give me all your kings’, they must have at least one card of that value;
* Either: 
  a) the asked player hands over the cards, a 'catch', and the asking player’s turn continues, or
  b) the asked player has none and says ‘go fish!’, and it becomes their turn, and the asking player picks up another card from the deck;
* When a player acquires four of a kind (a ‘book’), they lay them face up on the table;
* When all the books are won, the game ends;
* The player with the most books wins.

## Scheme example

Look in the `racket` folder. Run `make test` to run the tests.
