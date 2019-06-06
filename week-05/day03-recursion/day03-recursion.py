###### Number adder
def sum(n):
    if n == 0:
        return 0
    else:
        return n + sum(n - 1)

print(sum(3))


###### Sum Digits
def getDigitSum(num):
    if num == 0:
        return num
    else:
        return num%10 + getDigitSum(num//10)

print(getDigitSum(123))


###### Power
def rpower(num,idx):
    if(idx==1):
       return(num)
    else:
       return(num*rpower(num,idx-1))

print(rpower(3,2))


###### Greatest Common Divisor
def gcd_recursive(a, b):
    if b == 0:
        return a
    else:
        return gcd_recursive(b, a % b)

print(gcd_recursive(20,8))


###### Bunnies
def bunnies(ears):
    if len(ears)==0:
        return 0
    else:
        return ears[0] + bunnies(ears[1:]) 

print(bunnies([2, 2, 2, 2, 2]))


###### Bunnies again
def sum_even_odd(lst):
    if not lst:                      
        return (0, 0)                
    elif lst[0] % 2 == 0:            
        x, y = sum_even_odd(lst[1:]) 
        return (lst[0] + x, y)       
    else:                            
        x, y = sum_even_odd(lst[1:])
        return (x, lst[0] + y) 

print(sum_even_odd([1,2,3,4,5]))


###### Strings
def replaceChar(inval, old, new):
    if inval == '':
        return ''
    if inval[0] == old:
        return new + replaceChar(inval[1:], old, new)
    return inval[0] + replaceChar(inval[1:], old, new)

print(replaceChar("xxxx",'x','y'))



###### Strings again
def removeChar(inval, old, new):
    if inval == '':
        return ''
    if inval[0] == old:
        return new + removeChar(inval[1:], old, new)
    return inval[0] + removeChar(inval[1:], old, new)

print(removeChar("xxhskx",'x',''))

###### Strings again and again



###### Fibonacci
def recur_fibo(n):
   if n <= 1:
       return n
   else:
       return(recur_fibo(n-1) + recur_fibo(n-2))

print(recur_fibo(5))


