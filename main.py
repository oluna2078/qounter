# --INPUT--
# list of addends
sums: list[float] = [45.87, 67.88, 67.96, 67.02, 128.89, 200.74, 140.25, 69.69, 100.37, 40.7, 500.59, 30.45, 45.89]
# sum of some addends the program solves for
partial_sum: float = 421.24
# number of categories used for addend comparison
CATEGORY_RES: int = 5


# calculate total sum
#total_sum: float = 0
#for i in sums:
#    total_sum = total_sum + i
#total_sum = round(total_sum, 2)


categorised_sums: list[list[float]] = []


# remove all bigger than partial_sum
for i in sums:
    if i > partial_sum:
        sums.remove(i)
    elif i == partial_sum:
        print(i)

# split sums into different category sizes
rest: list[float] = []

for i in range(CATEGORY_RES):
    cat_limit: float = partial_sum / (CATEGORY_RES - i)
    categorised_sums.append([])
    for j in sums:
        if j <= cat_limit:
            print(j)
            categorised_sums[i].append(j)
        else:
            rest.append(j)
    sums = rest
    print(f"------- CAT_LIMIT_{CATEGORY_RES - i}: {cat_limit}")
    rest = []
    


print(categorised_sums)

