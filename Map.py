import customtkinter
import tkintermapview

# Create the main window using customtkinter
window = customtkinter.CTk()

# Set appearance mode and color theme for customtkinter
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("green")

# Create a frame for the map widget
frame = customtkinter.CTkFrame(window)
frame.pack(pady=20, fill="both", expand=True)

# Add the map widget to the frame
map_widget = tkintermapview.TkinterMapView(frame, width=800, height=600, corner_radius=0)
map_widget.set_position(12.969938, 79.1556)  # Vellore's coordinates
map_widget.set_tile_server("https://mt0.google.com/vt/Lyrs=m&hl=en&x={x}&y={y}&z={z}&s=Ga", max_zoom=22)

# Pack the map widget inside the frame
map_widget.pack(fill="both", expand=True)

# Define a button action
def button():
    print("Button pressed")

# Add a button using customtkinter
button = customtkinter.CTkButton(master=window, text="Testing", command=button)
button.place(relx=0.5, rely=0.9, anchor=customtkinter.CENTER)

# Start the main event loop
window.mainloop()
