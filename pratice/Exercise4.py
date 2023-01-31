

#day 3
# functions exercise

def person(name, email):
    return name, email
# return tupple
# print(person(name="francis", email="francisdequito@gmail.com"))

def not_many_args(*args):
    for i in args:
        print(i)
# not_many_args(10,20,30)
# not_many_args("francis", "dequito")

def add_sub(a, b):
    add = a+b
    sub = a-b
    return add, sub
# print(add_sub(10,5))

def employee(name, salary=9000):
    return name, salary
# print(employee("Person A",12000))
# print(employee("francis"))

def nested_function(a,b):
    def addition(a,b):
        return a+b
    def subtraction(a,b):
        return a-b
    add = addition(a,b)
    sub = subtraction(a,b)
    return add, sub
# print(nested_function(12,4))

def hero(name, power):
    return name, power
# person1 = hero("spider-man", "swing crawl super sense")
# print(person1)

def generate_even():
    start = 4
    end = 30
    temp = []
    for i in range(4,end,2):
        temp.append(i)
    return temp
# print(generate_even())

def largest_item(list1):
    a = sorted(list1)
    return a[-1]
given = [4, 6, 8, 24, 12, 2]
# print(largest_item(given))


    