
# remove all bigger than key
def list_clean(list: list[float], key: float):
    list_out = list.copy()
    for i in list:
        if i > key:
            list_out.remove(i)

    return list_out

# split sums into different equally split category sizes
def categorise(list: list[float], key: float):
    label_list: list[int] = []

    #cat_res: int = round((key / min(list)) + 0.5)
    cat_res: int = int(len(list) / 3) * 2

    for i in range(len(list)):
        label_list.append(cat_res)

    for i in range(cat_res):
        cat_limit: float = key / cat_res * (cat_res - i)

        for j in range(len(list)):
            if list[j] <= cat_limit:
                label_list[j] = cat_res - i -1
                #print(list[j])

        #print(f"------- CATEGORY {cat_res - i - 1} | {cat_res - i}: <= {cat_limit}")

    return [cat_res, label_list]



def rec_sum_search_helper(
    rec_depth: int,
    list: list[float],
    label_list: list[int], # category of [index] element in list
    key: float,
    categories: int,   # number of categories
    past_sum: float,   # accumulator: all addends summed up before next recursion
    visual: str,       # accumulator: same as above but for visual output
    cat_sum_ceil: int, # acc: check for too big sums
    cat_sum_floor: int # acc: check for too little sums
):
    # base case: final recursion layer, searches for matching sums
    if rec_depth <= 0:
        cat_sum_floor = cat_sum_floor + max(label_list) + 1
        # special case: sum too small
        if cat_sum_floor < categories:
            #print(f"PASS: Too small {cat_sum_floor}")
            return

        for i in list:
            test_sum = round(past_sum + i, 2)
            #print(f"{visual}{i} = {test_sum}")
            if test_sum == key:
                print(f"FOUND SOLUTION: {visual}{i} = {test_sum}")

    # recursive case: spawns another search function for next addend
    else:
        # special case: sum too big
        if cat_sum_ceil >= categories:
            #print(f"PASS: Too big {cat_sum_ceil}")
            return

        list_cut = list.copy()
        lbl_list_cut = label_list.copy()
        for i in range(len(list) - 1):
            past_sum_new = round(past_sum + list_cut.pop(0), 2)
            visual_new = f"{visual}{list[i]} + "

            current_cat = lbl_list_cut.pop(0)
            cat_sum_ceil_new = cat_sum_ceil + current_cat
            cat_sum_floor_new = cat_sum_floor + current_cat + 1

            rec_sum_search_helper(rec_depth - 1, list_cut, lbl_list_cut, key, categories, past_sum_new, visual_new, cat_sum_ceil_new, cat_sum_floor_new)



def rec_sum_search(
    list: list[float],         # list of possible addends
    key: float,                # sum of some addends the program solves for
    rec_depth: int|None = None # max number of addends the solution can be made of
                               # default: length of list
):
    list = list_clean(list, key)
    get_cat_data: list = categorise(list, key)
    categories = get_cat_data[0]
    list_lbl = get_cat_data[1]

    if rec_depth is None:
        rec_depth = len(list)

        # recursively search through rec_depth number of addends
        for layer in range(rec_depth + 1):
            rec_sum_search_helper(
                    rec_depth=layer,
                    list=list,
                    label_list=list_lbl, 
                    key=key, 
                    categories=categories,
                    past_sum=0,
                    visual="",
                    cat_sum_ceil=0,
                    cat_sum_floor=0
            )
    else:
        rec_sum_search_helper(
                rec_depth=rec_depth,
                list=list,
                label_list=list_lbl, 
                key=key, 
                categories=categories,
                past_sum=0,
                visual="",
                cat_sum_ceil=0,
                cat_sum_floor=0
        )




# list of addends
#sums: list[float] = [
#        45.87, 67.88, 67.96, 67.02, 128.89, 200.74, 140.25, 69.69, 100.37, 40.7, 500.59, 30.45, 45.89, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#
#rec_sum_search(list=sums, key=421.24, rec_depth=0)
