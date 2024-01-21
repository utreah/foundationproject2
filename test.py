import tkinter as tk
from tkinter import ttk
# Find a way to count how many item is in product_name. Adjust product_quantity with that information
main_pos_name = tk.Tk()



# Define treeview identifiers
treeview_customer_basket_identifier_columns = ('product_name', 'product_size', 'product_quantity', 'product_price')
# Create a treeview
customer_basket_treeview = ttk.Treeview(main_pos_name, columns=treeview_customer_basket_identifier_columns, show='headings')
# Create headings and place treeview onto frame 'button_section_frame'
customer_basket_treeview.heading('product_name', text='Product Name')
customer_basket_treeview.heading('product_size', text='Product Size')
customer_basket_treeview.heading('product_quantity', text='Product Quantity')
customer_basket_treeview.heading('product_price', text='Product Price')
customer_basket_treeview.pack()
# Create a tuple and append product information

# ARRAYS
product_name = ["test1", "test2", "test3", "test1", "test1", "test2", "test3","TEST1"]
product_quantity = ["1", "2", "3", "1", "1", "2", "3"]
product_size = ["S", "L", "S", "S", "S", "L", "S","L"]
product_price = ["1", "2", "5", "1", "1", "2", "5","8"]
product_mix_name_size = []
test_seen = set()
#for i in range(0,len(product_name)):
#    product_mix_name_size.append((product_name[i],product_size[i]))
def delete():
    for item in customer_basket_treeview.get_children():
        customer_basket_treeview.delete(item)
def find_food_price(productName):
    get_index = product_name.index(productName)
    return product_price[get_index]
def add():
    for i,k in zip(product_name, range(0, len(product_name))):
        if i not in test_seen:
            foodPrice = find_food_price(i)
            count = product_name.count(i)
            product_mix_name_size.append((product_name[k], product_size[k], count,foodPrice))
            test_seen.add(i)
    #print("First append: ", product_mix_name_size)
    # [('test1', 'S'), ('test2', 'L'), ('test3', 'S'), ('test1', 'S'), ('test1', 'S'), ('test2', 'L'), ('test3', 'S'), ('TEST1', 'L')]
    # 3 adet TEST1 S || 2 ADET TEST2 L || 2 ADET TEST3 S || 1 adet TEST1 L
    #print("After count append:", product_mix_name_size)

    print("Last append: ", product_mix_name_size)
    for testings in product_mix_name_size:
        customer_basket_treeview.insert('', tk.END,values=testings)
test_button = tk.Button(main_pos_name, text="Test Button", command=delete).pack()
test_button_v2 = tk.Button(main_pos_name, text="Add button", command = add).pack()
main_pos_name.mainloop()