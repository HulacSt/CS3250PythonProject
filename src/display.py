from tkinter import *
import tkinter as tk


def helloWorld(str):
    root = Tk()
    var = StringVar()
    label = Message(root, textvariable=var)  # relief=RAISED
    window_text = label.cget("text")
    var.set(str)

    root.geometry("100x50")

    button = tk.Button(text="Click and Quit", command=root.quit)
    button.pack()

    label.pack()
    root.mainloop()
    return window_text
