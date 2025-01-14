La = [1,2,3,5,7,8,9]

print("the original elements are : ")
for x in range(len(La)):
    print("La", [x], "= ", La[x])

La[2] = 10
print("elements after updating")
for x in range(len(La)):
    print("La", [x], "= ", La[x])