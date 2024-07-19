import sys
sys.path.append(r'C:\Users\sambh\Desktop\workspace\DAQPersonal\hostui')

import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from utils import file_utils


class file_ui:
    def __init__(self, root):
        self.root = root
        self.file_path = None
        self.init_ui()

    def init_ui(self):
        self.root.title("DAQ UI")
        self.root.geometry("500x500")

        self.frame1 = ttk.Frame(self.root)
        self.frame2 = ttk.Frame(self.root)
        self.frame3 = ttk.Frame(self.root)
        self.frame4 = ttk.Frame(self.root)
        self.frame5 = ttk.Frame(self.root)

        self.load_file_btn = ttk.Button(self.frame1, text="Load file", command=self.load_file)
        self.load_file_btn.pack(side="left")

        self.create_labels()
        self.create_textboxes()
        self.create_buttons()

        self.data_displayer = ttk.Text(self.frame5, height=100, width=150)
        self.data_displayer.pack()

        self.pack_frames()

    def create_labels(self):
        t1_label = ttk.Label(self.frame2, text="Function code", font='Calibri 16')
        t1_label.pack(side='left', padx=10)

        t2_label = ttk.Label(self.frame2, text="1st databyte", font='Calibri 16')
        t2_label.pack(side='left', padx=10)

        t3_label = ttk.Label(self.frame2, text="2nd databyte", font='Calibri 16')
        t3_label.pack(side='left', padx=10)

    def create_textboxes(self):
        self.t1_data = ttk.StringVar()
        self.t2_data = ttk.StringVar()
        self.t3_data = ttk.StringVar()

        t1 = ttk.Entry(self.frame3, textvariable=self.t1_data)
        t1.pack(side="left", padx=10)

        t2 = ttk.Entry(self.frame3, textvariable=self.t2_data)
        t2.pack(side="left", padx=10)

        t3 = ttk.Entry(self.frame3, textvariable=self.t3_data)
        t3.pack(side="left", padx=10)

    def create_buttons(self):
        append_button = ttk.Button(self.frame4, text="Append data", command=self.append_data)
        append_button.pack(side="right", padx=10)

        refresh_button = ttk.Button(self.frame4, text="Refresh", command=self.read_file)
        refresh_button.pack(side="right", padx=10)

        send_button = ttk.Button(self.frame4, text="Send")
        send_button.pack(side="right", padx=10)

    def pack_frames(self):
        self.frame1.pack(pady=10)
        self.frame2.pack(pady=30)
        self.frame3.pack(pady=10)
        self.frame4.pack(pady=10)
        self.frame5.pack(pady=30)

    def load_file(self):
        self.file_path = file_utils.choose_file()

    def read_file(self):
        content = file_utils.read_file(self.file_path)
        self.data_displayer.delete('1.0', END)
        self.data_displayer.insert(END, content)

    def append_data(self):
        data = self.t1_data.get() + self.t2_data.get() + self.t3_data.get()
        file_utils.append_file(self.file_path, data)

if __name__ == "__main__":
    root = ttk.Window(themename='darkly')
    file_ui(root)
    root.mainloop()