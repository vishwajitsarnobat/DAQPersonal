import serial

def setup():
    global ser
    ser = serial.Serial('COM3', 9600, timeout=0)
    
def main():
    if ser.readline().decode("utf-8").startswith("/*"):
        read()

def read():
    data = []
    i = 0
    while i < 10:
        data.append(ser.readline().decode("utf-8"))
        i += 1
    print(data)
    
setup()
while True:
    main()
