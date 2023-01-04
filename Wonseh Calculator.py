#!/usr/bin/env python
# coding: utf-8

# In[ ]:


print("\n\tWelcome to Wonseh Calculator")
print("\t_____________________________")

while True: 
    num1 = int(input("Enter: "))
    op = input("Enter: ")
    num2 = int(input("Enter: "))
    if op == "+": 
        result = num1 + num2
        print(result)
    elif op == "-": 
        result = num1 - num2
        print(result)
    elif op == "*": 
        result = num1*num2
        print(result)
    elif op == "/": 
        result = num1/num2
        print(result)
    elif op == "**": 
        result = num1**num2
        print(result)
    else: 
        print("Syntax Error")

