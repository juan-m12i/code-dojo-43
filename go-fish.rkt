#lang racket/base

(require rackunit)

(test-case
 "Check unit tests work"
 (let ([plus +][mult *])
   (check-equal? (plus 41 1) 42 "Simple addition")
   (check-equal? (mult 6 9) 42 "Simple multiplication")))
