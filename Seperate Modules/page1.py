import tkinter
from tkinter import messagebox

window = tkinter.Tk()
window.title("Hospital Login form Raghav_k_12_E3")
window.geometry('600x400')
window.configure(bg='#333333')


def enter():
    messagebox.showinfo("Info", "in")
    window.destroy()
    import entry


def out():
    messagebox.showinfo("Info", "out")
    window.destroy()
    import exit


def mpl():
    messagebox.showinfo("Info", "mpl")
    window.destroy()
    import graph_plot


def exit():
    raise SystemExit


frame = tkinter.Frame(bg='#333333')

# Creating widgets
title_label = tkinter.Label(
    frame, text="Welcome", bg='#333333', fg="#FF3399", font=("Arial", 30))
in_btn = tkinter.Button(
    frame, text="Patient Incoming ", bg="#FF3399", fg="#FFFFFF", font=("Arial", 16), command=enter)
out_btn = tkinter.Button(
    frame, text="Patient outgoing", bg="#FF3399", fg="#FFFFFF", font=("Arial", 16), command=out)
mpl_btn = tkinter.Button(
    frame, text="Plot graph", bg="#FF3399", fg="#FFFFFF", font=("Arial", 16), command=mpl)
exit_btn = tkinter.Button(
    frame, text="Exit", bg="#FF3399", fg="#FFFFFF", font=("Arial", 16), command=exit)

# Placing widgets on the screen
title_label.grid(row=0, column=2, columnspan=2, sticky="news", pady=30)
in_btn.grid(row=1, column=0, columnspan=2, pady=10)

out_btn.grid(row=2, column=0, columnspan=2, pady=10)
mpl_btn.grid(row=1, column=4, columnspan=2, pady=10)
exit_btn.grid(row=2, column=4, columnspan=2, pady=10)

frame.pack()

window.mainloop()
