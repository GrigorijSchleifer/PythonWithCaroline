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

# print a new line for better visibility 
print("\n")
    
# Write a function that takes in a list of drugs, returns all unique 2-drug combinations as a list of pairs
def make_unique_combinations(list_of_items: list) -> list:
    """
    Take list of drugs and return all unique 2-item combinations 
    as a list of pairs and filters out all repeat
    
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


unique_combinations = make_unique_combinations(all_combinations)

# print unique pairs 
# for i in unique_combinations:
#     print(i)

# I am not sure I understand how this method works
# This is why I am debugging the code at the moment and will not start with task 4 
# until I have at least a better grasp of the recursion method I am using here ...
def make_defined_combinations(list_of_items: list, number_of_combinations: int) -> list:
    """
    Take in a list of drugs and the number of drugs in a combination
    And return unique combinations that match that user defined number

    Args:
    list_of_items (list): a list of items to be filtered for unique combinations
    user defined number of drugs in a combination

    Return:
    A list lists of user defined x-length
    """
    if number_of_combinations == 0:
        return [[]]
     
    l =[]
    for i in range(0, len(list_of_items)):
        # i is not a sting but an integer
        m = list_of_items[i]
        # this will store the rest of the list
        remLst = list_of_items[i + 1:]
        # recursive function call ... but  
        remainlst_combo = make_defined_combinations(remLst, number_of_combinations-1)
        for p in remainlst_combo:
                # append will add a list, extend would add all list items, not a whole list
                # https://scripteverything.com/what-does-asterisk-before-variable-name-mean-in-python/
                l.append([m, *p])    
    
    return l

defined_combinations = make_defined_combinations(drug_list, 4)
for itm in defined_combinations:
    print(itm)

