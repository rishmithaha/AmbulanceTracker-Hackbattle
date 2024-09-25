from tkinter import *
import customtkinter
import tkintermapview

welcome = Tk()
click = Button(welcome, text = "Welcome to the ambulance tracker!")

window = customtkinter.CTk()

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("green")

frame = customtkinter.CTkFrame(window)
frame.pack(pady=20, fill="both", expand=True)

map_widget = tkintermapview.TkinterMapView(frame, width=800, height=600, corner_radius=0)
map_widget.set_position(12.969938, 79.1556, marker=True)
map_widget.set_tile_server("https://mt0.google.com/vt/Lyrs=m&hl=en&x={x}&y={y}&z={z}&s=Ga", max_zoom=22)

map_widget.pack(fill="both", expand=True)

book = customtkinter.CTkButton(master=window, text="Book", corner_radius= 0,height=30)
book.place(relx=0.95, rely=0.5, anchor=customtkinter.E)

window.mainloop()
