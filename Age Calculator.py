#!/usr/bin/env python
# coding: utf-8

# In[ ]:


while True: 
    father = int(input("Enter Father year of birth: "))
    mother = int(input("Enter Monther year of birth: "))
    child = int(input("Enter Child year of birth: "))
    def ages(father, mother, child):
        age_father = child - father
        age_mother = child - mother
        if age_father < 18 or age_mother<18: 
            print('One or more parent age is too low')
        elif age_father>60 or age_mother > 60: 
            print('One or more parent ages is too high')
        else: 
            print('Fathers age: ', age_father)
            print('Mothers age: ', age_mother)

    ages(father, mother, child)

