from tkinter import *
import serial.tools.list_ports
import serial
from database import *
import csv

def connect_menu():
    global root, connect_btn, refresh_btn, deafult_btn, read_btn, store_btn, flag, stop_store_btn, canvas
    flag = True
    
    root = Tk()
    root.title("DAQ UI")
    root.geometry("500x500")
    root.config(bg="white")

    port_label = Label(root, text="Available Port(s): ", bg="white")
    port_label.grid(column=1, row=2, pady=20, padx=10)

    port_bd = Label(root, text="Baud Rate: ", bg="white")
    port_bd.grid(column=1, row=3, pady=20, padx=10)

    refresh_btn = Button(root, text="Refresh", height=2, width=10, command=com_select)
    refresh_btn.grid(column=3 , row=2)

    connect_btn = Button(root, text="Connect", height=2, width=10, state='disabled', command=connect)
    connect_btn.grid(column=3 , row=4)
    
    deafult_btn = Button(root, text="Set to default", height=2, width=10, command=default)
    deafult_btn.grid(column=2, row=5)

    store_btn = Button(root, text="Store to DB", height=2, width=12, state='disabled', command=store)
    store_btn.grid(column=1, row=8)

    stop_store_btn = Button(root, text="Stop", height=2, width=12, state='disabled', command=stop_store)
    stop_store_btn.grid(column=3, row=8)

    read_btn = Button(root, text="Read from CSV", height=2, width=12, state='disabled', command=read)
    read_btn.grid(column=1, row=10)

    canvas = Canvas(root, bg="grey")
    canvas.grid(row=12, column=0, columnspan=99, sticky="nsew")  # Spanning all columns

    # Configure rows and columns to resize with the window
    for i in range(12):
        root.grid_rowconfigure(i, weight=1)
    for i in range(99):
        root.grid_columnconfigure(i, weight=1)
    
    baud_select()
    com_select()
    

def resize_canvas(event):
    canvas.config(width=event.width, height=event.height)
    
def baud_select():
    global clicked_bd, drop_bd
    clicked_bd = StringVar()
    bds = [
        "-",
        "300",
        "600",
        "1200",
        "2400",
        "4800",
        "9600",
        "14400",
        "19200",
        "28800",
        "38400",
        "56000",
        "57600",
        "115200",
        "128000",
        "256000"
    ]
    clicked_bd.set(bds[0])
    
    drop_bd = OptionMenu(root, clicked_bd, *bds, command=connect_check) # clicked_bd will be updated with OptionMenu
    drop_bd.config(width=20)
    drop_bd.grid(column=2, row=3, padx=50)
    
def com_select():
    global clicked_com, coms, drop_com
    ports = serial.tools.list_ports.comports()
    coms = [com[0] for com in ports] # extracts only the serial port from the entire name (e.g. only COM3 from the entire name) 
    coms.insert(0, "-")
    try:
        drop_com.destroy()
    except:
        pass
    
    clicked_com = StringVar()
    clicked_com.set(coms[0])
    drop_com = OptionMenu(root, clicked_com, *coms, command=connect_check) # clicked_com gets updated with selection in OptionMenu
    drop_com.config(width=20)
    drop_com.grid(column=2, row=2, padx=50)

def connect_check(args):
    if "-" in clicked_com.get() or "-" in clicked_bd.get():
        connect_btn["state"] = "disabled"
    else:
        connect_btn["state"] = "active"
    
def default():
    clicked_bd.set("9600")
    connect_btn["state"] = "active"
    try:
        clicked_com.set(coms[1])
    except:
        pass
          
def connect():
    if (connect_btn.cget('text') == "Connect"):
        connect_btn.config(text="Disconnect")
        refresh_btn.config(state='disabled')
        deafult_btn.config(state='disabled')
        drop_bd.config(state='disabled')
        drop_com.config(state='disabled')
        read_btn.config(state='active')
        store_btn.config(state='active')

    else:
        connect_btn.config(text="Connect")
        refresh_btn.config(state='active')
        deafult_btn.config(state='active')
        drop_bd.config(state='active')
        drop_com.config(state='active')
        read_btn.config(state='disabled')
        store_btn.config(state='disabled')

def read():
    serial_port = clicked_com.get()
    baud_rate = clicked_bd.get()
    ser = serial.Serial(serial_port, baud_rate)
    dataarr = []
    csv_file = 'input.csv'

    with open(csv_file, 'r') as file:
        csv_reader = csv.reader(file)
        for data in csv_reader:
            dataarr.append(bytes(data))

    ser.write(dataarr)
    ser.close()
    print(dataarr)
    
def store():
    stop_store_btn.config(state='active')
    serial_port = clicked_com.get()
    baud_rate = clicked_bd.get()
    ser = serial.Serial(serial_port, baud_rate)
    print("Storing pin data into the database...")

    database_connect() # connect
    while flag: # store
        database_store(ser)
        root.update()
    database_disconnect() # disconnect

def stop_store():
    global flag
    flag = False
    stop_store_btn.config(state='disabled')

connect_menu() # running the ui

root.mainloop()