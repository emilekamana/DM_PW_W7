# A python program that takes as input 2 finite sets or lists (you decide) X and Y , where X, Y are members of  Z,
# and outputs a truth value (’True’ or ’False’) for the following statement:
# ∀x ∈ X, ∃y ∈ Y such that y | x.

def check_user_input(usr_input):
    try:
        # Convert it into integer
        val = int(usr_input)
        return val
    except ValueError:
        print("Input is not an integer number. Number = ", usr_input)
        new_nbr = input("Enter a new number:")
        return check_user_input(new_nbr)


# Receiving user inputs
user_input1 = input("Please enter integers for list X:(separate by space) ")
user_input2 = input("Please enter integers for list Y:(separate by space) ")

input_X = (user_input1.split(" "))
input_Y = (user_input2.split(" "))

for i in range(len(input_X)):
    input_X[i] = check_user_input(input_X[i])

for i in range(len(input_Y)):
    input_Y[i] = check_user_input(input_Y[i])


def divisibility(list1, list2):
    divisible = []
    for x in list1:
        for y in list2:
            if x % y == 0:
                divisible.append(x)
    if set(list1).difference(set(divisible)):
        print('The statement ∀x ∈ X, ∃y ∈ Y such that y | x, is false.')
    else:
        print('The statement ∀x ∈ X, ∃y ∈ Y such that y | x, is true.')


divisibility(input_X, input_Y)
