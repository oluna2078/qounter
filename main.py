from src import gui

# --INPUT--
# list of addends
sums: list[float] = [45.87, 67.88, 67.96, 67.02, 128.89, 200.74, 140.25, 69.69, 100.37, 40.7, 500.59, 30.45, 45.89]
# sum of some addends the program solves for
partial_sum: float = 421.24
# number of categories used for addend comparison
MAX_RES: int = 10


# calculate total sum
#total_sum: float = 0
#for i in sums:
#    total_sum = total_sum + i
#total_sum = round(total_sum, 2)


#categorised_sums: list[list[float]] = []



# split sums into category sizes that half every step
#rest: list[float] = []
#cat_upper_limit: float = partial_sum
#cat_counter: int = 0
#
#sums_temp: list[float] = sums.copy()
#
#while sums_temp != []:
#    cat_lower_limit = cat_upper_limit / 2
#    categorised_sums.append([])
#    print(f"------- CATEGORY_{cat_counter}: <= {cat_upper_limit} && > {cat_lower_limit}")
#    for j in sums_temp:
#        if j <= cat_upper_limit and j > cat_lower_limit:
#            print(j)
#            categorised_sums[cat_counter].append(j)
#        else:
#            rest.append(j)
#    sums_temp = rest
#    rest = []
#    cat_upper_limit = cat_upper_limit / 2
#    cat_counter = cat_counter + 1
#categorised_sums.pop(0)


# split sums into different equally split category sizes
#rest: list[float] = []
#categorised_sums = []
#CATEGORY_RES: int = 5
#
#for i in range(CATEGORY_RES):
#    cat_limit: float = partial_sum / (CATEGORY_RES - i)
#    categorised_sums.append([])
#    for j in sums:
#        if j <= cat_limit:
#            print(j)
#            categorised_sums[i].append(j)
#        else:
#            rest.append(j)
#    sums = rest
#    print(f"------- CATEGORY_{CATEGORY_RES - i}: <= {cat_limit}")
#    rest = []
#    
#
#
#print(categorised_sums)

