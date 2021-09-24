# this program will do a mathematical operation, that is given by the user, on 2 given numbers, which is also given by the user.
from time import sleep
import os
def clear():
    os.system("cls")

def exit(n):
    while n != 0:
        clear()
        print("The program will exit in " + str(n) + " seconds")
        sleep(1)
        clear()
        n -= 1

def calculator():
    # input of the first number
    print("Type in a number")
    num1 = input("Input: ")
    print()

    # input of the mathematical operator
    clear()
    print("Your equation: " + num1)
    print("Type in the mathematical operation (\"+\",\"-\",\"*\",\"/\")")
    operator = input("Input: ")
    print()

    # input of the second number
    clear()
    print("Your equation: "+ num1+operator)
    print("Type in another number")
    num2 = input("Input: ")
    print()

    # output of the answer
    clear()
    print("Your equation is: "+num1+operator+num2)
    num1 = float(num1)
    num2 = float(num2)
    if num1 % 1 == 0:
        num1 == int(num1)
    else:
        num1 == float(num1)

    if num2 % 1 == 0:
        num2 == int(num2)
    else:
        num2 == float(num2)

    if operator == "+":
        answer = num1+num2
    elif operator == "-":
        answer = num1-num2
    elif operator == "*":
        answer = num1*num2
    elif operator == "/":
        answer = num1/num2

    if answer % 1 == 0:
        print("Which equals to: "+str(int(answer)))
    else:
        print("Which equals to: "+str(answer))
    yesList = ["y","Y"]
    noList = ["n","N"]
    con = input("Do you want to make another calculation? (Y,N)\n")
    if con in yesList:
        clear()
        calculator()
    elif con in noList:
        exit(3)
    else:
        print("You managed to say neither of the choices.")
calculator()
