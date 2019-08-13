import os
from random import randint,uniform,random

def Z():
    AnsZ = randint(0,100)
    return AnsZ
#this funcion generates float numbers

def R():
    AnsR = uniform(0,100)
    return AnsR
#Main 
os.system("clear")
print("The integer random number is: ", Z())
r = R()
print("The float random number is: ", r)





