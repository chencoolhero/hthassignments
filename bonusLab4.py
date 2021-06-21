a = [1, 6, 7, 12, 58, -25, 19]
b = [2, 5, 6, 7, 2, 75, 34, 76, 23]

def closestSum(target):
    index1 = 0
    index2 = 0
    difference = abs(target - (a[0]+b[0]))
    for i in range(0, len(a)):
        for j in range(0, len(b)):
            if abs(target - (a[i] + b[j])) < difference:
                difference = abs(target - (a[i] + b[j]))
                index1 = i
                index2 = j
    return [a[index1], b[index2]]

print(closestSum(14))