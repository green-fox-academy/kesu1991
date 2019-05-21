import statistics

def add(a, b):
    sum = a + b
    return sum

def max_of_three(a, b, c):
    list_max = [a,b,c]
    max_num = max(list_max)
    return max_num

def median(pool):
    median_num = statistics.median(pool)
    return median_num 

def is_vovel(char):
    return char in ['a', 'u', 'o', 'e', 'i']

def translate(hungarian):
    teve = hungarian
    for char in teve:
        if is_vovel(char):
            teve = (char+'v'+char).join(teve.split(char))
    return teve
