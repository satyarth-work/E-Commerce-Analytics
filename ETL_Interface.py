import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import subprocess
import os
import time

def upload_file():
    global file_path
    file_path = filedialog.askopenfilename(filetypes=[("", "*.csv"), ("", "*.xlsx")])
    if file_path:
        upload_label.config(text=f"File Selected: {os.path.basename(file_path)}", fg="#2ecc71")
    else:
        messagebox.showerror("Error", "No file selected. Please select a valid file.")

def update_progress(progress_bar, percentage_label, value):
    progress_bar['value'] = value
    percentage_label.config(text=f"{value}% Completed", font=("Arial", 12, "bold"))
    root.update_idletasks()
    time.sleep(0.5)

def run_script(script_name):
    try:
        subprocess.run(["python", script_name], check=True)
        return True
    except subprocess.CalledProcessError as e:
        messagebox.showerror("Error", f"Failed to execute {script_name}: {str(e)}")
        return False

def extract_data():
    if 'file_path' in globals() and file_path:
        progress_bar['value'] = 0
        update_progress(progress_bar, percentage_label, 25)
        
        extract_success = run_script("extract.py")
        
        if extract_success:
            update_progress(progress_bar, percentage_label, 100)
            messagebox.showinfo("Success, Data extracted successfully!")
    else:
        messagebox.showerror("Error", "Please upload a file first")

def transform_data():
    progress_bar['value'] = 0
    update_progress(progress_bar, percentage_label, 25)
    
    transform_success = run_script("transform.py")
    
    if transform_success:
        update_progress(progress_bar, percentage_label, 100)
        messagebox.showinfo("Success", "Data transformed successfully!")

def load_data():
    progress_bar['value'] = 0
    update_progress(progress_bar, percentage_label, 25)
    
    load_success = run_script("load_to_sql.py")
    
    if load_success:
        update_progress(progress_bar, percentage_label, 100)
        messagebox.showinfo("Success", "Data loaded successfully into the database!")

# Creating the GUI window
root = tk.Tk()
root.title("ETL Process Interface")
root.state("zoomed")  # Full-screen mode
root.configure(bg="#2c3e50")

# Styling
button_style = {"font": ("Arial", 14, "bold"), "bg": "#27ae60", "fg": "white", "width": 20, "height": 2}
label_style = {"font": ("Arial", 12, "bold"), "bg": "#2c3e50", "fg": "white"}

# Main Frame
main_frame = tk.Frame(root, bg="#2c3e50")
main_frame.pack(expand=True, fill="both")

# Upload File Section
upload_btn = tk.Button(main_frame, text="Upload File", command=upload_file, **button_style)
upload_btn.pack(pady=10)

upload_label = tk.Label(main_frame, text="No file selected", **label_style)
upload_label.pack()

# Progress Bar & Percentage Label
progress_bar = ttk.Progressbar(main_frame, orient="horizontal", length=500, mode="determinate")
progress_bar.pack(pady=10)

percentage_label = tk.Label(main_frame, text="0% Completed", **label_style)
percentage_label.pack()

# ETL Buttons
extract_btn = tk.Button(main_frame, text="Extract Data", command=extract_data, **button_style)
extract_btn.pack(pady=10)

transform_btn = tk.Button(main_frame, text="Transform Data", command=transform_data, **button_style)
transform_btn.pack(pady=10)

load_btn = tk.Button(main_frame, text="Load Data", command=load_data, **button_style)
load_btn.pack(pady=10)

# Run the GUI
root.mainloop()
