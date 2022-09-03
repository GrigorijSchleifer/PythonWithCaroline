def no_recursion_test(list_of_items: list) -> list:
    """
    Testing the function where length of a list inside a list is defined by the user
    But not implementing the recursion ... just to see what is going on and what is returned 
    Without recursion
    
    Args: 
    Same as the make_defined_combinations funciton
    
    Return:
    A list lists of user defined x-length
    """
    l = []
    for i in range(0, len(list_test)):
        m = list_of_items[i]
        remLst = list_of_items[i + 1:]
        for p in remLst: 
            # what is asterix doing here ...  
            l.append([m, *p])
            
    for itm in l: 
        print(itm)

no_recursion_test(list_test)

def recursion_test(list_of_items: list, number_of_combinations: int) -> list:
    """
    ...
    
    Args: 
    Same as the make_defined_combinations funciton
    
    Return:
    A list lists of user defined x-length
    """
    l = []
    for i in range(0, len(list_test)):
        m = list_of_items[i]
        remLst = list_of_items[i + 1:]
        remainlst_combo = no_recursion_test(remLst, number_of_combinations -1)
        for p in list_of_items: 
            l.append([m, *p])
            
    for itm in l: 
        print(itm)


list_test = [['one'],['two'], ['three'], ['four'], ['five'], ['six']]
list_test_simple = ['one','two', 'three', 'four', 'five', 'six']

ll = []
xy = 'Cool Daddy'

for itm in list_test:
    ll.append([xy, itm])

print(*list_test)
unpacked = 'cool'
print(*unpacked)