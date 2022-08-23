drug_list = [
    "paracetamol",
    "ibuprofen",
    "co-codamol",
    "vitamin b12"]

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
print(all_combinations)

# print a new line for better visibility 
print("\n")

# Write a function that takes in a list of drugs, returns all unique 2-drug combinations as a list of pairs
def task_two(list_of_combinations):
    for idx, drug in enumerate(list_of_combinations):
        if drug[0] == drug[1]:
            print(drug[0])
            print(drug[1])
            list_of_combinations.pop(idx)
    return list_of_combinations 

unique_combinations = task_two(all_combinations)
# print unique pairs 
print(unique_combinations)








