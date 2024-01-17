import tkinter as tk
from tkinter import ttk
import datetime

from time import strftime
def print_items_in_food_menu():
    clear_screen()
    time_on_screen()

    test_food_frame = ttk.Frame(main_pos_name)
    test_food_frame.pack()

    # Use PhotoImage to load the image
    test_button_image = tk.PhotoImage(file="images/kebab.png")

    # Create a button and place the image on it
    test_button = ttk.Button(test_food_frame, image=test_button_image)
    test_button.image = test_button_image
    test_button.pack(side=tk.LEFT,padx=5,pady=5)




def time_on_screen():
    # Create a label frame for time
    time_outside_frame = tk.LabelFrame(main_pos_name)
    time_outside_frame.pack(fill="both")


    # Create a label and call get_computer_time_date to update time and date everysecond
    global time_label_top_left_corner
    time_label_top_left_corner = tk.Label(time_outside_frame, font=('Helvatica', 15, 'bold'))
    time_label_top_left_corner.pack(side=tk.TOP)


    # UPDATE DATE AND TIME LABEL WITH COMPUTER TIME USING DATETIME
    get_computer_time_date()


def get_computer_time_date():

    get_time = datetime.datetime.now()
    time_label_top_left_corner.config(text=f"DATE: {get_time.day}/0{get_time.month}/{get_time.year} TIME: {get_time.hour}:{get_time.minute}:{get_time.second}")
    time_label_top_left_corner.after(1000,get_computer_time_date)

def main_menu():
    time_on_screen()

    # Create a BUTTON SECTION frame
    button_section_frame = tk.Frame(main_pos_name)
    button_section_frame.pack(fill="both", expand=True)

    # FOOD BUTTON
    food_button = tk.Button(button_section_frame, text="FOOD", bg="RED", font=('bold'), fg="WHITE", command=print_items_in_food_menu)
    food_button.place(x=50, y=50, width=200, height=200)

    # DRINK BUTTON
    drink_button = tk.Button(button_section_frame, text="DRINK", bg="BLUE", font=('bold'), fg="WHITE")
    drink_button.place(x=300, y=50, width=200, height=200)

    # COCKTAILS BUTTON
    cocktails_button = tk.Button(button_section_frame, text="COCKTAILS", bg="GREEN", font=('bold'), fg="WHITE")
    cocktails_button.place(x=550, y=50, width=200, height=200)

    # KIDS BUTTON
    kids_menu_button = tk.Button(button_section_frame, text="KIDS MENU", bg="ORANGE", font=('bold'), fg="WHITE")
    kids_menu_button.place(x=50, y=300, width=200, height=200)

    # MOCKTAILS BUTTON
    mocktails_button = tk.Button(button_section_frame, text="MOCKTAILS", bg="GREY", font=('bold'), fg="WHITE")
    mocktails_button.place(x=300, y=300, width=200, height=200)

    # COFFEE BUTTON
    coffee_button = tk.Button(button_section_frame, text="COFFEE", bg="BLACK", font=('bold'), fg="WHITE")
    coffee_button.place(x=550, y=300, width=200, height=200)



def clear_screen():
    for widgets in main_pos_name.winfo_children():
        print("Widgets:",widgets)
        widgets.destroy()

# Set main settings, name and title
main_pos_name = tk.Tk()
main_pos_name.title("Foundation Project Market with GUI version 0.0.0.1")
main_pos_name.resizable(False,False)

# Get screen res and set window size and set geometry size using screen res + window size
get_screen_res_width = main_pos_name.winfo_screenwidth()
get_screen_res_height = main_pos_name.winfo_screenheight()
set_window_size_width = -10
set_window_size_height = 0
main_pos_name.geometry(f"{get_screen_res_width}x{get_screen_res_height-72}+{set_window_size_width}+{set_window_size_height}")




test_button = tk.Button(main_pos_name, text="Test Button", command=main_menu).pack()




main_pos_name.mainloop()