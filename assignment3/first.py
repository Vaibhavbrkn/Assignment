"""Write a Python Program to implement your own myreduce() function which works exactly
like Python's built-in function reduce()"""

"""Write a Python program to implement your own myfilter() function which works exactly
like Python's built-in function filter()"""


# myreduce function
def myreduce(func , sequence):
    result = sequence[0]
    
    for item in sequence[1:]:
        result = func(result , item)
    
    return result


# Custom filter function 
def myfilter(func, sequence):
 result = []
 for item in sequence:
  if func(item):
   result.append(item)
 return result


def multipy(x , y):
    return x*y

def ispositive(x):
    if (x <= 0): 
        return False 
    else: 
        return True
    

print ("multipication on list [1,2,3,4,5,6] using myreduce function : "   + str(myreduce(multipy, [1,2,3,4,5,6])) )
print ("Filter only positive Integers on list [0,1,-2,3,4,-5,11] using custom filter function"  + str(myfilter(ispositive, [0,1,-2,3,4,-5,11])))