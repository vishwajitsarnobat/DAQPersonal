import ttkbootstrap as ttk
import serial.tools.list_ports
import serial
import sys
from tkinter import messagebox

sys.path.append(r'C:\Users\sambh\Desktop\workspace\DAQPersonal\hostui')
from utils import database_utils, csv_utils, text_utils
from setup.setup_ui import DAQSetupUI

class DAQStoreUI:
    def __init__(self, root):
        self.root = root
        # self.root.title("DAQ Storage Management")
        # self.root.geometry("1200x800")
        self.init_ui()

    def init_ui(self):
        self.create_frames()
        self.create_setup()
        self.create_widgets()
        self.pack_frames()

    def create_frames(self):
        self.frame1 = ttk.Frame(self.root)
        self.frame2 = ttk.Frame(self.root)
        self.frame3 = ttk.Frame(self.root)
        self.frame4 = ttk.Frame(self.root)
        self.frame5 = ttk.Frame(self.root)

    def create_setup(self):
        DAQSetupUI(self.frame1)

    def create_widgets(self):
        self.create_store_buttons()
        self.create_data_displayer()

    def create_store_buttons(self):
        self.store_btn = ttk.Button(self.frame2, text="Store to DB", state='disabled', command=self.store)
        self.store_btn.pack(side='left', padx=10)
        self.stop_store_btn = ttk.Button(self.frame2, text="Stop", state='disabled', command=self.stop_store)
        self.stop_store_btn.pack(side='left', padx=10)
        self.csv_store_btn = ttk.Button(self.frame3, text="Store to CSV", state='disabled', command=self.csv_store)
        self.csv_store_btn.pack(side='left', padx=10)
        self.csv_stop_btn = ttk.Button(self.frame3, text="Stop", state='disabled', command=self.csv_stop_store)
        self.csv_stop_btn.pack(side='left', padx=10)
        self.text_store_btn = ttk.Button(self.frame4, text="Store to Text file", state='disabled', command=self.text_store)
        self.text_store_btn.pack(side='left', padx=10)
        self.text_stop_btn = ttk.Button(self.frame4, text="Stop", state='disabled', command=self.text_stop_store)
        self.text_stop_btn.pack(side='left', padx=10)

    def create_data_displayer(self):
        self.data_displayer = ttk.Text(self.frame5, height=100, width=150)
        self.data_displayer.pack()

    def pack_frames(self):
        self.frame1.pack(pady=10)
        self.frame2.pack(pady=10)
        self.frame3.pack(pady=10)
        self.frame4.pack(pady=10)
        self.frame5.pack(pady=30)

    def store(self):
        self.stop_store_btn['state'] = 'active'
        self.store_btn['state'] = 'disabled'
        serial_port = self.clicked_com.get()
        baud_rate = self.clicked_bd.get()
        ser = serial.Serial(serial_port, baud_rate)
        messagebox.showinfo("Storing initiated", "Storing pin data into the database ...")
        database_utils.database_connect()
        flag = True
        while flag:
            self.display(database_utils.database_store(self.read_serial(ser)))
            self.root.update()
        database_utils.database_disconnect()

    def stop_store(self):
        global flag
        flag = False
        self.store_btn['state'] = 'active'
        self.stop_store_btn['state'] = 'disabled'

    def csv_store(self):
        self.csv_stop_btn['state'] = 'active'
        self.csv_store_btn['state'] = 'disabled'
        serial_port = self.clicked_com.get()
        baud_rate = self.clicked_bd.get()
        ser = serial.Serial(serial_port, baud_rate)
        messagebox.showinfo("Storing initiated", "Storing pin data into the output.csv ...")
        flag = True
        while flag:
            self.display(csv_utils.store(self.read_serial(ser)))
            self.root.update()

    def csv_stop_store(self):
        global flag
        flag = False
        self.csv_stop_btn['state'] = 'disabled'
        self.csv_store_btn['state'] = 'active'

    def text_store(self):
        self.text_stop_btn['state'] = 'active'
        self.text_store_btn['state'] = 'disabled'
        serial_port = self.clicked_com.get()
        baud_rate = self.clicked_bd.get()
        ser = serial.Serial(serial_port, baud_rate)
        messagebox.showinfo("Storing initiated", "Storing pin data into the output.txt ...")
        flag = True
        while flag:
            self.display(text_utils.store(self.read_serial(ser)))
            self.root.update()

    def text_stop_store(self):
        global flag
        flag = False
        self.text_stop_btn['state'] = 'disabled'
        self.text_store_btn['state'] = 'active'

    def read_serial(ser):
        line = ser.readline()
        decoded_line = line.decode('utf-8')
        return decoded_line
    
    def display(self, data):
        self.data_displayer.insert('end', data)

if __name__ == "__main__":
    root = ttk.Window(themename='superhero')
    DAQStoreUI(root)
    root.mainloop()