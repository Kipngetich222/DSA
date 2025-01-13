def insert(arr, element):
    arr.append(element)

if __name__ == "__main__":
    #declaring array
    LA = [0,0,0]
    x = 0

    print("array before inserting")
    for x in range(len(LA)):
        print("LA", [x], "= ", LA[x])
    print("inserting elements..")

    for x in range(len(LA)):
        LA.append(x);
        LA[x] = x+1;

    print("array after insertion")
    for x in range(len(LA)):
        print("LA", [x], "+ ", LA[x])