drug_list = [
    "paracetamol",
    "ibuprofen",
    "co-codamol",
    "vitamin b12",
    "metoprolol"
    ]

# empty list for drug combinations
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
            if item == second_item:
                continue    
            combinations.append([item, second_item])
    return combinations

all_combinations = make_combinations(drug_list)
# print list with all combinations


