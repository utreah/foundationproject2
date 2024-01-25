import tkinter as tk
from tkinter import ttk
# Find a way to count how many item is in product_name. Adjust product_quantity with that information
main_pos_name = tk.Tk()
current_value = tk.IntVar()
test_list = []
def test():
    print(current_value.get())
for i in range(0,100):
    test_list.append(i)
print(test_list)
spin_box_test = ttk.Spinbox(main_pos_name, from_=0, to=100, textvariable=current_value, wrap=True).pack()

set_quantity = tk.Button(main_pos_name, text="SET QUANTITY",command=test).pack()


main_pos_name.mainloop()