import re
import sys
from itertools import product


def input_r():
    r_format = re.compile('.*,.*')
    r = input("Please enter items in the list R: ").split(" ")
    for x in range(len(r)):
        if r:
            if r_format.match(r[x]) is not None:
                r[x] = tuple(r[x].split(","))
            else:
                print("The format of R doesn't match the requested x1,y1 x2,y2 ... xn,yn. Please try again.")
                return input_r()
    return r


print('In this program you are going to input a list A in the form x1 x2 x3 x4 separate by spacing')
print('And a list R where R is of the form (written mathematically) x1,y1 x2,y2 xn,yn \n (skip input for empty set)')

A = input("Please enter items in the list A: ").split(" ")
print(A)
R = input_r()

cartesian_product = set(product(list(A), list(A)))
if set(R).issubset(cartesian_product):
    print("R is a set")
    print("R is a subset of AxA")
    print("R is a relation on A")
else:
    print("R is a set")
    print("R is not a subset of AxA because the following element is in R but not in AxA: " , end=" ")
    for x in set(R).difference(cartesian_product):
        print(str(x) + ",", end=" ")
    print()
    print("R is not a relation on A")
    exit()

non_reflex = []
for x in A:
    if (x, x) not in R:
        non_reflex.append(x)

if len(non_reflex) == 0:
    print("R is reflexive")
else:
    print("R is not reflexive: ", end=" ")
    for x in non_reflex:
        print(str(x) + ",", end=" ")
    print()

non_transitive = []
for a, b in R:
    for c, d in R:
        if b == c and (a, d) not in R:
            non_transitive.append((a, b))

if len(non_transitive) == 0:
    print("R is transitive")
else:
    print("R is not transitive:", end=" ")
    for x in non_transitive:
        print(str(x) + ",", end=" ")
    print()

non_symmetric = []
symmetric = []
for x, y in R:
    if (y, x) not in R:
        non_symmetric.append((x, y))

if len(non_symmetric) == 0:
    print("R is symmetric")
else:
    print("R is not symmetric: ", end=" ")
    for x in non_symmetric:
        print(str(x) + ",", end=" ")
