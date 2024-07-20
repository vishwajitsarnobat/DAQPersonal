import ttkbootstrap as ttk
import serial.tools.list_ports
import serial
import sys
from tkinter import messagebox

sys.path.append(r'C:\Users\sambh\Desktop\workspace\DAQPersonal\hostui')
from utils import database_utils, csv_utils, text_utils

class DAQStoreUI:
    def __init__(self, root):
        self.root = root
        # self.root.title("DAQ Storage Management")
        # self.root.geometry("1200x800")
        self.init_ui()

    def init_ui(self):
        self.create_frames()
        self.create_widgets()
        self.pack_frames()
        self.com_select()
        self.baud_select()

    def create_frames(self):
        self.frame1 = ttk.Frame(self.root)
        self.frame2 = ttk.Frame(self.root)
        self.frame3 = ttk.Frame(self.root)
        self.frame4 = ttk.Frame(self.root)
        self.frame5 = ttk.Frame(self.root)
        self.frame6 = ttk.Frame(self.root)
        self.frame7 = ttk.Frame(self.root)

    def create_widgets(self):
        self.create_port_widgets()
        self.create_baud_widgets()
        self.create_control_buttons()
        self.create_store_buttons()
        self.create_data_displayer()

    def create_port_widgets(self):
        self.port_label = ttk.Label(self.frame1, text="Available Port(s): ", font='Calibri 16')
        self.port_label.pack(side='left', padx=10)

    def create_baud_widgets(self):
        self.bd_label = ttk.Label(self.frame2, text="Baud Rate: ", font='Calibri 16')
        self.bd_label.pack(side='left', padx=10)

    def create_control_buttons(self):
        self.connect_btn = ttk.Button(self.frame3, text="Connect", state='disabled', command=self.connect)
        self.connect_btn.pack(side='left', padx=10)
        self.default_btn = ttk.Button(self.frame3, text="Set to default", command=self.default)
        self.default_btn.pack(side='left', padx=10)
        self.refresh_btn = ttk.Button(self.frame3, text="Refresh", command=self.com_select)
        self.refresh_btn.pack(side='left', padx=10)

    def create_store_buttons(self):
        self.store_btn = ttk.Button(self.frame4, text="Store to DB", state='disabled', command=self.store)
        self.store_btn.pack(side='left', padx=10)
        self.stop_store_btn = ttk.Button(self.frame4, text="Stop", state='disabled', command=self.stop_store)
        self.stop_store_btn.pack(side='left', padx=10)
        self.csv_store_btn = ttk.Button(self.frame5, text="Store to CSV", state='disabled', command=self.csv_store)
        self.csv_store_btn.pack(side='left', padx=10)
        self.csv_stop_btn = ttk.Button(self.frame5, text="Stop", state='disabled', command=self.csv_stop_store)
        self.csv_stop_btn.pack(side='left', padx=10)
        self.text_store_btn = ttk.Button(self.frame6, text="Store to Text file", state='disabled', command=self.text_store)
        self.text_store_btn.pack(side='left', padx=10)
        self.text_stop_btn = ttk.Button(self.frame6, text="Stop", state='disabled', command=self.text_stop_store)
        self.text_stop_btn.pack(side='left', padx=10)

    def create_data_displayer(self):
        self.data_displayer = ttk.Text(self.frame7, height=100, width=150)
        self.data_displayer.pack()

    def pack_frames(self):
        self.frame1.pack(pady=10)
        self.frame2.pack(pady=10)
        self.frame3.pack(pady=20)
        self.frame4.pack(pady=10)
        self.frame5.pack(pady=10)
        self.frame6.pack(pady=10)
        self.frame7.pack(pady=30)

    def baud_select(self):
        self.clicked_bd = ttk.StringVar()
        bds = ["-", "300", "600", "1200", "2400", "4800", "9600", "14400", "19200", "28800", "38400", "56000", "57600", "115200", "128000", "256000"]
        self.clicked_bd.set(bds[0])
        self.drop_bd = ttk.OptionMenu(self.frame2, self.clicked_bd, *bds, command=self.connect_check)
        self.drop_bd.config(width=20)
        self.drop_bd.pack(side='left', padx=10)

    def com_select(self):
        self.clicked_com = ttk.StringVar()
        ports = serial.tools.list_ports.comports()
        self.coms = [com[0] for com in ports]
        self.coms.insert(0, "-")
        self.clicked_com.set(self.coms[0])
        try:
            self.drop_com.destroy()
        except AttributeError:
            pass
        self.drop_com = ttk.OptionMenu(self.frame1, self.clicked_com, *self.coms, command=self.connect_check)
        self.drop_com.config(width=20)
        self.drop_com.pack(side='left', padx=10)

    def connect_check(self, args=None):
        if "-" in self.clicked_com.get() or "-" in self.clicked_bd.get():
            self.connect_btn["state"] = "disabled"
        else:
            self.connect_btn["state"] = "active"

    def default(self):
        if len(self.coms) > 1:
            self.clicked_bd.set("115200")
            self.connect_btn["state"] = "active"
            self.clicked_com.set(self.coms[1])
        else:
            messagebox.showerror("Port error", "No device was detected, please make sure device is properly connected")

    def connect(self):
        if self.connect_btn.cget('text') == "Connect":
            self.connect_btn['text'] = "Disconnect"
            self.refresh_btn['state'] = 'disabled'
            self.default_btn['state'] = 'disabled'
            self.drop_bd['state'] = 'disabled'
            self.drop_com['state'] = 'disabled'
            self.store_btn['state'] = 'active'
            self.csv_store_btn['state'] = 'active'
            self.text_store_btn['state'] = 'active'
        else:
            self.connect_btn['text'] = "Connect"
            self.refresh_btn['state'] = 'active'
            self.default_btn['state'] = 'active'
            self.drop_bd['state'] = 'active'
            self.drop_com['state'] = 'active'
            self.csv_store_btn['state'] = 'disabled'
            self.text_store_btn['state'] = 'disabled'
            self.store_btn['state'] = 'disabled'

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
    root = ttk.Window(themename='darkly')
    DAQStoreUI(root)
    root.mainloop()