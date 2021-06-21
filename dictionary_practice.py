grocery_list = {"chicken":1.59, "beef":1.99, "cheese":1.00, "milk":2.50, "coke":1.00, "chips":3.50, "bread":4.50}
colors = {1:"red", 2:"blue", 3:"black", 4:"white", 5:"green", 6:"gray", 7:"pink"}

# function practice

def keyFinder(color):
    for key in colors:
        if colors[key] == color:
            return key
    else:
        return "color is not in dictionary"

print(keyFinder("red"))
print(keyFinder("purple"))

chicken_price = grocery_list["chicken"]
beef_price = grocery_list["beef"]
cheese_price = grocery_list["cheese"]
milk_price = grocery_list["milk"]
print(chicken_price)
print(beef_price)
print(cheese_price)
print(milk_price)

# function practice

def totalPrice(key1, key2):
    if key1 in grocery_list and key2 in grocery_list:
        return ("The total price of " + key1 + " and " + key2 + " is " + str(grocery_list[key1] + grocery_list[key2]))
    else:
        return("One or both of your keys is not in the dictionary")

print (totalPrice("chicken", "beef"))

def priceDiff(key1, key2):
    if key1 in grocery_list and key2 in grocery_list:
        return ("The difference in price of " + key1 + " and " + key2 + " is " + str(abs(grocery_list[key1] - grocery_list[key2])))
    else:
        return("One or both of your keys is not in the dictionary")

print(priceDiff("chicken", "beef"))


red = colors[1]
blue = colors[2]
black = colors[3]
white = colors[4]
print(red)
print(blue)
print(black)
print(white)

shoe_stock = {"Jordan 13":1, "Yeezy":8, "Foamposite": 10, "Air Max":5, "SB Dunk":20, "Nike":20, "Adidas":20, "AllBirds":20}
shoe_stock["SB Dunk"] -= 2
shoe_stock["Yeezy"] += 1
shoe_stock["Yeezy"] += 7
shoe_stock["Jordan 13"] += 7
shoe_stock["Foamposite"] += 7
shoe_stock["Air Max"] += 7
shoe_stock["SB Dunk"] += 7
shoe_stock["Yeezy"] -= 3
shoe_stock["Jordan 13"] -= 3
shoe_stock["Foamposite"] -= 3
shoe_stock["Air Max"] -= 3
shoe_stock["SB Dunk"] -= 3
print(shoe_stock)

# function practice

def restock(key1, multiplier):
    if key1 in shoe_stock:
        shoe_stock[key1] = shoe_stock[key1]*multiplier
        return shoe_stock
    else:
        return "invalid key"

print(restock("Yeezy", 3))

def restockAll(multiplier):
    for key in shoe_stock:
        shoe_stock[key] = shoe_stock[key]*multiplier
    return shoe_stock  

print(restockAll(5))

def clearance(key1, multiplier):
    if key1 in shoe_stock:
        shoe_stock[key1] = shoe_stock[key1]//multiplier
        return shoe_stock
    else:
        return "invalid key"

print(clearance("Yeezy", 3))

def clearanceAll(multiplier):
    for key in shoe_stock:
        shoe_stock[key] = shoe_stock[key]//multiplier
    return shoe_stock 

print(clearanceAll(5))


del grocery_list["chicken"]
del grocery_list["chips"]
print(grocery_list)

del colors[1]
del colors[3]
print(colors)

del shoe_stock["Yeezy"]
del shoe_stock["Air Max"]
print(shoe_stock)