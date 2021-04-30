numbers = [2, 2, 4, 4, 6, 6, 7, 7]
uniques = []
for number in numbers:
    if number not in uniques:
        uniques.append(number)
print(uniques)