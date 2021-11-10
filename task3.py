user_input1 = input("Please enter items in the list ")
user_input2 = input("Please enter items in the list ")
A = user_input1.split(" ")
B = user_input2.split(" ")


def duplicate_removal(user_input):
    list_1 = []
    for a in user_input:
        if a not in list_1:
            list_1.append(a)
    return list_1


A = duplicate_removal(A)
B = duplicate_removal(B)

# checking if B is subset of A
is_subset = True
for x in B:
    if x not in A:
        is_subset = False
        break

if is_subset:
    print("B is a subset of A")
else:
    print("B is not a subset of A")

# A-B.
list_2 = []
for x in A:
    if x not in B:
        list_2.append(x)
print('A-B = ' + str(list_2))

# cartesian product of A and B.
list_3 = []
for x in A:
    for y in B:
        list_3.append([x, y])
print('AXB = ' + str(list_3))
