from tkinter import * 
from tkinter import ttk
from tkinter import messagebox

# Currencies
currencies = ["Dollar", "Egyptian Pound", "Yen", "Euro"]

# Convert function
def convert():
    try:
        from_currency = combo_from.get()
        to_currency = combo_to.get()
        amount = float(eamount.get())

        if from_currency == '' or to_currency == '':
            sad_message = messagebox.showwarning(title="Warning", message="Please check that you entered the currencies")
            clear()
            return
                
        if from_currency != to_currency:
            exchange = float(eexchange_rate.get())
        
        elif from_currency == to_currency:
            eexchange_rate.delete(0, "end")
            eexchange_rate.insert(0, "1")
            exchange = float(eexchange_rate.get())

        amount_with_the_other_currency = round(exchange * amount, 2)
        message =  messagebox.showinfo(title="Operation done", message=f"{amount} {from_currency}s = {amount_with_the_other_currency} {to_currency}s")
        clear()
        return
    except ValueError:
        sad_message = messagebox.showerror(title="Error", message="Please check that all values you entered are valid")
        clear()
        return

# Clear function
def clear():
    eexchange_rate.delete(0, "end")
    combo_from.delete(0, "end")
    combo_to.delete(0, "end")
    eamount.delete(0, "end")
    combo_from.focus_set()

# Start
root = Tk()
root.title("Currency converter")
root.geometry("310x250")
root.resizable(0, 0)
root.grid_anchor("center")

# Welcome
welcome = Label(root, text="Convert Currencies At No Time", font="Arial 15 bold", fg="#d19303")
welcome.grid(row=0, column=0, columnspan=4, sticky="we", padx=3, pady=10)

# From
lfrom = Label(root, text="From:", fg="#000000")
lfrom.grid(row=1, column=0, padx=3, pady=10)

combo_from = ttk.Combobox(root, values=currencies, width=15, state="readonly")
combo_from.grid(row=1, column=1, padx=2, pady=10)
combo_from.focus_set()

# Amount
lfrom = Label(root, text="Amount:", fg="#000000")
lfrom.grid(row=2, column=0, padx=3, pady=10)

eamount = ttk.Entry(root, width=7)
eamount.grid(row=2, column=1, padx=2, pady=10)

# To
lto = Label(root, text="To:", fg="#000000")
lto.grid(row=3, column=0, padx=3, pady=10)

combo_to = ttk.Combobox(root, values=currencies, width=15, state="readonly")
combo_to.grid(row=3, column=1, padx=2, pady=10)

# Exchange rate
lexchange_rate = Label(root, text="Exchange rate:", fg="#000000")
lexchange_rate.grid(row=4, column=0, padx=3, pady=10)

eexchange_rate = ttk.Entry(root, width=7)
eexchange_rate.grid(row=4, column=1, padx=2, pady=10)

# Convert
converting = ttk.Button(root, text="➡", command=convert, width=2)
converting.place(relx=1.0, rely=1.0, anchor="se", x=-10, y=-10)

# Update
root.mainloop()