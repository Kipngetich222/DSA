def findElement(arr, n, value):
    for i in range(n):
        if(arr[i] == value):
            return i
    return -1

if __name__ == "__main__":
    LA= [1,3,5,7,9]
    print("Array element are: ")
    for x in range(len(LA)):
        print("LA", [x], " = ", LA[x])

    value = 5
    n = len(LA)

    index = findElement(LA, n, value)
    if index != -1:
        print("Element", value, "found at position: " + str(index + 1))
    else:
        print("element not found")