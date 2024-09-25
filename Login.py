import customtkinter as ctk
from tkinter import messagebox
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="rishmi@123",
    database="Ambulance"
)

mycursor = mydb.cursor()

ctk.set_appearance_mode("System")  # Modes: "System" (default), "Dark", "Light"
ctk.set_default_color_theme("green")  # Themes: "blue" (default), "dark-blue", "green"

def login_window():
    
    login = ctk.CTkToplevel()  # Use CTkToplevel for windows
    login.title("Welcome Back")
    login.geometry("300x200")
    login.resizable(0, 0)  

    name_label = ctk.CTkLabel(login, text="Name")
    name_label.place(x=50, y=10)
    name_entry = ctk.CTkEntry(login)
    name_entry.place(x=50, y=40)

    phoneno_label = ctk.CTkLabel(login, text="Phone Number")
    phoneno_label.place(x=50, y=80)
    phoneno_entry = ctk.CTkEntry(login)
    phoneno_entry.place(x=50, y=110)
    
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

    login_button = ctk.CTkButton(login, text="Login", command=check_credentials)
    login_button.place(x=110, y=160)

def registration_window():
    registration = ctk.CTkToplevel()
    registration.title("Welcome to Ambulance Tracker")
    registration.geometry("300x200")
    registration.resizable(0, 0)  

    name_label = ctk.CTkLabel(registration, text="Name")
    name_label.place(x=50, y=10)
    name_entry = ctk.CTkEntry(registration)
    name_entry.place(x=50, y=40)

    phoneno_label = ctk.CTkLabel(registration, text="Phone Number")
    phoneno_label.place(x=50, y=80)
    phoneno_entry = ctk.CTkEntry(registration)
    phoneno_entry.place(x=50, y=110)

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

    register_button = ctk.CTkButton(registration, text="Register", command=add_user)
    register_button.place(x=110, y=160)

root = ctk.CTk()  # Use CTk instead of Tk
root.title("Login")
root.geometry("300x200")
root.resizable(0, 0)

login_button = ctk.CTkButton(root, text="Login", command=login_window)
login_button.place(x=85, y=50)

register_button = ctk.CTkButton(root, text="Register", command=registration_window)
register_button.place(x=85, y=110)

root.mainloop()
