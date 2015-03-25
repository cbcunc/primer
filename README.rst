A primer for prime numbers
==========================

Brute force functions for teaching purposes. Not performant.

To use as a package:

    >>> import primer
    >>> primer.primes(10)
    [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    >>> primer.prime(10)
    29
    >>> primer.primorial(10)
    6469693230
    >>> pg = primer.pgf()
    >>> pg.next()
    2
    >>> pg.next()
    3
    >>> pg.next()
    5
    >>>

To use as a script:

    $ python -m primer [-h] [-t] [N]

    Display the first N primes.

    positional arguments:
      N           Number of primes to generate (default: 100)

    optional arguments:
      -h, --help  show this help message and exit
      -t          Display elapsed time (default: False)
