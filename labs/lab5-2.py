# Lab 5 stuff
# Author: Connor Clark

from math import *


def main():
    sleepy()
    ascend()
    loopy()
    triangle()


def triangle():
    """Problem 12 on lab 5"""
    a = eval(input("Enter the length of side a: "))
    b = eval(input("Enter the length of side b: "))
    hyp = eval(input("Enter the length of the hypotenuse: "))
    triangle = False

    if (a ** 2) + (b ** 2) > hyp ** 2:
        triangle = True

    if not triangle:
        print("Triangle not possible!")
    else:
        print("Triangle possible! Here is the data: ")
        angleA = degrees(acos((b ** 2 + hyp ** 2 - a ** 2) / (2 * (b * hyp))))
        angleB = degrees(acos((hyp ** 2 + a ** 2 - b ** 2) / (2 * (hyp * a))))
        angleC = 180 - angleA - angleB
        print("A: " + str(a) + "\n Angle A: " + str(round(angleA, 2)) +
              "\n B: " + str(b) + "\n  Angle B: " + str(round(angleB, 2)) +
              "\n C: " + str(hyp) + "\n Angle C: " + str(round(angleC, 2)))


def loopy():
    """Problem 11 for lab 5"""
    num = 0.0
    while not isinstance(num, int):
        num = eval(input("Enter a positive integer: "))
        if isinstance(num, float):
            print("Please enter an int!")
        elif num < 0:
            print("Please enter a positive int!")
            num = 0.0
    sum = 0
    loop = 1
    while loop <= num:
        sum += loop
        loop += 1
    print(sum)
    fact = 1
    loop2 = 1
    while loop2 <= num:
        fact *= loop2
        loop2 += 1
    print(fact)


def ascend():
    """Problem 10 for lab 5"""
    x = eval(input("enter a number: "))
    y = eval(input("enter a number: "))
    z = eval(input("enter a number: "))
    # Re order nums
    first, second, third = 0, 0, 0
    # get biggest
    if x >= y and x >= z:
        first = x
    elif y >= x and y >= z:
        first = y
    else:
        first = z

    if first == x:
        if y >= z:
            second = y
            third = z
        else:
            second = z
            third = y
    elif first == y:
        if x >= z:
            second = x
            third = z
        else:
            second = z
            third = x
    elif first == z:
        if x >= y:
            second = x
            third = y
        else:
            second = y
            third = x

    print(first, second, third)


def sleepy():
    """Problem 9 for lab 5"""
    tired = input("Are you tired? (y/n): ")
    if tired == 'y' or tired == 'Y' or tired == 'Yes':
        print("You should get more sleep!")
    elif tired == 'n' or tired == 'N' or tired == 'No':
        print('Good job getting sleep!')
    else:
        print("I told you to enter y or n...")
    print("Have a good day!")


main()
