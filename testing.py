drug_list = [
    "paracetamol",
    "ibuprofen",
    "co-codamol",
    "vitamin b12",
    "metoprolol"
]


def make_defined_combinations(list_of_items: list, number_of_combinations: int) -> list:

    if number_of_combinations == 0:
        return [[]]

    l = []
    for i in range(0, len(list_of_items)):
        m = list_of_items[i]
        # print(f"{m} is the one")
        remLst = list_of_items[i + 1:]
        remainlst_combo = make_defined_combinations(remLst, number_of_combinations-1)
        # print(remainlst_combo)
        for p in remainlst_combo:
            l.append([m, *p])
            print(l)

    return l

defined_combinations = make_defined_combinations(drug_list, 4)

def loop_test(list_of_items):
    for itm in list_of_items:
        m = list_of_items[itm]
        print(f"{m} is the one")

loop_test(drug_list)