import tkinter
from tkinter import messagebox
import pandas as pd

window = tkinter.Tk()
window.title("Hospital Login form Raghav_k_12_E3")
window.geometry('600x400')
window.configure(bg='#333333')
# Change the below path to the path of your csv file
data_csv_path = "E://python project//bed_vacancy_details.csv"
x = pd.read_csv(data_csv_path)
global data
global place
num_var = tkinter.IntVar()

data = tkinter.StringVar()
data.set('0')
global d
d = pd.DataFrame(x)
d.set_index('Place', inplace=True)
print(d.loc['Chengalpattu', 'Vacant'])


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


def entry():
    if data.get() == '0' or str(num_var.get()) == '0':
        messagebox.showerror(title="Error", message="Please select a place and enter number of beds")
    elif num_var.get() > int(data.get()):
        messagebox.showerror(title="Error", message="Please enter number of beds less than or equal to available beds")
    else:
        d.loc[place, 'Vacant'] = d.loc[place, 'Vacant'] - num_var.get()
        d.to_csv(data_csv_path)
        messagebox.showinfo(title="Success", message="Bed entry successful")
        window.destroy()
        import  page1


frame = tkinter.Frame(bg='#333333')

# Creating widgets
entry_label = tkinter.Label(text="Entry Register page", bg='#333333', fg="#FF3399", font=("Arial", 20))

Chengalpattu_rdo = tkinter.Radiobutton(text="Chengalpattu", bg='#333333', fg="#FFFFFF", font=("Arial", 16),
                                       variable=data, command=chengalpattu)
Chennai_rdo = tkinter.Radiobutton(text="Chennai", bg='#333333', fg="#FFFFFF", font=("Arial", 16), variable=data,
                                  command=chennai)
Madurai_rdo = tkinter.Radiobutton(text="Madurai", bg='#333333', fg="#FFFFFF", font=("Arial", 16), variable=data,
                                  command=madurai)
Coimbatore_rdo = tkinter.Radiobutton(text="Coimbatore", bg='#333333', fg="#FFFFFF", font=("Arial", 16), variable=data,
                                     command=coimbatore)
Salem_rdo = tkinter.Radiobutton(text="Salem", bg='#333333', fg="#FFFFFF", font=("Arial", 16), variable=data,
                                command=salem)

label = tkinter.Label(window, textvariable=data, font=("Roboto", 20), bg='#333333', fg="#FF3399")
count_ind = tkinter.Label(text="Vacant beds = ", bg='#333333', fg="#FF3399", font=("Roboto", 16))
entry_button = tkinter.Button(text="Submit", bg="#FF3399", fg="#FFFFFF", font=("Arial", 16), command=entry)
num_entry = tkinter.Entry(textvariable=num_var, font=('Arial', 10))
num_ind = tkinter.Label(text="No of beds required = ", bg='#333333', fg="#FF3399", font=("Roboto", 16))
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
