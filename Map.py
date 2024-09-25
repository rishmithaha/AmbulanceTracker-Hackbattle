import customtkinter
import tkintermapview
from PIL import Image, ImageTk

window = customtkinter.CTk()

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("green")

frame = customtkinter.CTkFrame(window)
frame.pack(pady=20, fill="both", expand=True)

map_widget = tkintermapview.TkinterMapView(frame, width=800, height=600, corner_radius=0)
map_widget.set_position(12.992840, 79.152810, marker = True, text="Current location")
map_widget.set_tile_server("https://mt0.google.com/vt/Lyrs=m&hl=en&x={x}&y={y}&z={z}&s=Ga", max_zoom=22)

map_widget.pack(fill="both", expand=True)

ambulance_image = Image.open("ambulance.png")
ambulance_image = ambulance_image.resize((30, 30))
ambulance_icon = ImageTk.PhotoImage(ambulance_image)

ambulance_statuses = ["Available", "Available", "Available", "Available"]

ambulance_1 = map_widget.set_marker(12.992840, 79.152810, text=f"Ambulance 1: {ambulance_statuses[0]}",
                                    icon=ambulance_icon)
ambulance_2 = map_widget.set_marker(12.943470, 79.158540, text=f"Ambulance 2: {ambulance_statuses[1]}",
                                    icon=ambulance_icon)
ambulance_3 = map_widget.set_marker(12.965500, 79.158000, text=f"Ambulance 3: {ambulance_statuses[2]}",
                                    icon=ambulance_icon)
ambulance_4 = map_widget.set_marker(12.923340, 79.140970, text=f"Ambulance 4: {ambulance_statuses[3]}",
                                    icon=ambulance_icon)

path1 = map_widget.set_path([(12.992840, 79.152810), (12.943470, 79.158540)])

def update_ambulance_status(ambulance_number):
    global ambulance_statuses
  
    if ambulance_statuses[ambulance_number] == "Available":
        ambulance_statuses[ambulance_number] = "Busy"
    else:
        ambulance_statuses[ambulance_number] = "Available"
      
    if ambulance_number == 0:
        ambulance_1.set_text(f"Ambulance 1: {ambulance_statuses[0]}")
    elif ambulance_number == 1:
        ambulance_2.set_text(f"Ambulance 2: {ambulance_statuses[1]}")
    elif ambulance_number == 2:
        ambulance_3.set_text(f"Ambulance 3: {ambulance_statuses[2]}")
    elif ambulance_number == 3:
        ambulance_4.set_text(f"Ambulance 4: {ambulance_statuses[3]}")

    print(f"Ambulance {ambulance_number + 1} status updated to: {ambulance_statuses[ambulance_number]}")

button_ambulance_1 = customtkinter.CTkButton(master=window, text="Ambulance 1 Status",
                                             command=lambda: update_ambulance_status(0))
button_ambulance_1.place(relx=0.2, rely=0.9, anchor=customtkinter.CENTER)

button_ambulance_2 = customtkinter.CTkButton(master=window, text="Ambulance 2 Status",
                                             command=lambda: update_ambulance_status(1))
button_ambulance_2.place(relx=0.4, rely=0.9, anchor=customtkinter.CENTER)

button_ambulance_3 = customtkinter.CTkButton(master=window, text="Ambulance 3 Status",
                                             command=lambda: update_ambulance_status(2))
button_ambulance_3.place(relx=0.6, rely=0.9, anchor=customtkinter.CENTER)

button_ambulance_4 = customtkinter.CTkButton(master=window, text="Ambulance 4 Status",
                                             command=lambda: update_ambulance_status(3))
button_ambulance_4.place(relx=0.8, rely=0.9, anchor=customtkinter.CENTER)

window.mainloop()
