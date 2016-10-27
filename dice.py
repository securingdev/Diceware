""" 
This is an example of the Random Number Generation, and subsequent random 
word selection process, which I am hoping to port to both Java and C or C++.


@author K. M. Hoodlet

Version 1.11 : 08/29/2016
"""

##=========================================================================
import os
from os import urandom
import random
from random import SystemRandom
import re

random.seed(os.urandom(1024))

words = []
groups = []
wordlist = [None] * 55555

##=========================================================================
## Collect all numbers and associated words

with open('eff_large_wordlist.txt') as f:
    for line in f:
        match = re.search('(\d{5}).(.*)', line)
        if match:
            location = int(match.group(1))
            location = (location - 11111)
            wordlist.insert(location, match.group(2))

##=========================================================================
## Retrieve a Securely Random number.

def get_rand():

    n = SystemRandom( os.urandom(1024) ).getrandbits(3)

    if ( n == 0 or n == 7 ):
        n = get_rand()

    return n

##=========================================================================
## Retrieve $count sets of numbers

def random_numbers(count):

    numbers = []
    count = str(count)
    # Check for integer values & intelligent count size.
    if (count.isdigit() and int(count) > 0):

        for i in range(0, int(count)):
            values = ""

            # Fill the list "numbers".
            for i in range(5):
                numbers.append(get_rand())

            # Concatenate the items in "numbers" into a single string.
            for number in numbers:
                values += str(number) 

            # Reset "numbers" and append "values" to the "groups" list.
            numbers = []
            groups.append(int(values))
    else:
        count = raw_input("Please enter a positive number: ")
        random_numbers(count)

##=========================================================================
## Request a number of passwords to generate and then perform the
## "random_numbers" function $count number of times.

count = raw_input("How many words would you like to generate? ")
random_numbers(count) 

##=========================================================================
## Append the numbers retrieved and associated words to the output list

for g in groups:
    number = int(g)
    word = wordlist[number-11111]
    words.append(str(number) + "     " + word)

##=========================================================================
## Print the words onto the display.

print " "

for w in words:
    print w

print " "
