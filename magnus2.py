from tkinter import *
import tkinter as tk
import sqlite3

window = tk.Tk()
window.title("Magnus - Manage Your Finances")
window.geometry("330x400")

conn = sqlite3.connect('magnus.db')
cursor = conn.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS expenses (
    expense_name text,
    expense_amount integer
)"""
)

#Functions
def add():
    conn = sqlite3.connect('magnus.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO expenses VALUES (:expense_name, :expense_amount)",
                    {'expense_name':expense_name_entry.get(),
                     'expense_amount':expense_amount_entry.get()}
)
    conn.commit()
    conn.close()
    expense_name_entry.delete(0, 'end')
    expense_amount_entry.delete(0, 'end')

def show_expenses():
    conn = sqlite3.connect('magnus.db')
    cursor = conn.cursor()
    cursor.execute("SELECT *, oid FROM expenses") #oid is like unique id given to each data
    records = cursor.fetchall() #you can also do fetchone() or fetchmany(40)
    a = 8
    b = 0
    name_label = tk.Label(window, text="Expense Name").grid(row=7, column=0)
    amount_label = tk.Label(window, text="Expense Amount").grid(row=7, column=1)
    id_label = tk.Label(window, text="ID").grid(row=7, column=2)
    for record in records:
        print("record: " + str(record))
        b = 0
        for detail in record:
            detail_label = tk.Label(window, text=detail).grid(row=a, column=b)
            print(detail)
            b += 1
        a += 1
    amounts = [x[1] for x in records]
    sum_amount = sum(amounts)
    total_label = tk.Label(window, text="Total: ").grid(row=a, column=0)
    sum_label = tk.Label(window, text=sum_amount).grid(row=a, column=1)
    conn.commit()
    conn.close()
    

def delete():
    conn = sqlite3.connect('magnus.db')
    cursor = conn.cursor()
    cursor.execute("DELETE FROM expenses WHERE oid=" + delete_id_entry.get())
    conn.commit()
    conn.close()
    delete_id_entry.delete(0, 'end')

#Widgets
expense_name_entry = tk.Entry(window, width=20)
expense_amount_entry = tk.Entry(window, width=20)

expense_name_label = tk.Label(window, text="Name of expense: ")
expense_amount_label = tk.Label(window, text="Amount of expense: ")

submit_button = tk.Button(window, text="Add", command=add, width=40)

show_expenses_button = tk.Button(window, text="Show All Expenses", command=show_expenses, width=40)

delete_id_label = tk.Label(window, text="ID To Delete: ")
delete_id_entry = tk.Entry(window, width=20)
delete_id_button = tk.Button(window, text="Delete Item", command=delete, width=40)



#Layout
expense_name_label.grid(row=0, column=0)
expense_name_entry.grid(row=0, column=1)
expense_amount_label.grid(row=1, column=0)
expense_amount_entry.grid(row=1, column=1)
submit_button.grid(row=2, column=0, columnspan=2, pady=10)
show_expenses_button.grid(row=3, column=0, columnspan=2, pady=10)
delete_id_label.grid(row=5, column=0)
delete_id_entry.grid(row=5, column=1)
delete_id_button.grid(row=6, column=0, columnspan=2, pady=10)

conn.commit()
conn.close()

window.mainloop()
