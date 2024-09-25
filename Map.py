from tkinter import *
import tkintermapview

window = Tk()

window.title("Testing Map")

label = LabelFrame(window)
label.pack(pady = 20)

map_widget = tkintermapview.TkinterMapView(label, width= 3840, height = 2160 , corner_radius=0)
map_widget.set_position(12.969938, 79.1556)
map_widget.set_tile_server("https://mt0.google.com/vt/Lyrs=m&hl=en&x={x}&y={y}&z={z}&s=Ga", max_zoom=22)

map_widget.pack()

window.mainloop()
