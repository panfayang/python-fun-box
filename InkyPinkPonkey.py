"""
Welcome to the game of inkyPinkyPonkey!
Assume there is a chant of k words, and there are n kids sitting in a circle.
Starting from the first kid, they each chant one word of the chant in turn, and whoever finishes the chant is out.
Then the chant start again from the next kid, and the kid who gets the last word is out again.
The last one standing is the winner.
"""
__author__ = "Fayang Pan"
__date__ = "Date: 7/5/13"

def inkyPinkyPonkey(k,n):
        """
        k is the number of words in the Chant,
        n is the number of kids.
        The game starts from the first kid.
        This function returns the final winner of the game.
        """
        print "The game of InkyPinkyPonkey begins!"
        assert (type(k)==type(n)==int and  k>0 and n>0), "Please enter Positive integers!"
        kidLi = []
        for i in range(1,n+1):
                kidLi.append(i)
        tempPos = 0
        for i in range(n-1):
                tempPos = (tempPos + k)%(n-i)-1
                if tempPos == -1:
                        tempPos = len(kidLi)-1
                print "child number " + str(kidLi.pop(tempPos)) + " is out."
        return "child number " + str(kidLi.pop(0)) + " wins!"

print inkyPinkyPonkey(3,5)
##print inkyPinkyPonkey(1,1)
