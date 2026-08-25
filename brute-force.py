# --INPUT--
# list of addends
sums: list[float] = [45.87, 67.58, 67.96, 67.02, 128.89, 200.74, 140.25, 69.69, 100.37, 40.7, 500.59, 30.45, 45.89, 45.11, 67.88, 67.99, 67.20, 124.77, 240.74, 600.25, 69.69, 111.37, 4011.7, 510.59, 10.45, 45.29, 5.66, 3.93, 2.1, 75.09, 7.04]
# sum of some addends the program solves for
partial_sum: float = 600.25

# remove all bigger than partial_sum
new_sums = sums.copy()
for i in sums:
    if i > partial_sum:
        new_sums.remove(i)
    elif i == partial_sum:
        print(f"FOUND SOLUTION: {i} = {i}")
sums = new_sums



# 2 addends
sums_1 = sums.copy()
for i in sums:
    sums_1.pop(0)
    for j in sums_1:
        test_sum = round(i + j, 2)
        print(f"{i} + {j}")
        #print(sums_1)
        if test_sum == partial_sum:
            print(f"FOUND SOLUTION: {i} + {j} = {test_sum}")


# 3 addends
sums_1 = sums.copy()
for i in sums:
    sums_1.pop(0)
    sums_2 = sums_1.copy()
    for j in sums_1:
        sums_2.pop(0)
        for h in sums_2:
            test_sum = round(i + j + h, 2)
            print(f"{i} + {j} + {h}")
            #print(sums_1)
            if test_sum == partial_sum:
                print(f"FOUND SOLUTION: {i} + {j} + {h} = {test_sum}")


# 4 addends
sums_1 = sums.copy()
for i in sums:
    sums_1.pop(0)
    sums_2 = sums_1.copy()

    for j in sums_1:
        sums_2.pop(0)
        sums_3 = sums_2.copy()

        for h in sums_2:
            sums_3.pop(0)

            for g in sums_3:
                test_sum = round(i + j + h + g, 2)
                print(f"{i} + {j} + {h} + {g} = {test_sum}")
                #print(sums_1)
                if test_sum == partial_sum:
                    print(f"FOUND SOLUTION: {i} + {j} + {h} + {g} = {test_sum}")


# 5 addends
sums_1 = sums.copy()
for i in sums:
    sums_1.pop(0)
    sums_2 = sums_1.copy()

    for j in sums_1:
        sums_2.pop(0)
        sums_3 = sums_2.copy()

        for h in sums_2:
            sums_3.pop(0)
            sums_4 = sums_3.copy()

            for g in sums_3:
                sums_4.pop(0)

                for f in sums_4:
                    test_sum = round(i + j + h + g + f, 2)
                    print(f"{i} + {j} + {h} + {g} + {f} = {test_sum}")
                    #print(sums_1)
                    if test_sum == partial_sum:
                        print(f"FOUND SOLUTION: {i} + {j} + {h} + {g} + {f} = {test_sum}")


# 6 addends
sums_1 = sums.copy()
for i in sums:
    sums_1.pop(0)
    sums_2 = sums_1.copy()

    for j in sums_1:
        sums_2.pop(0)
        sums_3 = sums_2.copy()

        for h in sums_2:
            sums_3.pop(0)
            sums_4 = sums_3.copy()

            for g in sums_3:
                sums_4.pop(0)
                sums_5 = sums_4.copy()

                for f in sums_4:
                    sums_5.pop(0)

                    for e in sums_5:
                        test_sum = round(i + j + h + g + f + e, 2)
                        print(f"{i} + {j} + {h} + {g} + {f} + {e} = {test_sum}")
                        #print(sums_1)
                        if test_sum == partial_sum:
                            print(f"FOUND SOLUTION: {i} + {j} + {h} + {g} + {f} + {e} = {test_sum}")


