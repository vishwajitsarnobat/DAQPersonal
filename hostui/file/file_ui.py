import sys
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import messagebox
import serial

# Add the path to the hostui module
sys.path.append(r'C:\Users\sambh\Desktop\workspace\DAQPersonal\hostui')
from utils import file_utils

class DAQFileUI:
    def __init__(self, root):
        self.root = root
        self.file_path = None  # Initialize file_path
        self.init_ui()

    def init_ui(self):
        # self.root.title("DAQ File Management")
        # self.root.geometry("1200x800")

        self.create_frames()
        self.create_labels()
        self.create_textboxes()
        self.create_buttons()
        self.create_text_displayer()
        self.pack_frames()

    def create_frames(self):
        self.frame1 = ttk.Frame(self.root)
        self.frame2 = ttk.Frame(self.root)
        self.frame3 = ttk.Frame(self.root)
        self.frame4 = ttk.Frame(self.root)
        self.frame5 = ttk.Frame(self.root)
        self.frame6 = ttk.Frame(self.root)

    def create_labels(self):
        t1_label = ttk.Label(self.frame2, text="Function code", font='Calibri 16')
        t1_label.pack(side='left', padx=20)

        t2_label = ttk.Label(self.frame2, text="First Byte", font='Calibri 16')
        t2_label.pack(side='left', padx=20)

        t3_label = ttk.Label(self.frame2, text="Second Byte", font='Calibri 16')
        t3_label.pack(side='left', padx=20)

    def create_textboxes(self):
        self.t1_data = ttk.StringVar()
        self.t2_data = ttk.StringVar()
        self.t3_data = ttk.StringVar()

        t1 = ttk.Entry(self.frame3, textvariable=self.t1_data)
        t1.pack(side="left", padx=5)

        t2 = ttk.Entry(self.frame3, textvariable=self.t2_data)
        t2.pack(side="left", padx=5)

        t3 = ttk.Entry(self.frame3, textvariable=self.t3_data)
        t3.pack(side="left", padx=5)

    def create_buttons(self):
        load_file_btn = ttk.Button(self.frame1, text="Load file into displayer", command=self.load_file)
        load_file_btn.pack(side="left", padx=10)

        create_file_btn = ttk.Button(self.frame1, text="Create file for displayer data", command=self.create_file)
        create_file_btn.pack(side="right", padx=10)

        append_button = ttk.Button(self.frame4, text="Append data to file", command=self.append_data)
        append_button.pack(side="right", padx=10)

        sync_fd__button = ttk.Button(self.frame4, text="Sync displayer with file", command=self.sync_fd)
        sync_fd__button.pack(side="right", padx=10)

        sync_df__button = ttk.Button(self.frame4, text="Sync file with displayer", command=self.sync_df)
        sync_df__button.pack(side="right", padx=10)

        # send_button = ttk.Button(self.frame6, text="Send and store feedback to database", command=self.send_and_store_data)
        # send_button.pack(side="right", padx=10)

    def create_text_displayer(self):
        self.data_displayer = ttk.Text(self.frame5, height=35, width=150)
        self.data_displayer.pack()

    def pack_frames(self):
        self.frame1.pack(pady=10)
        self.frame2.pack(pady=5)
        self.frame3.pack(pady=20)
        self.frame4.pack(pady=10)
        self.frame5.pack(pady=30)
        self.frame6.pack(pady=10)

    def load_file(self):
        self.file_path = file_utils.choose_file()

    def create_file(self):
        data = self.data_displayer.get("1.0", END)
        if data.strip():
            file_path = file_utils.create_new_file()
            if file_path:
                file_utils.write_file(file_path, data)
        else:
            messagebox.showwarning("No content error", "Cannot make an empty file, put some data on displayer first")

    def sync_fd(self): # put content of file in displayer
        if self.file_path:
            content = file_utils.read_file(self.file_path)
            self.data_displayer.delete('1.0', END)
            self.data_displayer.insert(END, content)
        else:
            messagebox.showerror("No file error", "Please select a file first")

    def sync_df(self): # put content of displayer in file
        data = self.data_displayer.get("1.0", END)
        if data.strip():
            file_utils.write_file(self.file_path, data)
        else:
            messagebox.showwarning("No content error", "Cannot make an empty file, put some data on displayer first")

    def append_data(self):
        if self.file_path:
            data = self.t1_data.get() + self.t2_data.get() + self.t3_data.get()
            file_utils.append_file(self.file_path, data)
        else:
            messagebox.showerror("No file error", "Please select a file first")

    # def send_and_store_data():
        

if __name__ == "__main__":
    root = ttk.Window(themename='superhero')
    DAQFileUI(root)
    root.mainloop()