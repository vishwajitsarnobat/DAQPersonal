import ttkbootstrap as ttk
import ui.file_utils as file_utils

# some required functions for this specific program
def load_file():
    global file_path
    file_path = file_utils.choose_file()

def read_file():        
    content = file_utils.read_file(file_path)
    data_displayer.delete('1.0', ttk.END)
    data_displayer.insert(ttk.END, content)


file_root = ttk.Window(themename = 'darkly')
file_root.title("DAQ UI")
file_root.geometry("500x500")

# frames
frame1 = ttk.Frame(file_root)
frame2 = ttk.Frame(file_root)
frame3 = ttk.Frame(file_root)
frame4 = ttk.Frame(file_root)
frame5 = ttk.Frame(file_root)

load_file_btn = ttk.Button(frame1, text="Load file", command=load_file)
load_file_btn.pack(side="left")

# textbox labels
t1_label = ttk.Label(frame2, text="Function code", font = 'Calibri 16')
t1_label.pack(side = 'left', padx = 10)

t1_label = ttk.Label(frame2, text="1st databyte", font = 'Calibri 16')
t1_label.pack(side = 'left', padx = 10)

t1_label = ttk.Label(frame2, text="2nd databyte", font = 'Calibri 16')
t1_label.pack(side = 'left', padx = 10)

# textboxes data
t1_data = ttk.StringVar()
# t1_data.set("function code")
t2_data = ttk.StringVar()
# t2_data.set("databyte 1")
t3_data = ttk.StringVar()
# t3_data.set("databyte 2")

# textboxes
t1 = ttk.Entry(frame3, textvariable=t1_data)
t1.pack(side="left", padx=10)

t2 = ttk.Entry(frame3, textvariable=t2_data)
t2.pack(side="left", padx=10)

t3 = ttk.Entry(frame3, textvariable=t3_data)
t3.pack(side="left", padx=10)

# put data enter in textbox into the file and display on displayer
append_button = ttk.Button(frame4, text="Append data", command= lambda: file_utils.append_file(file_path, (t1_data.get() + t2_data.get() + t3_data.get())))
append_button.pack(side="right", padx=10)

refresh_button = ttk.Button(frame4, text="Refresh", command=read_file)
refresh_button.pack(side="right", padx=10)

# data displayer
data_displayer = ttk.Text(frame5, height=100, width=150)
data_displayer.pack()

send_button = ttk.Button(frame4, text="Send") # , command=send
frame1.pack(pady = 10)
frame2.pack(pady = 30)
frame3.pack(pady = 10)
frame4.pack(pady = 10)
frame5.pack(pady = 30)

file_root.mainloop()