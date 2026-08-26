import csv

with open("data.csv", "r") as r:
    data = csv.reader(r)
    output_list: list = []
    for row in data:
        try:
            input_data: float = float(row.pop(0))
            output_list.append(input_data)
        except:
            break

    print(output_list)
