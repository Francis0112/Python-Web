

# return product if result < 1000 else return sum
def two_number(a, b):
    if a*b<=1000:
        return a*b
    else:
        return a+b
#print(two_number(10,100))

def current_previous_numbers():
    prev = 0
    total = 0
    for i in range(10):
        total = i+prev
        print(f"current number: {i} previous number: {prev} Sum: {total}")
        prev = i
#current_previous_numbers()

def display_string(string):
    n = ""
    for i in range(0,len(string),2):
        n += string[i]
    return n       
#print(display_string("francis"))


def remove_string(string, num):
    return string[num:]
#print(remove_string("francis", 2))


#check list if first index and last index is the same. onegai shimas
def onegai_list(list1):
    a = list1[0]
    b = list1[-1]
    if a==b:
        return True
    else:
        return False
#print(onegai_list([1,2,3,4,2]))

#list that return divisible by 5 
def divisible_five(list1):
    n = []
    for i in list1:
        if i%5==0:
            n.append(i)
    return n

#print(divisible_five([1,2,3,5,11,10,20,15]))

# return count of the sub string to a string
def sub_string(string, sub):
    return f"{sub} appeared {string.count(sub)}"    
#print(sub_string("onegai francis, hello francis how are you francis", "francis"))

# loop print pattern
def pattern():
    for i in range(5+1):
        for x in range(i):
            print(i, end="")
        print(" ")
#pattern()

#check if the number is a palindrome
def palindrome(num):
    #convert int to string
    string1 = str(num)
    n = string1[::-1]
    if string1 == n:
        return True
    else:
        return False    
#print(palindrome("123"))

# get odd index from the 1st list and even from the 2nd list
def odd_even_list(list1, list2):
    n = []
    for i in range(len(list2)):
        if i%2==0:
            n.append(list2[i])
    for x in range(0,len(list1),2):
        n.append(list1[x])
    return n
#print(odd_even_list(['a','b','c','d','e'],[1,2,3,4,5]))

# return int to string and reverse
def reverse_int(num):
    new = str(num)
    for i in range(len(new)-1,-1,-1):
        print(new[i], end=" ")    
#reverse_int(126)


def interest(tax):
    percent = [0, 0.1, 0.2]
    total = tax*percent[0]+tax*percent[1]+tax*percent[2]
    return total 
#print(interest(45000))


def multi_table():
    for i in range(1,11):
        for x in range(1,11):
            print(i*x, end=" ")
        print("\t\t")

#multi_table()

#power base
def _power(base, exp):
    import math
    c = math.pow(base, exp)
    return c

print(_power(2, 5))

