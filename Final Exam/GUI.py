# Grace Foster
# ITP 100-01
# Program 03 - GUI
# GUI.py
# -------------------------------------------------
from tkinter import *
from tkinter import ttk

class GUI:

    def __init__(self, rootWindow):
        self.buttonsEnabled = IntVar()
        self.buttonsEnabled.set(1)
        self.label = ttk.Checkbutton(rootWindow, text="Enable", variable=self.buttonsEnabled)
        self.label.grid(row=1, column=0)

        self.label = ttk.Label(rootWindow, text="Title Editor")
        '''self.label = ttk.Label(rootWindow, text="Hello World!")'''
        self.label.grid(row=0, column=0)

        self.text = Text(rootWindow, width=80, height=30, background="yellow")
        self.text.grid(row=1, column=0, columnspan=4)

        self.button1 = ttk.Button(rootWindow, text="Clear", command=self.clear)
        '''self.button1 = ttk.Button(rootWindow, text="Hello", command=self.hello)'''
        self.button1.grid(row=0, column=1)
        self.button2 = ttk.Button(rootWindow, text="Bye", command=self.bye)
        self.button2.grid(row=0, column=2)

    '''def bye(self):
        if self.buttonsEnabled.get() >= 1:
            self.label.config(text="Goodbye World!")'''

    '''def hello(self):
        if self.buttonsEnabled.get() >= 1:
            self.label.config(text="Hello World!")'''

    def bye(self):
        exit()

    def clear(self):
        self.text.delete(1.0, END)


def main():
    global label
    rootWindow = Tk()

    gui = GUI(rootWindow)
    rootWindow.mainloop()


main()
