from itertools import combinations

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