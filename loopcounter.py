def calculate(num):
    return num*3

loopCounter = 20

for x in range(loopCounter):
    value = int(input("Enter a number between 1 and 10 inclusive"))

    if value > 0 and value < 11:
        print(calculate(value))