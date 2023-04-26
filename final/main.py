global tk
global pd
global login_csv_path
global data_csv_path
import tkinter as tk
import pandas as pd

login_csv_path = "E://loginid.csv"
data_csv_path = "E://python project//bed_vacancy_details.csv"


def register():
    global tk
    global pd

    window = tk.Tk()

    # setting the roots size
    window.geometry("600x400")
    window.configure(bg='#333333')
    name_var = tk.StringVar()
    passw_var = tk.StringVar()
    l1 = tk.Label(text="Hospital Login form-Raghav_K_12_E3")
    l1.place()

    def log():
        window.destroy()
        loggin()

    def submit():
        name = name_var.get()

        password = passw_var.get()

        print("The name is : " + name)

        print("The password is : " + password)
        name_var.set("")

        passw_var.set("")
        global login_csv_path
        df = pd.read_csv(login_csv_path)
        # check if username already exists
        if name in df['Username'].values:
            print("Username already exists")
            return
        # if username does not exist, add it to the csv file
        else:
            df.loc[len(df)] = [name, password]
        print(df)

        df.to_csv(login_csv_path, index=False)

    frame = tk.Frame(bg='#333333')
    register_label = tk.Label(frame, text="Register", bg='#333333', fg="#FF3399", font=("Arial", 30))

    name_label = tk.Label(frame, text='Enter your name', bg='#333333', fg="#FFFFFF", font=("Arial", 16))
    name_entry = tk.Entry(frame, textvariable=name_var, font=('Arial', 16))
    passw_label = tk.Label(frame, text='Password', bg='#333333', fg="#FFFFFF", font=('Arial', 16))
    passw_entry = tk.Entry(frame, textvariable=passw_var, font=('Arial', 16), show='*')

    sub_btn = tk.Button(frame, text='Submit', bg="#FF3399", fg="#FFFFFF", font=("Arial", 16), command=submit)
    login_btn = tk.Button(frame, text='Login', bg="#FF3399", fg="#FFFFFF", font=("Arial", 16), command=log)

    register_label.grid(row=0, column=0, columnspan=2, sticky="news", pady=40)
    name_label.grid(row=1, column=0)
    name_entry.grid(row=1, column=1, pady=20)

    passw_label.grid(row=3, column=0, pady=20)
    passw_entry.grid(row=3, column=1, pady=20)
    sub_btn.grid(row=4, column=0, columnspan=2, pady=30)
    login_btn.grid(row=4, column=2, columnspan=2, pady=30)

    # for the frame to display
    frame.pack()
    window.mainloop()


def loggin():
    global tk
    from tkinter import messagebox
    global pd

    window = tk.Tk()
    window.title("Hospital Login form Raghav_k_12_E3")
    window.geometry('600x400')
    window.configure(bg='#333333')
    global login_csv_path

    global df
    df = pd.read_csv(login_csv_path)
    df.set_index('Username', inplace=True)

    def login():
        if username_entry.get() in df.index:
            if str(df.loc[username_entry.get(), 'pwd']) == str(password_entry.get()):
                messagebox.showinfo("Login", "Login successful")
                window.destroy()
                page1()

            else:
                messagebox.showerror(title="Error", message="Invalid password.")
        else:
            messagebox.showerror(title="Error", message="Invalid login.")

    frame = tk.Frame(bg='#333333')

    # Creating widgets
    login_label = tk.Label(
        frame, text="Hospital Login", bg='#333333', fg="#FF3399", font=("Arial", 30))
    username_label = tk.Label(
        frame, text="Username", bg='#333333', fg="#FFFFFF", font=("Arial", 16))
    username_entry = tk.Entry(frame, font=("Arial", 16))
    password_entry = tk.Entry(frame, show="*", font=("Arial", 16))
    password_label = tk.Label(
        frame, text="Password", bg='#333333', fg="#FFFFFF", font=("Arial", 16))
    login_button = tk.Button(
        frame, text="Login", bg="#FF3399", fg="#FFFFFF", font=("Arial", 16), command=login)

    login_label.grid(row=0, column=0, columnspan=2, sticky="news", pady=40)
    username_label.grid(row=1, column=0)
    username_entry.grid(row=1, column=1, pady=20)
    password_label.grid(row=2, column=0)
    password_entry.grid(row=2, column=1, pady=20)
    login_button.grid(row=3, column=0, columnspan=2, pady=30)

    frame.pack()

    window.mainloop()


def page1():
    global tk
    from tkinter import messagebox

    window = tk.Tk()
    window.title("Hospital Login form Raghav_k_12_E3")
    window.geometry('600x400')
    window.configure(bg='#333333')

    def enter():
        messagebox.showinfo("Info", "in")
        window.destroy()
        entry()

    def out():
        messagebox.showinfo("Info", "out")
        window.destroy()
        exitt()

    def mpl():
        messagebox.showinfo("Info", "mpl")

        graph_plot()

    def exita():
        raise SystemExit

    frame = tk.Frame(bg='#333333')

    # Creating widgets
    title_label = tk.Label(
        frame, text="Welcome", bg='#333333', fg="#FF3399", font=("Arial", 30))
    in_btn = tk.Button(
        frame, text="Patient Incoming ", bg="#FF3399", fg="#FFFFFF", font=("Arial", 16), command=enter)
    out_btn = tk.Button(
        frame, text="Patient outgoing", bg="#FF3399", fg="#FFFFFF", font=("Arial", 16), command=out)
    mpl_btn = tk.Button(
        frame, text="Plot graph", bg="#FF3399", fg="#FFFFFF", font=("Arial", 16), command=mpl)
    exit_btn = tk.Button(
        frame, text="Exit", bg="#FF3399", fg="#FFFFFF", font=("Arial", 16), command=exita)

    title_label.grid(row=0, column=2, columnspan=2, sticky="news", pady=30)
    in_btn.grid(row=1, column=0, columnspan=2, pady=10)
    out_btn.grid(row=2, column=0, columnspan=2, pady=10)
    mpl_btn.grid(row=1, column=4, columnspan=2, pady=10)
    exit_btn.grid(row=2, column=4, columnspan=2, pady=10)

    frame.pack()

    window.mainloop()


def entry():
    global tk
    from tkinter import messagebox
    global pd

    window = tk.Tk()
    window.title("Hospital Login form Raghav_k_12_E3")
    window.geometry('600x400')
    window.configure(bg='#333333')
    global data_csv_path
    global data
    global place
    num_var = tk.IntVar()

    data = tk.StringVar()
    data.set('0')
    global d
    d = pd.read_csv(data_csv_path)
    d.set_index('Place', inplace=True)

    def chengalpattu():
        print("Chengalpattu")
        global data
        global place
        place = 'Chengalpattu'
        data.set(d.loc['Chengalpattu', 'Vacant'])

    def chennai():
        print("Chennai")
        global data
        global place
        place = 'Chennai'
        data.set(d.loc['Chennai', 'Vacant'])

    def coimbatore():
        print("Coimbatore")
        global data
        global place
        place = 'Coimbatore'
        data.set(d.loc['Coimbatore', 'Vacant'])

    def madurai():
        print("Madurai")
        global data
        global place
        place = 'Madurai'
        data.set(d.loc['Madurai', 'Vacant'])

    def salem():
        print("Salem")
        global data
        global place
        place = 'Salem'
        data.set(d.loc['Salem', 'Vacant'])

    def entry_sub():
        if data.get() == '0' or str(num_var.get()) == '0':
            messagebox.showerror(title="Error", message="Please select a place and enter number of beds")
        elif num_var.get() > int(data.get()):
            messagebox.showerror(title="Error",
                                 message="Please enter number of beds less than or equal to available beds")
        else:
            d.loc[place, 'Vacant'] = d.loc[place, 'Vacant'] - num_var.get()
            d.to_csv(data_csv_path)
            messagebox.showinfo(title="Success", message="Bed entry successful")
            window.destroy()
            page1()

    # Creating widgets
    entry_label = tk.Label(text="Entry Register page", bg='#333333', fg="#FF3399", font=("Arial", 20))

    Chengalpattu_rdo = tk.Radiobutton(text="Chengalpattu", bg='#333333', fg="#FFFFFF", font=("Arial", 16),
                                      variable=data, command=chengalpattu)
    Chennai_rdo = tk.Radiobutton(text="Chennai", bg='#333333', fg="#FFFFFF", font=("Arial", 16), variable=data,
                                 command=chennai)
    Madurai_rdo = tk.Radiobutton(text="Madurai", bg='#333333', fg="#FFFFFF", font=("Arial", 16), variable=data,
                                 command=madurai)
    Coimbatore_rdo = tk.Radiobutton(text="Coimbatore", bg='#333333', fg="#FFFFFF", font=("Arial", 16), variable=data,
                                    command=coimbatore)
    Salem_rdo = tk.Radiobutton(text="Salem", bg='#333333', fg="#FFFFFF", font=("Arial", 16), variable=data,
                               command=salem)

    label = tk.Label(window, textvariable=data, font=("Roboto", 20), bg='#333333', fg="#FF3399")
    count_ind = tk.Label(text="Vacant beds = ", bg='#333333', fg="#FF3399", font=("Roboto", 16))
    entry_button = tk.Button(text="Submit", bg="#FF3399", fg="#FFFFFF", font=("Arial", 16), command=entry_sub)
    num_entry = tk.Entry(textvariable=num_var, font=('Arial', 10))
    num_ind = tk.Label(text="No of beds required = ", bg='#333333', fg="#FF3399", font=("Roboto", 16))
    # Placing widgets on the screen

    Chengalpattu_rdo.grid(row=1, column=2, pady=20)
    Chennai_rdo.grid(row=1, column=1, pady=20)
    Madurai_rdo.grid(row=2, column=2, pady=20)
    Coimbatore_rdo.grid(row=2, column=1, pady=20)
    Salem_rdo.grid(row=3, column=1, pady=20)
    entry_label.grid(row=0, column=2, columnspan=2, sticky="news", pady=10)
    label.place(x=500, y=130)
    count_ind.place(x=350, y=135)
    num_ind.place(x=250, y=275)
    entry_button.grid(row=5, column=0, columnspan=2, pady=30)
    num_entry.grid(row=5, column=5, pady=10)

    window.mainloop()


def exitt():
    import tkinter as tk
    from tkinter import messagebox
    global pd
    window = tk.Tk()
    window.title("Hospital Login form Raghav_k_12_E3")
    window.geometry('600x400')
    window.configure(bg='#333333')
    global data_csv_path
    global data
    global place
    num_var = tk.IntVar()

    data = tk.StringVar()
    data.set('0')
    global d
    d = pd.read_csv(data_csv_path)
    d.set_index('Place', inplace=True)

    def chengalpattu():
        print("Chengalpattu")
        global data
        global place
        place = 'Chengalpattu'
        data.set(d.loc['Chengalpattu', 'Vacant'])

    def chennai():
        print("Chennai")
        global data
        global place
        place = 'Chennai'
        data.set(d.loc['Chennai', 'Vacant'])

    def coimbatore():
        print("Coimbatore")
        global data
        global place
        place = 'Coimbatore'
        data.set(d.loc['Coimbatore', 'Vacant'])

    def madurai():
        print("Madurai")
        global data
        global place
        place = 'Madurai'
        data.set(d.loc['Madurai', 'Vacant'])

    def salem():
        print("Salem")
        global data
        global place
        place = 'Salem'
        data.set(d.loc['Salem', 'Vacant'])

    def ext_sub():
        if data.get() == '0' or str(num_var.get()) == '0':
            messagebox.showerror(title="Error", message="Please select a place and enter number of beds")
        elif num_var.get() > int(data.get()):
            messagebox.showerror(title="Error",
                                 message="Please enter number of beds less than or equal to available beds")
        else:
            d.loc[place, 'Vacant'] = d.loc[place, 'Vacant'] + num_var.get()
            d.to_csv(data_csv_path)
            messagebox.showinfo(title="Success", message="Bed vacancy registered")
            window.destroy()
            page1()

    frame = tk.Frame(bg='#333333')

    # Creating widgets
    exit_label = tk.Label(text="Exit Register page", bg='#333333', fg="#FF3399", font=("Arial", 20))

    Chengalpattu_rdo = tk.Radiobutton(text="Chengalpattu", bg='#333333', fg="#FFFFFF", font=("Arial", 16),
                                      variable=data, command=chengalpattu)
    Chennai_rdo = tk.Radiobutton(text="Chennai", bg='#333333', fg="#FFFFFF", font=("Arial", 16), variable=data,
                                 command=chennai)
    Madurai_rdo = tk.Radiobutton(text="Madurai", bg='#333333', fg="#FFFFFF", font=("Arial", 16), variable=data,
                                 command=madurai)
    Coimbatore_rdo = tk.Radiobutton(text="Coimbatore", bg='#333333', fg="#FFFFFF", font=("Arial", 16), variable=data,
                                    command=coimbatore)
    Salem_rdo = tk.Radiobutton(text="Salem", bg='#333333', fg="#FFFFFF", font=("Arial", 16), variable=data,
                               command=salem)

    label = tk.Label(window, textvariable=data, font=("Roboto", 20), bg='#333333', fg="#FF3399")
    count_ind = tk.Label(text="Vacant beds = ", bg='#333333', fg="#FF3399", font=("Roboto", 16))
    exit_button = tk.Button(text="Submit", bg="#FF3399", fg="#FFFFFF", font=("Arial", 16), command=ext_sub)
    num_exit = tk.Entry(textvariable=num_var, font=('Arial', 10))
    num_ind = tk.Label(text="No of beds freed = ", bg='#333333', fg="#FF3399", font=("Roboto", 16))

    Chengalpattu_rdo.grid(row=1, column=2, pady=20)
    Chennai_rdo.grid(row=1, column=1, pady=20)
    Madurai_rdo.grid(row=2, column=2, pady=20)
    Coimbatore_rdo.grid(row=2, column=1, pady=20)
    Salem_rdo.grid(row=3, column=1, pady=20)
    exit_label.grid(row=0, column=2, columnspan=2, sticky="news", pady=10)
    label.place(x=500, y=130)
    count_ind.place(x=350, y=135)
    num_ind.place(x=250, y=275)
    exit_button.grid(row=5, column=0, columnspan=2, pady=30)
    num_exit.grid(row=5, column=5, pady=10)

    window.mainloop()


def graph_plot():
    # matplotlib area graph of vacant bed to occupied bed
    import matplotlib.pyplot as plt
    global pd
    global data_csv_path
    d = pd.read_csv(data_csv_path)
    d.set_index('Place', inplace=True)
    print(d)
    d.plot(kind='area', stacked=True, figsize=(10, 5))

    plt.title('Number of available beds in each place and total number of beds')
    plt.ylabel('Number of beds')
    plt.xlabel('Place')

    plt.show()


if __name__ == '__main__':
    register()
