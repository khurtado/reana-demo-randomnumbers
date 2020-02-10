# -*- coding: utf-8 -*-

from __future__ import absolute_import, print_function

import argparse
import errno
import os
import sys
import time
import socket
import random

def generate(seed=1, maxlimit=100, outputfile="results/random.txt", sleeptime=0.0):
    """Generate random number

    :param seed: Random seed
    :param outputfile: The relative path to the file where greeting
        should be stored. Creates the file if it does not exist.
    :param sleeptime: A waiting period (in seconds)

    """
    # ensure output directory exists:
    # influenced by http://stackoverflow.com/a/12517490
    if not os.path.exists(os.path.dirname(outputfile)):
        try:
            os.makedirs(os.path.dirname(outputfile))
        except OSError as exc:  # guard against race condition
            if exc.errno != errno.EEXIST:
                raise

    
    # generate number:
    random.seed(seed)
    x = random.randint(0, maxlimit)

    # write number
    with open(outputfile, "w+") as f:
        f.write("{}\n".format(x))
    time.sleep(sleeptime)
    return


if __name__ == '__main__':
    args = sys.argv[1:]

    parser = argparse.ArgumentParser()

    parser.add_argument("-o", "--outputfile",
                        help="Relative path to the file where greeting \
                                  should be stored. \n \
                                  [default=results/greetings.txt]",
                        default="results/greetings.txt",
                        required=False)

    parser.add_argument("-s", "--sleeptime",
                        help="Waiting period (in seconds) between \
                                  writing characters of greeting. \n \
                                  [default=1]",
                        default=1.0,
                        type=float,
                        required=False)

    parser.add_argument("-S", "--seed",
                        help="Random seed \
                                  [default=1]",
                        default=1.0,
                        type=int,
                        required=False)

    parser.add_argument("-m", "--maxlimit",
                        help="Max upper limit \
                                  [default=100]",
                        default=100,
                        type=int,
                        required=False)


    parsed_args = parser.parse_args(args)

    generate(parsed_args.seed, parsed_args.maxlimit, parsed_args.outputfile, parsed_args.sleeptime)
