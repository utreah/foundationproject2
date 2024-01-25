import tkinter as tk

def button_click(event):
    # Access the widget name/identifier
    widget_name = event.widget.winfo_name()
    print("Widget Name:", widget_name)

root = tk.Tk()
button = tk.Button(root, text="Click Me", name="my_button", command=button_click)
button.pack()
button.bind("<Button-1>", button_click)

root.mainloop()
