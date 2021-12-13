# Grace Foster
# ITP 100-01
# EXERCISE: 11
# NAgf.py
# ----------------------------------------------------------------
import tkinter as tk

main_window = tk.Tk()
main_window.title("My Name and Address")
top_frame = tk.Frame()
mid_frame = tk.Frame()
bottom_frame = tk.Frame()

name = tk.Label(top_frame, width=55)
name.pack()

address1 = tk.Label(mid_frame, width=0)
address1.pack()

address2 = tk.Label(mid_frame, width=0)
address2.pack()


def name_address():
    name.config(text="Grace Foster")
    address1.config(text="2624 Alabama Ave")
    address2.config(text="Lynchburg, VA 24502")


def quitCallBack():
    exit()


Button1 = tk.Button(bottom_frame, text="Show Info", command=name_address,)
Button2 = tk.Button(bottom_frame, text="Quit", command=quitCallBack)

Button1.pack(side='left', pady=15)
Button2.pack(side='left', pady=5, padx=15)

top_frame.pack()
mid_frame.pack()
bottom_frame.pack()

main_window.mainloop()
