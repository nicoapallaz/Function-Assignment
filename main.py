import math


def circleArea(radius):
    area = math.pi * radius ** 2
    return round(area, 2)

def totalDue(money, tax):
    total = money + (money * tax)
    return round(total, 2)

def ftoc(fahrenheit):
    celsius = (fahrenheit - 32) * (5/9)
    return round(celsius, 4)

radius = int(input("Enter the radius of the circle: "))
print(circleArea(radius))
money = int(input("Enter the amount of money: "))
tax = float(input("Enter the tax (6% = .06): "))
print(totalDue(money, tax))
fahrenheit = int(input("Enter the temperature in Fahrenheit: "))
print(ftoc(fahrenheit))