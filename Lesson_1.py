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


def make_combinations(list_of_items: list) -> list:
    """
    Take list of items and return all 2-item combinations except identical combinations 

    Args:
    list_of_items (list): a list of items to be combined

    Returns:
    list: A list of lists of pairs
    """
    # first loop to extract the first item
    for item in list_of_items:
        # second loop to
        for second_item in list_of_items:
            combinations.append([item, second_item])
            if item == second_item:
                continue    
    return combinations

all_combinations = make_combinations(drug_list)
# print list with all combinations
for i in all_combinations:
    print(i)
# print a new line for better visibility 
print("\n")
    
# Write a function that takes in a list of drugs, returns all unique 2-drug combinations as a list of pairs
def make_unique_combinations(list_of_items: list) -> list:
    """
    Take list of drugs and return all unique 2-item combinations as a list of pairs
    
    Args:
    list_of_items (list): a list of items to be filtered for unique combinations

    Returns:
    list: A list of lists of unique pairs
    """
    for idx, drug in enumerate(list_of_items):
        return list_of_items 

unique_combinations = make_unique_combinations(all_combinations)
# print unique pairs 
for i in unique_combinations:
    print(i)




