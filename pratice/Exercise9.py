

# day 5
# Data Structure
# tuple Exercise

def reverse_tuple():
    # reverse the tuple
    a = (i for i in range(11))
    a = list(a)
    n = list()
    for i in range(len(a)-1,-1,-1):
        v = a[i]
        n.append(v)
    return tuple(n)
# print(reverse_tuple())

def locate_20():
    # The given tuple is a nested tuple. write a Python program to print the value 20.
    tuple1 = ("Orange", [10, 20, 30], (5, 15, 25))
    return tuple1[1][1]
# print(locate_20())

def item_50():
    # Create a tuple with single item 50
    a = tuple(range(50,50+1,1))
    return a
# print(item_50())


def unpack():
    # Write a program to unpack the following tuple into four variables and display each variable.
    tuple1 = (10,20,30,40)
    a,b,c,d = tuple1
    print(f"{a}\n{b}\n{c}\n{d}")
# unpack()


def swap_tuples():
    # Swap two tuples in Python
    a = (11, 22)
    b = (99, 88)
    a,b = b,a
    print(f"tuple1: {a}\ntuple2: {b}")
# swap_tuples()


def breaking_bad():
    # Exercise 6: Copy specific elements from one tuple to a new tuple
    # Write a program to copy elements 44 and 55 from the following tuple into a new tuple.
    tuple1 = (11, 22, 33, 44, 55, 66)
    n = (tuple1[3], tuple1[4])
    return n
# print(breaking_bad())


def modify_nested_tuple():
    # Given is a nested tuple. Write a program to modify the first item (22) of a list inside a following tuple to 222
    a = (11, [22, 33], 44, 55)
    a[1][0]=222
    return a
# print(modify_nested_tuple())


def tuple_snort():
    # Exercise 8: Sort a tuple of tuples by 2nd item
    # hard level
    a = (('a', 23),('b', 37),('c', 11), ('d',29))
    a = tuple(sorted(list(a), key=lambda x: x[1]))
    return a
# print(tuple_snort())
    

def versatile():
    # Exercise 9: Counts the number of occurrences of item 50 from a tuple
    a = (50, 10, 60, 70, 50)
    return a.count(50)
# print(versatile())


def clone():
    # Exercise 10: Check if all items in the tuple are the same
    # hard
    a = (1,1,1,1)
    for i in list(a):
        x = next(iter(list(a)))
        if i==x:
            flag=True
        else:
            flag=False
            break
    return flag
# print(clone())

