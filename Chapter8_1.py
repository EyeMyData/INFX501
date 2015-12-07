## Exercise 1: Write a function called chop that takes a list and modifies it, removing
## the first and last elements, and returns None. Then write a function called middle that
## takes a list and returns a new list that contains all but the first and last elements.

list_one = ['a', 'b', 'c', 'd', 'e', 'f']
list_two = ['z', 'y', 'x', 'w', 'v', 'u']

print('List 1: ',list_one)
print('List 2: ',list_two)

def chop(x):
    del x[:1]
    del x[-1:]
    return x

chop(list_one)
print('chop() returns:', list_one)

def middle(y):
    del y[0]
    del y[len(y) - 1]
    return y
new_list = middle(list_two)

print('middle() returns:', new_list)
