import tkinter as tk
from tkinter import ttk
import datetime

def get_computer_time_date():
    while True:
        print(datetime.datetime.now())



main_pos_name = tk.Tk()
main_pos_name.title("Foundation Project Market with GUI version 0.0.0.1")

# Get screen res and set window size and set geometry size using screen res + window size
get_screen_res_width = main_pos_name.winfo_screenwidth()
get_screen_res_height = main_pos_name.winfo_screenheight()
set_window_size_width = -10
set_window_size_height = 0
main_pos_name.geometry(f"{get_screen_res_width}x{get_screen_res_height-68}+{set_window_size_width}+{set_window_size_height}")


















main_pos_name.mainloop()