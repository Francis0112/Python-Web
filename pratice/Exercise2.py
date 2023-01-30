
# day 2
import os

def enter_two_number(num1,num2):
    return num1*num2
# print(enter_two_number(int(input("Enter number:")),int(input("Enter number:"))))

def enter_string():
    print(input("Enter String: "),input("Enter String: "),input("Enter String: "), sep='**')
# enter_string()

def decimal_to_octal(num):
    return "%o" %num
# num = int(input("Enter a number: "))
# print(decimal_to_octal(num))

def two_decimal_place(num):
    return "%0.2f" %num
# print(two_decimal_place(float(input("Enter a float number: "))))

def five_float():
    list1 = []
    for i in range(5):
        n = float(input("Enter a float number: "))
        list1.append(n)
    return list1
# print(five_float())

def write_file():
    with open("language.txt","r") as f:
        lines = f.readlines()
        counter = 0
        for i in lines:
            if counter == 4:
                counter+=1
                continue
            else:
                print(i)
            counter+=1
    # write_file()


def three_string():
    name = input("Enter your name: ")
    a = name.split()
    print(f"name1: {a[0]}\nname2: {a[1]}\nname3: {a[2]}")
# three_string()

def format_string(monster, starlevel, atk, deff, attri, mtype, effect):
    return "{0} {1} {2:.2f} {3:.2f} {4} {5} {6}".format(monster, starlevel, atk, deff, attri, mtype, effect)
# print(format_string(monster="elemental hero spark-man", starlevel=4, atk=1600.12345, deff=1300.5555, attri="thunder", mtype="duel card monster", effect="yu gi oh elemental hero spark - man fusion material"))

def check_file(file1):
    if os.path.exists(file1):
        with open(file1, "r") as f:
            lines = f.readlines()
            for i in lines:
                if lines==0:
                    return "file is empty"
                else:
                    print(i)
    else:
        print("file do not exists.")
# check_file("language.txt")

def file_read_line_4(file1):
    try:
        if os.path.exists(file1):
            with open(file1, "r") as f:
                lines = f.readlines()
                print(lines[3])
        else:
            print("File do not exists.")
    except Exception as e:
        raise e
# file_read_line_4("language.txt")