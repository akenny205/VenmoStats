import tkinter as tk
from tkinter import ttk


# Example methods that might return large outputs
def method1():
    return [i for i in range(150)]  # Return a list with 150 elements


def method2():
    return 42  # Return a simple number


def method3():
    return "Hello, World!"  # Return a string


# Function to call the selected method and display the result
def call_method():
    selected_method = method_var.get()
    if selected_method == "Method 1":
        result = method1()
    elif selected_method == "Method 2":
        result = method2()
    elif selected_method == "Method 3":
        result = method3()

    # Temporarily enable the textbox to modify it
    result_textbox.config(state="normal")

    # Clear the text box first
    result_textbox.delete(1.0, tk.END)

    # Insert the result into the text box
    if isinstance(result, list):
        # For lists, join the items into a formatted string
        result_textbox.insert(tk.END, "\n".join(map(str, result)))
    else:
        result_textbox.insert(tk.END, str(result))

    # Disable the textbox to make it uneditable
    result_textbox.config(state="disabled")


# Create the main window
root = tk.Tk()
root.title("Method Selector")

# Make the window resizable
root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=1)
root.grid_rowconfigure(2, weight=1)
root.grid_rowconfigure(3, weight=10)  # Give more weight to the result area

# Dropdown menu to select the method
method_var = tk.StringVar(value="Method 1")
method_dropdown = ttk.Combobox(root, textvariable=method_var)
method_dropdown['values'] = ("Method 1", "Method 2", "Method 3")
method_dropdown.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

# Button to call the selected method
call_button = tk.Button(root, text="Call Method", command=call_method)
call_button.grid(row=1, column=0, padx=10, pady=10, sticky="ew")

# Label for the result
result_label = tk.Label(root, text="Result:")
result_label.grid(row=2, column=0, padx=10, pady=5, sticky="w")

# Text box to display the result with a vertical scrollbar
result_textbox = tk.Text(root, wrap="word", height=10)
result_textbox.grid(row=3, column=0, padx=10, pady=5, sticky="nsew")

# Add a vertical scrollbar
scrollbar = tk.Scrollbar(root, command=result_textbox.yview)
result_textbox.config(yscrollcommand=scrollbar.set)
scrollbar.grid(row=3, column=1, sticky="ns")

# Make the textbox uneditable from the start
result_textbox.config(state="disabled")

# Make all columns and rows expandable
root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(3, weight=1)

# Run the application
root.mainloop()
