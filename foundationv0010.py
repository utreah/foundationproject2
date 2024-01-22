import tkinter as tk
from tkinter import ttk
import datetime
from tkinter.messagebox import showerror, showwarning, showinfo
# [DONE] Using food's name, match the name with PRODUCT_LIST-> get index of the food and use that index to get food's portion prices.
# [BUG/FIXED] creates multiple child_window(s) when button pressed more than once. Find a way to check whether a child window is open or not.
# [DONE] ADD FOOD NAME TO RADIOBUTTON CHILD WINDOW -> Pleace choose a food portion: {FOOD NAME}
# [BUG/FIXED] When you insert same food it doesnt increase the quantity but makes a new entry and increases the quantity by 1
# [BUG/FIXED] ValueError: 'LAMB KEBAB WRAP' is not in list// check append_to_basket function
# [BUG/FIXED] If customer dont choose a size, it automatically adds LARGE portion name and price but not product size.
# [BUG] Large portions are being added to CUSTOMER_BASKET capitalized. Not important but can be fixed to improve eye appeal.
# [BUG/FIXED] Portion window not opening after closing. You have to restart the whole application in order to make it work.
# [DONE] Now it calculates the price based on quantity.


PRODUCT_LIST = ["Lamb Kebab Wrap", "Lahmacun", "Cag Kebab", "Iskender", "Ezogelin", "Kisir", "Mercimek Kofte", "Sarma"]
PRICE_LIST = [(10.99,  15.99), (3.99, 5.99), (18.99, 25.99), (16.99, 22.99), (7.99, 9.99), (5.49, 6.85), (8.45, 9.99),(7.58, 9.45)]
CUSTOMER_BASKET = []
CUSTOMER_BASKET_PRICE = []
CUSTOMER_BASKET_PRODUCT_SIZE = []
isChildWindowOpen = False
treeview_tuple = []
treeview_seen = set()
def append_to_basket(product_name, product_size ):
    food_index = 0
    # Find Dish's INDEX in PRODUCT_LIST
    for food in PRODUCT_LIST:
        if food in product_name:
            food_index = PRODUCT_LIST.index(food)
    if product_size == 'S':
        CUSTOMER_BASKET.append(product_name)
        CUSTOMER_BASKET_PRICE.append(PRICE_LIST[food_index][0])
    else:
        product_name_capitalized = product_name.upper()
        CUSTOMER_BASKET.append(product_name_capitalized)
        CUSTOMER_BASKET_PRICE.append(PRICE_LIST[food_index][1])
    CUSTOMER_BASKET_PRODUCT_SIZE.append(product_size)
    showinfo(title="Choice", message=f"'{product_name}' has been added to your basket")
    destroy_child_window()

def on_close_child_window(child_window):
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

        get_portion_button = ttk.Button(child_window, text="Choose Portion", command=lambda : append_to_basket(product_name, get_food_portion.get()))
        get_portion_button.pack()
        child_window.protocol('WM_DELETE_WINDOW',lambda: on_close_child_window(child_window))
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
#        if CUSTOMER_BASKET[loop_counter].lower() in PRODUCT_LIST[loop_counter].lower():
#            product_test = loop_counter
#            print(f"Treeview food list test: {product_test}", CUSTOMER_BASKET[loop_counter])
        if product_name_treeview not in treeview_seen:
            get_product_price = find_product_price(product_name_treeview,CUSTOMER_BASKET_PRODUCT_SIZE[loop_counter])
            count = CUSTOMER_BASKET.count(product_name_treeview)
            treeview_tuple.append((CUSTOMER_BASKET[loop_counter], CUSTOMER_BASKET_PRODUCT_SIZE[loop_counter], count, f'{round(get_product_price*count,2)}£'))
            treeview_seen.add(product_name_treeview)
    for add_to_treview in treeview_tuple:
        customer_basket_treeview.insert('', tk.END, values=add_to_treview)
def treeview_create_customer_basket():
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
    customer_basket_treeview.place(x=840, y=40, height=650, width=825)
    treeview_scrollbar = ttk.Scrollbar(button_section_frame, orient=tk.VERTICAL, command=customer_basket_treeview.yview)
    customer_basket_treeview.configure(yscroll= treeview_scrollbar.set)
    treeview_scrollbar.grid(row=0, column=1, sticky='ns')
    treeview_print_to_screen()


def find_product_price(product_name, product_size):
    get_product_index = 0
    for i in range(0,len(PRODUCT_LIST)):
        if product_name.lower() in PRODUCT_LIST[i].lower():
            get_product_index = i

    if product_size == 'S':
        return PRICE_LIST[get_product_index][0]
    return PRICE_LIST[get_product_index][1]


def go_back_to_main_menu():
    back_to_menu_button_image = tk.PhotoImage(file="images/other/back_to_main_menu.png")
    back_to_menu_button_image_to_display = back_to_menu_button_image.subsample(x=4,y=4)
    another_test_button = tk.Button(main_pos_name, text="BACK TO MENU", command=main_menu, image=back_to_menu_button_image_to_display)
    another_test_button.image = back_to_menu_button_image_to_display
    another_test_button.place(x=1715, y=800, width=200, height=200)


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
    food_kebab_image = tk.PhotoImage(file="images/food/food_kebab.png").subsample(x=4,y=4)
    kebab_button = tk.Button(food_frame, image=food_kebab_image, command=lambda: get_portion("Lamb Kebab Wrap"))
    kebab_button.image = food_kebab_image
    kebab_button.place(x=40, y=5, width=200, height=200)

    # Create label for dish feature(s) -> Name, price, V/VE/GF
    kebab_dish_information = tk.Label(food_frame, text="Name: Lamb Kebab Wrap \nPrice(S/L): 10.99£/15.99£")
    kebab_dish_information.place(x=65, y=210)

    # Create a button and add food_lahmacun.png
    food_lahmacun_image = tk.PhotoImage(file="images/food/food_lahmacun.png").subsample(x=4,y=4)
    lahmacun_button = tk.Button(food_frame, image=food_lahmacun_image, command=lambda: get_portion("Lahmacun"))
    lahmacun_button.image = food_lahmacun_image
    lahmacun_button.place(x=315, y=5, width=200, height=200)

    # Create label for dish feature(s) -> Name, price, V/VE/GF
    lahmacun_dish_information = tk.Label(food_frame, text="Name: Lahmacun \nPrice(S/L): 3.99£/5.99£ \nV/VE option available!")
    lahmacun_dish_information.place(x=355, y=210)

    # Create a button and add food_cagkebab.png
    cag_kebab_image = tk.PhotoImage(file="images/food/food_cagkebab.png").subsample(x=4,y=4)
    cag_kebab_button = tk.Button(food_frame,image=cag_kebab_image, command=lambda: get_portion("Cag Kebab"))
    cag_kebab_button.image = cag_kebab_image
    cag_kebab_button.place(x=610, y=5, width=200, height=200)

    # Create label for dish feature(s) -> Name, price, V/VE/GF
    cag_kebab_dish_information = tk.Label(food_frame, text="Name: Cag Kebab \nPrice(S/L): 18.99£/25.99£")
    cag_kebab_dish_information.place(x=640, y=210)

    # Create a button and add food_iskender.png
    food_iskender_image = tk.PhotoImage(file="images/food/food_iskender.png").subsample(x=4,y=4)
    iskender_button = tk.Button(food_frame, image=food_iskender_image, command=lambda: get_portion("Iskender"))
    iskender_button.image = food_iskender_image
    iskender_button.place(x=895, y=5, width=200, height=200)

    # Create label for dish feature(s) -> Name, price, V/VE/GF
    iskender_dish_information = tk.Label(food_frame, text="Name: Iskender \nPrice(S/L): 16.99£/22.99£")
    iskender_dish_information.place(x=935, y=210)

    # Create a button and add food_ezogelin.png
    food_ezogelin_image = tk.PhotoImage(file="images/food/food_ezogelin.png").subsample(x=4,y=4)
    ezogelin_button = tk.Button(food_frame, image=food_ezogelin_image, command=lambda: get_portion("Ezogelin"))
    ezogelin_button.image = food_ezogelin_image
    ezogelin_button.place(x=40, y=300, width=200, height=200)

    # Create label for dish feature(s) -> Name, price, V/VE/GF
    ezogelin_dish_information = tk.Label(food_frame, text="Name: Ezogelin \nPrice(S/L): 7.99£/9.99£ \nV/VE")
    ezogelin_dish_information.place(x=80, y=505)

    # Create a button and add food_kisir.png
    food_kisir_image = tk.PhotoImage(file="images/food/food_kisir.png").subsample(x=4,y=4)
    kisir_button = tk.Button(food_frame, image=food_kisir_image, command=lambda: get_portion("Kisir"))
    kisir_button.image = food_kisir_image
    kisir_button.place(x=315, y=300,width=200, height=200)

    # Create label for dish feature(s) -> Name, price, V/VE/GF
    kisir_dish_information = tk.Label(food_frame, text="Name: Kisir \nPrice(S/L): 5.49£/6.85£ \nV/VE")
    kisir_dish_information.place(x=360, y=505)

    # Create a button and add food_mercimekkofte.png
    food_mercimekkofte_image = tk.PhotoImage(file="images/food/food_mercimekkofte.png").subsample(x=4,y=4)
    mercimekkofte_button = tk.Button(food_frame, image=food_mercimekkofte_image, command=lambda: get_portion("Mercimek Kofte"))
    mercimekkofte_button.image = food_mercimekkofte_image
    mercimekkofte_button.place(x=610, y=300,width=200, height=200)

    # Create label for dish feature(s) -> Name, price, V/VE/GF
    mercimekkofte_dish_information = tk.Label(food_frame, text="Name: Mercimek Kofta \nPrice(S/L): 8.45£/9.99£ \nV/VE")
    mercimekkofte_dish_information.place(x=640, y=505)

    # Create a button and add food_mercimekkofte.png
    food_sarma_image = tk.PhotoImage(file="images/food/food_sarma.png").subsample(x=4,y=4)
    sarma_button = tk.Button(food_frame, image=food_sarma_image, command=lambda: get_portion("Mercimek Kofte"))
    sarma_button.image = food_sarma_image
    sarma_button.place(x=895, y=300, width=200, height=200)

    # Create label for dish feature(s) -> Name, price, V/VE/GF
    sarma_dish_information = tk.Label(food_frame, text="Name: Sarma \nPrice(S/L): 9.45£/13.99£ \nV/VE")
    sarma_dish_information.place(x=935, y=505)




    go_back_to_main_menu()


def print_items_in_drink_menu():
    clear_screen()
    time_on_screen()
    # Create a frame for drink section
    drink_frame = tk.Frame(main_pos_name)
    drink_frame.pack(fill=tk.BOTH, expand=True)

    # Create a button and add image -> Cola
    drink_button_cola_image = tk.PhotoImage(file="images/drinks/drinks_cola.png")
    drink_button_cola_image_to_display = drink_button_cola_image.subsample(x=4, y=4)
    drink_button_cola = tk.Button(drink_frame, image=drink_button_cola_image_to_display)
    drink_button_cola.image = drink_button_cola_image_to_display
    drink_button_cola.place(x=40, y=5,width=200, height=200)
    # Cola information
    drink_cola_information = tk.Label(drink_frame, text="Name: Coca Cola\n Price(S/L): 2.99£/3.99£")
    drink_cola_information.place(x=75,y=210)

    # Create a button and add image -> Soda
    drink_button_soda_image = tk.PhotoImage(file="images/drinks/drinks_soda.png")
    drink_button_soda_image_to_display = drink_button_soda_image.subsample(x=4, y=4)
    drink_button_soda = tk.Button(drink_frame, image=drink_button_soda_image_to_display)
    drink_button_soda.image = drink_button_soda_image_to_display
    drink_button_soda.place(x=330, y=5,width=200, height=200)
    # Soda information
    drink_soda_information = tk.Label(drink_frame, text="Name: Soda\n Price(S/L): 2.55£/3.67£")
    drink_soda_information.place(x=365, y=210)
    # Create a button and add image -> Apple Juice
    drink_button_applejuice_image = tk.PhotoImage(file="images/drinks/drinks_apple_juice.png")
    drink_button_applejuice_image_to_display = drink_button_applejuice_image.subsample(x=4, y=4)
    drink_button_applejuice = tk.Button(drink_frame, image=drink_button_applejuice_image_to_display)
    drink_button_applejuice.image = drink_button_applejuice_image_to_display
    drink_button_applejuice.place(x=620, y=5,width=200, height=200)
    # Apple Juice information
    applejuice_drinks_information = tk.Label(drink_frame, text="Name: Apple Juice\n Price(S/L): 2.99£/3.99£")
    applejuice_drinks_information.place(x=655, y=210)
    # Create a button and add image -> Orange Juice
    drink_button_orangejuice_image = tk.PhotoImage(file="images/drinks/drinks_orange_juice.png")
    drink_button_orangejuice_image_to_display = drink_button_orangejuice_image.subsample(x=4, y=4)
    drink_button_orangejuice = tk.Button(drink_frame, image=drink_button_orangejuice_image_to_display)
    drink_button_orangejuice.image = drink_button_orangejuice_image_to_display
    drink_button_orangejuice.place(x=910, y=5,width=200, height=200)
    # Orange Juice information
    orangejuice_drinks_information = tk.Label(drink_frame, text="Name: Orange Juice\n Price(S/L): 3.87£/7.80£")
    orangejuice_drinks_information.place(x=945, y=210)
    # Create a button and add image -> Tango
    drink_button_tango_image = tk.PhotoImage(file="images/drinks/drinks_tango.png")
    drink_button_tango_image_to_display = drink_button_tango_image.subsample(x=4, y=4)
    drink_button_tango = tk.Button(drink_frame, image=drink_button_tango_image_to_display)
    drink_button_tango.image = drink_button_tango_image_to_display
    drink_button_tango.place(x=40, y=300,width=200, height=200)
    # Tango information
    tango_drinks_information = tk.Label(drink_frame, text="Name: Tango\n Price(S/L): 1.99£/2.99£")
    tango_drinks_information.place(x=75, y=505)
    # Create a button and add image -> Ayran
    drink_button_ayran_image = tk.PhotoImage(file="images/drinks/drinks_ayran.png")
    drink_button_ayran_image_to_display = drink_button_ayran_image.subsample(x=4, y=4)
    drink_button_ayran = tk.Button(drink_frame, image=drink_button_ayran_image_to_display)
    drink_button_ayran.image = drink_button_ayran_image_to_display
    drink_button_ayran.place(x=330, y=300,width=200, height=200)
    # Ayran information
    ayran_drinks_information = tk.Label(drink_frame, text="Name: Ayran\n Price(S/L): 0.99£/1.99£")
    ayran_drinks_information.place(x=365, y=505)
    # Create a button and add image -> Ice Tea
    drink_button_iced_tea_image = tk.PhotoImage(file="images/drinks/drinks_iced_tea.png")
    drink_button_iced_tea_image_to_display = drink_button_iced_tea_image.subsample(x=4, y=4)
    drink_button_iced_tea = tk.Button(drink_frame, image=drink_button_iced_tea_image_to_display)
    drink_button_iced_tea.image = drink_button_iced_tea_image_to_display
    drink_button_iced_tea.place(x=620, y=300,width=200, height=200)
    # Ice Tea information
    iced_tea_drinks_information = tk.Label(drink_frame, text="Name: Ice Tea\n Price(S/L): 3.99£/5.99£")
    iced_tea_drinks_information.place(x=665, y=505)
    # Create a button and add image -> Root Beer
    drink_button_root_beer_image = tk.PhotoImage(file="images/drinks/drinks_root_beer.png")
    drink_button_root_beer_image_to_display = drink_button_root_beer_image.subsample(x=4, y=4)
    drink_button_root_beer = tk.Button(drink_frame, image=drink_button_root_beer_image_to_display)
    drink_button_root_beer.image = drink_button_root_beer_image_to_display
    drink_button_root_beer.place(x=910, y=300,width=200, height=200)
    # Root Beer information
    root_beer_drinks_information = tk.Label(drink_frame, text="Name: Root Beer\n Price(S/L): 3.99£/5.99£")
    root_beer_drinks_information.place(x=955, y=505)


    go_back_to_main_menu()


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
    drink_button = tk.Button(button_section_frame, text="DRINK", bg="BLUE", font=('bold'), fg="WHITE", command=print_items_in_drink_menu)
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
    treeview_create_customer_basket()
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