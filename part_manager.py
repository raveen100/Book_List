from tkinter import*

#functions

def populate_list():
    print('Populate')

def add_item():
    print('Add')

def remove_item():
    print('Remove')

def update_item():
    print('Update')

def clear_text():
    print('Clear')


#create the window
app = Tk()
app.title('Part Manager')
app.geometry('1200x650')

#part
part_text = StringVar()
part_label = Label(app, text='Part Name', font=('bold', 14), pady='20')
part_label.grid(row=0, column=0, sticky=W)
part_entry = Entry(app, textvariable=part_text)
part_entry.grid(row=0, column=1)

#customer
customer_text = StringVar()
customer_label = Label(app, text='Customer ', font=('bold', 14), pady='20')
customer_label.grid(row=0, column=2, sticky=W)
customer_entry = Entry(app, textvariable=customer_text)
customer_entry.grid(row=0, column=3)

#retailer
retailer_text = StringVar()
retailer_label = Label(app, text='Retailer', font=('bold', 14), pady='20')
retailer_label.grid(row=1, column=0, sticky=W)
retailer_entry = Entry(app, textvariable=retailer_text)
retailer_entry.grid(row=1, column=1)

#price
price_text = StringVar()
price_label = Label(app, text='Price', font=('bold', 14), pady='20')
price_label.grid(row=1, column=2, sticky=W)
price_entry = Entry(app, textvariable=price_text)
price_entry.grid(row=1, column=3)

#parts list
part_list = Listbox(app, height='20', width='100')
part_list.grid(row='3',column='0', rowspan='3', columnspan='6', pady='20',padx='20')

#create scrollbar
scrollbar = Scrollbar(app)
scrollbar.grid(row=3, column=6)
#set scroll to listbox
part_list.configure(yscrollcommand=scrollbar.set)
scrollbar.configure(command=part_list.yview)

#buttons
add_btn = Button(app, text='Add Item', width='12', command=add_item)
add_btn.grid(row=2, column=0)

remove_btn = Button(app, text='Remove Item', width='12', command=remove_item)
remove_btn.grid(row=2, column=1)

update_btn = Button(app, text='Update Item', width='12', command=update_item)
update_btn.grid(row=2, column=2)

clear_btn = Button(app, text='Clear Input', width='12', bg='red', command=clear_text)
clear_btn.grid(row=2, column=3)

#populate data
populate_list()

#start the program
app.mainloop()