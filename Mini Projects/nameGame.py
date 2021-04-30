""" nameGame.py
    illustrate basic string functions
    Nathan Harris
    01/Jan/21
    """
userName = input("Please tell me your name: ")
print("I will shout your name: ", userName.upper())
print("Now I shall whisper your name: ", userName.lower())
print("How about inverting the case? ", userName.swapcase())
numChars = len(userName)
print("Your name has ", numChars, " characters")
print("Now I'll pronounce your name like a cartoon characer: ")
userName = userName.upper()
username = userName.replace("R", "W")
userName = userName.title()
print(userName)
