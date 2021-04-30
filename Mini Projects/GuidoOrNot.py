""" GuidoOrNot.py
    Illustrates if - else structure
    Say something nice if the user's name is Guido
    and asks for Guido if user enters another name. """

firstName = input("What is your first name? ")
firstName = firstName.title()
print("Nice to see you, " + firstName + ".")

if(firstName.upper() == "GUIDO"):
    print("Hey, thanks for inventing Python!")
elif(firstName.upper() == "NATHAN"):
    print("Allo Natan, 'ave you seen Guido around?")
else:
    print("Where is Guido?")
