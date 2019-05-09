##########################################################################
Expressions and Control Flow
##########################################################################


######Hello_me
print("Hello_me") 


######humpty_dumpty
print("Humpty Dumpty sat on a wall,")
print("Humpty Dumpty had a great fall.")
print("All the king's horses and all the king's men")
print("Couldn't put Humpty together again.")


######hello_others
print("Hello, Ray! \nHello, Santi! \nHello, Liaoyuan")


######introduce_yourself
print("Ke Su \n27 \n1.71")


######two_numbers
a = 13
b = 22
print(a+b)
print(b-a)
print(a*b)
print(22/13)
print(22//13)
print(22%13)


######coding_hours
print("Total hours spend with coding in a semester by an attendee is "+str(5*6*17)+" hours.")
print("Precentage of the coding hours in the semester is "+str(round(((5*6*17/(56*17))*100),1))+"%.")


######favorite_number
favorite_number = 8
print(f"My favorite number is: {favorite_number}")


#####swap
a = 526
b = 123
print(a)
print(b)


#####bmi
massInkg = 81.2
heightInM = 1.78
bmi = round(81.2/(1.78**2),2)
print(f"BMI is {bmi}.")


#####define_basic_info
name = "Ke Su"
age = 27
height = 1.71
married = False
print(f"{name}\n{age}\n{height}\n{married}")


#####variable_mutation
a = 3
a += 10
print(a)

b = 100
b -= 7
print(b)

c = 44
c *= 2
print(c)

d = 125
d /= 5
print(d)

e = 8
print(e**3)

f1 = 123
f2 = 345
T = True
F = False
if f1 > f2:
    print(T)
else:
    print(F)
    
g1 = 350
g2 = 200
T = True
F = False
if g2*2 > g1:
    print(T)
else:
    print(F)
    
h = 1357988018575474
T = True
F = False
if h%11 == 0 :
    print(T)
    
i1 = 10
i2 = 3
if i1 > i2**2:
    print("i1 is higher than i2 squared")
elif i1 < i2**3:
    print("i1 is smaller than i2 cubed")      
    
j = 1521
T = True
if j%3 == 0:
    print(f"j is dividible by 3: {T}")
elif j%5 == 0:
    print(f"j is dividible by 5: {T}")


###### cuboid
w = 1
l = 2
h = 3

area = 2*w*l+2*w*h+2*l*h
volumn = w*l*h
print(f"Surface Area: {area}\nVolumn: {volumn}")


###### seconds_in_a_day
current_hours = 14
current_minutes = 34
current_seconds = 42

total_sec = 24*60*60
current_seconds = 14*60*60+34*60+42

remaining = total_sec - current_seconds

print(f"Remaining seconds is {remaining}s.")


###### hello_user
user = input()
print(f"Hello, {user}!")


###### mile_to_km_converter
miles = int(input())
km = miles * 1.60934
print(km)


###### animals_and_legs
numChicken = int(input())
numPig = int(input())

legChicken = 2*numChicken
legPig = 4*numPig
totalLegs = legChicken+legPig

print(f"Total number of legs are {totalLegs}.")


###### average_of_input
import statistics
i = list(map(int, input("Enter five values: ").split()))
total = sum(i)
average = statistics.mean(i)
print(f"sum: {total}, Average: {average}")


###### odd_even
i = int(input("Enter a number: "))
if i%2 == 0:
    print("Even")
elif i%2 != 0:
    print("Odd")
	
	
###### one_two_a_lot
i = int(input("Enter a number: "))
if i <= 0:
    print("Not enough")
elif i == 1:
    print("One")
elif i == 2:
    print("Two")
else:
    print("A lot")


###### print_bigger
first = int(input("Enter first number: "))
second = int(input("Enter second number: "))
if first < second :
    print(f"Second number {second} is bigger.")
else:
    print(f"first number {first} is bigger.")

	
###### party_indicator
first = int(input("Enter number of girls: "))
second = int(input("Enter number of boys: "))
if first == second and first+second > 20:
    print("The party is exellent!")
elif first != second and first+second > 20:
    print("Quite cool party!")
elif first != 0 and first+second < 20:
    print("Average party...")
elif first == 0:
    print("Sausage party")
	
	
###### conditional_variable_mutation
a = 24
out = 0
if a%2 == 0:
    out += 1
    print(out)


b = 13
out2 = ""
if b>=10 and b<=20:
    out2 = "Sweet!"
    print(out2)
elif b<=10:
    out2 = "Less!"
    print(out2)
elif b>=20:
    out2 = "More!"
    print(out2)


	
c = 123
credits = 100
is_bonus = False

if credits >= 50 and is_bonus == False:
    c -= 2
    print(c)   
elif credits < 50 and is_bonus == False:
    c -= 1
    print(c)
elif is_bonus == True:
    print(c)
	
	
d = 8
time = 120
out3 = ""

if d%4 == 0 and time <= 200:
    out3 = "check"
    print(out3)
elif time > 200:
    out3 = "Time out"
    print(out3)
else:
    out3 = "Run Forest Run"
    print(out3)


###### i_wont_cheat_on_the_exams
for i in range(100):
    print("I won't cheat on the exam!")


###### print_even
for i in range(0,500,2):
    print(i)
	
	
###### multiplication_table
num = int(input("Enter a number: "))
for i in range(1,11):
    result = i*num
    print(f"i * 15 = {result}")

	
###### count_from_to
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if num2 > num1:
    for i in range(num1,num2):
        print(i)
else:
    print("The second number should be bigger")
	
	
###### fizz_buzz
for i in range(1,101):
    if i%3 == 0 and i%5 == 0:
        print("FizzBuzz")
    elif i%5 == 0:
        print("Buzz")
    elif i%3 == 0:
        print("Fizz")
    else:
        print(i)


###### draw_triangle
num = int(input("Enter a number here: "))
for i in range(num):
    print("*"*(i+1))


###### draw_pyramid
num = int(input("Enter a number here: "))
for i in range(num):
    print(' '*(num-i-1) + '*'*(2*i+1))


###### parametric_average
user_input = input("Enter the numbers separated by commas: ")
input_list = user_input.split(',')

input_int_list = [int(i) for i in input_list]

sum_input = sum(input_int_list)
average_input = round(sum_input/len(input_int_list),1)
print(f"Sum: {sum_input}, Average: {average_input}")
	
##########################################################################        
Lists
##########################################################################

###### print elements
numbers = [4,5,6,7]
for i in range(len(numbers)):
    print(numbers[i])
	
###### third 
q = [4,5,6,7]
print(q[2])

###### compare length
p1 = [1,2,3]
p2 = [4,5]
if len(p2) > len(p1) :
    print("p2 is longer")
else:
    print("p1 is longer")
	
###### sum elements
r = [54,23,66,12]
print(sum([r[1],r[2]]))

###### change elements
s = [1,2,3,8,5,6]
index = s.index(8)
s[3] = 4
print(s[3])

###### increment elements
t = [1,2,3,4,5]
t[2] += 1
print(

###### matrix


###### double items
numList = [3,4,5,6,7]
for i in range(len(numList)):
    numList[i] = numList[i]*2
print(numList)


###### colors
colors = [["lime", "forest green", "olive", "pale green", "spring green"],
          ["orange red", "red", "tomato"],
          ["orchid", "violet", "pink", "hot pink"]]
print(colors[0])
print(colors[1])
print(colors[2])


###### append a
animals = ["koal", "pand", "zebr"]
for i in range(len(animals)):
    animals[i] = animals[i] + "a"
print(animals)


###### swap elements
abc = ["first", "second", "third"]
sub = abc[0]
temp = sub
abc[0] = abc[2]
abc[2] = temp
print(abc)


###### sum all elements
ai = [3,4,5,6,7]
print(sum(ai))


###### reverse list
aj = [3,4,5,6,7]
aj = aj[::-1]
print(aj)
