import csv
from datetime import datetime
import serial
from setup import *
import sys
import signal

def read():
    data_2d = []

    csv_file = 'output.csv'

    with open(csv_file, 'r') as file:
        csv_reader = csv.reader(file)

        for row in csv_reader:
            converted_row = [int(cell) for cell in row]  # Use int() for integers or float() for floats
            data_2d.append(converted_row)

    print(data_2d)
    
def signal_handler(sig, frame):
    print("Stopping the second program...")
    sys.exit(0)
    
def store():
    ser = serial.Serial(serial_port, baud_rate)

    result_list = []

    with open('output.csv', 'a', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        
        while True:
            current_time = datetime.now()
            formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S.%f")
            result_list.append(formatted_time)
            line = ser.readline()
            for byte in line:
                if byte == ord('0'):
                    result_list.append(0)
                elif byte == ord('1'):
                    result_list.append(1)
            
            print(result_list)
            
            csv_writer.writerow(result_list)
            
            result_list.clear()
            

serial_port = sys.argv[1]
baud_rate = sys.argv[2]
signal.signal(signal.SIGINT, signal_handler)

try:
        while True:
            store()
except KeyboardInterrupt:
    print("\nCtrl+C detected. Stopping the second program...")
    sys.exit(0)