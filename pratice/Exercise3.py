

# day 2
# day 3
# loop exercise

def loop():
    for i in range(1,10+1):
        print(i)
# loop()

def pattern1():
    for i in range(1,5+1):
        for x in range(1, i+1):
            print(x, end= " ")
        print("")
# pattern1()

def calc_range(num):
    total = 0
    for i in range(1, num+1):
        total = total+i 
    return total
# print(calc_range(int(input("Enter a number: "))))

def multiple_by(num):
    for i in range(1, 10+1, 1):
        t = i*num
        print(t, end=" ")
# multiple_by(10)

def list_divisible_by_5(list1):
    for i in list1:
        if i>500:
            break
        elif i>150:
            continue
        elif i%5==0:
            print(i)
# numbers = [12, 75, 150, 180, 145, 525, 50]
# list_divisible_by_5(numbers)

def digits():
    digits = int(input("Enter a number: "))
    counter = 0
    while digits!=0:
        digits = digits//10
        print(digits)
        counter = counter+1
    print(counter)
# digits()

def pattern_revese():
    for i in range(0,5+1):
        for x in range(5-i,0,-1):
            print(x, end=" ")
        print("")
# pattern_revese()

def list_revese(list1):
    for i in range(len(list1), -1, -1):
        print(i)
# list_revese([1,2,3,4,5])

def reverse_loop():
    for i in range(-10, 0 ,1):
        print(i)
# reverse_loop()

def done_message():
    for i in range(1,5+1):
        print(i)
    else:
        print("done")
# done_message()

def prime_range(start, end):
    for i in range(start, end+1):
        if i > 1:
            for x in range(2, i):
                if i%x==0:
                    break
            else:
                print(i)
# prime_range(25,50)


def fibonacci_10():
    num1 = 0
    num2 = 1
    temp = 0
    for i in range(10):
        print(num1, end=" ")
        temp = num1+num2
        num1=num2
        num2=temp
# fibonacci_10()

def factorial(num):
    res = 1
    for i in range(num,0,-1):
        res = res*i
    print(res)
# factorial(5)

def reverse_integer(num):
    new = str(num)
    for i in range(len(new)-1,-1,-1):
        print(new[i], end=" ")
# reverse_integer(654)

def odd_index_list(list1):
    for i in list1[1::2]:
        print(i)
# odd_index_list([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])


def ice_cube():
    for i in range(1,5+1):
        print(f"current number: {i} cube number: {i*i*i}")
# ice_cube()

def series(n):
    total = 0
    st = "2"
    given = 2
    for i in range(0,n):
        print(st, end="+")
        st+=str(given)
        total+=int(st)
    print("\nsum: %d" %total)
# series(5)

def flag():
    for i in range(0,5,1):
        for x in range(i):
            print("*", end="")
        print("")
    for i in range(5,-1,-1):
        for x in range(i):
            print("*", end="")
        print("")
# flag()



