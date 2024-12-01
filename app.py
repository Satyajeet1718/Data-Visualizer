import tkinter as tk
from tkinter import ttk, messagebox

class DataVisualizerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Data Visualizer")
        self.root.geometry("800x600")
        self.root.configure(bg="#1c1c1c")  # Dark background

        # Variables
        self.data = None
        self.columns = []
        self.graph_type = tk.StringVar()
        self.x_column = tk.StringVar()
        self.y_column = tk.StringVar()

        # Header
        header = tk.Label(
            root,
            text="Data Visualizer",
            bg="#1c1c1c",
            fg="#e63946",
            font=("Helvetica", 24, "bold")
        )
        header.pack(pady=10)

        # Data Options
        data_frame = tk.Frame(root, bg="#1c1c1c")
        data_frame.pack(pady=20)

        self.manual_entry_button = tk.Button(
            data_frame,
            text="Enter Data Manually",
            command=self.enter_data_manually,
            bg="#e63946",
            fg="white",
            font=("Helvetica", 12),
            relief="flat",
            padx=10,
            pady=5
        )
        self.manual_entry_button.grid(row=0, column=0, padx=10)

        self.load_file_button = tk.Button(
            data_frame,
            text="Load Data from File",
            command=self.load_file,
            bg="#e63946",
            fg="white",
            font=("Helvetica", 12),
            relief="flat",
            padx=10,
            pady=5
        )
        self.load_file_button.grid(row=0, column=1, padx=10)

        # Graph Selection
        graph_frame = tk.Frame(root, bg="#2e2e2e", bd=1, relief="groove")
        graph_frame.pack(pady=20, fill="x", padx=20)

        graph_label = tk.Label(
            graph_frame,
            text="Select Graph Type:",
            bg="#2e2e2e",
            fg="white",
            font=("Helvetica", 12)
        )
        graph_label.grid(row=0, column=0, padx=10, pady=10)

        self.graph_dropdown = ttk.Combobox(
            graph_frame,
            textvariable=self.graph_type,
            values=["Bar Graph", "Histogram", "Line Graph", "Scatter Plot"],
            state="readonly",
            font=("Helvetica", 12)
        )
        self.graph_dropdown.grid(row=0, column=1, padx=10, pady=10)

        # Column Selection
        column_frame = tk.Frame(root, bg="#1c1c1c")
        column_frame.pack(pady=10)

        x_label = tk.Label(
            column_frame,
            text="X-Axis:",
            bg="#1c1c1c",
            fg="white",
            font=("Helvetica", 12)
        )
        x_label.grid(row=0, column=0, padx=5, pady=5)

        self.x_dropdown = ttk.Combobox(
            column_frame,
            textvariable=self.x_column,
            font=("Helvetica", 12),
            state="readonly"
        )
        self.x_dropdown.grid(row=0, column=1, padx=5, pady=5)

        y_label = tk.Label(
            column_frame,
            text="Y-Axis:",
            bg="#1c1c1c",
            fg="white",
            font=("Helvetica", 12)
        )
        y_label.grid(row=1, column=0, padx=5, pady=5)

        self.y_dropdown = ttk.Combobox(
            column_frame,
            textvariable=self.y_column,
            font=("Helvetica", 12),
            state="readonly"
        )
        self.y_dropdown.grid(row=1, column=1, padx=5, pady=5)

        # Buttons
        button_frame = tk.Frame(root, bg="#1c1c1c")
        button_frame.pack(pady=20)

        self.plot_button = tk.Button(
            button_frame,
            text="Plot Graph",
            command=self.plot_graph,
            bg="#e63946",
            fg="white",
            font=("Helvetica", 14),
            relief="flat",
            padx=15,
            pady=10
        )
        self.plot_button.grid(row=0, column=0, padx=10)

        self.save_button = tk.Button(
            button_frame,
            text="Save Graph",
            command=self.save_graph,
            bg="#e63946",
            fg="white",
            font=("Helvetica", 14),
            relief="flat",
            padx=15,
            pady=10
        )
        self.save_button.grid(row=0, column=1, padx=10)

    def enter_data_manually(self):
        """
        Opens a new interface for manual data entry.
        """
        manual_window = tk.Toplevel(self.root)
        manual_window.title("Enter Data Manually")
        manual_window.geometry("500x400")
        manual_window.configure(bg="#2e2e2e")

        tk.Label(manual_window, text="X-Axis Data (Comma-separated):", bg="#2e2e2e", fg="white", font=("Helvetica", 12)).pack(pady=10)
        x_entry = tk.Entry(manual_window, font=("Helvetica", 12), width=50)
        x_entry.pack(pady=10)

        tk.Label(manual_window, text="Y-Axis Data (Comma-separated):", bg="#2e2e2e", fg="white", font=("Helvetica", 12)).pack(pady=10)
        y_entry = tk.Entry(manual_window, font=("Helvetica", 12), width=50)
        y_entry.pack(pady=10)

        tk.Label(manual_window, text="X-Axis Title:", bg="#2e2e2e", fg="white", font=("Helvetica", 12)).pack(pady=10)
        x_title_entry = tk.Entry(manual_window, font=("Helvetica", 12), width=50)
        x_title_entry.pack(pady=10)

        tk.Label(manual_window, text="Y-Axis Title:", bg="#2e2e2e", fg="white", font=("Helvetica", 12)).pack(pady=10)
        y_title_entry = tk.Entry(manual_window, font=("Helvetica", 12), width=50)
        y_title_entry.pack(pady=10)

        def save_manual_data():
            """
            Save the manually entered data and titles.
            """
            try:
                x_data = [float(i.strip()) if i.strip().isdigit() else i.strip() for i in x_entry.get().split(",")]
                y_data = [float(i.strip()) for i in y_entry.get().split(",")]

                if len(x_data) != len(y_data):
                    messagebox.showerror("Error", "X and Y data must have the same number of values.")
                    return

                app.data = {"X": x_data, "Y": y_data}
                app.columns = ["X", "Y"]
                app.x_column.set("X")
                app.y_column.set("Y")
                messagebox.showinfo("Success", "Manual data entered successfully!")
                manual_window.destroy()
            except ValueError:
                messagebox.showerror("Error", "Please enter valid numeric data for Y-axis.")

        save_button = tk.Button(
            manual_window,
            text="Save Data",
            command=save_manual_data,
            bg="#e63946",
            fg="white",
            font=("Helvetica", 14),
            relief="flat",
            padx=15,
            pady=10
        )
        save_button.pack(pady=20)

    def load_file(self):
        from file_handler import load_data_from_file  # Import function
        self.data, self.columns = load_data_from_file()
        if self.data is not None:
            self.x_dropdown['values'] = self.columns
            self.y_dropdown['values'] = self.columns
            self.graph_dropdown.set("Bar Graph")
            messagebox.showinfo("Success", "File loaded successfully!")

    def plot_graph(self):
        from plotter import plot_graph  # Import function
        plot_graph(self)

    def save_graph(self):
        from plotter import save_graph  # Import function
        save_graph()

if __name__ == "__main__":
    root = tk.Tk()
    app = DataVisualizerApp(root)
    root.mainloop()
