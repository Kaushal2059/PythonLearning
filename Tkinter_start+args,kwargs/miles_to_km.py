from tkinter import *

window = Tk()
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)
window.title("Miles to km converter")

def convert():
    a = int(input.get())
    mile = a*1.60934
    label3.config(text = int(mile))


label1= Label(text= "Miles", font = ("Arial", 14))
label1.grid(row=0, column=2)

label2= Label(text= "is equal to", font = ("Arial", 14))
label2.grid(row=1, column=0)

label3= Label(text= "0", font = ("Arial", 14, "bold"))
label3.grid(row=1, column=1)

input = Entry(width = 10)
input.grid(row = 0, column = 1)

label4 =Label(text= "Km", font = ("Arial", 14))
label4.grid(row=1, column=2)

button = Button(text="Calculate", command=convert)
button.grid(row=2, column=1)


window.mainloop()