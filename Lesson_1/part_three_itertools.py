from itertools import combinations
 
"""
Use combinations module from itertools package 
Not clear at all what is going on under the hood

Args: Not clear

Return: List
"""

drug_list = [
    "paracetamol",
    "ibuprofen",
    "co-codamol",
    "vitamin b12",
    "metoprolol"
    ]
   

combis = list(combinations(drug_list, 3))

for itm in combis:
    print(itm)