def rec_sum_search_helper(
    rec_depth: int,
    list: list[float],
    key: float,
    past_sum: float,   # accumulator: all addends summed up before next recursion
    visual: str        # accumulator: same as above but for visual output
):
    # base case: final recursion layer, searches for matching sums
    if rec_depth <= 0:
        for i in list:
            test_sum = round(past_sum + i, 2)
            #print(f"{visual}{i} = {test_sum}")
            if test_sum == key:
                print(f"FOUND SOLUTION: {visual}{i} = {test_sum}")

    # recursive case: spawns another search function for next addend
    else:
        list_cut = list.copy()
        for i in list:
            past_sum_new = round(past_sum + list_cut.pop(0), 2)
            visual_new = f"{visual}{i} + "
            rec_sum_search_helper(rec_depth - 1, list_cut, key, past_sum_new, visual_new)



def rec_sum_search(
    list: list[float],         # list of possible addends
    key: float,                # sum of some addends the program solves for
    rec_depth: int|None = None # max number of addends the solution can be made of
                               # default: length of list
):
    if not rec_depth:
        rec_depth = len(list)

    # remove all bigger than key
    new_list = list.copy()
    for i in list:
        if i > key:
            new_list.remove(i)
    list = new_list.copy()

    # recursively search through rec_depth number of addends
    for layer in range(rec_depth + 1):
        rec_sum_search_helper(layer, list, key, 0, "")




## list of addends
sums: list[float] = [
        45.87, 67.88, 67.96, 67.02, 128.89, 200.74, 140.25, 69.69, 100.37, 40.7, 500.59, 30.45, 45.89, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

rec_sum_search(list=sums, key=421.24)
