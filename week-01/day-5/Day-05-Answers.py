##########################################################################
Sorting Algorithm
##########################################################################

###### Insertion Sort
def insertionSort(arr): 
 
    for i in range(1, len(arr)): 
  
        key = arr[i] 
        j = i-1
        while j >=0 and key < arr[j] : 
                arr[j+1] = arr[j] 
                j -= 1
        arr[j+1] = key

###### Qicksort
 		
##########################################################################
Basic matrix operations
##########################################################################

###### Addition
def addMatrix(m1,m2):
    
# define matrix with all 0
    result = [[0,0,0],         
              [0,0,0], 
              [0,0,0]]
    
# iterate through rows     
    for i in range(len(m1)):
        
# iterate through columns 
        for j in range(len(m1[0])): 
            result[i][j] = m1[i][j] + m2[i][j] 

    for r in result: 
        print(r)


# Testing 
        
X = [[1,2,3], 
    [4,5,6], 
    [7,8,9]] 
  
Y = [[9,8,7], 
    [6,5,4], 
    [3,2,1]]

addMatrix(X,Y)

###### Subtraction
def subMatrix(m1,m2):
    
# define matrix with all 0
    result = [[0,0,0],         
              [0,0,0], 
              [0,0,0]]
    
# iterate through rows     
    for i in range(len(m1)):
        
# iterate through columns 
        for j in range(len(m1[0])): 
            result[i][j] = m1[i][j] - m2[i][j] 

    for r in result: 
        print(r)


# Testing 
        
X = [[1,2,3], 
    [4,5,6], 
    [7,8,9]] 
  
Y = [[9,8,7], 
    [6,5,4], 
    [3,2,1]]

addMatrix(X,Y)

###### Scalar Multiplication
def scaMulMatrix(scalar,m):
    
# define matrix with all 0
    result = [[0,0,0],         
              [0,0,0], 
              [0,0,0]]
         
    for i in range(len(m)):
        for j in range(len(m[i])):
            result[i][j] = m[i][j] * scalar

    for r in result: 
        print(r)
  
# Testing
  
X = 2
  
Y = [[1,2,3], 
    [4,5,6], 
    [7,8,9]] 

scaMulMatrix(X,Y)


###### Transposition
def trans(x):

    trans_X = [*zip(*X)]

    print(trans_X)
    
    
X = [[1,2,3], 
     [4,5,6]]
trans(X)


###### vertical and horizontal flipping easy way
def matrixflipEasy(m,d):   # horizontal d = h, vertical d = v
    tempm = m.copy()
    if d=='h':
        for i in range(0,len(tempm),1):
                tempm[i].reverse()
    elif d=='v':
        tempm.reverse()
    print(tempm)       
 
X = [[1,2,3], 
     [4,5,6]]

matrixflip(X,"h")


###### vertical and horizontal flipping hard way
import copy

def matrixflipHard(m,d):
    
    tempm = copy.deepcopy(m)
    
    j_rev_List = list(range(len(tempm[0])))       
    j_rev_List = j_rev_List[::-1]
    
    i_rev_List = list(range(len(tempm)))
    i_rev_List = i_rev_List[::-1]


    if d == "h":        
        for i in range(len(tempm)):
            for j in range(len(tempm[i])):
                tempm[i][j] = m[i][j_rev_List[j]]
        print(tempm)
    elif d == "v":
        for i in range(len(tempm)):
            for j in range(len(tempm[i])):
                tempm[i][j] = m[i_rev_List[i]][j]
        print(tempm)
        

x = [[1,2,3], 
     [4,5,6]]
matrixflipHard(x,"h")
matrixflipHard(x,"v")

