#!/usr/bin/env python
# coding: utf-8

# In[ ]:


lists = int(input("Enter list length: "))
num = [int(input("Enter number: ")) for list in range(lists)]
my_list = list(num)
def max_l(my_list):
    my_max = float('-inf')
    for e in my_list: 
        if e > my_max: 
            my_max = e
    return my_max

max_l(my_list)

