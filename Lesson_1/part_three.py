# hello from VS code on Ipad
drug_list = [
    "paracetamol",
    "ibuprofen",
    "co-codamol",
    "vitamin b12",
    "metoprolol"
    ]

# empty list for drug combinations
combinations = []

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
