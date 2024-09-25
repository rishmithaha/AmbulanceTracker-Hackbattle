import tkinter as tk
from tkinter import messagebox
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="rishmi@123",
    database="Ambulance"
)

mycursor = mydb.cursor()

def login_window():
    login = tk.Toplevel()
    login.title("Welcome Back")
    login.geometry("300x200")
    login.config(bg="#4876FF")
    login.resizable(0, 0)  

    name_label = tk.Label(login, text="Name", fg="black")
    name_label.place(x=50, y=20)
    name_entry = tk.Entry(login)
    name_entry.place(x=50, y=50)

    phoneno_label = tk.Label(login, text="Phone Number", fg="black")
    phoneno_label.place(x=50, y=90)
    phoneno_entry = tk.Entry(login)
    phoneno_entry.place(x=50, y=120)

    def check_credentials():
        name = name_entry.get()
        phoneno = phoneno_entry.get()

        try:
            mycursor.execute("SELECT * FROM details WHERE name=%s AND phoneno=%s", (name, phoneno))
            user = mycursor.fetchall()

            if user:
                login.destroy()
                messagebox.showinfo("Success", "User Login Successful!")
            else:
                messagebox.showerror("Error", "Invalid Name or Phone Number.")
        except mysql.connector.Error as err:
            messagebox.showerror("Database Error", str(err))

    login_button = tk.Button(login, text="Login", command=check_credentials, fg="black")
    login_button.place(x=110, y=160)

def registration_window():
    registration = tk.Toplevel()
    registration.title("Welcome to Ambulance Tracker")
    registration.geometry("300x200")
    registration.config(bg="#EEEE00")
    registration.resizable(0, 0)  

    name_label = tk.Label(registration, text="Name", fg="black")
    name_label.place(x=50, y=20)
    name_entry = tk.Entry(registration)
    name_entry.place(x=50, y=50)

    phoneno_label = tk.Label(registration, text="Phone Number", fg="black")
    phoneno_label.place(x=50, y=90)
    phoneno_entry = tk.Entry(registration)
    phoneno_entry.place(x=50, y=120)

    def add_user():
        name = name_entry.get()
        phoneno = phoneno_entry.get()

        try:
            mycursor.execute("INSERT INTO details (name, phoneno) VALUES (%s, %s)", (name, phoneno))
            mydb.commit()

            registration.destroy()
            messagebox.showinfo("Success", "User Registered Successfully!")
        except mysql.connector.Error as err:
            messagebox.showerror("Database Error", str(err))

    register_button = tk.Button(registration, text="Register", command=add_user)
    register_button.place(x=110, y=160)

root = tk.Tk()
root.title("Login")
root.geometry("300x200")
root.config(bg="#43CD80")
root.resizable(0, 0)

login_button = tk.Button(root, text="Login", command=login_window)
login_button.place(x=125, y=50)

register_button = tk.Button(root, text="Register", command=registration_window)
register_button.place(x=120, y=110)

root.mainloop()
