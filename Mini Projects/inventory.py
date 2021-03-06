""" inventory.py
    demonstrates lists
    03/Jan/21 """

inventory = [
    "toothbrush",
    "suit of armour",
    "latte espresso",
    "crochet hook",
    "towel"]

print("I packed these things for my adventures: ")
print(inventory)
print()

print("I love my", inventory[2], "and my", inventory[4])
print()

print("my first few items: ")
print(inventory[:3])
print()

print("third item:", inventory[3])
print()

print("changing third item...")
inventory[3] = "doily"
print("third item is now: ", inventory[3])
print()

print("revised inventory: ")
print(inventory)
print()

print("adding kitchen sink")
inventory.append("kitchen sink")
print(inventory)
print()

print("never mind... I don't need that")
inventory.remove("kitchen sink")
print(inventory)
print()
