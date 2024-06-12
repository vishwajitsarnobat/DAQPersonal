import csv
from datetime import datetime
import serial
import sys

def read():
    serial_port = sys.argv[1]
    baud_rate = sys.argv[2]
    ser = serial.Serial(serial_port, baud_rate)
    
    dataarr = []
    csv_file = 'input.csv'

    with open(csv_file, 'r') as file:
        csv_reader = csv.reader(file)
        for data in csv_reader:
            dataarr.append(bytes(data))

    ser.write(dataarr)
    ser.close()
    
def store():
    serial_port = sys.argv[1]
    baud_rate = sys.argv[2]
    ser = serial.Serial(serial_port, baud_rate)

    csv_file = 'output.csv'
    result_list = []

    with open(csv_file, 'a', newline='') as file:
        csv_writer = csv.writer(file)
        
        while True:
            current_time = datetime.now()
            formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S.%f")
            result_list.append(formatted_time)
            line = ser.readline()
            for byte in line:
                if byte == ord('0'): # this checks if byte(which is converted to ASCII automatically) matches with 0s ASCII.
                    result_list.append(0) # byte will print ASCII value of 0, hence this is needed.
                elif byte == ord('1'):
                    result_list.append(1)
            
            print(result_list)
            csv_writer.writerow(result_list)