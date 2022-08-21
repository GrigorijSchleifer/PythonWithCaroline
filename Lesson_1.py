drug_list = [
    "paracetamol",
    "ibuprofen",
    "co-codamol",
    "vitamin b12"]

# first loop to extract the first drug
for drug in drug_list:
    # second loop to 
    for i in drug_list[1:]:
        print("[" + str(drug) + "," + str(i) + "]") 