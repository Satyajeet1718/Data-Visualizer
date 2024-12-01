import matplotlib.pyplot as plt
from tkinter import messagebox, filedialog
import os

def plot_graph(app):
    if app.data is None:
        messagebox.showerror("Error", "No data loaded! Please load a file or enter data manually.")
        return

    # Get user inputs
    x_col = app.x_column.get()
    y_col = app.y_column.get()
    graph_type = app.graph_type.get()

    # Validate inputs
    if not x_col or not y_col:
        messagebox.showerror("Error", "Please select both X and Y-axis columns.")
        return

    if x_col not in app.columns or y_col not in app.columns:
        messagebox.showerror("Error", f"Invalid columns selected: {x_col}, {y_col}")
        return

    # Prepare data
    x_data = app.data[x_col]
    y_data = app.data[y_col]

    # Plot based on graph type
    plt.figure(figsize=(8, 6))
    if graph_type == "Bar Graph":
        plt.bar(x_data, y_data, color="#e63946")
    elif graph_type == "Histogram":
        plt.hist(y_data, bins=10, color="#e63946", edgecolor="black")
    elif graph_type == "Line Graph":
        plt.plot(x_data, y_data, color="#e63946", marker="o")
    elif graph_type == "Scatter Plot":
        plt.scatter(x_data, y_data, color="#e63946")

    # Set labels and title
    plt.xlabel(x_col, fontsize=12)
    plt.ylabel(y_col, fontsize=12)
    plt.title(f"{graph_type} of {x_col} vs {y_col}", fontsize=14)
    plt.grid(visible=True, linestyle="--", alpha=0.7)

    # Show plot
    plt.tight_layout()
    plt.show()

def save_graph():
    try:
        file_path = filedialog.asksaveasfilename(defaultextension=".png",
                                                 filetypes=[("PNG files", "*.png"),
                                                            ("JPEG files", "*.jpg"),
                                                            ("All Files", "*.*")])
        if not file_path:
            return
        plt.savefig(file_path)
        messagebox.showinfo("Success", f"Graph saved successfully at {file_path}")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to save graph: {e}")
