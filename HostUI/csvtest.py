import csv
import time
import serial

def store():
    serial_port = 'COM3'  # will be taken from setup page
    baud_rate = 9600  # will be taken from setup page

    csv_file = 'output.csv'

    ser = serial.Serial(serial_port, baud_rate)  # Initialize serial communication

    # Open the CSV file in append mode ('a') so that existing data is not overwritten
    with open(csv_file, 'a', newline='') as file:
        writer = csv.writer(file)

        while True:
            # Read a line from the serial port
            line = ser.readline().decode().strip()
            
            # Check if the received line is not empty
            if line:
                # row = [for val in line.split()]
                writer.writerow(row)
                file.flush()  # Flush the buffer to ensure data is written immediately

            time.sleep(0.01)

    ser.close()

def read():
    data_2d = []

    csv_file = 'output.csv'

    with open(csv_file, 'r') as file:
        csv_reader = csv.reader(file)

        for row in csv_reader:
            converted_row = [int(cell) for cell in row]  # Use int() for integers or float() for floats
            data_2d.append(converted_row)

    print(data_2d)

store()