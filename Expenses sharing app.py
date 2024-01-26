from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from datetime import datetime

def get_current_date():
    current_date = datetime.now().strftime("%Y-%m-%d")
    dopvar.set(current_date)

def save_record():
    # Placeholder function for saving record
    item_name_value = item_name.get()
    item_amt_value = amtvar.get()
    dop_value = dopvar.get()

    # Add your logic to save the record to your data structure or database
    # For now, let's just print the values
    print("Item Name:", item_name_value)
    print("Item Amount:", item_amt_value)
    print("Purchase Date:", dop_value)

def clear_entry():
    # Placeholder function for clearing entry fields
    item_name.delete(0, END)
    amtvar.set(0)
    dopvar.set("")

def exit_app():
    # Placeholder function for exiting the application
    ws.destroy()

# Placeholder functions for additional buttons
def calculate_total_balance():
    pass

def update_record():
    pass

def delete_record():
    pass

ws = Tk()
ws.title('Office Expense')

f = ('Times new roman', 14)
amtvar = IntVar()
dopvar = StringVar()

f2 = Frame(ws)
f2.pack()

f1 = Frame(
    ws,
    padx=10,
    pady=10,
)
f1.pack(expand=True, fill=BOTH)

Label(f1, text='ITEM NAME', font=f).grid(row=0, column=0, sticky=W)
Label(f1, text='ITEM PRICE', font=f).grid(row=1, column=0, sticky=W)
Label(f1, text='PURCHASE DATE', font=f).grid(row=2, column=0, sticky=W)

item_name = Entry(f1, font=f)
item_amt = Entry(f1, font=f, textvariable=amtvar)
transaction_date = Entry(f1, font=f, textvariable=dopvar)

item_name.grid(row=0, column=1, sticky=EW, padx=(10, 0))
item_amt.grid(row=1, column=1, sticky=EW, padx=(10, 0))
transaction_date.grid(row=2, column=1, sticky=EW, padx=(10, 0))

cur_date = Button(f1, text='Current Date', font=f, bg='#04C4D9', command=get_current_date, width=15)
submit_btn = Button(f1, text='Save Record', font=f, command=save_record, bg='#42602D', fg='white')
clr_btn = Button(f1, text='Clear Entry', font=f, command=clear_entry, bg='#D9B036', fg='white')
quit_btn = Button(f1, text='Exit', font=f, command=exit_app, bg='#D33532', fg='white')
total_bal = Button(f1, text='Total Balance', font=f, command=calculate_total_balance)
update_btn = Button(f1, text='Update', bg='#C2BB00', command=update_record, fg='white', font=f)
del_btn = Button(f1, text='Delete', bg='#BD2A2E', fg='white', command=delete_record, font=f)

cur_date.grid(row=3, column=1, sticky=EW, padx=(10, 0))
submit_btn.grid(row=0, column=2, sticky=EW, padx=(10, 0))
clr_btn.grid(row=1, column=2, sticky=EW, padx=(10, 0))
quit_btn.grid(row=2, column=2, sticky=EW, padx=(10, 0))
total_bal.grid(row=0, column=3, sticky=EW, padx=(10, 0))
update_btn.grid(row=1, column=3, sticky=EW, padx=(10, 0))
del_btn.grid(row=2, column=3, sticky=EW, padx=(10, 0))

tv = ttk.Treeview(f2, selectmode='browse', columns=(1, 2, 3, 4), show='headings', height=8, )
tv.pack(side="left")

tv.column(1, anchor=CENTER, stretch=NO, width=70)
tv.column(2, anchor=CENTER)
tv.column(3, anchor=CENTER)
tv.column(4, anchor=CENTER)
tv.heading(1, text="Serial no")
tv.heading(2, text="Item Name", )
tv.heading(3, text="Item Price")
tv.heading(4, text="Purchase Date")

style = ttk.Style()
style.theme_use("default")
style.map("Treeview")

scrollbar = Scrollbar(f2, orient='vertical')
scrollbar.configure(command=tv.yview)
scrollbar.pack(side="right", fill="y")
tv.config(yscrollcommand=scrollbar.set)

ws.mainloop()
