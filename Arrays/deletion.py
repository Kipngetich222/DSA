if __name__ == '__main__':
    LA = [0,0,0]
    n = len(LA)
    
    print("array before deleting")
    for x in range(len(LA)):
        LA.append(x)
        LA[x] = x + 3
        print("LA", [x], "= ", LA[x])

    for x in range(1, n-1):
        LA[x] = LA[x+1]
        n = n-1

    print("array after deletion")
    for  x in range(n):
        print("LA", [x], "= ", LA[x])