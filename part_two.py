drug_list = [
    "paracetamol",
    "ibuprofen",
    "co-codamol",
    "vitamin b12",
    "metoprolol"
    ]

# empty list for drug combinations
combinations = []

# Write a function that takes in a list of drugs, returns all unique 2-drug combinations as a list of pairs
def make_unique_combinations(list_of_items: list) -> list:
    """
    Take list of drugs and return all unique 2-item combinations 
    as a list of pairs and filters out all repeats
    
    Combination like ['paracetamol', 'ibuprofen'] == ['ibuprofen', 'paracetamol'] will be removed
    
    Args:
    list_of_items (list): a list of items to be filtered for unique combinations

    Returns:
    list: A list of lists of unique pairs
    """
    for drug in list_of_items:
        if drug[::-1] in list_of_items:
            list_of_items.remove(drug[::-1])
    return list_of_items 

unique_combinations = make_unique_combinations(drug_list)
