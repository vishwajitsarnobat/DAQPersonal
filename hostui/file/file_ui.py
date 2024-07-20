import sys
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

# Add the path to the hostui module
sys.path.append(r'C:\Users\sambh\Desktop\workspace\DAQPersonal\hostui')
from utils import file_utils

class DAQFileUI:
    def __init__(self, root):
        self.root = root
        self.file_path = None  # Initialize file_path
        self.init_ui()

    def init_ui(self):
        """Initialize the user interface components."""
        # self.root.title("DAQ File Management")
        # self.root.geometry("1200x800")

        # Create and pack frames
        self.create_frames()
        self.create_labels()
        self.create_textboxes()
        self.create_buttons()
        self.create_text_displayer()
        self.pack_frames()

    def create_frames(self):
        """Create frames for layout."""
        self.frame1 = ttk.Frame(self.root)
        self.frame2 = ttk.Frame(self.root)
        self.frame3 = ttk.Frame(self.root)
        self.frame4 = ttk.Frame(self.root)
        self.frame5 = ttk.Frame(self.root)

    def create_labels(self):
        """Create labels for the UI."""
        t1_label = ttk.Label(self.frame2, text="Function code", font='Calibri 16')
        t1_label.pack(side='left', padx=10)

        t2_label = ttk.Label(self.frame2, text="1st databyte", font='Calibri 16')
        t2_label.pack(side='left', padx=10)

        t3_label = ttk.Label(self.frame2, text="2nd databyte", font='Calibri 16')
        t3_label.pack(side='left', padx=10)

    def create_textboxes(self):
        """Create textboxes for user input."""
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
        """Create buttons for the UI."""
        load_file_btn = ttk.Button(self.frame1, text="Load file", command=self.load_file)
        load_file_btn.pack(side="left")

        append_button = ttk.Button(self.frame4, text="Append data", command=self.append_data)
        append_button.pack(side="right", padx=10)

        refresh_button = ttk.Button(self.frame4, text="Refresh", command=self.read_file)
        refresh_button.pack(side="right", padx=10)

        send_button = ttk.Button(self.frame4, text="Send")
        send_button.pack(side="right", padx=10)

    def create_text_displayer(self):
        """Create a text displayer to show file content."""
        self.data_displayer = ttk.Text(self.frame5, height=100, width=150)
        self.data_displayer.pack()

    def pack_frames(self):
        """Pack the frames."""
        self.frame1.pack(pady=10)
        self.frame2.pack(pady=30)
        self.frame3.pack(pady=10)
        self.frame4.pack(pady=10)
        self.frame5.pack(pady=30)

    def load_file(self):
        """Load a file using the file_utils module."""
        self.file_path = file_utils.choose_file()

    def read_file(self):
        """Read the content of the loaded file and display it."""
        if self.file_path:
            content = file_utils.read_file(self.file_path)
            self.data_displayer.delete('1.0', END)
            self.data_displayer.insert(END, content)
        else:
            ttk.messagebox.showinfo("No file selected", "Please load a file first.")

    def append_data(self):
        """Append user input data to the loaded file."""
        if self.file_path:
            data = self.t1_data.get() + self.t2_data.get() + self.t3_data.get()
            file_utils.append_file(self.file_path, data)
        else:
            ttk.messagebox.showinfo("No file selected", "Please load a file first.")

if __name__ == "__main__":
    root = ttk.Window(themename='darkly')
    DAQFileUI(root)
    root.mainloop()