from datetime import datetime
import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Clock App")

# Create a label for displaying the time
def update_time():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    time_label.config(text=current_time)
    time_label.after(1000, update_time)

time_label = tk.Label(root, font=("Helvetica", 80), bg="#333333", fg="#FFFFFF")
time_label.pack(pady=50)
update_time()
root.mainloop()
