#! /usr/bin/env python

"""
Package of prime number objects.
"""

from functools import reduce


def _prime_generator_function():
    """Return a generator for prime numbers."""

    p = [2, ]
    while True:
        yield p[-1]
        q = p[-1] + 1
        while True:
            for x in p:
                if not (q % x):
                    break
            else:
                p.append(q)
                break
            q += 1


_pgf = _prime_generator_function


def primes(n):
    """
    Return the sequence of the first n primes.

    primes(n) -> [2, 3, 5, ..., Pn]

    where Pn is the nth prime number.
    """

    pg = _pgf()
    return [next(pg) for x in range(n)]


def prime(n):
    """
    Return the nth prime.

    prime(n) -> Pn

    where Pn is the nth prime number.
    """

    return primes(n)[-1]


def primorial(n):
    """Return the nth primorial.

    primorial(n) -> Pn#

    where Pn# is the nth primorial number.
    """

    return reduce(lambda x, y: x * y, primes(n))


def sieve(n):
    """
    Return the sequence of primes less than n.

    sieve(n) -> (2, 3, 5, ..., Px)

    where Px is the greatest prime less than n.

    Uses the Sieve of Eratosthenes algorithm.
    """

    p = list(range(2, n))
    for x in range(0, (n // 2) - 1):
        if p[x]:
            y = (x + 1) * 2
            z = x + 2
            m = len(p[y::z])
            p[y::z] = [0] * m
    return [q for q in p if q]
