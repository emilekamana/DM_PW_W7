#import itertools
from itertools import product
#getting user input
user_input1 = input("Please enter items in the list A ")
user_input2 = input("Please enter items in the list B ")

A = set(user_input1.split(" "))
B = set(user_input2.split(" "))


#  checking if B is subset of A
print("B is a subset of A: " + str(B.issubset(A)))

# A-B
print("A-B: " + str(A.difference(B)))

# cartesian product of A and B.
cartesian_product = product(list(A), list(B))
print("AXB: " + str(set(cartesian_product)))
