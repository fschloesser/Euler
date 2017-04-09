# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

(use numbers)

(define fib 
  (lambda (x)
    (case x 
      ((0 1) 1) 
      (else (+ 
	     (fib (- x 1))
	     (fib (- x 2)))))))

(define msum 
  (lambda (x)
    (define y (fib x))
    (if (< y 4e6)
	(if (eq? (modulo y 2) 0)
	    (+ y (msum (+ x 1)))
	    (msum (+ x 1)))
	0)))

(display (msum 1))
