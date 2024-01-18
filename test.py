import tkinter as tk
from tkinter import ttk
# Find a way to count how many item is in product_name. Adjust product_quantity with that information
main_pos_name = tk.Tk()


seenProduct = set()

test_tuple_v2 = []


# Define treeview identifiers
treeview_customer_basket_identifier_columns = ('product_name', 'product_quantity', 'product_size', 'product_price')
# Create a treeview
customer_basket_treeview = ttk.Treeview(main_pos_name, columns=treeview_customer_basket_identifier_columns, show='headings')
# Create headings and place treeview onto frame 'button_section_frame'
customer_basket_treeview.heading('product_name', text='Product Name')
customer_basket_treeview.heading('product_quantity', text='Product Quantity')
customer_basket_treeview.heading('product_size', text='Product Size')
customer_basket_treeview.heading('product_price', text='Product Price')
customer_basket_treeview.pack()
# Create a tuple and append product information
test_tuple = []
product_name = ["test1", "test2", "test3", "test1", "test1", "test2", "test3"]
product_quantity = ["1", "2", "3", "1", "1", "2", "3"]
product_size = ["S", "L", "S", "S", "S", "L", "S"]
product_price = ["1", "2", "3", "1", "1", "2", "3"]
for productCounter in product_name:
    if productCounter not in seenProduct:
        count = product_name.count(productCounter)
        test_tuple_v2.append((f'{productCounter}', f'{count}'))
        seenProduct.add(productCounter)
        print(productCounter, count)
        test_tuple.append((f'{productCounter}', f'{count}' ))  
print(test_tuple_v2)

for i in range(len(product_name)):
   test_tuple.append((f'{product_size[i]}', f'{product_price[i]}'))

for appendToTreeview in test_tuple:
   customer_basket_treeview.insert('', tk.END, values=appendToTreeview)




main_pos_name.mainloop()