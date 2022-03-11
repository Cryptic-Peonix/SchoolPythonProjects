# Program to compute the quadratic formula.
# 2/24/2022
# Author: Connor Clark.

import math


def main():
    xsquared = eval(input("Enter the amount of x squared values: "))
    x = eval(input("Enter the amount of x's: "))
    constant = eval(input("Enter the constant: "))

    if ((x**2) - (4 * xsquared * constant)) < 0:
        print("Answer: Undefined")
        exit(0)

    anspos = -x + (math.sqrt((x**2) - (4 * xsquared * constant))) / 2 * xsquared
    ansneg = -x - (math.sqrt((x**2) - (4 * xsquared * constant))) / 2 * xsquared

    print("\n" + "Answer 1: " + str(anspos))
    print("Answer 2: " + str(ansneg))


main()
