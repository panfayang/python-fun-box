## Problem 2:
"""
This is the and of bulls and cows, for python IDLE/command line/Terminal.
Upon running, the computer picks a random integer of 4-6 unique digits, and you would like to guess it.
In this setting, you have 5 chances to guess it right, but you can change the number of your tries at the last line.
After 5 times of failure or one time success, a message will acknowledge your failure/success and display the random number.
"""
__author__ = "Fayang Pan"
__date__ = "Date: 7/5/13"
import random

def randNumGen(n):
    """
    This internal function generates a number with n unique digits.
    0 < n < 11
    """
    numList = []
    for i in range(1,10):
        numList.append(i)
    first = random.choice(numList)
    numList.remove(first)
    numList.append(0)
    finalNum = str(first)

    for i in range(n-1):
        temp = random.choice(numList)
        numList.remove(temp)
        finalNum += str(temp)
    return int(finalNum)

def checkUnique(num):
    """
    This function checks if all digits of the number are unique.
    """
    numDict = {}
    for i in str(num):
        if i in numDict:
            return False
        numDict[i] = 1
    return True

def bullsAndCows(actual):
    """
    This internal function compares and returns the result of bulls and cows.
    """
    actualStr = str(actual)
    numDigits = len(actualStr)
    guess = raw_input("Please enter a positive integer with %d digits of unique numbers:" %numDigits)

    ## Check if the input is a valid one.
    while True:
        try:
            guess = int(guess)
            guessStr = str(guess)
            assert((len(guessStr) == numDigits) and (type(guess) is int) and (guess>0) and (checkUnique(guess) is True)), "Requirement not met"
            break
        except (ValueError,AssertionError):
            guess = raw_input("Please be serious and enter a positive integer with %d digits of unique numbers:" %numDigits)

    bulls = 0
    cows = 0
    guessLi = []
    actualLi = []
    
    ## This is to fetch the results of bulls by comparing two digits in the same place.
    for i in range(numDigits):
        guessLi.append(guessStr[i])
        actualLi.append(actualStr[i])
        if guessStr[i] == actualStr[i]:
            bulls += 1

    ## If every digit is in place, it's done.
    if bulls == numDigits:
        return "Hooray! You win! The number is: " + actualStr
    
    ## This is to fetch the results of cows.
    for i in actualLi:
        if i in guessLi:
            cows += 1
    cows = cows - bulls
    
    return str(bulls) + " bulls and " + str(cows) + " cows."


def playBC(numOfTries):
    """
    This is the play Bulls and Cows function
    numOfTries is the number of tries a person is allowed to have.
    """
    n = random.randrange(4,7)
    secret = randNumGen(n)
##For testing winning situation:
##    print secret
    counter = numOfTries
    print "Welcome to bulls and cows! You have %d chances" %counter
    while counter > 0:
        result = bullsAndCows(secret)
        print result
        ## Check if it's already won.
        if "Hooray" in result:
            return 
        counter = counter - 1
        print "now you have %d chances left!" %counter
    print "Sorry you lost... The number is %d" %secret
    return

if __name__ == "__main__":
    playBC(5)
