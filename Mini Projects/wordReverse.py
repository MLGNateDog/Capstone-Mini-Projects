""" wordReverse.py
    demostrates how to use loops
    for sting manipulation
    17 Jan 2021"""

inWord = input("Please type a word or phrase: ")
outWord = " "

# remember, I want to count backwards to character zero, so negative one is the boundary

firstChar = -1

# The length of the word is how many charcters are in it, the last character  in the word is word length minus one.

maxIndex = len(inWord) - 1

# Go backwords from the last character to the first character counting by negative one each time through the loop

for charPos in range(maxIndex, firstChar, -1):

    #Add the current character to the output string

    outWord += inWord[charPos]

#After the loop is finished, print our the results

print(outWord)
