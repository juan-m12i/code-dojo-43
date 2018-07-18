# Go Fish! kata handout

## Go Fish! rules of play

Write a simple app to allow a player to play the card game ‘Go Fish!’ against the computer. A command-line/terminal app is all that is required, no GUI is necessary. Keep It Stupidly Simple (KISS).

* Each player is dealt seven cards from an ordinary shuffled 52-card deck;
* Each player takes a turn to ask the other player for all the cards they have of a certain value e.g. ‘give me all your kings’, they must have at least one card of that value;
* Either:
  - the asked player hands over the cards, a 'catch', and the asking player’s turn continues, or
  - the asked player has none and says ‘go fish!’, and it becomes their turn, and the asking player picks up another card from the deck;
* When a player acquires four of a kind (a ‘book’), they lay them face up on the table;
* When all the books are won, the game ends;
* The player with the most books wins.

## Simple Design

Simple Design is code that:

* Passes all the tests
* Is clear, expressive and consistent
* Duplicates no behaviour or configuration
* Minimises the number of moving parts

## Refactoring

* Make sure all the tests pass
* Make a small change to the design of the code that improves it
* Make sure all the tests still pass
