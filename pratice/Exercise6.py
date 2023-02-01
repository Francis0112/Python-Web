

# day 3
# day 4

# Data Structure
# list exercise

def reverse_list(list1):
    temp = []
    for i in range(len(list1)-1,-1,-1):
        temp.append(list1[i])
    return temp
# print(reverse_list([1,2,3,4,5,6,7,8]))

def concatinate():
    a = ["M", "na", "i", "fran"]
    b = ["y", "me", "s", "cis"]
    res = [a[0]+b[0],a[1]+b[1],a[2]+b[2],a[3]+b[3]]
    return res
# print(concatinate())

def squared_list():
    num = []
    n = []
    for i in range(1,7+1):
        num.append(i)
    for i in num:
        n.append(i*i)
    return n 
# print(squared_list())

def order_concat():
    a = ["Hello ", "take "]
    b = ["Dear", "Sir"]
    res = [a[0]+b[0], a[0]+b[1],a[1]+b[0],a[1]+b[1]]
    return res
# print(order_concat())

def iterate_both_list():
    a = [10, 20, 30, 40]
    b = [100, 200, 300, 400]
    res = zip(a,b)
    for i,v in tuple(res):
        print(i, v)
# iterate_both_list()

# with enumarate
def remove_null_items():
    a = ["Mike", "", "Emma", "Kelly", "", "Brad"]
    for i,v in enumerate(a):
        if v=="":
            a.pop(i)
    return a
# print(remove_null_items())

# with range
def remove_null_items1():
    n=[]
    a = ["Mike", "", "Emma", "Kelly", "", "Brad"]
    for i in range(len(a)):
        v = a[i]
        if v!="":
            n.append(v)
    return n
# print(remove_null_items1())

# with filter
def remove_null_items2():
    a = ["Mike", "", "Emma", "Kelly", "", "Brad"]
    x = filter(lambda y: y!="", a)
    return list(x)
# print(remove_null_items2())


def nested_list():
    a = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
    print(a[0])
    print(a[1])
    print(a[2])
    print(a[3])
    print(a[4])
    print(a[2][2])
    print(a[2][2][0])
    print(a[2][2][1])
    print(a[2][0])
    print(a[2][1])
    print(a[2][-1])
    print(a[2][2][0])
    a[2][2].insert(1, ">-||||-_-||||-<")
    print(a)
# nested_list()


def extend_nested_list():
    a = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
    b = ["h", "i", "j"]
    a[2][1][2].insert(2, b[0])
    a[2][1][2].insert(3, b[1])
    a[2][1][2].insert(4, b[2])
    print(a[2][1][2][1])
    print(a)
# extend_nested_list()

# only first occurence 20
def replace_item_list():
    a = [5, 10, 15, 20, 25, 50, 20]
    for i in range(len(a)):
        v=a[i]
        if v==20:
            a[i]=200
            break
    return a
# print(replace_item_list())

# remove all 20
def remove_item_list():
    n=[]
    a = [5, 10, 15, 20, 25, 50, 20]
    for i in range(len(a)):
        v=a[i]
        if v!=20:
            n.append(v)
    return n
# print(remove_item_list())