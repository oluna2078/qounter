import csv

def csv_to_lst(filepath: str):
    with open(filepath, "r") as r:
        data = csv.reader(r)
        output_list: list = []
        for row in data:
            try:
                input_data: float = float(row.pop(0))
                output_list.append(input_data)
            except:
                break

        print(f"Converted list: [{output_list[0]}, ... , {output_list[len(output_list)-1]}]")
        return output_list
