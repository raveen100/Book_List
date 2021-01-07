from tkinter import*
from db import Database
from tkinter import messagebox

db = Database('store.db')

#functions

def populate_list():
    book_list.delete(0, END)
    for row in db.fetch():
        book_list.insert(END, row)

def select_item(event):
    try:
        global selected_item
        index = book_list.curselection()[0]
        selected_item = book_list.get(index)
        print(selected_item)

        book_entry.delete(0, END)
        book_entry.insert(END, selected_item[1])
        author_entry.delete(0, END)
        author_entry.insert(END, selected_item[2])
        startDate_entry.delete(0, END)
        startDate_entry.insert(END, selected_item[3])
        price_entry.delete(0, END)
        price_entry.insert(END, selected_item[4])
    except IndexError:
        pass

def add_item():

    if book_text.get() == '' or author_text.get() == '' or startDate_text.get() == '' or price_text.get() == '' :
        messagebox.showerror('Required fields', 'Please include all fiellds')
        return

    db.insert(book_text.get(), author_text.get(), startDate_text.get(), price_text.get())
    book_list.delete(0,END)
    book_list.insert(END, (book_text.get(), author_text.get(), startDate_text.get(), price_text.get()))
    clear_text()
    populate_list()

def remove_item():
    db.remove(selected_item[0])
    clear_text()
    populate_list()

def update_item():
    db.update(selected_item[0], book_text.get(), author_text.get(), startDate_text.get(), price_text.get())
    populate_list()

def clear_text():
    book_entry.delete(0, END)
    author_entry.delete(0, END)
    startDate_entry.delete(0, END)
    price_entry.delete(0, END)


#create the window
app = Tk()
app.title('book Manager')
app.geometry('800x550')

#book
book_text = StringVar()
book_label = Label(app, text='book Name', font=('bold', 14), pady='20')
book_label.grid(row=0, column=0, sticky=W)
book_entry = Entry(app, textvariable=book_text)
book_entry.grid(row=0, column=1)

#author
author_text = StringVar()
author_label = Label(app, text='author ', font=('bold', 14), pady='20')
author_label.grid(row=0, column=2, sticky=W)
author_entry = Entry(app, textvariable=author_text)
author_entry.grid(row=0, column=3)

#startDate
startDate_text = StringVar()
startDate_label = Label(app, text='startDate', font=('bold', 14), pady='20')
startDate_label.grid(row=1, column=0, sticky=W)
startDate_entry = Entry(app, textvariable=startDate_text)
startDate_entry.grid(row=1, column=1)

#price
price_text = StringVar()
price_label = Label(app, text='Price', font=('bold', 14), pady='20')
price_label.grid(row=1, column=2, sticky=W)
price_entry = Entry(app, textvariable=price_text)
price_entry.grid(row=1, column=3)

#books list
book_list = Listbox(app, height='20', width='100')
book_list.grid(row=3, column=0, columnspan=3, rowspan=6, pady=20, padx=20)

# Create scrollbar
scrollbar = Scrollbar(app)
scrollbar.grid(row=3, rowspan=6, column=3,pady=20, padx=20, sticky=N)
# Set scroll to listbox
book_list.configure(yscrollcommand=scrollbar.set)
scrollbar.configure(command=book_list.yview)
# Bind select
book_list.bind('<<ListboxSelect>>', select_item)


#buttons
add_btn = Button(app, text='Add Item', width='12', command=add_item)
add_btn.grid(row=2, column=0)

remove_btn = Button(app, text='Remove Item', width='12', command=remove_item)
remove_btn.grid(row=2, column=1)

update_btn = Button(app, text='Update Item', width='12', command=update_item)
update_btn.grid(row=2, column=2)

clear_btn = Button(app, text='Clear Input', width='12', bg='red', bd='0', command=clear_text)
clear_btn.grid(row=2, column=3)

#populate data
populate_list()

#start the program
app.mainloop()