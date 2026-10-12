import tkinter as tk
window = tk.Tk()
frame = tk.Frame(master=window, width=200, height=100, bg="#18354C")
frame.pack()
label = tk.Label(master=frame, text="Hola mundo")
label.place(x=50, y=30)

input("")