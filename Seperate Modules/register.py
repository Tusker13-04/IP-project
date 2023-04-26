import tkinter as tk
import pandas as pd

root = tk.Tk()

# setting the roots size
root.geometry("600x400")
root.configure(bg='#333333')
# change the below path to your csv file
login_csv_path = "E://loginid.csv"
name_var = tk.StringVar()
passw_var = tk.StringVar()
l1 = tk.Label(text="Hospital Login form-Raghav_K_12_E3")
l1.place()


# defining a function that will
# get the name and password and
# print them on the screen
def log():
    root.destroy()
    import login


def submit():
    name = name_var.get()

    password = passw_var.get()

    print("The name is : " + name)

    print("The password is : " + password)
    name_var.set("")

    passw_var.set("")

    df = pd.read_csv(login_csv_path)
    df.loc[len(df)] = [name, password]
    print(df)
    # x = len(df.axes) - 1
    # df.loc[x, 'Username'] = name
    # df.loc['pwd'] = password
    df.to_csv(login_csv_path, index=False)


frame = tk.Frame(bg='#333333')
# creating a label for
# name using widget Label
register_label = tk.Label(
    frame, text="Register", bg='#333333', fg="#FF3399", font=("Arial", 30))

name_label = tk.Label(frame, text='Enter your name', bg='#333333', fg="#FFFFFF", font=("Arial", 10))

# creating a entry for input
# name using widget Entry
name_entry = tk.Entry(frame, textvariable=name_var, font=('Arial', 10))

# creating a label for password
passw_label = tk.Label(frame, text='Password', bg='#333333', fg="#FFFFFF", font=('Arial', 10))

# creating a entry for password
passw_entry = tk.Entry(frame, textvariable=passw_var, font=('Arial', 10), show='*')

# creating a button using the widget
# Button that will call the submit function
sub_btn = tk.Button(frame, text='Submit', bg="#FF3399", fg="#FFFFFF", font=("Arial", 16), command=submit)
login_btn = tk.Button(frame, text='Login', bg="#FF3399", fg="#FFFFFF", font=("Arial", 16), command=log)

# placing the label and entry in
# the required position using grid
# method
register_label.grid(row=0, column=0, columnspan=2, sticky="news", pady=40)
name_label.grid(row=1, column=0)
name_entry.grid(row=1, column=1, pady=20)

passw_label.grid(row=3, column=0, pady=20)
passw_entry.grid(row=3, column=1, pady=20)
sub_btn.grid(row=4, column=0, columnspan=2, pady=30)
login_btn.grid(row=4, column=2, columnspan=2, pady=30)
# performing an infinite loop
# for the frame to display
frame.pack()
root.mainloop()
