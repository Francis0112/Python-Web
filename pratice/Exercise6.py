

# day 3
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
    pass
