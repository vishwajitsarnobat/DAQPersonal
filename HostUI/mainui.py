import tkinter as tk
import serial.tools.list_ports
import serial
from database import *
from csv_functions import *
import csv
import ttkbootstrap as ttk

def baud_select():
    global clicked_bd, drop_bd
    clicked_bd = ttk.StringVar()
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
    
    drop_bd = ttk.OptionMenu(frame2, clicked_bd, *bds, command=connect_check) # clicked_bd will be updated with OptionMenu
    drop_bd.config(width=20)
    drop_bd.pack(side = 'left', padx = 10)
    
def com_select():
    global clicked_com, coms, drop_com
    ports = serial.tools.list_ports.comports()
    coms = [com[0] for com in ports] # extracts only the serial port from the entire name (e.g. only COM3 from the entire name) 
    coms.insert(0, "-")
    try:
        drop_com.destroy()
    except:
        pass
    
    clicked_com = ttk.StringVar()
    clicked_com.set(coms[0])
    drop_com = ttk.OptionMenu(frame1, clicked_com, *coms, command=connect_check) # clicked_com gets updated with selection in OptionMenu
    drop_com.config(width=20)
    drop_com.pack(side = 'left', padx = 10)

def connect_check(args):
    if "-" in clicked_com.get() or "-" in clicked_bd.get():
        connect_btn["state"] = "disabled"
    else:
        connect_btn["state"] = "active"
    
def default():
    clicked_bd.set("115200")
    connect_btn["state"] = "active"
    try:
        clicked_com.set(coms[1])
    except:
        pass
          
def connect():
    if (connect_btn.cget('text') == "Connect"):
        connect_btn['text'] = "Disconnect"
        refresh_btn['state'] = 'disabled'
        deafult_btn['state'] = 'disabled'
        drop_bd['state'] = 'disabled'
        drop_com['state'] = 'disabled'
        read_btn['state'] = 'active'
        store_btn['state'] = 'active'

    else:
        connect_btn['text'] = "Connect"
        refresh_btn['state'] = 'active'
        deafult_btn['state'] = 'active'
        drop_bd['state'] = 'active'
        drop_com['state'] = 'active'
        read_btn['state'] = 'disabled'
        store_btn['state'] = 'disabled'
    
def store():
    stop_store_btn['state'] = 'disabled'
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
    stop_store_btn['state'] = 'disabled'

flag = True

root = ttk.Window(themename = 'darkly')
root.title("DAQ UI")
root.geometry("500x500")

frame1 = ttk.Frame(root)
frame2 = ttk.Frame(root)
frame3 = ttk.Frame(root)
frame4 = ttk.Frame(root)
frame5 = ttk.Frame(root)

port_label = ttk.Label(frame1, text="Available Port(s): ", font = 'Calibri 16')
port_label.pack(side = 'left', padx = 10)

refresh_btn = ttk.Button(frame3, text="Refresh", command=com_select)
refresh_btn.pack(side = 'left', padx = 10)

port_bd = ttk.Label(frame2, text="Baud Rate: ", font = 'Calibri 16')
port_bd.pack(side = 'left', padx = 10)

connect_btn = ttk.Button(frame3, text="Connect", command=connect)
connect_btn.pack(side = 'left', padx = 10)

deafult_btn = ttk.Button(frame3, text="Set to default", command=default)
deafult_btn.pack(side = 'left', padx = 10)

store_btn = ttk.Button(frame4, text="Store to DB", state='disabled', command=store)
store_btn.pack(side = 'left', padx = 10)

stop_store_btn = ttk.Button(frame4, text="Stop", state='disabled', command=stop_store)
stop_store_btn.pack(side = 'left', padx = 10)

read_btn = ttk.Button(frame5, text="Read from CSV", state='disabled', command=read)
read_btn.pack(side = 'left', padx = 10)

frame1.pack(pady = 10)
frame2.pack(pady = 10)
frame3.pack(pady = 20)
frame4.pack(pady = 10)
frame5.pack(pady = 10)

baud_select()
com_select()

root.mainloop()