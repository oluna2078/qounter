sums: list[float] = [45.87, 67.88, 67.96, 67.02, 128.89, 200.74, 140.25, 69.69, 100.37, 40.7, 500.59, 30.45, 45.89]

partial_sum: float = 421.24
total_sum: float = 1506.3


CATEGORY_RES: int = 10
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
            print(f"++ {j}")
            categorised_sums[i].append(j)
        else:
            rest.append(j)
    sums = rest
    print(f"--------------------- CAT_LIMIT_{i+1}: {cat_limit}")
    #print(rest)
    rest = []
    




print(sums)
print(categorised_sums)

