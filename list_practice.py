empty_list = []
cities = ["Oakland", "Atlanta", "New York City", "Seattle", "Memphis", "Miami", "Boston", "Los Angeles", "Denver", "New Orleans"] 
print(cities)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(numbers)

print(cities[0])
print(cities[3])
print(cities[6])
print(numbers[1])
print(numbers[2])
print(numbers[5])

slice = cities[1:3] + numbers[2:4]
print(slice)

cities[0] = "San Francisco"
cities[2] = "Brooklyn"
cities[7] = "Hollywood"
cities[5] = "Tampa"

cities.append("New Jersey")
cities.extend(["Santa Cruz", "Selma", "Chicago"])
cities.insert(7, "Washington, D.C.")
print(cities)

cities.append("Oakland")
cities.extend(["New York City", "Los Angeles"])
cities.insert(0, "Miami")
print(cities)

cities.pop(3)
cities.remove("Atlanta")
del cities[5] # think the instructions are wrong about using clear() as that clears the entire list 
print(cities)

print("function practice below")
#function practice

def printCities():
    for city in cities:
        print(city)

printCities()


def printLongCities():
    for i in range(1, len(cities)):
        if len(cities[i]) > len(cities[i-1]):
            print(cities[i] + "12")

printLongCities()

print(cities) 

def shortCities():
    for i in range(0, len(cities)-1):
        if(len(cities[i]) > len(cities[i+1])):
            cities.append(cities[i+1])
            cities.pop(i+1)
    return cities

print(shortCities())


def sumArray():
    sum = 0
    for num in numbers:
        sum += num
    return sum

print(sumArray())