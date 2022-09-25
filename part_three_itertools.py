from itertools import combinations

drug_list = [
    "paracetamol",
    "ibuprofen",
    "co-codamol",
    "vitamin b12",
    "metoprolol"
    ]


unique_comb = [",".join(map(str, comb)) for comb in combinations(drug_list, 3)]

for comb in unique_comb:
    print(comb)