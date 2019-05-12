##########################################################################
Functions
##########################################################################

###### Doubling
base_num = 123
def doubling(para):
    double = para*2
    print(double)
    return double

doubling(base_num)


###### Greeter function
al = "Greenfox"
def greet(para):
    print(f"Greetings, dear {para}")

greet(al)


###### Append a
typo = "Chinchill"
def append_a_func(para):
    append_para = para+"a"
    print(append_para)
    return(append_para)
    
    
append_a_func(typo)


###### Summing
def sum(para):
    result = 0
    for i in range(1,(para+1)):
        result = result + i
    print(result)
    return(result)
    
sum(4)

###### Factorial
def factorio(para):
    result = 1
    for i in range(1,para+1):
        result = result*i
    print(result)
    return result
    
factorio(4)


###### Print arguments
def print_params(*para):
    print(para)
    
print_params("a","b")


###### Find part of an integer
def subint(num,list_num):
    list_result = []
    for i in range(len(list_num)):     
        if str(num) in str(list_num[i]):        
           list_result.append(i)
    print(list_result)
    return list_result
           
           
subint(1,[1,11,34,52,61])
subint(9,[1,11,34,52,61])


###### Unique
def unique(list_num):
    list_num.sort()
    set_num = set(list_num)
    list_result = list(set_num)
    list_result.sort()
    return list_result

print(unique([1, 11, 34, 11, 52, 61, 1, 34]))


###### Anagram
def is_anagram(input1, input2): 
	print(sorted(input1) == sorted(input2))

is_anagram("dog","god")

###### Palindrome builder
def create_palindrome(inputs):  
    list_input1 = []    
    list_input1[:] = inputs
    reversed_input1 = list_input1[::-1]

    input_string = ''.join(list_input1)
    reversed_string = ''.join(reversed_input1)
    print(input_string + reversed_string)

create_palindrome("shenzhen")


###### Palindrome searcher

###### Sort that list
def bubble(arr):
    arr.sort()
    print(arr)
    
bubble([43,12,24,9,5])

def advanced_bubble(arr, is_descending):
    if is_descending:
        arr.sort()
        print(arr[::-1])
      
advanced_bubble([43, 12, 24, 9, 5], True)

##########################################################################
Data Structure
##########################################################################

###### Simple replace
example = "In a dishwasher far far away"
list_example = example.split()
list_example[2] = "galaxy"
str_result = ' '.join(list_example)
print(str_result)


###### Url fixer
import re
url = "https//www.reddit.com/r/nevertellmethebots"
print(re.sub("bots","odds",url))


###### Takes longer
quote = "Hofstadter's Law: It you expect, even when you take into account Hofstadter's Law."
list_example = quote.split()
list_example.insert(3,"always takes longer than")
str_result = ' '.join(list_example)
print(str_result)


###### Todo print
todoText = " - Buy milk\n"
todoText1 = "My todo:\n" + todoText
todoText2 = todoText1 + " - Download games"
todoText3 = todoText2 + "\n     - Diablo"
print(todoText3)


###### Reverse
def reverse(para):
    list_input = []
    reversed_list = []    
    list_input[:] = para
    reversed_list = list_input[::-1]
    str_reversed = "".join(reversed_list)
    print(str_reversed)

reverse(".eslaf eb t'ndluow ecnetnes siht ,dehctiws erew eslaf dna eurt fo sgninaem eht fI")

###### List introduction 1
names = []
print(len(names))
names.append("William")


if len(names) ==0:
    print("empty")
else:
    print("non-empty")
    
names.append("John")
names.append("Amanda")
print(len(names))
print(names[2])

for i in range(len(names)):
    print(names[i])
    
for i in range(len(names)):
    num = i+1
    print(f"{num}. "+names[i])
    
del names[1]

for i in range(len(names)):
    print(names[i]) 

names = []


###### Map introduction 1
map = {}

print(map)

map = {'97': 'a', '98': 'b', '99': 'c', '65':'A', '66':'B', '67':'C'}

print(map)

print(map.keys())

print(map.values())

map['68'] = "D"

print(map)

print(len(map))

print(map['99'])

del map['97']
print(map)

print(map['100'])

map.clear()
print(map)


###### List introduction 2
List_A = ["Apple", "Avocado", "Blueberries", "Durian", "Lychee"]

List_B = List_A[:]
print(List_B)

for i in List_A: 
    if(i == "Durian") : 
        print ("Element Exists") 
        
List_B.remove("Durian")
print(List_B)

List_A.insert(4,"Kiwifruit")
print(List_A)

if len(List_A) > len(List_B):
    print("List A is bigger")
else:
    print("List B is bigger")
    
pos = List_A.index("Avocado")
print(pos)

#pos = List_B.index("Durian")
#print(pos)

List_B.extend(["Passion Fruit","Pummelo"])
print(List_B)
    
print(List_A[2])

###### Map introduction 2
map = {'978-1-60309-452-8': 'A Letter to Jo', 
       '978-1-60309-459-7': 'lupus',
       '978-1-60309-444-3': 'Red Panda and Moon Bear', 
       '978-1-60309-461-0':'The Lab'}
print(map)

for key,val in map.items():
    print(f"{val} (ISBN: {key})")

del map['978-1-60309-444-3']
print(map)

for k,v in list(map.items()):
    if v == 'The Lab':
       del map[k]
print(map)

map['978-1-60309-450-4'] = "They Called Us Enemy"
map['978-1-60309-453-5'] = "Why Did We Trust Him?"
print(map)

if '478-0-61159-424-8' in map.keys():
    print("There exists association value.")
else:
    print("No association value")

print(map['978-1-60309-453-5'])


###### Personal finance
def expenseCal(list_exp):
    total_spend = sum(list_exp)
    print(f"The total spend is {total_spend}")
    
    largest = max(list_exp)
    print(f"The greatest spend is {largest}")
    
    cheapest = min(list_exp)
    print(f"The cheapest spend is {cheapest}")
    
    avg_spend = round(total_spend/len(list_exp),2)
    print(f"The average spend is {avg_spend}")

expenseCal([500,1000,1250,175,800,120])


###### Telephone book
map = {'William A. Lathan': '405-709-1865', 
       'John K. Miller': '402-247-8568',
       'Hortensia E. Foster': '606-481-6467', 
       'Amanda D.Newland': '319-243-5613',
       'Brooke P. Askew': '307-687-2982'}
print(map)

def personalInfo(maps):
    jkPhone = maps['John K. Miller']
    print(f"John K. Miller's phone number is {jkPhone}.")
    
    for key,val in maps.items():
        if val == "307-687-2982":
            print(f"{key}'s phone number is {val}.")
            
    if "Chris E. Myer" in map.keys():
        print("Yes, we know.")
    else:
        print("No, we don't.") 
    
personalInfo(map)

###### Shopping list
shoppingList = ["Eggs", "milk", "fish", "apples", "bread", "chicken"]

def food(food_str,fruit_List):
    
    for i in shoppingList:     
        if(i == food_str):            
            print(f"{food_str} exists")

food("milk",shoppingList)
food("bananas",shoppingList)


###### product database
map = {'Eggs': 200, 
       'Milk': 200,
       'Fish': 400, 
       'Apples': 150,
       'Bread': 50,
       'Chicken': 550}
print(map)

def foodInfo(maps):
    fishPrice = maps['Fish']
    print(f"Fish's price is {fishPrice}.")
    
    priceList = list(maps.values())
    avgPrice = round(sum(priceList)/len(priceList),2)
    print(f"Average price is {avgPrice}.")
    
    count = 0
    for i in range(len(priceList)):
        if priceList[i] < 300:
            count += 1
    print(f"{count} products is below 300.")
    
    for k,v in maps.items():
        if v == 125:
            print(f"We can buy {k}.")
    
    for k,v in maps.items():
        min_price = min(priceList)
        if v == min_price:
            print(f"The cheapest product is {k}")
            
foodInfo(map)


###### product database 2
map = {'Eggs': 200, 
       'Milk': 200,
       'Fish': 400, 
       'Apples': 150,
       'Bread': 50,
       'Chicken': 550}
print(map)

def foodInfo(maps):
    
    for k,v in maps.items():
        if v < 201:
            print(f"{k}'s price is less than 201")
    
    for k,v in maps.items():
        if v > 150:
            print(f"{k}'s price is {v}, it is more than 150")
            
foodInfo(map)


###### Shopping list 2
food_price = {'Eggs': 3.14, 
       'Milk': 1.07,
       'Rice': 1.59,
       'Cheese': 12.60,
       'Chicken Breasts': 9.40, 
       'Apples': 2.31,
       'Tomato': 2.58,
       'Potato': 1.75,
       'Onion': 1.10}

bob = {'Eggs': 2, 
       'Milk': 3,
       'Rice': 2,
       'Cheese': 1,
       'Chicken Breasts': 4, 
       'Apples': 1,
       'Tomato': 2,
       'Potato': 1}

alice = {'Eggs': 5, 
       'Rice': 1,
       'Chicken Breasts': 2, 
       'Apples': 1,
       'Tomato': 10}

def foodInfo(maps):
    
    price = 0
    for key,val in food_price.items():
        for k,v in bob.items():
            if k == key:
                init = v*val
                price = price + init
    print(f"Bob paid {price}.")
    
    price = 0
    for key,val in food_price.items():
        for k,v in alice.items():
            if k == key:
                init = v*val
                price = price + init
    print(f"Alice paid {price}.")    

    if bob['Rice'] > alice['Rice']:
        print("Bob buys more rice.")
    else:
        print("Alice buys more rice.")
    
    if "Potato" in alice.keys() and "Potato" in bob.keys():      
        if bob['Potato'] > alice['Potato']:
            print("Bob buys more Potato.")
        else:
            print("Alice buys more Potato.")
    
    bob_item = len(list(bob.keys()))
    alice_item = len(list(alice.keys()))    
    if bob_item > alice_item:
        print("Bob buys more different products.")
    else:
        print("Alice buys more different products.") 
        
    bob_sum_item = sum(list(bob.values()))
    alice_sum_item = sum(list(alice.values()))
    if bob_sum_item > alice_item:
        print("Bob buys more piece of products.")
    else:
        print("Alice buys more piece of products.")
    
foodInfo(map)

##########################################################################
Sets
##########################################################################

###### Set introduction
sets = set([])
print(type(sets))

num = [1,2,3,4,6]
sets = set(num)
print(sets)

sets.remove(6)
print(sets)

for i in sets:
    print(i)
 
for i in list(sets):
    if i == 482:
        sets.remove(i)
print(sets)

###### What's in my bag
oliver = set(["Laptop","Notebook","Pen","Sunglasses",
              "Hand sanitizer"])

ethan = set(["Sunglasses","Notebook","Phone"])
mia = set(["Laptop","Sunglasses","Hand sanitizer"])

e_and_m = ethan & mia
print(e_and_m)

o_not_m = oliver - mia
print(o_not_m)

emo = ethan & mia & oliver
print(emo)

###### Unique with set
name = ["Ava","Oliver","Ethan","Amelia",
            "Oliver","Mia","Lucas","Ava",
            "Ethan","Enzo"]

name_nodup = set(name)
print(name_nodup)
