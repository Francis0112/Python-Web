

# day 5
# Data structure
# Set Exercise

# warmp up
def onegai():
    # comprehension
    odd = {i for i in range(11) if i%2==1}
    even = {i for i in range(11) if i%2==0}
    prime = {i for i in range(2,11) if all(i%y!=0 for y in range(2, i))}
    n1 = {1,2,3,4,5}
    n2 = {5,6,7,8,9}
    n3 = {10,11,12,13}
    res = n1.issubset(n3)
    return res
# print(onegai())


def list_set():
    sample_set = {"Yellow", "Orange", "Black"}
    sample_list = ["Blue", "Green", "Red"]
    for i in sample_list:
        sample_set.add(i)
    return sample_set
# print(list_set())


def return_double():
    set1 = {10, 20, 30, 40, 50}
    set2 = {30, 40, 50, 60, 70}
    res = set1.intersection(set2)
    return res
# print(return_double())


def return_unique():
    set1 = {10, 20, 30, 40, 50}
    set2 = {30, 40, 50, 60, 70}
    res = set1.difference(set2)
    return res
# print(return_unique())


def update_first_set():
    set1 = {10, 20, 30}
    set2 = {20, 40, 50}
    return set1.difference(set2)
# print(update_first_set())


def remove_items_at_once():
    # Write a Python program to remove items 10, 20, 30 from the following set at once.
    set1 = {10, 20, 30, 40, 50}
    set1.difference_update({10,20,30})
    return set1
# print(remove_items_at_once())

def return_unique_1():
    # Exercise 6: Return a set of elements present in Set A or B, but not both
    set1 = {10, 20, 30, 40, 50}
    set2 = {30, 40, 50, 60, 70}
    res = set1.symmetric_difference(set2)
    return res
# print(return_unique_1())

def common_elements():
    # Exercise 7: Check if two sets have any elements in common. If yes, display the common elements
    set1 = {10, 20, 30, 40, 50}
    set2 = {60, 70, 80, 90, 10}
    set1.intersection_update(set2)
    return set1
# print(common_elements())

def update_set1():
    # Exercise 8: Update set1 by adding items from set2, except common items
    set1 = {10, 20, 30, 40, 50}
    set2 = {30, 40, 50, 60, 70}
    set1.symmetric_difference_update(set2)
    return set1
# print(update_set1())

def remove_item_set1():
    # Exercise 9: Remove items from set1 that are not common to both set1 and set2
    set1 = {10, 20, 30, 40, 50}
    set2 = {30, 40, 50, 60, 70}
    set1.intersection_update(set2)
    return set1
# print(remove_item_set1())











