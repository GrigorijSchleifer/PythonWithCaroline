drug_list = [
    "paracetamol",
    "ibuprofen",
    "co-codamol",
    "vitamin b12",
    "metoprolol",
    "penicillin",
    "aspirin",
    "suprarenine"]

combinations = []


# Write a function that takes in a list of drugs, and returns all 2-drug combinations as a list of pairs. 
def task_one(list_of_drugs):
    # first loop to extract the first drug
    for drug in drug_list:
        # second loop to 
        for i in drug_list:
            combinations.append([drug, i])
    return combinations

all_combinations = task_one(drug_list)
# print list with all combinations
for i in all_combinations:
    print(i)

# print a new line for better visibility 
print("\n")
    
# Write a function that takes in a list of drugs, returns all unique 2-drug combinations as a list of pairs
def task_two(list_of_combinations):
    for idx, drug in enumerate(list_of_combinations):
        if drug[0] == drug[1]:
            list_of_combinations.pop(idx)
        if drug[::-1] in list_of_combinations:
            list_of_combinations.pop(idx)
    return list_of_combinations 

unique_combinations = task_two(all_combinations)
# print unique pairs 
for i in unique_combinations:
    print(i)




