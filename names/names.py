import time
from bst import BinarySearchTree

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()


duplicates = []

# -------------- My solution is O(n log n)
bst = BinarySearchTree(names_1[0])
for name_1 in names_1:
    if name_1 != names_1[0]:
        bst.insert(name_1)

for name_2 in names_2:
    if bst.contains(name_2):
        duplicates.append(name_2)


# -------------- original solution is O(n^2)
# for name_1 in names_1:
    # for name_2 in names_2:
    #     if name_1 == name_2:
    #         duplicates.append(name_1)

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish with no restrictions on techniques or data
# structures?
