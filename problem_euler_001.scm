# if we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.

(define ir? 
  (lambda (x)
    (or (eq? (modulo x 3) 0) (eq? (modulo x 5) 0))))

(define msum 
  (lambda (x)
    (case x
      ((0) 0)
      (else  
       (if (ir? x)
	   (+ x (msum (- x 1))) 
	   (msum (- x 1)))))))

(display (msum 999))
(newline)
(exit)
