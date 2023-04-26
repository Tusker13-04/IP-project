import matplotlib.pyplot as pyplot
import pandas as pd
import tkinter


def on_close(event):
    print("closing")
    import page1
    page1.frame.pack()
    page1.window.mainloop()


# code to plot area graph of number of available beds in each place and total number of beds
data_csv_path = "E://python project//bed_vacancy_details.csv"
x = pd.read_csv(data_csv_path)
d = pd.DataFrame(x)
d.set_index('Place', inplace=True)
print(d)
d.plot(kind='area', stacked=True, figsize=(10, 5))

pyplot.title('Number of available beds in each place and total number of beds')
pyplot.ylabel('Number of beds')
pyplot.xlabel('Place')

pyplot.show()
fig = pyplot.gcf()
fig.canvas.mpl_connect('close_event', on_close)
