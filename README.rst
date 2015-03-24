Brute force primes demo
=======================

To use as a package:

    >>> import primes
    >>> primes.primes(10)
    [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    >>> primes.prime(10)
    29
    >>> pg = primes.pgf()
	>>> pg.next()
	2
	>>> pg.next()
	3
	>>> pg.next()
	5
	>>>

To use as a script:

	usage: python -m primes [-h] [-t] [N]

	Display the first N primes.

	positional arguments:
	  N           Number of primes to generate (default: 100)

	optional arguments:
	  -h, --help  show this help message and exit
	  -t          Display elapsed time (default: False)
