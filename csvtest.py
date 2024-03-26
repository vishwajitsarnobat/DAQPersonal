import csv
import os
from datetime import datetime

def store():
    
    data = [
        [1, 1, 1, 0, 0, 1, 0, 1],
        [1, 0, 0, 1, 0, 1, 1, 0],
        [0, 1, 1, 0, 0, 1, 0, 1],
        [0, 0, 0, 1, 1, 0, 1, 1]
    ]

    print(f'Current working directory: {os.getcwd()}')

    csv_file = 'output.csv'

    try:
        
        with open(csv_file, 'w', newline='') as file:
            csv_writer = csv.writer(file)

            for row in data:
                csv_writer.writerow(row)

        print(f'Data has been written to {csv_file}')
    except Exception as e:
        print(f'Error: {e}')
        

def read():
    data_2d = []

    csv_file = 'output.csv'
    # Open the CSV file for reading
    with open(csv_file, 'r') as file:
        # Create a CSV reader object
        csv_reader = csv.reader(file)
        
        # Iterate over each row in the CSV file
        for row in csv_reader:
            # Convert each 8-bit binary string to a list of integers (bits)
            byte_data = [int(bit) for bit in row[0]]
            
            # Append the list of bits to the 2D array
            data_2d.append(byte_data)

    # Print the 2D array (optional)
    for byte in data_2d:
        print(byte)
        
# Execution of functions
read()