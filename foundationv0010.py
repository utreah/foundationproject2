import tkinter as tk
from tkinter import ttk
import datetime
from tkinter.messagebox import showerror, showwarning, showinfo
# [DONE] Using food's name, match the name with FOOD_LIST-> get index of the food and use that index to get food's portion prices.
# [BUG/FIXED] creates multiple child_window(s) when button pressed more than once. Find a way to check whether a child window is open or not.
# [DONE] ADD FOOD NAME TO RADIOBUTTON CHILD WINDOW -> Pleace choose a food portion: {FOOD NAME}
# [BUG/FIXED] When you insert same food it doesnt increase the quantity but makes a new entry and increases the quantity by 1
# [BUG/FIXED] ValueError: 'LAMB KEBAB WRAP' is not in list// check append_to_basket function
# [BUG/FIXED] If customer dont choose a size, it automatically adds LARGE portion name and price but not product size.
# [BUG] Large portions are being added to CUSTOMER_BASKET capitalized. Not important but can be fixed to improve eye appeal.
# [BUG/FIXED] Portion window not opening after closing. You have to restart the whole application in order to make it work.
# [DONE] Now it calculates the price based on quantity.


FOOD_LIST = ["Lamb Kebab Wrap", "Lahmacun", "Cag Kebab", "Iskender", "Ezogelin", "Kisir", "Mercimek Kofte", "Sarma"]
PRICE_LIST = [(10.99,  15.99), (3.99, 5.99), (18.99, 25.99), (16.99, 22.99), (7.99, 9.99), (5.49, 6.85), (8.45, 9.99),(7.58, 9.45)]
CUSTOMER_BASKET = []
CUSTOMER_BASKET_PRICE = []
CUSTOMER_BASKET_PRODUCT_SIZE = []
isChildWindowOpen = False
treeview_tuple = []
treeview_seen = set()
def append_to_basket(product_name, product_size ):
    food_index = 0
    # Find Dish's INDEX in FOOD_LIST
    for food in FOOD_LIST:
        if food in product_name:
            food_index = FOOD_LIST.index(food)
    if product_size == 'S':
        CUSTOMER_BASKET.append(product_name)
        CUSTOMER_BASKET_PRICE.append(PRICE_LIST[food_index][0])
    else:
        product_name_capitalized = product_name.upper()
        CUSTOMER_BASKET.append(product_name_capitalized)
        CUSTOMER_BASKET_PRICE.append(PRICE_LIST[food_index][1])
    CUSTOMER_BASKET_PRODUCT_SIZE.append(product_size)
    showinfo(title="Choice", message=f"'{product_name}' has been added to your basket")
    print(f"{CUSTOMER_BASKET}, {CUSTOMER_BASKET_PRICE}, {CUSTOMER_BASKET_PRODUCT_SIZE}")
    destroy_child_window()

def child_window_on_close(child_window):
    global isChildWindowOpen
    isChildWindowOpen = False
    child_window.destroy()


def get_portion(product_name):
    global isChildWindowOpen

    # Create a top-level window (child windows)
    if not isChildWindowOpen:
        global child_window
        child_window = tk.Toplevel()
        child_window.title("Portions")
        isChildWindowOpen = True
        child_window.resizable(False, False)
        # Label
        food_portion_label = tk.Label(child_window, text=f"Please choose a food portion \n{product_name}")
        food_portion_label.pack()

        # Define portions and stringVar
        get_food_portion = tk.StringVar(None, "S")
        food_portions = (
            ("Small", "S"), ("Large", "L")
        )
        # Create Radiobutton
        for portion in food_portions:
            food_portion_radio = ttk.Radiobutton(child_window, text=portion[0], value=portion[1], variable=get_food_portion)
            food_portion_radio.pack()

        get_portion_button = ttk.Button(child_window, text="Choose Portion", command=lambda : append_to_basket(product_name, get_food_portion.get() ))
        get_portion_button.pack()
        child_window.protocol('WM_DELETE_WINDOW',lambda: child_window_on_close(child_window))
        child_window.mainloop()


def clear_treeview_all():
    # Clear treeview_tuple and treeview_seen to reset treeview. So we won't append the same product multiple times to screen.
    treeview_tuple.clear()
    treeview_seen.clear()
    # Clear childrens of treeview.
    for item in customer_basket_treeview.get_children():
        customer_basket_treeview.delete(item)

def treeview_print_to_screen():
    print(f"Treeview : {CUSTOMER_BASKET}, {CUSTOMER_BASKET_PRICE}, {CUSTOMER_BASKET_PRODUCT_SIZE}")
    clear_treeview_all()
    # Create a tuple, count how many, add if a product in list multiple amount to seen list and append product information
    for product_name_treeview, loop_counter in zip(CUSTOMER_BASKET, range(0, len(CUSTOMER_BASKET))):
#        if CUSTOMER_BASKET[loop_counter].lower() in FOOD_LIST[loop_counter].lower():
#            product_test = loop_counter
#            print(f"Treeview food list test: {product_test}", CUSTOMER_BASKET[loop_counter])
        if product_name_treeview not in treeview_seen:
            get_product_price = find_product_price(product_name_treeview,CUSTOMER_BASKET_PRODUCT_SIZE[loop_counter])
            count = CUSTOMER_BASKET.count(product_name_treeview)
            treeview_tuple.append((CUSTOMER_BASKET[loop_counter], CUSTOMER_BASKET_PRODUCT_SIZE[loop_counter], count, f'{get_product_price*count}£'))
            treeview_seen.add(product_name_treeview)
    for test in treeview_tuple:
        customer_basket_treeview.insert('', tk.END, values=test)
def customer_basket_treeview_insert():
    # Define treeview identifiers
    treeview_customer_basket_identifier_columns = ('product_name', 'product_size', 'product_quantity', 'product_price')
    # Create a treeview
    global customer_basket_treeview
    customer_basket_treeview = ttk.Treeview(button_section_frame, columns=treeview_customer_basket_identifier_columns, show='headings')
    # Create headings and place treeview onto frame 'button_section_frame'
    customer_basket_treeview.heading('product_name', text='Product Name')
    customer_basket_treeview.heading('product_size', text='Product Size')
    customer_basket_treeview.heading('product_quantity', text='Product Quantity')
    customer_basket_treeview.heading('product_price', text='Product Price')
    customer_basket_treeview.place(x=840, y=40, height=800)
    treeview_print_to_screen()


def find_product_price(product_name, product_size):
    get_product_index = 0
    for i in range(0,len(FOOD_LIST)):
        if product_name.lower() in FOOD_LIST[i].lower():
            get_product_index = i

    if product_size == 'S':
        return PRICE_LIST[get_product_index][0]
    return PRICE_LIST[get_product_index][1]


def main_menu():
    clear_screen()
    time_on_screen()
    # Create a BUTTON SECTION frame
    global button_section_frame
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
#  update_button = tk.Button(button_section_frame, text="UPDATE", command=treeview_print_to_screen).pack()
    customer_basket_treeview_insert()


def go_back_to_main_menu():
    another_test_button = tk.Button(main_pos_name, text="BACK TO MENU", command=main_menu, bg="RED", fg="WHITE", font=('Arial', 18, 'bold'))
    another_test_button.place(x=10, y=800, width=200, height=200)


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


def clear_screen():
    for widgets in main_pos_name.winfo_children():
        print("Widgets:", widgets)
        widgets.destroy()


def destroy_child_window():
    child_window.destroy()
    global isChildWindowOpen
    isChildWindowOpen = False
    print("Child windows has been successfully destroyed")

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

# Set main settings, name and title
main_pos_name = tk.Tk()
main_pos_name.title("Foundation Project Market with GUI version 0.0.1.0")
main_pos_name.resizable(False,False)

# Get screen res and set window size and set geometry size using screen res + window size
get_screen_res_width = main_pos_name.winfo_screenwidth()
get_screen_res_height = main_pos_name.winfo_screenheight()
set_window_size_width = -10
set_window_size_height = 0
main_pos_name.geometry(f"{get_screen_res_width}x{get_screen_res_height-72}+{set_window_size_width}+{set_window_size_height}")


main_menu()
#test_button = tk.Button(main_pos_name, text="Test Button", command=customer_basket_treeview)
#test_button.place(x=600,y=800)



main_pos_name.mainloop()