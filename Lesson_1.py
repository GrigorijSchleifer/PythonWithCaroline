drug_list = [
    "paracetamol",
    "ibuprofen",
    "co-codamol",
    "vitamin b12"]

combinations = []

for drug in drug_list:
    for index_drug in range(len(drug_list)):
        two_drugs = [drug, drug_list[1:len(drug_list)]]
        combinations.append(two_drugs)
        drug_list = drug_list[:len(drug_list)]

for i in combinations:
    print(i)