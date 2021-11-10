user_input = input("Please enter items in the list ")
list1 = user_input.split(" ")

item_set = set(list1)

if len(list1) != len(item_set):
    print("False")
else:
    print("True")

print('The set should be: ' + str(item_set))
