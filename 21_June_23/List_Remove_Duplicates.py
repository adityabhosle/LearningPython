dummy = [1, 2, 3, 4, 3, 2, 2, 5]

print("The list containing duplicates is", dummy)

result = []
for x in dummy:
    if x not in result:
        result.append(x)

print("The resultant list without duplicates is", result)

