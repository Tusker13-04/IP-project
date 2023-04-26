import tkinter
from tkinter import messagebox
import pandas as pd

window = tkinter.Tk()
window.title("Hospital Login form Raghav_k_12_E3")
window.geometry('600x400')
window.configure(bg='#333333')
# Change the below path to that of your csv file
x = pd.read_csv("E://loginid.csv")

global d
d = pd.DataFrame(x)
d.set_index('Username', inplace=True)


def login():
    if username_entry.get() in d.index:
        if str(d.loc[username_entry.get(), 'pwd']) == str(password_entry.get()):
            messagebox.showinfo("Login", "Login successful")
            window.destroy()
            import page1

        else:
            messagebox.showerror(title="Error", message="Invalid password.")
    else:
        messagebox.showerror(title="Error", message="Invalid login.")


frame = tkinter.Frame(bg='#333333')

# Creating widgets
login_label = tkinter.Label(
    frame, text="Hospital Login", bg='#333333', fg="#FF3399", font=("Arial", 30))
username_label = tkinter.Label(
    frame, text="Username", bg='#333333', fg="#FFFFFF", font=("Arial", 16))
username_entry = tkinter.Entry(frame, font=("Arial", 16))
password_entry = tkinter.Entry(frame, show="*", font=("Arial", 16))
password_label = tkinter.Label(
    frame, text="Password", bg='#333333', fg="#FFFFFF", font=("Arial", 16))
login_button = tkinter.Button(
    frame, text="Login", bg="#FF3399", fg="#FFFFFF", font=("Arial", 16), command=login)

# Placing widgets on the screen
login_label.grid(row=0, column=0, columnspan=2, sticky="news", pady=40)
username_label.grid(row=1, column=0)
username_entry.grid(row=1, column=1, pady=20)
password_label.grid(row=2, column=0)
password_entry.grid(row=2, column=1, pady=20)
login_button.grid(row=3, column=0, columnspan=2, pady=30)

frame.pack()

window.mainloop()
