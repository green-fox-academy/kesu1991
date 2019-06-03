import numpy, re, types

###### Create a new list which contains only the even numbers
def is_even(n):
    return n % 2 == 0

print(list(filter(is_even, [1, 3, -2, -4, -7, -3, -8, 12, 19, 6, 9, 10, 14])))


###### Create a new list which contains the positive items' squared value
def squ(x):
    return x * x

def is_pos(n):
    return n > 0

def prod(L):
    return map(squ, list(filter(is_pos,L)))

print(list(prod([1, 3, -2, -4, -7, -3, -8, 12, 19, 6, 9, 10, 14])))


###### Create a new list which contains the numbers if their squared value is above 20
def squ(x):
    return x * x

def greater_than_20(n):
    return n > 20

print(list(filter(greater_than_20,list(map(squ, [1, 3, -2, -4, -7, -3, -8, 12, 19, 6, 9, 10, 14])))))


###### Calculate the average of the odd numbers
def is_odd(n):
    return n % 2 == 1

def average_num(x):
    return numpy.average(x)

print(average_num(list(filter(is_odd, [1, 3, -2, -4, -7, -3, -8, 12, 19, 6, 9, 10, 14]))))


###### Calculate the sum of the even numbers which are below or equal to 10
def is_even(n):
    return n % 2 == 0 and n <= 10

def sum_of_even(x):
    return numpy.sum(x)

print(sum_of_even(list(filter(is_even, [1, 3, -2, -4, -7, -3, -8, 12, 19, 6, 9, 10, 14]))))


###### Determine whether it contains even numbers or not
def is_even(n):
    return n % 2 == 0

def if_contains_even(n):
    return any(n)

print(if_contains_even(list(map(is_even, [1, 3, -2, -4, -7, -3, -8, 12, 19, 6, 9, 10, 14]))))


###### Determine whether every number is positive or not
def is_pos(n):
    return n > 0

def if_every_pos(n):
    return all(n)

print(if_every_pos(list(map(is_pos, [1, 3, -2, -4, -7, -3, -8, 12, 19, 6, 9, 10, 14]))))


###### Students

Students = [ ['John', 16, 'male', [5,5,4,2]],
             ['Jane', 15, 'female', [4,3,4,4,5]],
             ['Bob', 17, 'male', [2,2,3,1]]   
           ]

# Create a new list that only includes the boys
def boys_only_1(x):
    for i in x:
        if i[2] == 'male':
            yield i[0]

print(list(boys_only_1(Students)))

def boys_only_2(x):
    for i in x:
        return x[2] == 'male'

print(list(filter(boys_only_2, Students)))


# Create a new list that only includes who's name starts with the letter J
def J_name_1(x):
    for i in x:
        if i[0].startswith('J'):
            yield i[0]

print(list(J_name_1(Students)))

def J_name_2(x):
    for i in x:
        return i[0].startswith('J')

print(list(filter(J_name_2, Students)))

# Create a new list that only includes the girls
def girls_only_1(x):
    for i in x:
        if i[2] == 'female':
            yield i[0]

print(list(girls_only_1(Students)))

def girls_only_2(x):
    for i in x:
        return x[2] == 'female'

print(list(filter(girls_only_2, Students)))

# Create a new list that only includes who's grade average is above 4
"""
def grade_above_4(x):
    for i in x:
        return numpy.average(i[3]) > 4

print(list(filter(grade_above_4, Students)))
"""

###### Create your own map function. It should take an iterable and an other function.
def mapper(func, sequences):
    if type(sequences) is list:
        for i in range(len(sequences)):
            ref = func(sequences[i])
            sequences[i] = ref
        return sequences
    else:
        return func(sequences)


def add(n):
    return n+1

print(mapper(add,2))
print(mapper(add,[1,2,3,4,5]))


###### Fibonacci generator
def recur_fibo(n):
   
   if n <= 1:
       return n
   else:
       return(recur_fibo(n-1) + recur_fibo(n-2))

def generator():
    i = 0
    while True:
        yield recur_fibo(i)
        i += 1

print(list(generator()))

