import csv
from datetime import datetime

def store():
    
    data = [
        [1, 1, 1, 0, 0, 1, 0, 1],
        [1, 0, 0, 1, 0, 1, 1, 0],
        [0, 1, 1, 0, 0, 1, 0, 1],
        [0, 0, 0, 1, 1, 0, 1, 1]
    ]

    csv_file = 'output.csv'

    with open(csv_file, 'w', newline='') as file:
        csv_writer = csv.writer(file)

        for row in data:
            row[0] = datetime.now()
            csv_writer.writerow(row)

        print(f'Data has been written to {csv_file}')
        

def read():
    data_2d = []

    csv_file = 'output.csv'

    with open(csv_file, 'r') as file:
        csv_reader = csv.reader(file)
        
        for row in csv_reader:
            converted_row = [int(cell) for cell in row]  # Use int() for integers or float() for floats
            data_2d.append(converted_row)

        print(data_2d)
