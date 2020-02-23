#lang racket
;;; Machine Simulator
;;; Author: Sidhant Rastogi
;;; Date: 7 October 2019

;;; Enumerate all strings accepted by a machine up to a specified length
;;; showing the name of the machine first, if one is specified.
(define (enumerate-accepted machine alphabet length)
  (let ((name (assoc 'name (nice-rest machine))))  ;; rest because first is machine type
    (begin
      (if name (println (second name)) null)
      (display-list (extract-accept (sim-to length machine alphabet))))))

;;; Simulate a machine for all inputs up to a specified length
;;; returning a list of pairs: (outcome input).
(define (sim-to length machine alphabet)
  (let ((inputs (enumerate-to length alphabet)))
    (map (lambda (input) (list (sim machine input) input)) inputs)))

(define (nice-first l)
  (if (empty? l)
      '(b)
      (first l)))

(define (nice-rest l)
  (if (empty? l)
      '(b)
      (rest l)))

;;; General machine simulator
(define (sim machine input)
  (let ((machine-type (nice-first machine)))
  (cond ;; eventually there will be other kinds of machines besides fsa
    ((equal? machine-type 'fsa) (sim-fsa (nice-rest machine) input))
    ((equal? machine-type 'tm) (sim-tm (nice-rest machine) input))
    (else (mk-error  "unrecognized machine type" machine)))))

;;; Finite-state acceptor specific simulator, top-level
(define (sim-fsa machine-parts input)
  (let ((errors (check-validity-fsa machine-parts)))
    (if (empty? errors)
        (let (
              (initial     (second (assoc 'initial machine-parts)))
              (accepting     (nice-rest (assoc 'accepting machine-parts)))
              (transitions   (nice-rest (assoc 'transitions machine-parts)))
              )
          (sim-fsa-loop transitions initial accepting input))
        (mk-error "errors: " errors))))

;;; Turing machine specific simulator, top-level
(define (sim-tm machine-parts input)
  (let ((errors (check-validity-tm machine-parts)))
    (if (empty? errors)
        (let (
              (blank     (second (assoc 'blank machine-parts)))
              (initial     (second (assoc 'initial machine-parts)))
              (accepting     (nice-rest (assoc 'accepting machine-parts)))
              (rejecting     (nice-rest (assoc 'rejecting machine-parts)))
              (transitions   (nice-rest (assoc 'transitions machine-parts)))
              )
          (sim-tm-loop transitions initial accepting rejecting blank '() input))
        (mk-error "errors: " errors))))

;;; Check the validity of an FSA specification, returning a list of errors.
;;; If there are no errors, an empty list will be returned.
(define (check-validity-fsa machine-parts)
  (let
      ((initial     (assoc 'initial machine-parts))
       (accepting   (assoc 'accepting machine-parts))
       (transitions (assoc 'transitions machine-parts))
       )
    (append ;; append any issues found into one list
     (if initial     empty '((no initial state)))
     (if accepting   empty '((no accepting states)))
     (if transitions empty '((no transitions))))))


;;; Check the validity of a TM specification, returning a list of errors.
;;; If there are no errors, an empty list will be returned.
(define (check-validity-tm machine-parts)
  (let
      ((blank       (assoc 'blank machine-parts))
       (initial     (assoc 'initial machine-parts))
       (accepting   (assoc 'accepting machine-parts))
       (rejecting   (assoc 'rejecting machine-parts))
       (transitions (assoc 'transitions machine-parts))
       )
    (append ;; append any issues found into one list
     (if blank       empty '((no blank state)))
     (if initial     empty '((no initial state)))
     (if accepting   empty '((no accepting states)))
     (if rejecting   empty '((no rejecting states)))
     (if transitions empty '((no transitions))))))

;;; Possible outcomes of one simulation
(define ACCEPT 'accept)
(define REJECT 'reject)

;;; Extract only the ACCEPT outcomes from a list of pairs
;;; and return a list of the corresponding inputs.
(define (extract-accept outcomes)
  (map second (filter (lambda (x) (equal? ACCEPT (nice-first x))) outcomes)))

;;; Simulate a finite-state acceptor given machine parts.
(define (sim-fsa-loop transitions current-state accepting input)
  (if (null? input)
      (if (member current-state accepting) ;; The input is empty, so indicate the outcome
          ACCEPT
          REJECT)
      (let ((current-symbol (nice-first input))                 ;; Input is not empty, keep going
            (row (assoc current-state transitions)))       ;; Find the state among transitions
        (if (not row)
            (mk-error "state not found:" current-state)    ;; Intended state not found
            (let ((col (assoc current-symbol (nice-rest row)))) ;; Find state-input combination
              (if (not col)
                  (mk-error "next-state not found for" (list current-state current-symbol))
                  (let ((next-state (second col)))         ;; Get the next state and continue
                    (sim-fsa-loop transitions next-state accepting (nice-rest input)))))))))

;;; Simulate a Turing machine given machine parts.
(define (sim-tm-loop transitions current-state accepting rejecting blank left-tape right-tape)
  (cond
    ((member current-state accepting) ACCEPT) ;;if the current state is accepting, immediately accept
    ((member current-state rejecting) REJECT)
    (else
       (let ((current-symbol (
                              if (empty? right-tape)
                                 blank
                                 (nice-first right-tape)))
      ;(let ((current-symbol (nice-first right-tape))            ;; Current state is not accepting, keep going
            (row (assoc current-state transitions)))       ;; Find the state among transitions
        (if (not row)
            REJECT                                         ;; Intended state not found
            (let ((col (assoc current-symbol (nice-rest row)))) ;; Find state-input combination
              (if (not col)
                  REJECT
                  (let ((next-state (second col)))
                    (cond
                        ((equal? (fourth col) 'right)
                          (let ((new-left (cons (third col) left-tape))
                                (new-right (nice-rest right-tape)))
                                (sim-tm-loop transitions next-state accepting rejecting blank new-left new-right)))
                        ((equal? (fourth col) 'left)
                          (let ((new-left (nice-rest left-tape))
                                (new-right (cons (nice-first left-tape) (cons (third col) (nice-rest right-tape)))))
                                (sim-tm-loop transitions next-state accepting rejecting blank new-left new-right)))
                        (else
                          (let ((new-right (cons (third col) (nice-rest right-tape))))
                                (sim-tm-loop transitions next-state accepting rejecting blank left-tape new-right))))))))))))


;;; Enumerate all strings over alphabet of a specified length.
(define (enumerate-at length alphabet)
  (if (<= length 0)
      '(())
      ;; Recursively enumerate strings at shorter length, then combine into one list
      (let ((sub-enumeration (enumerate-at (- length 1) alphabet)))
          (mappend (lambda(x) (map (lambda(y) (cons x y)) sub-enumeration)) alphabet))))

;;; Enumerate all strings over alphabet up to a specified length in increasing-length order.
(define (enumerate-to length alphabet)
  (if (<= length 0)
      '(())
      (append (enumerate-to (- length 1) alphabet)
              (enumerate-at length alphabet))))

;;; Utility: Map a function that returns lists over a list, then append results.
(define (mappend fun lol)
  (foldr append '() (map fun lol)))

;;; Display a list of elements one line at a time.
(define (display-list L)
  (if (null? L)
      (newline)
      (begin (writeln (nice-first L)) (display-list (nice-rest L)))))

;;; Cause an error message to be displayed along with the irritant.
(define (mk-error message irritant)
  (error (~a (list "error:" message irritant))))

;;; Some example machines

(define mod3 '(fsa
    (name "mod3")
    (initial 0)
    (accepting 0)
    (transitions
     (0 (0 0) (1 1))
     (1 (0 2) (1 0))
     (2 (0 1) (1 2))
     )))




(define 0-star-or-1-star '(fsa
    (name "0-star-or-1-star")
    (initial a)
    (accepting a b c)
    (transitions
     (a (0 b) (1 c))
     (b (0 b) (1 d))
     (c (0 d) (1 c))
     (d (0 d) (1 d)))))

(define ends-in-01 '(fsa
    (name "ends-in-01")
    (initial a)
    (accepting c)
    (transitions
     (a (0 b) (1 a))
     (b (0 b) (1 c))
     (c (0 b) (1 a)))))

(define odd-number-of-1s '(fsa
    (name "odd-number-of-1s")
    (initial a)
    (accepting b)
    (transitions
     (a (0 a) (1 b))
     (b (0 b) (1 a)))))

(define product-odd-1s-and-ends-01  ;; The product of the two preceding machines
  '(fsa                             ;; deciding the intersection of their languages
    (name "product-odd-1s-and-ends-01")
    (initial (a a))                 ;; States are pairs from the original machines.
    (accepting (c b))
    (transitions
     ((a a) (0 (b a)) (1 (a b)))
     ((a b) (0 (b b)) (1 (a a)))
     ((b a) (0 (b a)) (1 (c b)))
     ((b b) (0 (b b)) (1 (c a)))
     ((c a) (0 (b a)) (1 (a b)))
     ((c b) (0 (b b)) (1 (a a))))))

(define wwr
  '(tm
    (name "wwr")
    (blank b)
    (initial a)
    (accepting h)
    (rejecting r)
    (transitions
     (a (0 0 b right) (1 1 b right) (b h b none))
     (0 (0 0 0 right) (1 0 1 right) (b 2 b left))
     (1 (0 1 0 right) (1 1 1 right) (b 3 3 left))
     (2 (0 5 b left))
     (3 (1 5 b left))
     (5 (0 5 0 left) (1 5 1 left) (b a b right)))))

(enumerate-accepted wwr '(0 1) 8)
