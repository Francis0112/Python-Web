

# day 5
# day 6
# Data Stucture Bonus Round
# list, set, dictionary, tuple Exercise

def odd_even():
    # Exercise 1: Create a list by picking an odd-index items from the first list and even index items from the second
    l1 = [3, 6, 9, 12, 15, 18, 21]
    l2 = [4, 8, 12, 16, 20, 24, 28]
    return l1[1::2]+l2[::2]
# print(odd_even())


def vanishing():
    # Write a program to remove the item present at index 4 and add it to the 2nd position and at the end of the list.
    l1 = [54, 44, 27, 79, 91, 41]
    target = l1[4]
    l1.remove(target)
    print(l1)
    l1.insert(2, target)
    print(l1)
    l1.append(target)
    print(l1)
# vanishing()


def reverse_three():
    # Exercise 3: Slice list into 3 equal chunks and reverse each chunk
    sample_list = [11, 45, 8, 23, 14, 12, 78, 45, 89]
    a = sample_list[:3]
    b = sample_list[3:6]
    c = sample_list[6:]
    return a[::-1],b[::-1],c[::-1]
# print(reverse_three())

    
def occurence_count():
    # Exercise 4: Count the occurrence of each element from a list
    sample_list = [11, 45, 8, 23, 14, 12, 78, 45, 89]
    a = dict()
    for i in sample_list:
        if i in a:
            a[i]+=1
        else:
            a[i] = 1
    return a
# print(occurence_count())


def pairs():
    # Exercise 5: Create a Python set such that it shows the element from both lists in a pair
    first_list = [2, 3, 4, 5, 6, 7, 8]
    second_list = [4, 9, 16, 25, 36, 49, 64]
    x = zip(first_list, second_list)
    return set(x)
# print(pairs())



def intersection():
    # Exercise 6: Find the intersection (common) of two sets and remove those elements from the first set
    first_list1 = [2, 3, 4, 5, 6, 7, 8]
    second_list1 = [4, 9, 16, 25, 36, 49, 64]
    x = set(first_list1)
    y = set(second_list1)
    x.intersection_update(y)
    for i in first_list1:
        if i in x:
            first_list1.remove(i)
    return set(first_list1)
# print(intersection()) 


def sub_super():
    # Exercise 7: Checks if one set is a subset or superset of another set. If found, delete all elements from that set
    first_set = {27, 43, 34}
    second_set = {34, 93, 22, 27, 43, 53, 48}
    print("1st set is subset: ", first_set.issubset(second_set))
    print("2nd set is subset: ", second_set.issubset(first_set))
    print("")
    print("1st set is superset: ", first_set.issuperset(second_set))
    print("2nd set is superset: ", second_set.issuperset(first_set))
    if first_set.issubset(second_set):
        first_set.clear()
    else:
        second_set.clear()
    print(f"1st set: {first_set}\n2nd set: {second_set}")
# sub_super()


def list_key():
    # Exercise 8: Iterate a given list and check if a given element exists as a key’s value in a dictionary. If not, delete it from the list
    roll_number = [47, 64, 69, 37, 76, 83, 95, 97]
    sample_dict = {'Jhon':47, 'Emma':69, 'Kelly':76, 'Jason':97}
    x = sample_dict.values()
    for i in roll_number:
        if i not in x:
            roll_number.remove(i)
    return roll_number
# print(list_key())


def list_no_duplicates():
    # Exercise 9: Get all values from the dictionary and add them to a list but don’t add duplicates
    speed = {'jan': 47, 'feb': 52, 'march': 47, 'April': 44, 'May': 52, 'June': 53, 'july': 54, 'Aug': 44, 'Sept': 54}
    x = speed.values()
    x = set(x)
    return list(x)
# print(list_no_duplicates())


def min_max_no_duplicates():
    # Exercise 10: Remove duplicates from a list and create a tuple and find the minimum and maximum number
    sample_list = [87, 45, 41, 65, 94, 41, 99, 94]
    x = set(sample_list)
    a = max(tuple(x))
    b = min(tuple(x))
    return a,b
# print(min_max_no_duplicates())