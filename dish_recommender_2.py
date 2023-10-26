#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random
import sys
import json


# In[2]:




# searches for a dish by name and returns its list of ingredients
def IngredientsFromName (name):
    try:
        return my_dict["jidla"][name][name]["surky"]
    except KeyError as K:
        pokrm_co_chybi = str(K).split("'")[1]
        return f"KeyError: Pokrm zvany '{pokrm_co_chybi}' nebyl v kucharce nalezen."
        

# searches for a dish by name and returns its final cost vector
def CostVectFromName (name):
        return [ surky_doma[ingredient] for ingredient in IngredientsFromName(name)]



# returns ingredients amount vector from name
def IngrAmountVectFromName (name):
    try:
        return my_dict["jidla"][name][name]["mnozstvi"]
    except KeyError as K:
        pokrm_co_chybi = str(K).split("'")[1]
        return f"KeyError: Pokrm zvany '{pokrm_co_chybi}' nebyl v kucharce nalezen."



# searches for a dish by name and returns its final cost vector
def CostFromName (name):
        return round(sum([a * b for a,b in zip(CostVectFromName(name), IngrAmountVectFromName(name))]),2)



# searches for the dishes that are cookable with @home ingredients
def NameFromIngredients (*args):
    if len(args) < 1:
        return "NameFromIngredientsError: Zadne ingredience nebyly zadany -- nejake zadejte."
    else:
        set_of_args = set(args)
        foodnames = []
        for jidlo in list(my_dict["jidla"].keys()):
            if set(IngredientsFromName(jidlo)) <= set_of_args:
                foodnames.append(jidlo)
            else:
                pass
        return foodnames



# returns details from name nicely
def DetailsFromName (name):
    jidlo = my_dict["jidla"][name][name]
    return name, jidlo["surky"], jidlo["mnozstvi"], jidlo["postup"]


# prints details of a food nicely
def PrintDetailsFromName (name):
    dish, ingredients_vector, amount_vector, recipe = DetailsFromName(name) 
    print(f'{dish.upper()}:')
    print("---------------------------------------")
    print(f'''Postup:
{recipe}''')
    for ingredient, amount in zip(ingredients_vector, amount_vector):
        print(f'-- {ingredient} ... {amount}')



# read surky from file
surky_doma = {}
with open('./doma.surky', 'r') as surky_file:
    for line in surky_file:
        line = line.strip()  # Remove leading/trailing whitespace, including '\n'
        if not line.startswith('#'):
            line = line.split() # split by spaces
            surky_doma[line[0]]=float(line[1]) # add into dictionary



# read kucharka from file
with open("./kucharka_2.json", "r",) as kucharka_json_file:
    my_dict = json.load(kucharka_json_file)


# ### /\*jakoby\*/ main{...

# In[3]:


ingredients_at_home = list(surky_doma.keys())
names_of_dishes_availible = NameFromIngredients(*ingredients_at_home)
for dish in names_of_dishes_availible:
    print(f"{dish} ... {CostFromName(dish)},")


# In[4]:


names_of_dishes_availible


# In[5]:


for dish in names_of_dishes_availible:
    print("=======================================")
    PrintDetailsFromName(dish)
    print("=======================================")


# In[ ]:




