""" Calc.py
    given any two values, calculates the sum, difference, product, and quotient
    of those two values
    03/Jan/21 """

x = float(input("first number: "))
y = float(input("second number: "))


sum = x + y
difference = x - y
product = x * y
quotient = x/y

print(x, " + ", y, " = ", sum)
print(x, " - ", y, " = ", difference)
print(x, " * ", y, " = ", product)
print(x, "/", y, " = ", quotient)
