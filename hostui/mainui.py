import ttkbootstrap as ttk
import ui.file_utils as file_ui
import ui.store_ui as store_ui

root = ttk.Window(themename = 'darkly')
root.title("DAQ UI")
root.geometry("500x500")

notebook = ttk.Notebook(root)
notebook.pack(fill='both', expand=True)

store_ui = store_ui(notebook)
notebook.add(store_ui.frame, text="UI 1")

file_ui = file_ui(notebook)
notebook.add(file_ui.frame, text="UI 2")

root.mainloop()