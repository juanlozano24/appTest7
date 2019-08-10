#Basic Calc to junior users
#Developer: Juan Lozano

#Libraries###########################
import os
####################################


#Functions###########################
def calc(x,y):
    suma = x + y
    print("La suma es :  ", suma)
#Main###########################    
os.system("clear")
a = int(input("press number 1: "))
b = int(input("press number 1: "))
calc(a,b)