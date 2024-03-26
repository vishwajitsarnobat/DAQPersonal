from tkinter import *
import serial.tools.list_ports
import functools

ports = serial.tools.list_ports.comports()
serialObj = serial.Serial()

root = Tk()
root.config(bg='grey')

def initComPort(index):
    currentPort = str(ports[index])
    comPortVar = str(currentPort.split(' ')[0])
    serialObj.port = comPortVar
    serialObj.baudrate = 9600
    serialObj.open()

testButton1 = Button(root, text="testButton1", font = ('Calibri', 13), height = 1, width = 45)
testButton1.grid(row=0, column=0)
testButton2 = Button(root, text="testButton2", font = ('Calibri', 13), height = 1, width = 45)
testButton2.grid(row=1, column=0)
testButton3 = Button(root, text="testButton3", font = ('Calibri', 13), height = 1, width = 45)
testButton3.grid(row=2, column=0)
testButton4 = Button(root, text="testButton4", font = ('Calibri', 13), height = 1, width = 45)
testButton4.grid(row=3, column=0)
testButton5 = Button(root, text="testButton5", font = ('Calibri', 13), height = 1, width = 45)
testButton5.grid(row=4, column=0)
testButton6 = Button(root, text="testButton6", font = ('Calibri', 13), height = 1, width = 45)
testButton6.grid(row=5, column=0)

for onePort in ports:
    comButton = Button(root, text = onePort, font = ('Calibri', 13), height = 1, width = 45, command = functools.partial(initComPort, index = ports.index(onePort)))
    comButton.grid(row = ports.index(onePort), column = 0)

dataCanvas = Canvas(root, width = 600, height=400, bg='white')
dataCanvas.grid(row = 0, column = 1, rowspan = 100)

vsb = Scrollbar(root, orient='vertical', command=dataCanvas.yview)
vsb.grid(row=0, column=2, rowspan=100, sticky='ns')

dataCanvas.config(yscrollcommand=vsb.set)

dataFrame = Frame(dataCanvas, bg='white')
dataCanvas.create_window((10,0),window=dataFrame,anchor='nw')

def checkSerialPort():
    if serialObj.isopen() and serialObj.in_waiting:
        recentPacket = serialObj.readline()
        recentPackageString = recentPacket.decode('utf').rstrip('\n')
        Label(dataFrame, text = recentPackageString, font=('Calibri','13'), bg='white').pack()

while True:
    root.update()
    checkSerialPort()
    dataCanvas.config(scrollregion=dataCanvas.bbox("all"))