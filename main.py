from tkinter import *

def miles_to_km():
    miles = float(input_entry.get())
    km = miles * 1.609
    result_label.config(text=f"{km}")


window = Tk()
window.title("Miles to Km Converter")
window.minsize(width=500, height=300)
window.config(padx=100, pady=50)

input_entry = Entry(width=7)
input_entry.grid(column=1, row=0)

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

is_to_label = Label(text="is equal to")
is_to_label.grid(column=0, row=1)

result_label = Label(text="0")
result_label.grid(column=1, row=1)

km_label = Label(text="Km")
km_label.grid(column=2, row=1)

button =Button(text="Calculate", command=miles_to_km)
button.grid(column=1, row=2)





window.mainloop()