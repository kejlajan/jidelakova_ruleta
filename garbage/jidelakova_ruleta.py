#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random


# In[2]:


my_dict = {
    "jidla": [
        {
            "svickova": {
                "surky": ["maso", "mrkev", "cibule"],
                "postup": "Nakrajime surky, hodime je do hrnce a tak uvarime svickajdu, nebo ne, ja nevim",
            }
        },
        {
            "koprovka": {
                "surky": ["vejce", "kopr", "cibule"],
                "postup": "Nakrajime surky, hodime je do hrnce a tak uvarime kopracku, nebo ne, ja nevim",
            }
        },
	{
    "knedliky_se_shunkou_a_zervou": {
        "surky": ["knedliky", "shunka", "zervova omacka"],
        "postup": "Uvarte knedliky, nakrejte shunku, pripravte zervovou omacku. Podavejte knedliky s narezanou shunkou a zalijte zervovou omackou."
    }
},
{
    "bramborak_smasem": {
        "surky": ["brambory", "hovezi maso", "cibule", "vejce"],
        "postup": "Nakrejte brambory, osmahnete s hovezim masem a cibuli. Pridejte vajicka a smazte do zlatova."
    }
},
{
    "smazeny_syr": {
        "surky": ["syr", "mouka", "vejce", "strouhanka"],
        "postup": "Oblate syr v mouce, vejcih a strouhance. Smazte do zlatova. Podavejte s hranolkami nebo bramborovym salatem."
    }
},
{
    "svickova_na_smetane": {
        "surky": ["svickova", "mrkev", "cibule", "smetana"],
        "postup": "Osmahnete svickovou s mrkvi a cibuli, pridejte smetanu a dusime do mekka. Podavejte s houskovym knedlikem."
    }
},
{
    "rizek_s_kapustou": {
        "surky": ["rizek", "kapusta", "kmin"],
        "postup": "Umakejte rizek, uvarte kapustu s kminem. Podavejte rizek s kapustou a bramborovym salatem."
    }
}
    ]
}

# In[3]:


random.shuffle(my_dict["jidla"])


# In[4]:


# # Iterate through the outer dictionary
# for jidlo in my_dict["jidla"]:
#     # Iterate through the inner dictionaries
#     for jmeno, details in jidlo.items():
#         print("Jídlo:", jmeno)
#         for key, value in details.items():
#             if key == "surky":
#                 print("Suroviny:")
#                 for surovina in value:
#                     print("- " + surovina)
#             elif key == "postup":
#                 print("Postup:")
#                 print(value)
#             else:
#                 print(key + ":", value)
#         print()


# In[5]:


# Access the first item in the "jidla" list
first_dish = my_dict["jidla"][0]

# Iterate through the first dish
for jmeno, details in first_dish.items():
    print("\nJídlo:", jmeno)
    for key, value in details.items():
        if key == "surky":
            print("\nSuroviny:")
            for surovina in value:
                print("\t- " + surovina)
        elif key == "postup":
            print("\nPostup:")
            print(f"\t{value}")
        else:
            print(key + ":", value)


# In[ ]:




