


# trying python lates builtin methods version 3.11

print(abs(1-4j))

# any() bago ito. return bolean
print(any([0,1,1,1]))

# all() ito bago din. return bolean
print(all([1,1,1,0]))

print(ascii("franc~s"))

# bin() binary 
print(bin(404))

# bool() return bolean
question = "is this python? ito ba ay python?"
ans = bool(1)
print(question, ans)

# callable() return bolean
def hello():
    return "Hi "
a = 5
print(callable(a))
x = hello
print(callable(x))

# chr() return unicode character
print(chr(120))

# compile() mag compile lang ng code. 
nyork = "a=10\nb=12\nc=a+b\nprint('total:', c)"
cat = compile(nyork,'Python_builtin311','exec')
exec(cat)

# divmod() return quotient and reminder
res = divmod(8,2)
print(res)

# enumarate() return index and values of list. 0
ss = [i for i in range(3)]
print(list(enumerate(ss)))

# filter() paramter return methods
def even_checker(n):
    if n%2==0:
        return True
    return False

num = [i for i in range(20)]
x = filter(even_checker, num)
print(list(x))

# eval() paramter string format, return  res
onegai = eval("3+1")
print(onegai)

# float() cast number to float
print(float(69))


# format()
print(format(123, "b"))

# frozenset() param - iters freeze the iterables, list, tupple, dictionary
frozenset([1,2,3])

# getattr() return object attri meh


# globals() return all global variables
# print(globals())

# exec() execute code from a string or an object. 

# help() yes very nice for newbies like me. 
# help(onegai)

# hex() convert number to hexadecimal string.
print(hex(73))


# hash() crack that password. 
print(hash("password"))


# input() get user input. common na ito
pass


# id() return unique identity or just id
print(id(onegai))


# isinstance() return bolean if type is true else false
print(isinstance(onegai, int))


# int() cast to int in python
pass


# iter() and next() return next index of the iterables. mostly used in data structures
lawson_ulam = ["pork paksiw", "pork adobo", "pork sisig", "pork steak"]
next_ulam = iter(lawson_ulam)
print(next(next_ulam))
print(next(next_ulam))


# locals() return all local variable
pass


# map() param return method, iterables 
numbah = [i for i in range(2,10+1,2)]
def square_pants(n):
    return n*n
x = map(square_pants, numbah)
print(list(x))

# range() the range as it is
ds = range(1,5+1,1)
print(list(ds))
# reverse range()
sd = range(5,0,-1)
print(list(sd))


# slice() slicing strings and arrays
text = "francis dequito"
print(text[:7]) 

# sorted() return sorted list from small to big numbers
x1 = [3,5,3,2,6,1]
x2 = "cba"
print(sorted(x1), sorted(x2))


# zip() takes two or more iterables and return as tuple
language=["python","java","C"]
rate=[9,8,4]
x = zip(language, rate)
print(list(x))


