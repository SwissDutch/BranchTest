#http://stackoverflow.com/questions/4935957/fibonacci-numbers-with-an-one-liner-in-python-3

startNumber = int(raw_input("Enter the start number here "))
endNumber = int(raw_input("Enter the end number here "))

#FIB RECURSIVE
def fib_recursive(n):
    if n < 2:
        return n
    return fib_recursive(n-2) + fib_recursive(n-1)

print "recursief: ", map(fib_recursive, range(startNumber, endNumber))

#FIB WITH FOR LOOP
def fib_for(n):
 a,b = 1,1
 for i in range(n-1):
  a,b = b,a+b
  print a, b
 return a + b
print fib_for(8)


#startNumber = int(raw_input("Enter the start number here "))
#endNumber = int(raw_input("Enter the end number here "))

#FIB WITH THE HELP OF SQRT(5) FORMULA
from math import sqrt
def fib_formula(n):
    return ((1+sqrt(5))**n-(1-sqrt(5))**n)/(2**n*sqrt(5))

print "formula: ", map(fib_formula, range(startNumber, endNumber))

#FIB 1-LINER WITH THE HELP OM LAMBDA + REDUCE + RANGE
#this maintains a tuple mapped from [a,b] to [b,a+b], initialized to [0,1], iterated N times, then takes the first tuple element
fib_oneliner = lambda n:reduce(lambda x,n:[x[1],x[0]+x[1]], range(n),[0,1])[0]
print "oneline for 1 number", fib_oneliner(8)


#A rarely seen trick is that a lambda function can refer to itself recursively:
fib_oneliner_recursive = lambda n: n if n < 2 else fib_oneliner_recursive(n-1) + fib_oneliner_recursive(n-2)
print "oneliner recursive: ", fib_oneliner_recursive(8)


#The recursive oneline is rarely seen because it's confusing, and in this case it is also inefficient.
##It's much better to write it on multiple lines:
def fib_while():
    a = 0
    b = 1
    while True:
        yield a
        a, b = b, a + b
print "fib while: ", fib_while(8)


#I recently learned about using matrix multiplication to generate Fibonacci numbers, which was pretty cool.
#You take a base matrix:
#[1, 1]
#[1, 0]
#and multiply it by itself N times to get:
#[F(N+1), F(N)]
#[F(N), F(N-1)]
#This morning, doodling in the steam on the shower wall, I realized that you could cut the running time in half
#by starting with the second matrix, and multiplying it by itself N/2 times, then using N to pick an index from
#the first row/column.
#
#With a little squeezing, I got it down to one line:

import numpy

def matrix_fib(n):
    return (numpy.matrix([[2,1],[1,1]])**(n//2))[0,(n+1)%2]

>>> [matrix_fib(i) for i in range(20)]
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181]