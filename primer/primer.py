#! /usr/bin/env python

"""
Package of prime number objects.
"""

from functools import reduce


def _prod(s):
    """Compute the product of all the elements in a sequence."""

    return reduce(lambda x, y: x * y, s)


def primes(n):
    """
    Compute the sequence of the first n primes.

    primes(n) -> [2, 3, 5, ..., Pn]

    where Pn is the nth prime number.
    """

    p = []
    if n > 0:
        p = [2, ]
        for x in range(1, n):
            q = p[-1] + 1
            while True:
                for y in p:
                    if not (q % y):
                        break
                else:
                    p.append(q)
                    break
                q += 1
    return p


def prime(n):
    """
    Compute the nth prime.

    prime(n) -> Pn

    where Pn is the nth prime number.
    """

    return primes(n)[-1]


def primorial(n):
    """Compute the nth primorial.

    primorial(n) -> Pn#

    where Pn# is the nth primorial number.
    """

    return _prod(primes(n))


def sieve(n):
    """
    Compute the sequence of primes less than n.

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
