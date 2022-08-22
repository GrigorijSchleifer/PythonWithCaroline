drug_list = [
    "paracetamol",
    "ibuprofen",
    "co-codamol",
    "vitamin b12"]

combinations = []

# first loop to extract the first drug
for drug in drug_list:
    # second loop to 
    for i in drug_list:
        if i == drug:
            continue
        combinations.append("[" + str(drug) + "," + str(i) + "]") 

for item in combinations:
    print(item)