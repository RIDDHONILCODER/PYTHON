from tkinter import *
from tkinter import ttk,messagebox
from PIL import Image,ImageTk

window=Tk()
window.geometry("800x600")
window.title("restaurant management system")
canvas=Canvas(window,width=800,height=600)
canvas.pack()

upload_image=Image.open('res.png')
upload_image=upload_image.resize((800,600))
image=ImageTk.PhotoImage(upload_image)

lbl=Label(window, image=image)
lbl.place(x=5,y=10)

menu_items = {
            "FRIES MEAL": 2,
            "LUNCH MEAL": 2,
            "BURGER MEAL": 3,
            "PIZZA MEAL": 4,
            "CHEESE BURGER": 2.5,
            "DRINKS": 1
        }
frame = ttk.Frame(window)
frame.place(relx=0.5, rely=0.5,anchor=CENTER)  # Place it at the center of the window
# Heading label
ttk.Label(frame,text="Restaurant Order Management",font=("Arial", 20, "bold")).grid(row=0,columnspan=3,padx=10,pady=10)

def place_order():
    total_cost = 0
    exchange_rate = 82
    order_summary = "Order Summary:\n"
    currency = currency_var.get()
    symbol = "₹" if currency == "INR" else "$"
    rate = exchange_rate if currency == "INR" else 1
    for item, entry in menu_quantities.items():
        quantity = entry.get()
        if quantity.isdigit():
            quantity = int(quantity)
            price = menu_items[item] * rate
            cost = quantity * price
            total_cost += cost
            if quantity > 0:
                order_summary += f"{item}: {quantity} x {symbol}{price} = {symbol}{cost}\n"
    if total_cost > 0:
        order_summary += f"\nTotal Cost: {symbol}{total_cost}"
        messagebox.showinfo("Order Placed", order_summary)  # Show order summary in a message box
    else:
            # Show error if no items are ordered
        messagebox.showerror("Error", "Please order at least one item.")  


menu_labels = {}  # To store references to menu item labels
menu_quantities = {}  # To store references to quantity entry widgets

        # Create labels and entry widgets for each menu item
for i, (item, price) in enumerate(menu_items.items(), start=1):
    label = ttk.Label(frame,text=f"{item} (${price}):",font=("Arial", 12))
    label.grid(row=i, column=0, padx=10, pady=5)
    menu_labels[item] = label
    quantity_entry = ttk.Entry(frame, width=5)
    quantity_entry.grid(row=i, column=1, padx=10, pady=5)
    menu_quantities[item] = quantity_entry

# Currency selection
currency_var = StringVar()
ttk.Label(frame, text="Currency:",font=("Arial", 12)).grid(row=len(menu_items) + 1,column=0,padx=10,pady=5)
# Dropdown for currency selection
currency_dropdown = ttk.Combobox(frame,textvariable=currency_var,state="readonly",width=18,values=('USD', 'INR'))
currency_dropdown.grid(row=len(menu_items) + 1,
                               column=1,
                               padx=10,
                               pady=5)
currency_dropdown.current(0)  # Set default currency
# Button to place the order
order_button = ttk.Button(frame,text="Place Order",command=place_order)
order_button.grid(row=len(menu_items) + 2,
                          columnspan=3,
                          padx=10,
                          pady=10)
window.mainloop()

