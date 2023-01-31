
# day 3
#string exercise

# string is array. get first mid and last index.
def name(n):
    a = n[0]
    b = n[int(len(n)/2)]
    c = n[-1]
    res = a+b+c
    return res
# print(name(input("Enter your name: ")))

def name_part2(n):
    mid = int(len(n)/2)
    a = n[mid-1]
    b = n[mid]
    c = n[mid+1]
    res = a+b+c
    return res
# print(name_part2(input("Enter your name again: ")))

def append_string():
    s1 = "Ault"
    s2 = "Kelly"
    a = s1[:int(len(s1)/2)]
    b = s1[int(len(s1)/2):]
    return a + s2 + b
# print(append_string())

def two_string():
    s1 = "America"
    s2 = "Japan"
    a = s1[0]+s2[0]
    b = s1[int(len(s1)/2)]+s2[int(len(s2)/2)]
    c = s1[-1]+s2[-1]
    res = a+b+c
    return res
# print(two_string())

def low_up(s):
    low = ""
    up = ""
    for i in s:
        if i.islower():
            low+=i
        else:
            up+=i
    res = low+up
    return res
# print(low_up("FranCiS"))

def count_char(s):
    letter = ""
    digit = ""
    symbol = ""
    for i in s:
        if i.isdigit():
            digit+=i
        elif i.isalpha():
            letter+=i
        else:
            symbol+=i
    return len(letter), len(digit), len(symbol)
# print(count_char("Francis@123@gmail.com$45"))


def mix_string(s1,s2):
    res = s1[0]+s2[-1]+s1[1]+s2[1]+s1[-1]+s2[0]
    return res
# a = "Abc"
# b = "Xyz"
# print(mix_string(a, b))

def balance(s1, s2):
    flag = True
    for i in s1:
        if i in s2:
            continue
        else:
            flag = False
    return flag  
# print(balance("si","francis"))

def occurence(s, ss):
    x = s.count(ss)
    return f"{ss} appeared {x} times!"
# print(occurence("hello world, kamusta world?, world of fun, world of tanks, world of warcraft", "world"))

def sum_average_string(s):
    total = 0
    avg = 0
    n = ""
    for i in s:
        if i.isdigit():
            n+=i
    for i in n:
        total = total+int(i)
    avg = total/len(n)
    return total, avg
# print(sum_average_string("francis0112@rocketmissle.com94"))

def occurence_char(w):
    res = {}
    for i in w:
        count = w.count(i)
        res[i] = count
    return res
# print(occurence_char("francis dequito"))

def reverse_string(s):
    n = ""
    for i in range(len(s)-1,-1,-1):
        n+=s[i]
    return n
# print(reverse_string("francis"))

def index_substring(s):
    a = s.rfind("hmn")
    return f"last occurence of sub string: {a}"
# print(index_substring("hmn let me think.. hmn okey hmmn.. how to to this again?.. hmn.. i think i got it. hmn okey wait hmn.."))

def hyphens(s):
    n = s.split("-")        
    return n
# print(hyphens("hello-world-kamusta-mundo-maayong-buntag"))

def remove_empty():
    list1 = [1,2,3,4,5,"",3,5,"",10]
    for i, val in enumerate(list1):
        if val=="":
            list1.pop(i)
    print(list1)
# remove_empty()

def replace_jutsu(s,w,r):
    n = s.replace(w,r)
    return n
# print(replace_jutsu("hello world, kamusta world, paparts world", "world", "mundo"))



