import ttkbootstrap as ttk
import sys
sys.path.append(r'C:\Users\sambh\Desktop\workspace\DAQPersonal\hostui')
from file import file_ui
from store import store_ui

class main_ui:
    def __init__(self, window):
        self.window = window
        self.window.geometry("1200x800")
        self.window.resizable(0,0)
        self.window.state('zoomed')
        self.window.title('Data Acquisition Module')
        
if __name__ == '__main__':
    window = ttk.Window(themename='darkly')
    main_ui(window)
    window.mainloop()