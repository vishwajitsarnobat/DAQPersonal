import ttkbootstrap as ttk
from ..file import file_ui
from ..store import store_ui

root = ttk.Window(themename = 'darkly')
root.title("DAQ UI")
root.geometry("500x500")

# notebook = ttk.Notebook(root)
# notebook.pack(fill='both', expand=True)

# store_ui = store_ui(notebook)
# notebook.add(store_ui.frame, text="UI 1")

# file_ui = file_ui(notebook)
# notebook.add(file_ui.frame, text="UI 2")

notebook = ttk.Notebook(root)
notebook.pack(expand=True, fill='both')

frame1 = ttk.Frame(notebook)
notebook.add(frame1, text='UI 1')
store_ui(frame1)

frame2 = ttk.Frame(notebook)
notebook.add(frame2, text='UI 2')
file_ui(frame2)

root.mainloop()