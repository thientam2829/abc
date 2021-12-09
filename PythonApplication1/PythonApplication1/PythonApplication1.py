from math import sqrt
import math
from typing import cast
print("Quadratic Equation System Solver\n")
print("Hi.Please input an integer a : ")
a = int(input("a=  "))
print("Nice.Please input an integer b: ")
b = int(input("b = "))
print("Nice.Please input an integer c :")
c = int(input("c = "))
if(a==0):
    while True :
       a = int(input("Sorry, Please reInput .a= "))
       if (a >0) :
           break
delta = b*b - 4*a*c 
if (delta < 0):
 print ("Sorry, your Quadratic Equation has no solution. ")
        
elif (delta==0) :
     x = -b/(2*a)
     print("Your equation has both same of solution x1 = x2 = : " + str(x))
else :
    x1 = (-b + math.sqrt(delta))/(2*a)
    x2 = (-b - math.sqrt(delta))/(2*a)
    print ("Your equation has two distinct solution x1 = "+ str(x1) + "and "+"x2 = " +str(x2))  