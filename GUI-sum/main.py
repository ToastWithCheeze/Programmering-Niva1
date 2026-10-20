import tkinter as tk

def button_clicked():
    print("Button Clicked")
    top = tk.Toplevel()
    secondlabel = tk.Label(top, text="Muhehe")
    secondlabel.pack()
window = tk.Tk()

label = tk.Label(window, text="Muhehe")
label.pack()

button = tk.Button(window, text="Click Me", width=25, command=button_clicked)
button.pack()

window.mainloop()