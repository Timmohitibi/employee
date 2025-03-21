import tkinter as customtkinter
from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox
import tkinter as customtkinter
import database

# Initialize CustomTkinter App
app = customtkinter.CTk()
app.title("Employee Management System")
app.geometry("900x420")
app.configure(bg="#161c25")  # 'config' should be 'configure'

app.resizable(False, False)

# Fonts
font1 = ("Arial", 20, "bold")
font2 = ("Arial", 12, "bold")

def add_to_treeview():
  employees = database.fetch_employees()
  tree.delete(*tree.get_children())
  for employee in employees:
    tree.insert("", "end", values=employee)


def clear(*clicked):
  if clicked:
    tree.selection_remove(tree.focus())
    tree.focus('')
  id_entry.delete(0, END)
  name_entry.delete(0, END)
  role_entry.delete(0, END)
  variable1.set('Male')
  status_entry.delete(0, END)

def display_data(event):
  selected_item = tree.focus()
  if selected_item:
    row = tree.item(selected_item)['values']
    clear()
    id_entry.insert(0, row[0])
    name_entry.insert(0, row[1])
    role_entry.insert(0, row[2])
    variable1.set(row[3])
    status_entry.insert(0, row[4])
  else:
    pass

def insert():
  id = id_entry.get()
  name = name_entry.get()
  role =role_entry.get()
  gender = variable1.get()
  status = status_entry.get()
  if not (id and name and role and gender and status):
    messagebox.showerror("Error", "All fields are required")
  elif database.id_exists(id):
    messagebox.showerror("Error", "Employee with ID already exists")
  else:
    database.insert_employee(id, name, role, gender, status)
    add_to_treeview()
    clear()
    messagebox.showinfo("Success", "Employee added successfully")

def update():
  selected_item = tree.focus()
  if not selected_item:
    messagebox.showerror("Error", "Please select an employee to update")
  else:
    id = id_entry.get()
    name = name_entry.get()
    role = role_entry.get()
    gender = variable1.get()
    status = status_entry.get()
    database.update_employee(name, role, gender, status, id)
    add_to_treeview()
    clear()
    messagebox.showinfo('Success', 'Data has been updated.')


def delete():
  selected_item = tree.focus()
  if not selected_item:
    messagebox.showerror("Error", "Please select an employee to delete")
  else:
    id = id_entry.get()
    database.delete_employee(id)
    add_to_treeview()
    clear()
    messagebox.showinfo("Success", "Employee deleted successfully")


id_label = customtkinter.CTkLabel(app, text="ID", font=font2, bg="#161c25", fg="white")
id_label.place(x=50, y=50)

id_entry = customtkinter.CTkEntry(app, font=font2, bg="#161c25", fg="white")
id_entry.place(x=200, y=50)

name_label = customtkinter.CTkLabel(app, text="Name", font=font2, bg="#161c25", fg="white")
name_label.place(x=50, y=100)

name_entry = customtkinter.CTkEntry(app, font=font2, bg="#161c25", fg="white")
name_entry.place(x=200, y=100)

role_label = customtkinter.CTkLabel(app, text="Role", font=font2, bg="#161c25", fg="white")
role_label.place(x=50, y=150)

role_entry = customtkinter.CTkEntry(app, font=font2, bg="#161c25", fg="white")
role_entry.place(x=200, y=150)

gender_label = customtkinter.CTkLabel(app, font=font2, text='gender:', bg="#161c25, fg='white")
gender_label.place(x=50, y=200)

options = ['Male', 'Female']
variable1 = StringVar()

gender_options = customtkinter.CTkOptionMenu(app, variable1, * options)
gender_options.set('Male')
gender_options.place(x=200, y=200)

status_label = customtkinter.CTkLabel(app, text="Status", font=font2, bg="#161c25", fg="white")
status_label.place(x=50, y=250)

status_entry = customtkinter.CTkEntry(app, font=font2, bg="#161c25", fg="white")
status_entry.place(x=200, y=250)

add_button = customtkinter.CTkButton(app, COMMAND=insert, text="Add Employee", font=font2, bg="#161c25", fg="white")
add_button.place(x=50, y=300)

update_button = customtkinter.CTkButton(app, command=update, text="Update Employee", font=font2, bg="#161c25", fg="white")
update_button.place(x=200, y=300)

delete_button = customtkinter.CTkButton(app,command=delete, text="Delete Employee", font=font2, bg="#161c25", fg="white")
delete_button.place(x=400, y=300)

clear_button = customtkinter.CTkButton(app, command=lambda:clear(True), text="Clear", font=font2, bg="#161c25", fg="white")
clear_button.place(x=600, y=300)

# Treeview
style = ttk.Style(app)

style.theme_use("clam")
style.configure("Treeview", background="#161c25", fieldbackground="#161c25", foreground="white")
style.map("Treeview", background=[('selected', '#0078d7')])


tree = ttk.Treeview(app, height=15)

tree["columns"] = ("ID", "Name", "Role", "Gender", "Status")

tree.column("#0", width=0, stretch=customtkinter.NO)
tree.column("ID", anchor=customtkinter.W, width=100)
tree.column("Name", anchor=customtkinter.W, width=100)
tree.column("Role", anchor=customtkinter.W, width=100)
tree.column("Gender", anchor=customtkinter.W, width=100)
tree.column("Status", anchor=customtkinter.W, width=100)

tree.heading("#0", text="", anchor=customtkinter.W)
tree.heading("ID", text="ID", anchor=customtkinter.W)
tree.heading("Name", text="Name", anchor=customtkinter.W)
tree.heading("Role", text="Role", anchor=customtkinter.W)
tree.heading("Gender", text="Role", anchor=customtkinter.W)
tree.heading("Status", text="Role", anchor=customtkinter.W)

tree.place(x=400, y=50)

tree.bind("<ButtonRelease-1>", display_data)

add_to_treeview()


# Run the application
app.mainloop()
