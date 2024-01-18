import tkinter as tk
from tkinter import ttk
import datetime
# [DONE] Using food's name, match the name with FOOD_LIST-> get index of the food and use that index to get food's portion prices.
# [WIP] creates multiple child_window(s) when button pressed more than once. Find a way to check whether a child window is open or not.


FOOD_LIST = ["Lamb Kebab Wrap", "Lahmacun", "Cag Kebab", "Iskender", "Ezogelin", "Kisir", "Mercimek Kofte", "Sarma"]
FOOD_PRICE_LIST = [(10.99,  15.99), (3.99, 5.99), (18.99, 25.99), (16.99, 22.99), (7.99, 9.99), (5.49, 6.85), (8.45, 9.99),(7.58, 9.45)]

def test(args1, args2):
    print("Args1:", args1, "\nArgs2: £",args2)
    destroy_child_window()


def destroy_child_window():
    child_window.destroy()
    print("Child windows has been successfully destroyed")

def test_info():
#    child_window.protocol("WM_DELETE_WINDOW", )
    if child_window.winfo_exists():
        print("1")
        return True
    return False

def get_portion(food_name):
    food_index = 0
    # Find Dish's INDEX in FOOD_LIST
    for food in FOOD_LIST:
        if food.lower() in food_name.lower():
            food_index = FOOD_LIST.index(food)
    # Create a top-level window (child windows)
    global child_window
    child_window = tk.Toplevel()
    child_window.title("Portions")

    # Label
    food_portion_label = tk.Label(child_window, text="Please choose a food portion")
    food_portion_label.pack()

    # Define portions and stringVar
    get_food_portion = tk.StringVar()
    food_portions = (
        ("Small", f"{FOOD_PRICE_LIST[food_index][0]}"), ("Large", f"{FOOD_PRICE_LIST[food_index][1]}") # WILL BE CHANGED WITH PORTION PRICE ARRAY
    )
    # Create Radiobutton
    for portion in food_portions:
        food_portion_radio = ttk.Radiobutton(child_window, text=portion[0], value=portion[1], variable=get_food_portion)
        food_portion_radio.pack()


    get_portion_button = ttk.Button(child_window, text="Choose Portion", command=lambda : test(food_name, get_food_portion.get() ))
    get_portion_button.pack()

    child_window.mainloop()


def print_items_in_food_menu():
    # width = 245px,  height=186px for future references

    clear_screen()
    time_on_screen()
    # Create a frame
    food_frame = tk.Frame(main_pos_name)
    food_frame.pack(fill=tk.BOTH, expand=True)

    # Create a button and add food_kebab.png
    food_kebab_image = tk.PhotoImage(file="images/food/food_kebab.png")
    kebab_button = tk.Button(food_frame, image=food_kebab_image, command=lambda: get_portion("Lamb Kebab Wrap"))
    kebab_button.image = food_kebab_image
    kebab_button.place(x=40, y=5)

    # Create label for dish feature(s) -> Name, price, V/VE/GF
    kebab_dish_information = tk.Label(food_frame, text="Name: Lamb Kebab Wrap \nPrice(S/L): 10.99£/15.99£")
    kebab_dish_information.place(x=105, y=200)

    # Create a button and add food_lahmacun.png
    food_lahmacun_image = tk.PhotoImage(file="images/food/food_lahmacun.png")
    lahmacun_button = tk.Button(food_frame, image=food_lahmacun_image, command=lambda: get_portion("Lahmacun"))
    lahmacun_button.image = food_lahmacun_image
    lahmacun_button.place(x=330, y=5)

    # Create label for dish feature(s) -> Name, price, V/VE/GF
    lahmacun_dish_information = tk.Label(food_frame, text="Name: Lahmacun \nPrice(S/L): 3.99£/5.99£ \nV/VE option available!")
    lahmacun_dish_information.place(x=395, y=200)

    # Create a button and add food_cagkebab.png
    cag_kebab_image = tk.PhotoImage(file="images/food/food_cagkebab.png")
    cag_kebab_button = tk.Button(food_frame,image=cag_kebab_image, command=lambda: get_portion("Cag Kebab"))
    cag_kebab_button.image = cag_kebab_image
    cag_kebab_button.place(x=600, y=5, width=250)

    # Create label for dish feature(s) -> Name, price, V/VE/GF
    cag_kebab_dish_information = tk.Label(food_frame, text="Name: Cag Kebab \nPrice(S/L): 18.99£/25.99£")
    cag_kebab_dish_information.place(x=655, y=200)

    # Create a button and add food_iskender.png
    food_iskender_image = tk.PhotoImage(file="images/food/food_iskender.png")
    iskender_button = tk.Button(food_frame, image=food_iskender_image, command=lambda: get_portion("Iskender"))
    iskender_button.image = food_iskender_image
    iskender_button.place(x=870, y=5, width=250)

    # Create label for dish feature(s) -> Name, price, V/VE/GF
    iskender_dish_information = tk.Label(food_frame, text="Name: Iskender \nPrice(S/L): 16.99£/22.99£")
    iskender_dish_information.place(x=925, y=200)

    # Create a button and add food_ezogelin.png
    food_ezogelin_image = tk.PhotoImage(file="images/food/food_ezogelin.png")
    ezogelin_button = tk.Button(food_frame, image=food_ezogelin_image, command=lambda: get_portion("Ezogelin"))
    ezogelin_button.image = food_ezogelin_image
    ezogelin_button.place(x=40, y=300,width=269)

    # Create label for dish feature(s) -> Name, price, V/VE/GF
    ezogelin_dish_information = tk.Label(food_frame, text="Name: Ezogelin \nPrice(S/L): 7.99£/9.99£ \nV/VE")
    ezogelin_dish_information.place(x=110, y=500)

    # Create a button and add food_kisir.png
    food_kisir_image = tk.PhotoImage(file="images/food/food_kisir.png")
    kisir_button = tk.Button(food_frame, image=food_kisir_image, command=lambda: get_portion("Kisir"))
    kisir_button.image = food_kisir_image
    kisir_button.place(x=330, y=300,width=253)

    # Create label for dish feature(s) -> Name, price, V/VE/GF
    kisir_dish_information = tk.Label(food_frame, text="Name: Kisir \nPrice(S/L): 5.49£/6.85£ \nV/VE")
    kisir_dish_information.place(x=390, y=500)

    # Create a button and add food_mercimekkofte.png
    food_mercimekkofte_image = tk.PhotoImage(file="images/food/food_mercimekkofte.png")
    mercimekkofte_button = tk.Button(food_frame, image=food_mercimekkofte_image, command=lambda: get_portion("Mercimek Kofte"))
    mercimekkofte_button.image = food_mercimekkofte_image
    mercimekkofte_button.place(x=600, y=300,width=253)

    # Create label for dish feature(s) -> Name, price, V/VE/GF
    mercimekkofte_dish_information = tk.Label(food_frame, text="Name: Mercimek Kofta \nPrice(S/L): 8.45£/9.99£ \nV/VE")
    mercimekkofte_dish_information.place(x=660, y=500)

    # Create a button and add food_mercimekkofte.png
    food_sarma_image = tk.PhotoImage(file="images/food/food_sarma.png")
    sarma_button = tk.Button(food_frame, image=food_sarma_image, command=lambda: get_portion("Mercimek Kofte"))
    sarma_button.image = food_sarma_image
    sarma_button.place(x=870, y=300,width=253)

    # Create label for dish feature(s) -> Name, price, V/VE/GF
    sarma_dish_information = tk.Label(food_frame, text="Name: Sarma \nPrice(S/L): 9.45£/13.99£ \nV/VE")
    sarma_dish_information.place(x=935, y=500)




    go_back_to_main_menu()

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
main_pos_name.title("Foundation Project Market with GUI version 0.0.0.9")
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