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
        
        # Iterate through each row in the CSV file
        for row in csv_reader:
            # Convert each 8-bit binary string to a list of bits
            bits = [int(bit) for byte in row for bit in byte]
            
            # Append the list of bits to the 2D array
            data_2d.append(bits)

        # Print the 2D array (optional)
        for bits in data_2d:
            print(bits)
        
# Execution of functions
read()