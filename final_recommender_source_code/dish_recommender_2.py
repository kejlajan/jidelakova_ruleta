#!/usr/bin/env python
# coding: utf-8

# In[1]:


import json
import tkinter as tk
from tkinter import filedialog


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


# prints details of a dish nicely
def FormattedDetailsFromName (name):
    dish, ingredients_vector, amount_vector, recipe = DetailsFromName(name) 
    details = f'{dish.upper()}:\n'
    details += '---------------------------------------\n'
    details += 'Postup:\n'
    details += f'{recipe}\n'
    for ingredient, amount in zip(ingredients_vector, amount_vector):
        details += f'-- {ingredient} ... {amount}\n'
    return details
        
        
def ReadFiles():
    # read surky from file
    global surky_doma
    surky_doma = {}
    with open(selected_file_STR, 'r') as surky_file:
        for line in surky_file:
            line = line.strip()  # Remove leading/trailing whitespace, including '\n'
            if not line.startswith('#'):
                line = line.split() # split by spaces
                surky_doma[line[0]]=float(line[1]) # add into dictionary

    # read kucharka from file
    with open(selected_kuch_file_STR, "r",) as kucharka_json_file:
        global my_dict
        my_dict = json.load(kucharka_json_file)

    # 'calculate' the short output
def GetShortOutput():
    ingredients_at_home = list(surky_doma.keys())
    global names_of_dishes_availible
    names_of_dishes_availible = NameFromIngredients(*ingredients_at_home)
    global short_output
    short_output = ''
    for dish in names_of_dishes_availible:
        short_output += f"{dish} ... {CostFromName(dish)},-\n"
        
        
def GetLongOutput():
    global long_output
    long_output = ''
    for dish in names_of_dishes_availible:
        long_output += "=======================================\n"
        long_output += f"{FormattedDetailsFromName(dish)}\n"
    long_output += "=======================================\n"
    


# ### run GUI:

# In[3]:


def OpenFileOpenDialog():
    file_path = filedialog.askopenfilename(initialdir="./", title="Vyberte soubor se surovinami (inventář)")
    if file_path:
        inspect_file_BTN.config(state=tk.NORMAL)
        global selected_file_STR
        selected_file_STR = file_path
        UpdateSelectedFilepath()
        
def OpenKuchFileOpenDialog():
    file_path = filedialog.askopenfilename(initialdir="./", title="Vyberte soubor s recepty (kuchařku)")
    if file_path:
        inspect_file_BTN.config(state=tk.NORMAL)
        global selected_kuch_file_STR
        selected_kuch_file_STR = file_path
        UpdateSelectedKuchFilepath()

def InspectFile():
    if 'selected_file_STR' in globals():
        with open(selected_file_STR, 'r') as file:
            file_contents = file.read()
            display_WIN = tk.Toplevel(root_WIN)
            display_WIN.title("Obsah vaší spíže/lednice")
            file_contents_TXT = tk.Text(display_WIN)
            file_contents_TXT.insert(tk.END, file_contents)
            file_contents_TXT.pack()
            
def InspectKuchFile():
    if 'selected_kuch_file_STR' in globals():
        with open(selected_kuch_file_STR, 'r') as file:
            file_contents = file.read()
            display_WIN = tk.Toplevel(root_WIN)
            display_WIN.title("Obsah Vaší kuchařky")
            file_contents_TXT = tk.Text(display_WIN)
            file_contents_TXT.insert(tk.END, file_contents)
            file_contents_TXT.pack()

def UpdateSelectedFilepath():
    path_to_file_LBL.config(text = f"Soubor se surovinami: {selected_file_STR}")
    
def UpdateSelectedKuchFilepath():
    path_to_kuch_file_LBL.config(text = f"Soubor s kuchařkou: {selected_kuch_file_STR}")

def LaunchKucharka():
    ReadFiles()
    GetShortOutput()
    vypis_WIN = tk.Toplevel(root_WIN)
    vypis_WIN.title("Krátký výpis jídel")
    
    vypis_TXT = tk.Text(vypis_WIN)
    vypis_TXT.insert(tk.END, short_output)
    vypis_TXT.pack()
    
    GetLongOutput()
    long_vypis_WIN = tk.Toplevel(root_WIN)
    long_vypis_WIN.title("Podrobný výpis jídel")
    
    long_vypis_TXT = tk.Text(long_vypis_WIN)
    long_vypis_TXT.insert(tk.END, long_output)
    long_vypis_TXT.pack()
    
    

selected_file_STR = ' *** SOUBOR NEBYL VYBRÁN *** '

root_WIN = tk.Tk()
root_WIN.title("Doporučovač jídel")

select_file_BTN = tk.Button(root_WIN, text='Vybrat soubor', command = OpenFileOpenDialog)
select_file_BTN.pack()

path_to_file_LBL = tk.Label(root_WIN, text = f'Soubor se surovinami: {selected_file_STR}')
path_to_file_LBL.pack()


inspect_file_BTN = tk.Button(root_WIN, text = 'Prohlédnout soubor', command = InspectFile)
inspect_file_BTN.pack()




selected_kuch_file_STR = ' *** SOUBOR NEBYL VYBRÁN *** '


select_kuch_file_BTN = tk.Button(root_WIN, text='Vybrat soubor', command = OpenKuchFileOpenDialog)
select_kuch_file_BTN.pack()

path_to_kuch_file_LBL = tk.Label(root_WIN, text = f'Soubor s kuchařkou: {selected_kuch_file_STR}')
path_to_kuch_file_LBL.pack()


inspect_kuch_file_BTN = tk.Button(root_WIN, text = 'Prohlédnout soubor', command = InspectKuchFile)
inspect_kuch_file_BTN.pack()


launch_kucharka_BTN = tk.Button(root_WIN, text = 'Launch kucharka', command = LaunchKucharka )
launch_kucharka_BTN.pack()



root_WIN.mainloop()

