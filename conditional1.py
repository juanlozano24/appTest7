'''
this script let you apply basic match operations as:
add, mult, subs and div.
1. the user must press two numbers
2. the  user must press and option from menu
3. the function must apply the operation
'''
#Libraries
import os
#Function
def calc(x, y, z):
    if z==1 :
        Ans = x + y
    elif z==2 :
        Ans = x - y
    elif z==3 :
        Ans = x * y
    else :
        Ans = x / y
    return Ans
#Main##########
os.system("clear")
n1 = int(input("First number: "))
n2 = int(input("Second number: "))
print(":::Menu:::")
print("[1]. Add")
print("[1]. Subs")
print("[1]. Mult")
print("[1]. Div")
opt = int(input("Press a option: "))
print("The answer is: ",calc(n1,n2,opt))
