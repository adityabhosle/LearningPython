print("Hello, World!")

#Walrus operator
print(author:="yang")

#List Comprehenssions

Genius = ["Jerry", "Jack", " Tom", "Yang"]
L1 = [name if name.startswith('Y') else 'Not Genius' for name in Genius]
print(L1)

# Using * to upack iterable & desstructuring assignments
a, *mid, b = [1, 2, 3, 4, 5, 6]
print(a, mid, b)