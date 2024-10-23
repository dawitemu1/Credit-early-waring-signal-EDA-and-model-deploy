#!/usr/bin/env python
# coding: utf-8
# %%

# # Summer School

# %%


3 + 4
(9 + 3) / 6 
11 * 12


# %%


def average(a, b):
    return (a + b) * 0.5


# %%


e="selam"


# %%


f=d+e


# %%


type=f


# # FUNCTION

# %%


def mysum(a,b);
*** returen the sum of parameters a and b,***
return a*b


# %%


all functions do not have return values  to find the function. parts of function docstring, body of function 


# # conditional if- else

# # phyton value true and false special inbuilt objects
# a=true0
# we caan oeratr these two logical values using bpplean logic example the logical and operation(and)
# logical or and the nogetiation not
# either true or false  sometimes called predicate 
# example=x=30
# x>=30
# true
# x=>15
# true
# if-else command allow to branch the execution path depending on  acondition 
# example x=30
# ifx>30
# print("yes")
# else
# print("no")
# the general struchure of the if-else statement is
# if a
# B
# else
# c
# a is predicate
# if a evaluates to true then all commands b are carried out  and c is skipped 
# if a evaluates to false then all commands c are carried out b
# 
# #if- else example
# def slength(s)
# returens a string describing the length of the sequence(s)
# if len(s)>10
# 
# 
# #if-else example2
# def slength2(s)
# if len(s)==0
# and='empty'
# elif len(s)>10:
#     ans="very long'
#     elif len(s)>7:
#         ans='normal'
#         else
#         ans='short'
#         returen ans
#         >>> slength2("")
#         empty
#         >>> slength2("greetings")
#         'normal'
#         >>> slength2("hi")
#         'short'
#        
#         
#         
#         
#         

# # # squence 
# ' a string ' 
# "another string"
# string  with in the middle """ a string with triple quotes can extend over several lines """
# a= " hello world"
# a[4]
# '0'
# >>> a[4:7]
# '0 w'
# >>> len9a0
# 11
# >>> 'd' in a
# true
# >>> 'x' in a
# false
# >>> a+a
# ' hello world hello world'
# >>> 3* a
# 'hello world worldhello world'
#  define a, b and c 
#  # Loop
#  it excutes the same way 
#  *************************************************
#  animals=['dog', 'cat' ,' mouse']
#  for animal in animls:
#   print( f" this is the {animal}!")
#   this is dog
#   this is cat
#   this is mouse
#   ************************************************
#   for i in range(6):
#   print(f" the sques of {i} is {i**2}")
# 
#  products
#  the squre of 0 is 0
#  the squre of 1 is 1
#  the squre of 2 is 4
#  the squre of 3 is 9
#  the squre of 5 is 25
#  ******************************************************************
#  range
#  range(start,) stop(,stop) iteriates over intigers from start to stop (but not including stop)
#  for loop itrates over iteriables
#  squences are itriable
#  example
#  for i in [0,3,4,19]:
#  print(i)
#  for animal in ['dog','cat','mouse']:
#  *********************************************************************
#  # while loop
#  it is itrates while a condition is fulfilled
#  x=64
#  while x>10;
#  x= x//2
#  print(x)
#  product
#  32
#  16
#  8

# %%





# %%





# %%


import math


# %%


def box_volume(a,b,c):
    """ give parameter a,b and c compute return the volume of the corresponding cuboid """
    return a*b*c


# %%


box_volume(1, 2, 3)


# %%


4**0.5


# # String

# %%


a="one"
b="two"
c="four"
d="a+B+C"
d
'onetwofour'


# %%


5*'onetwofour'


# %%


5*d


# # List example 2

# %%


a=[]
a
[]
a.append('dog')
a


# %%


a.append('cat')
a


# %%


a[1]


# %%


a.append("mouse")
a[-1]


# %%


a


# %%


print (a)


# %%


print(a[2])


# %%


a[3]
Traceback(most recent cell last)
cell in (27), line 1
a


# # Loop

# %%


for latter in "jerry and seli":
    print(latter)


# %%


def skip13(a,b):
    result= []
    for k in rannge(a,b):
        if k==13:
            result.append(k)
    return result


# # while Loop example2

# %%





# %%


eps =1.0
while eps + 1>1:
    eps = eps/ 2.0
    print (f"epsilon is {eps}")


# # Algebera

# %%


import sympy
import numpy as np
from numpy.linalg import norm
from numpy.linalg import det
from numpy.linalg import inv


# %%


list1 = [10,20,30,40,50]
vtr1 = np.array(list1)
scalar_value = 5.
print("We create vector from a list 1:")
print(vtr1)


# %%


# printing scalar value.
print("Scalar Value : " + str(scalar_value))


# # column vector(listed in to Array)

# %%


vtr1 = np.array(vector_row)
x= np.array(vector_column)
vector_row=np.array([[1,-2,3,-7]])
vector_column= np.array([[1],
                       [-2],
                       [4],
                       [6]])
print (x,vtr1)


# %%


print(vector_row.shape)
print (vector_column.shape)


# %%


sum= 70+2
print(sum)


# %%


result=(5+7)/9
print(result)


# %%


mul= 23*12
print(mul)


# %%


res= 6 ** 3
print(res)


# %%


s= 2** 0.5
print(s)


# %%


def compute_average(n1 ,n2):
    sum=n1 + n2
    average=sum/2
    return(average)
num1=5
num2=20
avg=compute_average(num1,num2)
print("the aveage of " ,num1, "and" ,num2 ,avg)


# %%


def add(d,e):
    return d+e
add(3,9)


# %%


def distance(d,e):
    return d-e
distance(3,9),distance(9,3)


# %%


def com_distance( x,y):
    if x>y:
        return x-y
    else:
        return y-x
x1=6
y1=15
res=com_distance(x1,y1)
print("the distance betweem",x1,"and",y1, "is:",res)


# %%


a=5
h=10
def pyramid_volume(a ,h):
    return a *h/2
pyramid_volume(a,h)


# %%


def compute_sum(a ,b):
    return a+b
print("sum is:",compute_sum(10,20))


# %%


def compute_sum(arr):
    total = 0
    for num in arr:
        total += num
    return total
array=[1,2,3,4,5]
print(compute_sum(array))


# %%


def compute_distance(x1 ,y1):
    return math.sqrt(x1-y1)

print("distance is", com_distance(5,5))


# %%


def geometric_mean(numbers):
    product=1 
    for num in numbers:
    product *=num
return product **(1 / len(numbers))
geometric_mean(3,4)


# %%




