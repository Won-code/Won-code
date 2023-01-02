#!/usr/bin/env python
# coding: utf-8

# In[2]:


print("\tWelcome to Wondell's Bar and Restaurant")
print("\t_______________________________________")
print("\n\t\tPlease Choose a Category")
print("\n\t(1) Select one for Meal \n\t(2) Select two for Drinks\n\t(3) Select three for Snacks")


# In[15]:


def category():
    category = int(input("Enter the Category:"))
    if category == 1:
        print("\n\tWhat type of Meal")
        print("\n\t(1) Fufu = 350.00LRD \n\t(2)Rice & Soup = 300.00LRD\n\t(3) Dumboy Soup = 500LRD")
        categoryMeal = int(input("\n\tEnter Menu Here: "))
        if categoryMeal == 1:
            quantitymeal= int(input("\n\tEnter the quantity of meal\nType Here: "))
            mealprice= 0
            meal = 0 
            while meal < quantitymeal:
                Mealprice += 350
                meal += 1
                print("\n\tYour total bill:", mealprice)
                cash = int(input("\n\tEnter your cash: "))
                change = cash - mealprice
                print("\nYour change is:", change)
                print("\n\n\\t-----------Thanks for your Transaction---------")
        elif categoryMeal == 2: 
            quantitymeal2= int(input("\n\tEnter the quantity of meal\nType Here: "))
            mealprice2= 0
            meal2 = 0 
            while meal2 < quantitymeal2:
                mealprice2 += 350
                meal2 += 1
                print("\n\tYour total bill:", mealprice2)
                cash2 = int(input("\n\tEnter your cash: "))
                change2 = cash2 - mealprice2
                print("\nYour change is:", change2)
                print("\n\n\\t-----------Thanks for your Transaction---------")
        elif categoryMeal == 3: 
            quantitymeal3= int(input("\n\tEnter the quantity of meal\nType Here: "))
            mealprice3= 0
            meal3 = 0 
            while meal3 < quantitymeal3:
                mealprice3 += 350
                meal3 += 1
                print("\n\tYour total bill:", mealprice3)
                cash3 = int(input("\n\tEnter your cash: "))
                change3 = cash3 - mealprice3
                print("\nYour change is:", change3)
                print("\n\n\\t-----------Thanks for your Transaction---------")
    elif category == 2: 
        print("\n\tWhat type of Drinks you want")
        print("\n\t(1) Water = 50.00LRD \n\t(2)Beer = 300.00LRD\n\t(3) Stout = 350LRD\n\t(4) Juice = 200LRD")
        categoryDrink = int(input("\n\tEnter Drink Here: "))
        if categoryDrink == 1: 
            quantitydrink = int(input("\n\tEnter the quantity of drink\nType Here: "))
            drinkprice= 0
            drink = 0 
            while drink < quantitydrink:
                drinkprice += 50
                drink += 1
                print("\n\tYour total bill:", drinkprice)
                cashdrink = int(input("\n\tEnter your cash: "))
                changedrink = cashdrink - drinkprice
                print("\nYour change is:", changedrink)
                print("\n\n\\t-----------Thanks for your Transaction---------")
        elif categoryDrink == 2: 
            quantitydrink2 = int(input("\n\tEnter the quantity of drink\nType Here: "))
            drinkprice2= 0
            drink2 = 0 
            while drink2 < quantitydrink2:
                drinkprice2 += 50
                drink2 += 1
                print("\n\tYour total bill:", drinkprice2)
                cashdrink2 = int(input("\n\tEnter your cash: "))
                changedrink2 = cashdrink2 - drinkprice2
                print("\nYour change is:", changedrink)
                print("\n\n\\t-----------Thanks for your Transaction---------")
        elif categoryDrink == 3: 
            quantitydrink3 = int(input("\n\tEnter the quantity of drink\nType Here: "))
            drinkprice3= 0
            drink3 = 0 
            while drink3 < quantitydrink3:
                drinkprice3 += 50
                drink3 += 1
                print("\n\tYour total bill:", drinkprice3)
                cashdrink3 = int(input("\n\tEnter your cash: "))
                changedrink3 = cashdrink3 - drinkprice3
                print("\nYour change is:", changedrink3)
                print("\n\n\\t-----------Thanks for your Transaction---------")
        elif categoryDrink == 4: 
            quantitydrink4 = int(input("\n\tEnter the quantity of drink\nType Here: "))
            drinkprice4= 0
            drink4 = 0 
            while drink4 < quantitydrink4:
                drinkprice4 += 50
                drink4 += 1
                print("\n\tYour total bill:", drinkprice4)
                cashdrink4 = int(input("\n\tEnter your cash: "))
                changedrink4 = cashdrink4 - drinkprice4
                print("\nYour change is:", changedrink4)
                print("\n\n\\t-----------Thanks for your Transaction---------")
    elif category == 3: 
        print("\n\tWhat type of Snack you want")
        print("\n\t(1) Doughnut = 30.00LRD \n\t(2)Meat Pie = 75.00LRD\n\t(3) Tea & Bread = 150LRD\n\t(4) Spaghetti = 175LRD")
        categoryDrink = int(input("\n\tEnter Snack Here: "))
        if categorySack == 1: 
            quantitysnack = int(input("\n\tEnter the quantity of drink\nType Here: "))
            snackprice= 0
            snack = 0 
            while snack < quantitysnack:
                snackprice += 50
                snack += 1
                print("\n\tYour total bill:", snackprice)
                cashsnack = int(input("\n\tEnter your cash: "))
                changesnack = cashsnack - drinksnack
                print("\nYour change is:", changesnack)
                print("\n\n\\t-----------Thanks for your Transaction---------")
        elif categorysnack == 2: 
            quantitysnack2 = int(input("\n\tEnter the quantity of snack\nType Here: "))
            snackprice2= 0
            snack2 = 0 
            while snack2 < quantitysnack2:
                snackprice2 += 50
                snack2 += 1
                print("\n\tYour total bill:", snackprice2)
                cashsnack2 = int(input("\n\tEnter your cash: "))
                changesnak2 = cashsnack2 - drinksnack2
                print("\nYour change is:", changesnack)
                print("\n\n\\t-----------Thanks for your Transaction---------")
        elif categorysnack == 3: 
            quantitysnack3 = int(input("\n\tEnter the quantity of snack\nType Here: "))
            snackprice3= 0
            snack3 = 0 
            while snack3 < quantitysnack3:
                snackprice3 += 50
                snack3 += 1
                print("\n\tYour total bill:", snackprice3)
                cashsnack3 = int(input("\n\tEnter your cash: "))
                changedrink3 = cashdsnack3 - snackprice3
                print("\nYour change is:", changesnack3)
                print("\n\n\\t-----------Thanks for your Transaction---------")
        elif categorysnack == 4: 
            quantitysnack4 = int(input("\n\tEnter the quantity of snack\nType Here: "))
            snackprice4= 0
            snack4 = 0 
            while snack4 < quantitysnack4:
                snackprice4 += 50
                snack4 += 1
                print("\n\tYour total bill:", snackprice4)
                cashsnack4 = int(input("\n\tEnter your cash: "))
                changedrink4 = cashsnack4 - snackprice4
                print("\nYour change is:", changesnack4)
                print("\n\n\\t-----------Thanks for your Transaction---------")
    else: 
        print("\n\tYour Selection is not part of today's Menu, Thanks")
        
category()

