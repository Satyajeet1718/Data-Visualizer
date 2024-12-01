import pandas as pd
from tkinter import filedialog, messagebox

def load_data_from_file():
    try:
        file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv"),
                                                          ("Excel files", "*.xlsx"),
                                                          ("All Files", "*.*")])
        if not file_path:
            return None, []

        if file_path.endswith(".csv"):
            data = pd.read_csv(file_path)
        elif file_path.endswith(".xlsx"):
            data = pd.read_excel(file_path)
        else:
            messagebox.showerror("Error", "Unsupported file format!")
            return None, []

        columns = list(data.columns)
        messagebox.showinfo("Success", f"Data loaded successfully from {file_path}")
        return data, columns

    except Exception as e:
        messagebox.showerror("Error", f"Failed to load data: {e}")
        return None, []
