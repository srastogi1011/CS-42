#lang racket

(define (knapsack capacity items)
  (cond ((empty? items) (list 0 0 empty))
         ((<= capacity 0) (list 0 0 empty))
         (else (let ((First (first items))
                     (Rest (rest items)))
                 (cond ((> (first First) capacity) (knapsack capacity Rest))
                       (else (let* ((useit (knapsack (- capacity (first First)) Rest))
                                    (loseit (knapsack capacity Rest))
                                    (useit-total (+ (second First) (second useit)))
                                    (loseit-total (second loseit)))
                                (if (> useit-total loseit-total)
                                    (list (+ (first First) (first useit)) useit-total (cons First (third useit)))
                                    loseit))))))))

(define (test-knapsack capacity List)
  (let ((solution (knapsack capacity List) ))
    (begin
     (displayln (~a "\ncapacity " capacity ", (weight value) pairs: " List))
     (displayln (~a  "  weight " (first solution) ", value " 
                                 (second solution) ", items: "
                                 (third solution))))))

(test-knapsack 26 '((12 24) (7 13) (11 23) (8 15) (9 16)))
(test-knapsack 190 '((56 50) (59 50) (80 64) (64 46) (75 50) (17 5)))
(test-knapsack 50 '((31 70) (10 20) (20 39) (19 37) (4 7) (3 5) (6 10)))
(test-knapsack 104 '((25 350) (35 400) (45 450) (5 20) (25 70) (3 8) (2 5) (2 5)))
(test-knapsack 170 '((41 442) (50 525) (49 511) (59 593) (55 546) (57 564) (60 617)))
(test-knapsack 165 '((23 92) (31 57) (29 49) (44 68) (53 60) (38 43) (63 67) (85 84) (89 87) (82 72)))
(test-knapsack 750 '((70 135) (73 139) (77 149) (80 150) (82 156) (87 163) (90 173) (94 184) (98 192) (106 201) (110 210) (113 214) (115 221) (118 229) (120 240)))
