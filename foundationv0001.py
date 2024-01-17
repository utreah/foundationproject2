import tkinter as tk
from tkinter import ttk
import datetime

from time import strftime
def print_items_in_food_menu():
    # width = 245px,  height=186px for future references

    clear_screen()
    time_on_screen()
    # Create a frame
    food_frame = tk.Frame(main_pos_name)
    food_frame.pack(fill=tk.BOTH, expand=True)

    # Create a button and add food_kebab.png
    food_kebab_image = tk.PhotoImage(file="images/food/food_kebab.png")
    kebab_button = tk.Button(food_frame, image=food_kebab_image)
    kebab_button.image = food_kebab_image
    kebab_button.place(x=10, y=5)

    # Create label for dish feature(s) -> Name, price, V/VE/GF
    kebab_dish_information = tk.Label(food_frame, text="Name: Lamb Kebab \nPrice(S/L): 10.99£/15.99£")
    kebab_dish_information.place(x=75, y=200)

    # Create a button and add food_lahmacun.png
    food_lahmacun_image = tk.PhotoImage(file="images/food/food_lahmacun.png")
    lahmacun_button = tk.Button(food_frame, image=food_lahmacun_image)
    lahmacun_button.image = food_lahmacun_image
    lahmacun_button.place(x=300, y=5)

    # Create label for dish feature(s) -> Name, price, V/VE/GF
    lahmacun_dish_information = tk.Label(food_frame, text="Name: Lahmacun \nPrice(S/L): 3.99£/5.99£ \nV/VE option available!")
    lahmacun_dish_information.place(x=365, y=200)





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
    clear_screen()
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

def go_back_to_main_menu():
    another_test_button = tk.Button(main_pos_name, text="BACK TO MENU",command=main_menu, bg="RED",fg="WHITE", font=('Arial', 18, 'bold'))
    another_test_button.place(x=10, y=800, width=200, height=200)

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



main_menu()
#test_button = tk.Button(main_pos_name, text="Test Button", command=main_menu).pack()




main_pos_name.mainloop()