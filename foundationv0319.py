import tkinter as tk
from tkinter import ttk
import datetime
from tkinter.messagebox import showerror, showwarning, showinfo
# GITHUB : https://github.com/utreah/foundationproject2

# [BUG/FIXED] Make "Remove from basket" button disappear after an item is unselected on treeview.
# [BUG/FIXED] creates multiple child_window(s) when button pressed more than once. Find a way to check whether a child window is open or not.
# [BUG/FIXED] When you insert same food it doesnt increase the quantity but makes a new entry and increases the quantity by 1
# [BUG/FIXED] ValueError: 'LAMB KEBAB WRAP' is not in list// check append_product function
# [BUG/FIXED] If customer dont choose a size, it automatically adds LARGE portion name and price but not product size.
# [BUG/FIXED] Portion window not opening after closing. You have to restart the whole application in order to make it work.
# [BUG/FIXED] Now adjust quantity can increase or decrease quantity of the product.
# [TEMP FIXED] App only works on wide screen. Find a way to fit it into smaller screens <- temporaraly fixed, now it ask user to set their resolution 1920x1080 or higher
# [BUG] Large portions are being added to CUSTOMER_BASKET capitalized. Not important but can be fixed to improve eye appeal.
# [BUG/SEMI-FIXED] When portion/price changes through a button, button still remains on the screen. Problem fixed by calling main_menu() function but is not appealing to eye as it is flicks for a second to create the main menu.
# [DONE] ADD FOOD NAME TO RADIOBUTTON CHILD WINDOW -> Please choose a food portion: {FOOD NAME}
# [DONE] Using food's name, match the name with PRODUCT_LIST-> get index of the food and use that index to get food's portion prices.
# [DONE] Now it calculates the price based on quantity.
# [DONE] Remove 'Name:' from product information
# [DONE] Make a button to remove item from treeview and CUSTOMER_BASKET
# [DONE] Add adjust price button when an item on treeview is chosen.
# [DONE] Add adjust quantity(increment) on click treeview item. -> Get amount of quantity from user and use chosen item's name and size to find the product. Multiply that product with a loop and append it customer basket
# [DONE] Add Discount button to validate coupon and apply discount.
# [DONE] Save the percentage to a variable and use that variable to calculate discounted price.
# [DONE] All discount percentages has been added.
# [WIP] Add payment page button(only by card)

""" [BUG] Change price updates price labels but not treeview <- problem occurs because treeview get price information directly from PRICE_LIST TUPLE via find_product_price() function. 
Solution 1: Get treeview price from CUSTOMER_BASKET_PRICE or ask customer to how many price changes they'd like to do. Based on user input remove 'userinput' amount from both treeview 
and CUSTOMER_BASKET, CUSTOMER_BASKET_SIZE, CUSTOMER_BASKET_PRICE then add it back with new price + {name_of_the_product} + 'Price changed' """

PRODUCT_LIST = ["Lamb Kebab Wrap", "Lahmacun", "Cag Kebab", "Iskender", "Ezogelin", "Kisir", "Mercimek Kofte", "Sarma"]
PRICE_LIST = [(10.99,  15.99), (3.99, 5.99), (18.99, 25.99), (16.99, 22.99), (7.99, 9.99), (5.49, 6.85), (8.45, 9.99), (7.58, 9.45)]
CUSTOMER_BASKET = []
CUSTOMER_BASKET_PRICE = []
CUSTOMER_BASKET_PRODUCT_SIZE = []
isChildWindowOpen = False
treeview_tuple = []
treeview_seen = set()
test_tuple = []
print(CUSTOMER_BASKET_PRICE)
def find_product_price(product_name, product_size):
    get_product_index = find_index_of_product(product_name)

    if product_size == 'S':
        return PRICE_LIST[get_product_index][0]
    return PRICE_LIST[get_product_index][1]
def find_index_of_product(product_name):
    get_product_index = 0
    for i in range(0,len(PRODUCT_LIST)):
        if product_name.lower() in PRODUCT_LIST[i].lower():
            get_product_index = i
    return get_product_index
def append_product(product_name, product_size):
    food_index = find_index_of_product(product_name)
    print(f"index {food_index}")
    if product_size == 'S':
        CUSTOMER_BASKET.append(product_name)
        CUSTOMER_BASKET_PRICE.append(PRICE_LIST[food_index][0])
        CUSTOMER_BASKET_PRODUCT_SIZE.append(product_size)
    else:
        product_name_capitalized = product_name.upper()
        CUSTOMER_BASKET.append(product_name_capitalized)
        CUSTOMER_BASKET_PRICE.append(PRICE_LIST[food_index][1])
        CUSTOMER_BASKET_PRODUCT_SIZE.append(product_size)
    showinfo(title="Choice", message=f"'{product_name}' has been added to your basket")
    destroy_child_window()
def remove_product():
    print(f'Customer Basket : {CUSTOMER_BASKET}, Customer Basket Price : {CUSTOMER_BASKET_PRICE}, Customer Basket Product Size: {CUSTOMER_BASKET_PRODUCT_SIZE}')
    for selected_item in customer_basket_treeview.selection():
        item = customer_basket_treeview.item(selected_item)
        customer_basket_treeview.delete(selected_item)
        get_selected_product_info = item['values']
        remove_product_from_basket(get_selected_product_info[0], get_selected_product_info[1])

def set_quantity(spinbox_quantity, product_name, product_size, product_price):
    if len(CUSTOMER_BASKET) > 1:
        for _ in range(len(CUSTOMER_BASKET)):
            remove_product_from_basket(product_name, product_size)
    print(f'Q before : {len(CUSTOMER_BASKET)}')
    for i in range(spinbox_quantity):
#        product_price = int(product_price)
        CUSTOMER_BASKET.append(product_name)
        CUSTOMER_BASKET_PRICE.append(find_product_price(product_name, product_size))
        CUSTOMER_BASKET_PRODUCT_SIZE.append(product_size)

    treeview_print_to_screen()
    basket_total_information()
    destroy_child_window()
    main_menu()
def change_price(new_product_price, product_name, product_size):
    index_of_product = find_index_of_product(product_name)
    if new_product_price == CUSTOMER_BASKET_PRICE[index_of_product]:
        showerror("Error", "New and old price can not be same!")
        treeview_print_to_screen()
        basket_total_information()
        destroy_child_window()
    else:
        CUSTOMER_BASKET_PRICE[index_of_product] = new_product_price
        treeview_print_to_screen()
        basket_total_information()
        destroy_child_window()
    print(CUSTOMER_BASKET_PRICE)


def get_input_from_user_to_adjust_price():
    global isChildWindowOpen
    if not isChildWindowOpen:
        for selected_item in customer_basket_treeview.selection():
            item = customer_basket_treeview.item(selected_item)
            print(item)
            get_product_info = item['values']
        global child_window
        child_window = tk.Toplevel()
        child_window.title("Portions")
        # Get screen width and height. Set width and height for child_window
        screen_width = child_window.winfo_screenwidth()
        screen_height = child_window.winfo_screenheight()
        window_width = 200
        window_height = 100
        # Find center of the screen
        center_x = int(screen_width / 2 - window_width / 2)
        center_y = int(screen_height / 2 - window_height / 2)
        child_window.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
        isChildWindowOpen = True
        child_window.resizable(False, False)
        set_price_label = tk.Label(child_window, text="Please set new price").pack()
        price_var = tk.IntVar()
        get_price_entry = tk.Entry(child_window, textvariable=price_var).pack()
        get_price_button = tk.Button(child_window, text="Set new price", command=lambda: [change_price(price_var.get(), get_product_info[0], get_product_info[1])]).pack()
        print(price_var.get())

        child_window.protocol('WM_DELETE_WINDOW', lambda: on_close_child_window())
        child_window.mainloop()
def get_product_information_to_adjust_quantity():
    for selected_item in customer_basket_treeview.selection():
        item = customer_basket_treeview.item(selected_item)
        get_product_info = item['values']
        global isChildWindowOpen
        # Create a top-level window (child windows)
        if not isChildWindowOpen:
            global child_window
            child_window = tk.Toplevel()
            child_window.title("Portions")
            # Get screen width and height. Set width and height for child_window
            screen_width = child_window.winfo_screenwidth()
            screen_height = child_window.winfo_screenheight()
            window_width = 200
            window_height = 100
            # Find center of the screen
            center_x = int(screen_width / 2 - window_width / 2)
            center_y = int(screen_height / 2 - window_height / 2)
            child_window.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

            isChildWindowOpen = True
            child_window.resizable(False, False)
            get_quantity_from_spinbox = tk.IntVar()
            quantity_label = tk.Label(child_window, text="Please choose a quantity")
            quantity_label.pack()
            quantity_spinbox = tk.Spinbox(child_window,from_= 1, to=50, textvariable=get_quantity_from_spinbox,wrap=True)
            quantity_spinbox.pack()
            set_quantity_button = tk.Button(child_window, text="Set Quantity", command=lambda: (set_quantity(get_quantity_from_spinbox.get(), get_product_info[0], get_product_info[1], get_product_info[3]) , ))
            set_quantity_button.pack()

            child_window.protocol('WM_DELETE_WINDOW', lambda: on_close_child_window())
            child_window.mainloop()
def remove_product_from_basket(product_name, product_size):
    get_index_of_product = 0
    for i in range(len(CUSTOMER_BASKET)):
        if product_name.lower() == CUSTOMER_BASKET[i].lower():
            get_index_of_product = i
    print(CUSTOMER_BASKET[get_index_of_product])
    CUSTOMER_BASKET.remove(CUSTOMER_BASKET[get_index_of_product])
    if product_size == 'S':
        CUSTOMER_BASKET_PRODUCT_SIZE.remove('S')
        CUSTOMER_BASKET_PRICE.remove(find_product_price(product_name, product_size))
    else:
        CUSTOMER_BASKET_PRODUCT_SIZE.remove('L')
        CUSTOMER_BASKET_PRICE.remove(find_product_price(product_name, product_size))
    treeview_print_to_screen()
    basket_total_information()
def treeview_product_selected(event):
    #x=840, y=40, height=650, width=825
    remove_product_from_basket = tk.Button(button_section_frame, text="REMOVE ITEM", bg='red', fg='white', command=lambda: [remove_product(), remove_product_from_basket.destroy()], font=("Helvetica,40"))
    remove_product_from_basket.place(x=840, y=700, width=400, height=200)
    global change_product_quantity
    change_product_quantity = tk.Button(button_section_frame, text="CHANGE QUANTITY", bg='blue', fg='white', font=("Helvetica", 15), command=get_product_information_to_adjust_quantity)
    change_product_quantity.place(x=1680, y=265,width=200,height=200)
    global change_product_price
    change_product_price = tk.Button(button_section_frame, text="CHANGE PRICE", bg='grey', fg='white', font=("Helvetica", 15), command=get_input_from_user_to_adjust_price)
    change_product_price.place(x=1680, y=489, width=200,height=200)
def get_portion(product_name):
    global isChildWindowOpen

    # Create a top-level window (child windows)
    if not isChildWindowOpen:
        global child_window
        child_window = tk.Toplevel()
        child_window.title("Portions")
        # Get screen width and height. Set width and height for child_window
        screen_width = child_window.winfo_screenwidth()
        screen_height = child_window.winfo_screenheight()
        window_width = 200
        window_height = 100
        # Find center of the screen
        center_x = int(screen_width / 2 - window_width / 2)
        center_y = int(screen_height / 2 - window_height / 2)
        child_window.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

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

        get_portion_button = ttk.Button(child_window, text="Choose Portion", command=lambda: append_product(product_name, get_food_portion.get()))
        get_portion_button.pack()
        child_window.protocol('WM_DELETE_WINDOW', lambda: on_close_child_window())
        child_window.mainloop()

def clear_treeview_all():
    # Clear treeview_tuple and treeview_seen to reset treeview. So we won't append the same product multiple times to screen.
    treeview_tuple.clear()
    treeview_seen.clear()
    # Clear childrens of treeview.
    for item in customer_basket_treeview.get_children():
        customer_basket_treeview.delete(item)
def treeview_print_to_screen():
#    print(f"Treeview : {CUSTOMER_BASKET}, {CUSTOMER_BASKET_PRICE}, {CUSTOMER_BASKET_PRODUCT_SIZE}")
    clear_treeview_all()
    # Create a tuple, count how many, add if a product in list multiple amount to seen list and append product information
    for product_name_treeview, loop_counter in zip(CUSTOMER_BASKET, range(0, len(CUSTOMER_BASKET))):
        if product_name_treeview not in treeview_seen:
            get_product_price = find_product_price(product_name_treeview, CUSTOMER_BASKET_PRODUCT_SIZE[loop_counter])
            count = CUSTOMER_BASKET.count(product_name_treeview)
            treeview_tuple.append((CUSTOMER_BASKET[loop_counter], CUSTOMER_BASKET_PRODUCT_SIZE[loop_counter], count, f'{round(get_product_price*count,2)}£'))
            treeview_seen.add(product_name_treeview)
    treeview_tuple.append(("Lamb Kebab", "S", 1,'4£'))
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
#    treeview_scrollbar = ttk.Scrollbar(button_section_frame, orient=tk.VERTICAL, command=customer_basket_treeview.yview)
#    customer_basket_treeview.configure(yscroll= treeview_scrollbar.set)
#    treeview_scrollbar.grid(row=0, column=1, sticky='ns')
    treeview_print_to_screen()
    basket_total_information()
    customer_basket_treeview.bind('<<TreeviewSelect>>', treeview_product_selected)

def on_close_child_window():
    global isChildWindowOpen
    isChildWindowOpen = False
    child_window.destroy()
def destroy_child_window():
    child_window.destroy()
    global isChildWindowOpen
    isChildWindowOpen = False
    print("Child windows has been successfully destroyed")

def clear_screen():
    for widgets in main_pos_name.winfo_children():
        widgets.destroy()


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
    kebab_dish_information = tk.Label(food_frame, text=" Lamb Kebab Wrap \nPrice(S/L): 10.99£/15.99£")
    kebab_dish_information.place(x=65, y=210)

    # Create a button and add food_lahmacun.png
    food_lahmacun_image = tk.PhotoImage(file="images/food/food_lahmacun.png").subsample(x=4,y=4)
    lahmacun_button = tk.Button(food_frame, image=food_lahmacun_image, command=lambda: get_portion("Lahmacun"))
    lahmacun_button.image = food_lahmacun_image
    lahmacun_button.place(x=315, y=5, width=200, height=200)

    # Create label for dish feature(s) -> Name, price, V/VE/GF
    lahmacun_dish_information = tk.Label(food_frame, text=" Lahmacun \nPrice(S/L): 3.99£/5.99£ \nV/VE option available!")
    lahmacun_dish_information.place(x=355, y=210)

    # Create a button and add food_cagkebab.png
    cag_kebab_image = tk.PhotoImage(file="images/food/food_cagkebab.png").subsample(x=4,y=4)
    cag_kebab_button = tk.Button(food_frame,image=cag_kebab_image, command=lambda: get_portion("Cag Kebab"))
    cag_kebab_button.image = cag_kebab_image
    cag_kebab_button.place(x=610, y=5, width=200, height=200)

    # Create label for dish feature(s) -> Name, price, V/VE/GF
    cag_kebab_dish_information = tk.Label(food_frame, text=" Cag Kebab \nPrice(S/L): 18.99£/25.99£")
    cag_kebab_dish_information.place(x=640, y=210)

    # Create a button and add food_iskender.png
    food_iskender_image = tk.PhotoImage(file="images/food/food_iskender.png").subsample(x=4,y=4)
    iskender_button = tk.Button(food_frame, image=food_iskender_image, command=lambda: get_portion("Iskender"))
    iskender_button.image = food_iskender_image
    iskender_button.place(x=895, y=5, width=200, height=200)

    # Create label for dish feature(s) -> Name, price, V/VE/GF
    iskender_dish_information = tk.Label(food_frame, text=" Iskender \nPrice(S/L): 16.99£/22.99£")
    iskender_dish_information.place(x=935, y=210)

    # Create a button and add food_ezogelin.png
    food_ezogelin_image = tk.PhotoImage(file="images/food/food_ezogelin.png").subsample(x=4,y=4)
    ezogelin_button = tk.Button(food_frame, image=food_ezogelin_image, command=lambda: get_portion("Ezogelin"))
    ezogelin_button.image = food_ezogelin_image
    ezogelin_button.place(x=40, y=300, width=200, height=200)

    # Create label for dish feature(s) -> Name, price, V/VE/GF
    ezogelin_dish_information = tk.Label(food_frame, text=" Ezogelin \nPrice(S/L): 7.99£/9.99£ \nV/VE")
    ezogelin_dish_information.place(x=80, y=505)

    # Create a button and add food_kisir.png
    food_kisir_image = tk.PhotoImage(file="images/food/food_kisir.png").subsample(x=4,y=4)
    kisir_button = tk.Button(food_frame, image=food_kisir_image, command=lambda: get_portion("Kisir"))
    kisir_button.image = food_kisir_image
    kisir_button.place(x=315, y=300,width=200, height=200)

    # Create label for dish feature(s) -> Name, price, V/VE/GF
    kisir_dish_information = tk.Label(food_frame, text=" Kisir \nPrice(S/L): 5.49£/6.85£ \nV/VE")
    kisir_dish_information.place(x=360, y=505)

    # Create a button and add food_mercimekkofte.png
    food_mercimekkofte_image = tk.PhotoImage(file="images/food/food_mercimekkofte.png").subsample(x=4,y=4)
    mercimekkofte_button = tk.Button(food_frame, image=food_mercimekkofte_image, command=lambda: get_portion("Mercimek Kofte"))
    mercimekkofte_button.image = food_mercimekkofte_image
    mercimekkofte_button.place(x=610, y=300,width=200, height=200)

    # Create label for dish feature(s) -> Name, price, V/VE/GF
    mercimekkofte_dish_information = tk.Label(food_frame, text=" Mercimek Kofte \nPrice(S/L): 8.45£/9.99£ \nV/VE")
    mercimekkofte_dish_information.place(x=640, y=505)

    # Create a button and add food_mercimekkofte.png
    food_sarma_image = tk.PhotoImage(file="images/food/food_sarma.png").subsample(x=4,y=4)
    sarma_button = tk.Button(food_frame, image=food_sarma_image, command=lambda: get_portion("Sarma"))
    sarma_button.image = food_sarma_image
    sarma_button.place(x=895, y=300, width=200, height=200)

    # Create label for dish feature(s) -> Name, price, V/VE/GF
    sarma_dish_information = tk.Label(food_frame, text=" Sarma \nPrice(S/L): 9.45£/13.99£ \nV/VE")
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
    drink_cola_information = tk.Label(drink_frame, text=" Coca Cola\n Price(S/L): 2.99£/3.99£")
    drink_cola_information.place(x=75,y=210)

    # Create a button and add image -> Soda
    drink_button_soda_image = tk.PhotoImage(file="images/drinks/drinks_soda.png")
    drink_button_soda_image_to_display = drink_button_soda_image.subsample(x=4, y=4)
    drink_button_soda = tk.Button(drink_frame, image=drink_button_soda_image_to_display)
    drink_button_soda.image = drink_button_soda_image_to_display
    drink_button_soda.place(x=330, y=5,width=200, height=200)
    # Soda information
    drink_soda_information = tk.Label(drink_frame, text=" Soda\n Price(S/L): 2.55£/3.67£")
    drink_soda_information.place(x=365, y=210)
    # Create a button and add image -> Apple Juice
    drink_button_applejuice_image = tk.PhotoImage(file="images/drinks/drinks_apple_juice.png")
    drink_button_applejuice_image_to_display = drink_button_applejuice_image.subsample(x=4, y=4)
    drink_button_applejuice = tk.Button(drink_frame, image=drink_button_applejuice_image_to_display)
    drink_button_applejuice.image = drink_button_applejuice_image_to_display
    drink_button_applejuice.place(x=620, y=5,width=200, height=200)
    # Apple Juice information
    applejuice_drinks_information = tk.Label(drink_frame, text=" Apple Juice\n Price(S/L): 2.99£/3.99£")
    applejuice_drinks_information.place(x=655, y=210)
    # Create a button and add image -> Orange Juice
    drink_button_orangejuice_image = tk.PhotoImage(file="images/drinks/drinks_orange_juice.png")
    drink_button_orangejuice_image_to_display = drink_button_orangejuice_image.subsample(x=4, y=4)
    drink_button_orangejuice = tk.Button(drink_frame, image=drink_button_orangejuice_image_to_display)
    drink_button_orangejuice.image = drink_button_orangejuice_image_to_display
    drink_button_orangejuice.place(x=910, y=5,width=200, height=200)
    # Orange Juice information
    orangejuice_drinks_information = tk.Label(drink_frame, text=" Orange Juice\n Price(S/L): 3.87£/7.80£")
    orangejuice_drinks_information.place(x=945, y=210)
    # Create a button and add image -> Tango
    drink_button_tango_image = tk.PhotoImage(file="images/drinks/drinks_tango.png")
    drink_button_tango_image_to_display = drink_button_tango_image.subsample(x=4, y=4)
    drink_button_tango = tk.Button(drink_frame, image=drink_button_tango_image_to_display)
    drink_button_tango.image = drink_button_tango_image_to_display
    drink_button_tango.place(x=40, y=300,width=200, height=200)
    # Tango information
    tango_drinks_information = tk.Label(drink_frame, text=" Tango\n Price(S/L): 1.99£/2.99£")
    tango_drinks_information.place(x=75, y=505)
    # Create a button and add image -> Ayran
    drink_button_ayran_image = tk.PhotoImage(file="images/drinks/drinks_ayran.png")
    drink_button_ayran_image_to_display = drink_button_ayran_image.subsample(x=4, y=4)
    drink_button_ayran = tk.Button(drink_frame, image=drink_button_ayran_image_to_display)
    drink_button_ayran.image = drink_button_ayran_image_to_display
    drink_button_ayran.place(x=330, y=300,width=200, height=200)
    # Ayran information
    ayran_drinks_information = tk.Label(drink_frame, text=" Ayran\n Price(S/L): 0.99£/1.99£")
    ayran_drinks_information.place(x=365, y=505)
    # Create a button and add image -> Ice Tea
    drink_button_iced_tea_image = tk.PhotoImage(file="images/drinks/drinks_iced_tea.png")
    drink_button_iced_tea_image_to_display = drink_button_iced_tea_image.subsample(x=4, y=4)
    drink_button_iced_tea = tk.Button(drink_frame, image=drink_button_iced_tea_image_to_display)
    drink_button_iced_tea.image = drink_button_iced_tea_image_to_display
    drink_button_iced_tea.place(x=620, y=300,width=200, height=200)
    # Ice Tea information
    iced_tea_drinks_information = tk.Label(drink_frame, text=" Ice Tea\n Price(S/L): 3.99£/5.99£")
    iced_tea_drinks_information.place(x=665, y=505)
    # Create a button and add image -> Root Beer
    drink_button_root_beer_image = tk.PhotoImage(file="images/drinks/drinks_root_beer.png")
    drink_button_root_beer_image_to_display = drink_button_root_beer_image.subsample(x=4, y=4)
    drink_button_root_beer = tk.Button(drink_frame, image=drink_button_root_beer_image_to_display)
    drink_button_root_beer.image = drink_button_root_beer_image_to_display
    drink_button_root_beer.place(x=910, y=300,width=200, height=200)
    # Root Beer information
    root_beer_drinks_information = tk.Label(drink_frame, text=" Root Beer\n Price(S/L): 3.99£/5.99£")
    root_beer_drinks_information.place(x=955, y=505)


    go_back_to_main_menu()
def print_items_in_cocktail_menu():
    # width = 245px,  height=186px for future references

    clear_screen()
    time_on_screen()
    # Create a frame
    cocktail_frame = tk.Frame(main_pos_name)
    cocktail_frame.pack(fill=tk.BOTH, expand=True)

    # Create a button and add cocktail_cosmopolitan.png
    cosmopolitan_image = tk.PhotoImage(file="images/cocktails/cocktail_cosmopolitan.png").subsample(x=4,y=4)
    cosmopolitan_button = tk.Button(cocktail_frame, image=cosmopolitan_image)
    cosmopolitan_button.image = cosmopolitan_image
    cosmopolitan_button.place(x=40, y=5, width=200, height=200)

    # Create label for cocktail feature(s) -> Name, price
    cosmopolitan_information = tk.Label(cocktail_frame, text=" Cosmopolitan \nPrice: 8.99£")
    cosmopolitan_information.place(x=75, y=210)

    # Create a button and add cocktail_margarita.png
    margarita_image = tk.PhotoImage(file="images/cocktails/cocktail_margarita.png").subsample(x=4,y=4)
    margarita_button = tk.Button(cocktail_frame, image=margarita_image)
    margarita_button.image = margarita_image
    margarita_button.place(x=315, y=5, width=200, height=200)

    # Create label for cocktail feature(s) -> Name, price
    margarita_information = tk.Label(cocktail_frame, text=" Margarita \nPrice: 9.99£")
    margarita_information.place(x=375, y=210)

    # Create a button and add cocktail_martini.png
    martini_image = tk.PhotoImage(file="images/cocktails/cocktail_martini.png").subsample(x=4,y=4)
    martini_button = tk.Button(cocktail_frame, image=martini_image)
    martini_button.image = martini_image
    martini_button.place(x=610, y=5, width=200, height=200)

    # Create label for cocktail feature(s) -> Name, price
    martini_information = tk.Label(cocktail_frame, text=" Martini \nPrice: 10.99£")
    martini_information.place(x=670, y=210)

    # Create a button and add cocktail_mojito.png
    mojito_image = tk.PhotoImage(file="images/cocktails/cocktail_mojito.png").subsample(x=4,y=4)
    mojito_button = tk.Button(cocktail_frame, image=mojito_image)
    mojito_button.image = mojito_image
    mojito_button.place(x=895, y=5, width=200, height=200)

    # Create label for cocktail feature(s) -> Name, price
    mojito_information = tk.Label(cocktail_frame, text=" Mojito \nPrice: 7.99£")
    mojito_information.place(x=960, y=210)

    # Create a button and add cocktail_moscowmule.png
    moscowmule_image = tk.PhotoImage(file="images/cocktails/cocktail_moscowmule.png").subsample(x=4,y=4)
    moscowmule_button = tk.Button(cocktail_frame, image=moscowmule_image)
    moscowmule_button.image = moscowmule_image
    moscowmule_button.place(x=40, y=300, width=200, height=200)

    # Create label for cocktail feature(s) -> Name, price
    moscowmule_information = tk.Label(cocktail_frame, text=" Moscow Mule \nPrice: 8.45£")
    moscowmule_information.place(x=80, y=505)

    # Create a button and add cocktail_negroni.png
    negroni_image = tk.PhotoImage(file="images/cocktails/cocktail_negroni.png").subsample(x=4,y=4)
    negroni_button = tk.Button(cocktail_frame, image=negroni_image, command=lambda: get_portion("Negroni"))
    negroni_button.image = negroni_image
    negroni_button.place(x=315, y=300, width=200, height=200)

    # Create label for cocktail feature(s) -> Name, price
    negroni_information = tk.Label(cocktail_frame, text=" Negroni \nPrice: 9.50£")
    negroni_information.place(x=370, y=505)

    # Create a button and add cocktail_oldfashioned.png
    oldfashioned_image = tk.PhotoImage(file="images/cocktails/cocktail_oldfashioned.png").subsample(x=4,y=4)
    oldfashioned_button = tk.Button(cocktail_frame, image=oldfashioned_image, command=lambda: get_portion("Old Fashioned"))
    oldfashioned_button.image = oldfashioned_image
    oldfashioned_button.place(x=610, y=300, width=200, height=200)

    # Create label for cocktail feature(s) -> Name, price
    oldfashioned_information = tk.Label(cocktail_frame, text=" Old Fashioned \nPrice: 10.50£")
    oldfashioned_information.place(x=655, y=505)

    # Create a button and add cocktail_whiskeysour.png
    whiskeysour_image = tk.PhotoImage(file="images/cocktails/cocktail_whiskeysour.png").subsample(x=4,y=4)
    whiskeysour_button = tk.Button(cocktail_frame, image=whiskeysour_image, command=lambda: get_portion("Whiskey Sour"))
    whiskeysour_button.image = whiskeysour_image
    whiskeysour_button.place(x=895, y=300, width=200, height=200)

    # Create label for cocktail feature(s) -> Name, price
    whiskeysour_information = tk.Label(cocktail_frame, text=" Whiskey Sour \nPrice: 8.99£")
    whiskeysour_information.place(x=945, y=505)

    go_back_to_main_menu()
def print_items_in_mocktail_menu():
    # width = 245px,  height=186px for future references

    clear_screen()
    time_on_screen()
    # Create a frame
    mocktail_frame = tk.Frame(main_pos_name)
    mocktail_frame.pack(fill=tk.BOTH, expand=True)

    # Create a button and add mocktail_daiquiri.png
    daiquiri_image = tk.PhotoImage(file="images/mocktails/mocktail_daiquiri.png").subsample(x=4, y=4)
    daiquiri_button = tk.Button(mocktail_frame, image=daiquiri_image)
    daiquiri_button.image = daiquiri_image
    daiquiri_button.place(x=40, y=5, width=200, height=200)

    # Create label for mocktail feature(s) -> Name, price
    daiquiri_information = tk.Label(mocktail_frame, text=" Daiquiri \nPrice: 8.99£")
    daiquiri_information.place(x=75, y=210)

    # Create a button and add mocktail_mimosa.png
    mimosa_image = tk.PhotoImage(file="images/mocktails/mocktail_mimosa.png").subsample(x=4, y=4)
    mimosa_button = tk.Button(mocktail_frame, image=mimosa_image)
    mimosa_button.image = mimosa_image
    mimosa_button.place(x=315, y=5, width=200, height=200)

    # Create label for mocktail feature(s) -> Name, price
    mimosa_information = tk.Label(mocktail_frame, text=" Mimosa \nPrice: 9.99£")
    mimosa_information.place(x=375, y=210)

    # Create a button and add mocktail_pinacolada.png
    pinacolada_image = tk.PhotoImage(file="images/mocktails/mocktail_pinacolada.png").subsample(x=4, y=4)
    pinacolada_button = tk.Button(mocktail_frame, image=pinacolada_image)
    pinacolada_button.image = pinacolada_image
    pinacolada_button.place(x=610, y=5, width=200, height=200)

    # Create label for mocktail feature(s) -> Name, price
    pinacolada_information = tk.Label(mocktail_frame, text=" Pina Colada \nPrice: 10.99£")
    pinacolada_information.place(x=670, y=210)

    # Create a button and add mocktail_punch.png
    punch_image = tk.PhotoImage(file="images/mocktails/mocktail_punch.png").subsample(x=4, y=4)
    punch_button = tk.Button(mocktail_frame, image=punch_image)
    punch_button.image = punch_image
    punch_button.place(x=895, y=5, width=200, height=200)

    # Create label for mocktail feature(s) -> Name, price
    punch_information = tk.Label(mocktail_frame, text=" Punch \nPrice: 7.99£")
    punch_information.place(x=960, y=210)

    # Create a button and add mocktail_sangria.png
    sangria_image = tk.PhotoImage(file="images/mocktails/mocktail_sangria.png").subsample(x=4, y=4)
    sangria_button = tk.Button(mocktail_frame, image=sangria_image)
    sangria_button.image = sangria_image
    sangria_button.place(x=40, y=300, width=200, height=200)

    # Create label for mocktail feature(s) -> Name, price
    sangria_information = tk.Label(mocktail_frame, text=" Sangria \nPrice: 8.45£")
    sangria_information.place(x=80, y=505)

    # Create a button and add mocktail_shirlytemple.png
    shirlytemple_image = tk.PhotoImage(file="images/mocktails/mocktail_shirlytemple.png").subsample(x=4, y=4)
    shirlytemple_button = tk.Button(mocktail_frame, image=shirlytemple_image)
    shirlytemple_button.image = shirlytemple_image
    shirlytemple_button.place(x=315, y=300, width=200, height=200)

    # Create label for mocktail feature(s) -> Name, price
    shirlytemple_information = tk.Label(mocktail_frame, text=" Shirley Temple \nPrice: 9.50£")
    shirlytemple_information.place(x=370, y=505)

    # Create a button and add mocktail_virginmargarita.png
    virginmargarita_image = tk.PhotoImage(file="images/mocktails/mocktail_virginmargarita.png").subsample(x=4, y=4)
    virginmargarita_button = tk.Button(mocktail_frame, image=virginmargarita_image)
    virginmargarita_button.image = virginmargarita_image
    virginmargarita_button.place(x=610, y=300, width=200, height=200)

    # Create label for mocktail feature(s) -> Name, price
    virginmargarita_information = tk.Label(mocktail_frame, text=" Virgin Margarita \nPrice: 10.50£")
    virginmargarita_information.place(x=655, y=505)

    # Create a button and add mocktail_mojito.png
    mojito_image = tk.PhotoImage(file="images/mocktails/mocktail_virginmojito.png").subsample(x=4, y=4)
    mojito_button = tk.Button(mocktail_frame, image=mojito_image)
    mojito_button.image = mojito_image
    mojito_button.place(x=895, y=300, width=200, height=200)

    # Create label for mocktail feature(s) -> Name, price
    mojito_information = tk.Label(mocktail_frame, text=" Mojito \nPrice: 7.99£")
    mojito_information.place(x=960, y=505)

    go_back_to_main_menu()
def print_items_in_kids_menu():
    # width = 245px,  height=186px for future references

    clear_screen()
    time_on_screen()
    # Create a frame
    kids_menu_frame = tk.Frame(main_pos_name)
    kids_menu_frame.pack(fill=tk.BOTH, expand=True)

    # Create a button and add kids_nuggets.png
    kids_nuggets_image = tk.PhotoImage(file="images/kids_menu/kids_nuggets.png").subsample(x=4, y=4)
    nuggets_button = tk.Button(kids_menu_frame, image=kids_nuggets_image)
    nuggets_button.image = kids_nuggets_image
    nuggets_button.place(x=40, y=5, width=200, height=200)

    # Label for Chicken Nuggets
    nuggets_label = tk.Label(kids_menu_frame, text="Chicken Nuggets\nPrice: 4.99£")
    nuggets_label.place(x=75, y=210)

    # Create a button and add kids_salmon.png
    kids_salmon_image = tk.PhotoImage(file="images/kids_menu/kids_salmon.png").subsample(x=4, y=4)
    salmon_button = tk.Button(kids_menu_frame, image=kids_salmon_image)
    salmon_button.image = kids_salmon_image
    salmon_button.place(x=315, y=5, width=200, height=200)

    # Label for Easy Salmon Curry
    salmon_label = tk.Label(kids_menu_frame, text="Easy Salmon Curry\nPrice: 5.99£")
    salmon_label.place(x=350, y=210)

    # Create a button and add kids_potatoes.png
    kids_potatoes_image = tk.PhotoImage(file="images/kids_menu/kids_potatoes.png").subsample(x=4, y=4)
    potatoes_button = tk.Button(kids_menu_frame, image=kids_potatoes_image)
    potatoes_button.image = kids_potatoes_image
    potatoes_button.place(x=610, y=5, width=200, height=200)

    # Label for Air-fryer Jacket Potatoes
    potatoes_label = tk.Label(kids_menu_frame, text="Air-fryer Jacket Potatoes\nPrice: 3.99£")
    potatoes_label.place(x=645, y=210)

    # Create a button and add kids_pasta.png
    kids_pasta_image = tk.PhotoImage(file="images/kids_menu/kids_pasta.png").subsample(x=4, y=4)
    pasta_button = tk.Button(kids_menu_frame, image=kids_pasta_image)
    pasta_button.image = kids_pasta_image
    pasta_button.place(x=895, y=5, width=200, height=200)

    # Label for Chicken Pasta Bake
    pasta_label = tk.Label(kids_menu_frame, text="Chicken Pasta Bake\nPrice: 5.49£")
    pasta_label.place(x=930, y=210)

    # Create a button and add kids_finger.png
    kids_finger_image = tk.PhotoImage(file="images/kids_menu/kids_finger.png").subsample(x=4, y=4)
    finger_button = tk.Button(kids_menu_frame, image=kids_finger_image)
    finger_button.image = kids_finger_image
    finger_button.place(x=40, y=300, width=200, height=200)

    # Label for Homemade Fish Fingers
    finger_label = tk.Label(kids_menu_frame, text="Homemade Fish Fingers\nPrice: 4.99£")
    finger_label.place(x=75, y=505)

    # Create a button and add kids_chickenstew.png
    kids_chickenstew_image = tk.PhotoImage(file="images/kids_menu/kids_chickenstew.png").subsample(x=4, y=4)
    chickenstew_button = tk.Button(kids_menu_frame, image=kids_chickenstew_image)
    chickenstew_button.image = kids_chickenstew_image
    chickenstew_button.place(x=315, y=300, width=200, height=200)

    # Label for Creamy Chicken Stew
    chickenstew_label = tk.Label(kids_menu_frame, text="Creamy Chicken Stew\nPrice: 6.49£")
    chickenstew_label.place(x=350, y=505)

    # Create a button and add kids_burger.png
    kids_burger_image = tk.PhotoImage(file="images/kids_menu/kids_burger.png").subsample(x=4, y=4)
    burger_button = tk.Button(kids_menu_frame, image=kids_burger_image)
    burger_button.image = kids_burger_image
    burger_button.place(x=610, y=300, width=200, height=200)

    # Label for Swedish Meatball Burgers
    burger_label = tk.Label(kids_menu_frame, text="Swedish Meatball Burgers\nPrice: 5.99£")
    burger_label.place(x=645, y=505)

    # Create a button and add kids_burger.png
    kids_beefstew_image = tk.PhotoImage(file="images/kids_menu/kids_beefstew.png").subsample(x=4, y=4)
    beefstew_button = tk.Button(kids_menu_frame, image=kids_beefstew_image)
    beefstew_button.image = kids_beefstew_image
    beefstew_button.place(x=895, y=300, width=200, height=200)

    # Label for Swedish Meatball Burgers
    beefstew_label = tk.Label(kids_menu_frame, text="Healthy beef stew with veggie mash \nPrice: 5.99£")
    beefstew_label.place(x=900, y=505)

    go_back_to_main_menu()
def print_items_in_coffee_menu():
    # width = 245px,  height=186px for future references

    clear_screen()
    time_on_screen()
    # Create a frame
    coffee_menu_frame = tk.Frame(main_pos_name)
    coffee_menu_frame.pack(fill=tk.BOTH, expand=True)

    # Create a button and add coffee_latte.png
    coffee_latte_image = tk.PhotoImage(file="images/coffee_menu/coffee_latte.png").subsample(x=4, y=4)
    latte_button = tk.Button(coffee_menu_frame, image=coffee_latte_image)
    latte_button.image = coffee_latte_image
    latte_button.place(x=40, y=5, width=200, height=200)

    # Label for Latte
    latte_label = tk.Label(coffee_menu_frame, text="Latte\nPrice: 3.99£")
    latte_label.place(x=105, y=210)

    # Create a button and add coffee_cortado.png
    coffee_cortado_image = tk.PhotoImage(file="images/coffee_menu/coffee_cortado.png").subsample(x=4, y=4)
    cortado_button = tk.Button(coffee_menu_frame, image=coffee_cortado_image)
    cortado_button.image = coffee_cortado_image
    cortado_button.place(x=315, y=5, width=200, height=200)

    # Label for Cortado
    cortado_label = tk.Label(coffee_menu_frame, text="Cortado\nPrice: 2.99£")
    cortado_label.place(x=385, y=210)

    # Create a button and add coffee_espresso.png
    coffee_espresso_image = tk.PhotoImage(file="images/coffee_menu/coffee_espresso.png").subsample(x=4, y=4)
    espresso_button = tk.Button(coffee_menu_frame, image=coffee_espresso_image)
    espresso_button.image = coffee_espresso_image
    espresso_button.place(x=610, y=5, width=200, height=200)

    # Label for Espresso
    espresso_label = tk.Label(coffee_menu_frame, text="Espresso\nPrice: 1.99£")
    espresso_label.place(x=675, y=210)

    # Create a button and add coffee_flatblack.png
    coffee_flatblack_image = tk.PhotoImage(file="images/coffee_menu/coffee_flatblack.png").subsample(x=4, y=4)
    flatblack_button = tk.Button(coffee_menu_frame, image=coffee_flatblack_image)
    flatblack_button.image = coffee_flatblack_image
    flatblack_button.place(x=895, y=5, width=200, height=200)

    # Label for Flat Black
    flatblack_label = tk.Label(coffee_menu_frame, text="Flat Black\nPrice: 2.49£")
    flatblack_label.place(x=959, y=210)

    # Create a button and add coffee_flatwhite.png (second time if needed)
    coffee_flatwhite_image = tk.PhotoImage(file="images/coffee_menu/coffee_flatwhite.png").subsample(x=4, y=4)
    flatwhite_button = tk.Button(coffee_menu_frame, image=coffee_flatwhite_image)
    flatwhite_button.image = coffee_flatwhite_image
    flatwhite_button.place(x=40, y=300, width=200, height=200)

    # Label for Flat White
    flatwhite_label = tk.Label(coffee_menu_frame, text="Flat White\nPrice: 3.49£")
    flatwhite_label.place(x=105, y=505)

    # Create a button and add coffee_mocha.png
    coffee_mocha_image = tk.PhotoImage(file="images/coffee_menu/coffee_mocha.png").subsample(x=4, y=4)
    mocha_button = tk.Button(coffee_menu_frame, image=coffee_mocha_image)
    mocha_button.image = coffee_mocha_image
    mocha_button.place(x=315, y=300, width=200, height=200)

    # Label for Mocha
    mocha_label = tk.Label(coffee_menu_frame, text="Mocha\nPrice: 3.99£")
    mocha_label.place(x=380, y=505)

    # Create a button and add coffee_americano.png
    coffee_americano_image = tk.PhotoImage(file="images/coffee_menu/coffee_americano.png").subsample(x=4, y=4)
    americano_button = tk.Button(coffee_menu_frame, image=coffee_americano_image)
    americano_button.image = coffee_americano_image
    americano_button.place(x=610, y=300, width=200, height=200)

    # Label for Americano
    americano_label = tk.Label(coffee_menu_frame, text="Americano\nPrice: 2.99£")
    americano_label.place(x=680, y=505)

    coffee_cappucino_image = tk.PhotoImage(file="images/coffee_menu/coffee_cappucino.png").subsample(x=4, y=4)
    # Create a button and add coffee_americano.png
    cappucino_button = tk.Button(coffee_menu_frame, image=coffee_cappucino_image)
    cappucino_button.image = coffee_cappucino_image
    cappucino_button.place(x=895, y=300, width=200, height=200)

    # Label for Americano
    americano_label = tk.Label(coffee_menu_frame, text="Cappucino\nPrice: 2.99£")
    americano_label.place(x=960, y=505)
    go_back_to_main_menu()
def main_menu():
    clear_screen()
    time_on_screen()
    # Create a BUTTON SECTION frame
    global button_section_frame
    button_section_frame = tk.Frame(main_pos_name)
    button_section_frame.pack(fill="both", expand=True)
    # FOOD BUTTON
    food_button_image = tk.PhotoImage(file="images/other/food_button.png").subsample(x=4,y=4)
    food_button = tk.Button(button_section_frame, image=food_button_image, command=print_items_in_food_menu)
    food_button.image = food_button_image
    food_button.place(x=50, y=50, width=200, height=200)

    # DRINK BUTTON
    drink_button_image = tk.PhotoImage(file="images/other/drink_button.png").subsample(x=4, y=4)
    drink_button = tk.Button(button_section_frame, image=drink_button_image, command=print_items_in_drink_menu)
    drink_button.image = drink_button_image
    drink_button.place(x=300, y=50, width=200, height=200)

    # COCKTAILS BUTTON
    cocktails_button_image = tk.PhotoImage(file="images/other/cocktail_button.png").subsample(x=2, y=2)
    cocktails_button = tk.Button(button_section_frame, image=cocktails_button_image, command=print_items_in_cocktail_menu)
    cocktails_button.image = cocktails_button_image
    cocktails_button.place(x=550, y=50, width=200, height=200)

    # KIDS BUTTON
    kids_menu_button_image = tk.PhotoImage(file="images/other/kidsmenu_button.png").subsample(x=2, y=2)
    kids_menu_button = tk.Button(button_section_frame, image=kids_menu_button_image, command = print_items_in_kids_menu)
    kids_menu_button.image = kids_menu_button_image
    kids_menu_button.place(x=50, y=300, width=200, height=200)

    # MOCKTAILS BUTTON
    mocktails_button_image = tk.PhotoImage(file="images/other/mocktails_button.png").subsample(x=4, y=4)
    mocktails_button = tk.Button(button_section_frame, image=mocktails_button_image, command=print_items_in_mocktail_menu)
    mocktails_button.image = mocktails_button_image
    mocktails_button.place(x=300, y=300, width=200, height=200)

    # COFFEE BUTTON
    coffee_button_image = tk.PhotoImage(file="images/other/coffee_button.png").subsample(x=4, y=4)
    coffee_button = tk.Button(button_section_frame, image=coffee_button_image, command=print_items_in_coffee_menu)
    coffee_button.image = coffee_button_image
    coffee_button.place(x=550, y=300, width=200, height=200)

    # Discount Button
    discount_button = tk.Button(button_section_frame, text="Discount", bg='blue', fg='white', font=("Arial", 20), command=create_discount_window)
    discount_button.place(x=1680, y=40, width=200, height=200)
    # Payment Button
    payment_button = tk.Button(button_section_frame, text="PAYMENT", bg='green', fg='white', font=("Helvetica", 15), command=create_payment_screen)
    payment_button.place(x=1680, y=699, width=200,height=201)

#  update_button = tk.Button(button_section_frame, text="UPDATE", command=treeview_print_to_screen).pack()
    treeview_create_customer_basket()

def create_payment_screen():
    payment_window = tk.Toplevel()
    payment_window.title("Payment Screen")
    payment_window.resizable(False, False)
    # Get screen width and height. Set width and height for child_window
    screen_width = payment_window.winfo_screenwidth()
    screen_height = payment_window.winfo_screenheight()
    window_width = 400
    window_height = 180
    # Find center of the screen
    center_x = int(screen_width / 2 - window_width / 2)
    center_y = int(screen_height / 2 - window_height / 2)
    payment_window.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')


    payment_window.mainloop()
def go_back_to_main_menu():
    back_to_menu_button_image = tk.PhotoImage(file="images/other/back_to_main_menu.png")
    back_to_menu_button_image_to_display = back_to_menu_button_image.subsample(x=4,y=4)
    another_test_button = tk.Button(main_pos_name, text="BACK TO MENU", command=main_menu, image=back_to_menu_button_image_to_display)
    another_test_button.image = back_to_menu_button_image_to_display
    another_test_button.place(x=1715, y=800, width=200, height=200)
# Set main settings, name and title
def calculate_basket_subtotal():
    calculate_subtotal = 0
    for i in range(len(CUSTOMER_BASKET_PRICE)):
        calculate_subtotal += CUSTOMER_BASKET_PRICE[i]
    return round(calculate_subtotal,2)

def create_discount_window():
    global  discount_child_window
    discount_child_window = tk.Toplevel()
    # Get screen width and height. Set width and height for child_window
    screen_width = discount_child_window.winfo_screenwidth()
    screen_height = discount_child_window.winfo_screenheight()
    window_width = 200
    window_height = 100
    # Find center of the screen
    center_x = int(screen_width / 2 - window_width / 2)
    center_y = int(screen_height / 2 - window_height / 2)
    discount_child_window.geometry(f'{200}x{200}+{center_x}+{center_y}')
    discount_child_window.resizable(False,False)
    discount_child_window.title("Discount Window")
    ten_percent_discount_button = tk.Button(discount_child_window, text="%10", bg="black", fg="white", font=("Arial", 10), command=lambda:discount_percentage(10))
    ten_percent_discount_button.place(width=100, height=100,x=0,y=0)
    thirty_percent_discount_button = tk.Button(discount_child_window, text="%30", bg="green", fg="white", font=("Arial", 10), command=lambda:discount_percentage(30))
    thirty_percent_discount_button.place(width=100, height=100,x=100,y=0)
    fifty_percent_discount_button = tk.Button(discount_child_window, text="%50", bg="red", fg="white", font=("Arial", 10), command=lambda:discount_percentage(50))
    fifty_percent_discount_button.place(width=100, height=100,x=0,y=100)
    set_discount_amount_button = tk.Button(discount_child_window, text="%100", bg="blue", fg="white", font=("Arial", 8), command=lambda:discount_percentage(100))
    set_discount_amount_button.place(width=100, height=100, x=100,y=100)
    discount_child_window.mainloop()
is_discount_button_pressed = False
def isPressed():
    global is_discount_button_pressed
    if not is_discount_button_pressed:
        is_discount_button_pressed = not is_discount_button_pressed
        basket_total_information()
def calculate_basket_total():
    first_price_calculation = round(calculate_basket_subtotal() - (calculate_basket_subtotal()*discount_percentage_variable)/100,2)
    second_price_calculation = (first_price_calculation*18)/100 + first_price_calculation
    return round(second_price_calculation,2)

discount_percentage_variable = 0
def discount_percentage(percentage):
    global discount_percentage_variable
    discount_percentage_variable = percentage
    isPressed()
def basket_total_information():
#    voucher = False
    labelframe = tk.LabelFrame(main_pos_name)
    labelframe.place(x=1266, y=733,width=400 , height=202)
    subtotal_label = tk.Label(labelframe, text=f"Subtotal: {calculate_basket_subtotal()}£", font=("Helvetica", 20))
    subtotal_label.pack()
    if is_discount_button_pressed:
        discount_label = tk.Label(labelframe, text=f"Discount: {round((calculate_basket_subtotal()*discount_percentage_variable)/100,2)}£", font=("Helvetica", 20))
        discount_label.pack()
    tax_label = tk.Label(labelframe, text=f"Tax(%18)", font=("Helvetica", 20))
    tax_label.pack()
#    if voucher:
#        voucher = tk.Label(labelframe, text="Voucher: ", font=("Helvetica",20))
#        voucher.pack()
    total = tk.Label(labelframe, text=f"Total: {calculate_basket_total()}£", font=("Helvetica", 20))
    total.pack()




def check_computer_res():
    print(f'{get_screen_res_width}, {get_screen_res_height}')
    if get_screen_res_width != 1920 or get_screen_res_width < 1920:
        if get_screen_res_height < 1080:
            showerror("ERROR", "Please set your resolution to 1920x1080 higher in order to run this program PROPERLY.")
            main_pos_name.destroy()
main_pos_name = tk.Tk()


main_pos_name.title("Foundation Project Market with GUI version 0.3.1.9")
main_pos_name.resizable(False, False)
# Get screen res and set window size and set geometry size using screen res + window size
get_screen_res_width = main_pos_name.winfo_screenwidth()
get_screen_res_height = main_pos_name.winfo_screenheight()
set_window_size_width = -10
set_window_size_height = 0
check_computer_res()
main_pos_name.geometry(f"{get_screen_res_width}x{get_screen_res_height-72}+{set_window_size_width}+{set_window_size_height}")
main_menu()



#test_button = tk.Button(main_pos_name, text="Test Button", command=customer_basket_treeview)
#test_button.place(x=600,y=800)


main_pos_name.mainloop()