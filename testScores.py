testResults = [

[75, 65, 42, 73],
[62, 65, 67, 79],
[13, 17, 19, 17]

]

def studentScores(name):
    if name == "Bob":
        return testResults[0]
    elif name == "Helen":
        return testResults[1]
    elif name == "Vic":
        return testResults[2]
    else:
        return "Please enter a valid name"
    
print(studentScores("Vic"))
print(studentScores("Helen"))
print(studentScores("Bob"))
print(studentScores("Joe"))