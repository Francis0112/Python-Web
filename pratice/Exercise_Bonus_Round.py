

# day 5
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

    
def onegai_count():
    # Exercise 4: Count the occurrence of each element from a list
    sample_list = [11, 45, 8, 23, 14, 12, 78, 45, 89]
    a = dict()
    for i in sample_list:
        if i in a:
            a[i]+=1
        else:
            a[i] = 1
    return a
# print(onegai_count())




