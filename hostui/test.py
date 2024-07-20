import ttkbootstrap as tk
from tkinter import ttk

class TableApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Table Example")
        self.root.geometry("600x400")

        # Create a style
        style = ttk.Style()
        style.configure("Treeview", 
                        background="white",
                        foreground="black",
                        rowheight=25,
                        fieldbackground="white",
                        bordercolor="black", 
                        borderwidth=2)
        style.configure("Treeview.Heading", 
                        background="gray", 
                        foreground="black", 
                        bordercolor="black", 
                        borderwidth=2)
        style.map("Treeview", 
                  background=[('selected', 'blue')],
                  foreground=[('selected', 'white')])

        # Create a Treeview widget
        self.tree = ttk.Treeview(root, style="Treeview")

        # Define columns
        self.tree["columns"] = ("ID", "Name", "Age", "City")
        
        # Format columns
        self.tree.column("#0", width=0, stretch=tk.NO)  # Hide the first column
        self.tree.column("ID", anchor=tk.CENTER, width=80)
        self.tree.column("Name", anchor=tk.W, width=150)
        self.tree.column("Age", anchor=tk.CENTER, width=100)
        self.tree.column("City", anchor=tk.W, width=150)

        # Create column headings
        self.tree.heading("#0", text="", anchor=tk.W)
        self.tree.heading("ID", text="ID", anchor=tk.CENTER)
        self.tree.heading("Name", text="Name", anchor=tk.W)
        self.tree.heading("Age", text="Age", anchor=tk.CENTER)
        self.tree.heading("City", text="City", anchor=tk.W)

        # Add data
        data = [
            (1, "John Doe", 29, "New York"),
            (2, "Anna Smith", 34, "London"),
            (3, "Peter Brown", 45, "Berlin"),
            (4, "Linda Davis", 23, "Paris"),
        ]
        
        for item in data:
            self.tree.insert("", "end", values=item)

        # Pack the Treeview widget
        self.tree.pack(pady=20, padx=20, fill=tk.BOTH, expand=True)

if __name__ == "__main__":
    root = tk.Window(themename='darkly')
    app = TableApp(root)
    root.mainloop()
