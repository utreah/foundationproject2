import tkinter as tk
from tkinter import ttk
import datetime
from time import strftime

def get_computer_time_date():
    get_time = datetime.datetime.now()
    time_label_top_left_corner.config(text=f"DATE: {get_time.day}/0{get_time.month}/{get_time.year} TIME: {get_time.hour}:{get_time.minute}:{get_time.second}")
    time_label_top_left_corner.after(1000,get_computer_time_date)


# Set name and title
main_pos_name = tk.Tk()
main_pos_name.title("Foundation Project Market with GUI version 0.0.0.1")


# Get screen res and set window size and set geometry size using screen res + window size
get_screen_res_width = main_pos_name.winfo_screenwidth()
get_screen_res_height = main_pos_name.winfo_screenheight()
set_window_size_width = -10
set_window_size_height = 0
main_pos_name.geometry(f"{get_screen_res_width}x{get_screen_res_height-68}+{set_window_size_width}+{set_window_size_height}")

# Create a label frame for time
time_outside_frame = tk.LabelFrame(main_pos_name)
time_outside_frame.pack(fill="both")


# Create a label and call get_computer_time_date to update time and date everysecond
time_label_top_left_corner = tk.Label(time_outside_frame,font=('Helvatica', 15, 'bold'))
time_label_top_left_corner.pack()


# UPDATE DATE AND TIME LABEL WITH COMPUTER TIME USING DATETIME
get_computer_time_date()













main_pos_name.mainloop()