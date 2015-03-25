#! /usr/bin/env python

"""
A __main__ namespace for the primer package.
"""

import sys
import argparse
from time import time
from primer import primes


def main(argv):
    """Call primes when the package is run as a script."""

    parser = argparse.ArgumentParser(
        prog='primes',
        description='Display the first N primes.',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('number',
                        metavar='N',
                        nargs='?',
                        default='100',
                        help='Number of primes to generate')
    parser.add_argument('-t',
                        action='store_true',
                        help='Display elapsed time')
    args = parser.parse_args(argv)

    try:
        number = int(args.number, 0)
        if args.t:
            start = time()
        print " ".join([str(n) for n in primes((number))])
        if args.t:
            print
            print "Elapsed time is {} seconds.".format(time() - start)
    except Exception as e:
        parser.print_help()
        print
        print e


if __name__ == '__main__':
    main(sys.argv[1:])
