# --INPUT--
# list of addends
sums: list[float] = [45.87, 67.58, 67.96, 67.02, 128.89, 200.74, 140.25, 69.69, 100.37, 40.7, 500.59, 30.45, 45.89, 45.11, 67.88, 67.99, 67.20, 124.77, 240.74, 600.25, 69.69, 111.37, 4011.7, 510.59, 10.45, 45.29, 5.66, 3.93, 2.1, 75.09, 7.04]
# sum of some addends the program solves for
partial_sum: float = 600.25
REC_DEPTH: int = len(sums)

# remove all bigger than partial_sum
new_sums = sums.copy()
for i in sums:
    if i > partial_sum:
        new_sums.remove(i)
sums = new_sums


def rec_sum_search_helper(
    rec_depth: int,
    list: list[float],
    key: float,
    past_sum: float,
    visual: str
):
    if rec_depth <= 0:
        for i in list:
            test_sum = round(past_sum + i, 2)
            #print(f"{visual}{i} = {test_sum}")
            if test_sum == key:
                print(f"FOUND SOLUTION: {visual}{i} = {test_sum}")
    else:
        list_cut = list.copy()
        for i in list:
            past_sum_new = round(past_sum + list_cut.pop(0), 2)
            visual_new = f"{visual}{i} + "
            rec_sum_search_helper(rec_depth - 1, list_cut, key, past_sum_new, visual_new)


def rec_sum_search(rec_depth: int, list: list[float], key: float):
    rec_sum_search_helper(rec_depth, list, key, 0, "")


for i in range(REC_DEPTH + 1):
    rec_sum_search(i, sums, partial_sum)

