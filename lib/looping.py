#!/usr/bin/env python3

def happy_new_year():
    """Prints a countdown from 10 to 1 and then 'Happy New Year!'."""
    i = 10
    while i > 0:
        print(i)
        i -= 1
    print("Happy New Year!")


def square_integers(int_list):
    """Takes a list of integers and returns a list of their squares."""
    return [x ** 2 for x in int_list]


def fizzbuzz():
    """Prints numbers from 1 to 100 with FizzBuzz rules."""
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)
