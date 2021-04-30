""" password.py
    Ask the user for a password
    repear until user gets it right
    or has tried three times """

keepGoing = True
correct = "Python"
tries = 3

while keepGoing:
    guess = input("Please enter the password: ")
    tries -= 1

    if guess == correct:
        print("You may proceed")
        keepGoing = False
    else:
        print("That's not correct.")

        if tries <= 0:
            print("Sorry, you only had three tries")
