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

print(task_one(drug_list))

# Write a function that takes in a list of drugs, returns all unique 2-drug combinations as a list of pairs
def task_two(list_of_combinations):
    for idx, drug in enumerate(list_of_combinations):
        print(drug)
        if drug[0] == drug[1]:
            print(drug)
            list_of_combinations.pop(idx)
    print(list_of_combinations) 
    return list_of_combinations 

# create combination list 
unique_combinations = task_one(drug_list)

# print unique pairs 
task_two(unique_combinations)