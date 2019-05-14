###########################################################################
#OOP
###########################################################################

###### Divide by zero
def count(divisor):
    try:
        result = 10 / divisor
        print(result)
    
    except ZeroDivisionError:
        print('Can\'t divide by zero!')

count(0)

###### Print each line
try:
    my_files = open("my-file.txt","r")
    my_file_names = "my-file.txt"

    for line in my_files:
        print(line, end="")
  
except IOError:
    print('Unable to read file: ', my_file_names)
	

###### Count lines
def file(filename):
    try:
        file_name = filename
        my_file = open(file_name,"r")
        len_of_file = len(my_file.readlines())
        print(len_of_file)    
  
    except IOError:
        print("0")

file("my-file.txt")


###### Write single line
def write_file(file):
    
    file_name = file
    
    if file_name == "my-file.txt":
        
        my_file = open(file_name,"w")
        my_file.write("Ke Su")
        return my_file 
        my_file.close

    raise TypeError

try:

    print(write_file("my-file.txt"))

except TypeError:

    print("Unable to write file: my-file.txt")
	
	
###### Write multiple lines
def write_multi_file(path, word, number):
    
    file_path = path
    write_word = word
    file_lines = number

        
    my_file = open(file_path , "a")
    for i in range(file_lines):
        my_file.write(write_word+"\n")
    my_file.close()
    
    return my_file 
    my_file.close

write_multi_file("/Users/Ke_Su/Desktop/my-file.txt", "Great", 5)


###### Copy file
def copy_file(file_name_r, file_name_w):
    
    name = file_name_r
    new_file = file_name_w
    
    my_file = open(name , 'r')
    my_file_write = open(new_file, 'a')
    
    read_file = my_file.readlines()
    
    
    for line in read_file:
        my_file_write.write(line)
    
    my_file_write.close()
    my_file.close()

    my_file_wr = open(new_file,'r')
    read_wr = my_file_wr.readlines()
    
    print(read_file == read_wr)
    
    return my_file_write
        
copy_file("my-file.txt", "new_file.txt")


###### Tic-Tac-Toe
import re

def tic_tac_result(filename):

    line = filename

    matchOX = re.search(r'-(.?)\.txt$', line)
    matchDraw = re.search(r'([a-zA-Z]+)\.txt$', line)

    if matchOX:
        return (matchOX.group(1))
    elif matchDraw:
        return (matchDraw.group(1))

print(tic_tac_result("draw.txt"))
print(tic_tac_result("win-o.txt"))
print(tic_tac_result("win-x.txt"))


###### Logs

import re

def log(filename):
    
        file_name = filename
        my_file = open(file_name,"r")
        list_file = my_file.readlines()
        
        addressSet = set()
        postList = []
        getList = []
        
        for i in range(len(list_file)):
            
            pattern = list_file[i]

            matchAddress = re.search(r'(\d+\.\d+\.\d+\.\d+)', pattern)
            matchPostGet = re.search(r'(POST|GET)', pattern)   

            if matchAddress:
                addressSet.add(matchAddress.group(1))
            if matchPostGet:
                if matchPostGet.group(1) == "POST":
                    postList.append(matchPostGet.group(1))
                else:
                    getList.append(matchPostGet.group(1))
                    
        count_post = len(postList)
        count_get = len(getList)
        
        print(f"The Ratio of get and post is {count_get}:{count_post}")
        print(f"The array of address is {addressSet}")
        
log("log.txt")
