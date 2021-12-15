# Grace Foster
# ITP 100-01
# Program 2 - Shell
# shell.py
# -------------------------------------------------

from tkinter import *
from tkinter import ttk

rootWindow = Tk()
rootWindow.columnconfigure(0, minsize=50)
rootWindow.rowconfigure(0, minsize=50)


def hello():
    global label
    label.config(text="Hello World!")


def bye():
    global label
    label.config(text="Goodbye World!")


def main():
    global label
    label = ttk.Label(rootWindow, text="Hello World!")
    label.grid(row=0, column=0)

    button1 = ttk.Button(rootWindow, text="Hello!", command=hello, )
    button2 = ttk.Button(rootWindow, text="Bye!", command=bye, )
    button1.grid(row=0, column=1)
    button2.grid(row=0, column=2)

    rootWindow.mainloop()


main()
