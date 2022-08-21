drug_list = [
    "paracetamol",
    "ibuprofen",
    "co-codamol",
    "vitamin b12"]

combinations = []

# first loop to extract the first drug
for drug in drug_list:
    # second loop to 
    for index in range(len(drug_list)):
        two_drugs = [drug, drug_list[1]], [drug, drug_list[2]], [drug, drug_list[3]]
        combinations.append(two_drugs)
    drug_list.remove(drug)

for i in combinations:
    print(i)