""" raceAnnouncer.py
    demonstrates numeric comparisons and
    elif """

for lap in range(1, 11):
    print("lap", lap)

    if(lap == 1):
        print("Starting the race")
    elif(lap < 5):
        print("Still in the first half")
    elif(lap == 5):
        print("Halfway there...")
    elif(lap == 10):
        print("Finished!")
    elif(lap >= 6):
        print("Getting closer...")
    else:
        print("Something went wrong")

    print("Another great lap")
    print()

print("That was quite a race!")
