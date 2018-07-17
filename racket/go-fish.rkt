#lang racket/base

(require rackunit rackunit/text-ui)

(define first car)
(define second cadr)
(define suits '("Spade" "Heart" "Diamond" "Club"))
(define values '("2" "3" "4" "5" "6" "7" "8" "9" "10" "Jack" "Queen" "King" "Ace"))

(define (new-game)
  "Creates a new game object, with two players, each of which has seven cards"
  (list '(1 2 3 4 5 6 7) '(1 2 3 4 5 6 7)))

(define (draw-card)
  "Draws a random card, each card has a:
     Suit: one of Spade, Heart, Diamond or Club
     Value: one of 2,3,4,5,6,7,8,9,10,Jack,Queen,King or Ace"
  (list (list-ref values (random 1 13))
        (list-ref suits (random 1 4))))

(run-tests
  (test-suite
   "Go Fish! game tests"
   (test-case
    "Drawing a card should result in a card that is a Spade, Heart, Diamond or Club"
    (let ([card (draw-card)])
      (check-not-false (member (second card) suits))))

   (test-case
    "Drawing a card should result in a card that is a two to an Ace in value"
    (let ([card (draw-card)])
      (check-not-false (member (first card) values))))

   (test-case
    "Drawing a second card should be different from the first"
    (let ([first-card (draw-card)][second-card (draw-card)])
      (check-not-equal? first-card second-card "two consecutive draws should be different")))

   (test-case
    "A new game should have two players with seven cards each"
    (let ([my-game (new-game)])
      (check-equal? 2 (length my-game) "should have two players")
      (check-equal? 7 (length (first my-game)) "player one should have seven cards")
      (check-equal? 7 (length (second my-game)) "player one should have seven cards")))

   (test-case
    "Check unit tests work"
    (let ([plus +][mult *])
      (check-equal? (plus 41 1) 42 "Simple addition")
      (check-equal? (mult 6 7) 42 "Simple multiplication")))))

