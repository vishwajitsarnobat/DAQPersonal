from tkinter import *
import serial.tools.list_ports
import subprocess
import threading

def connect_menu():
    global root, connect_btn, refresh_btn
    root = Tk()
    root.title("Port Setup")
    root.geometry("500x500")
    root.config(bg="white")

    port_label = Label(root, text="Available Port(s): ", bg="white")
    port_label.grid(column=1, row=2, pady=20, padx=10)

    port_bd = Label(root, text="Baud Rate: ", bg="white")
    port_bd.grid(column=1, row=3, pady=20, padx=10)

    refresh_btn = Button(root, text="Refresh", height=2, width=10, command=com_select)
    refresh_btn.grid(column=3 , row=2)

    connect_btn = Button(root, text="Connect", height=2, width=10, state="disabled", command=connection)
    connect_btn.grid(column=3 , row=4)
    
    deafult_btn = Button(root, text="Set to default", height=2, width=10, command=default)
    deafult_btn.grid(column=2, row=5)
    
    # temp
    run_btn = Button(root, text="Run", height=2, width=10, command=run_ui())
    run_btn.grid(column=2, row=6)
    
    baud_select()
    com_select()
    
def baud_select():
    global clicked_bd, drop_bd
    clicked_bd = StringVar()
    bds = [
        "-",
        "300",
        "600",
        "1200",
        "2400",
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
    coms = [com[0] for com in ports] # Extracts only the serial port from the entire name (e.g. only COM3 from the entire name) 
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
    #connect_check(0)

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
    
def connection():
    global serialData, ser
    if connect_btn["text"] == "Disconnect":
        connect_btn["text"] = "Connect"
        drop_bd["state"] = "active"
        drop_com["state"] = "active"
        refresh_btn["state"] = "active"
        serialData = False
        
    else:
        connect_btn["text"] = "Disconnect"
        drop_bd["state"] = "disabled"
        drop_com["state"] = "disabled"
        refresh_btn["state"] = "disabled"
        serialData = True
        t1 = threading.Thread(target=run_ui)
        t1.daemon=True
        t1.start() 
        
def readSerial():
    while serialData:
        port = clicked_com.get()
        baud = clicked_bd.get()
        ser = serial.Serial(port, baud, timeout=0)
        bits = ser.readline()
        data = (bits.decode('UTF-8'))
        print(data)
          
def run_ui(): # Needs to be modified to be able to send clicked_com and clicked_bd as arguments
    try:
        subprocess.run(["python", "ui.py"])
    except:
        print("An error occurred")
    
connect_menu()

root.mainloop()