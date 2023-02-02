import csv

path = 'C:\\Users\\Pc\\Downloads\\Compressed\\data\\data\\data.csv'

def create_csv_file():
    with open(path, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['id', 'label'])
        for i in range(1, 2899):
            writer.writerow([i, ''])


create_csv_file()
