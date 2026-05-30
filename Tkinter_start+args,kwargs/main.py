from tkinter import *


def button_clicked():
    my_label["text"] = "I got clicked"
    new_text = input.get()
    my_label.config(text = new_text)
    #or my_label.config(text="I got clicked") both works

window = Tk()
window.title("My first GUI program")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

# Creating a label
my_label = Label(text= "This is a label", font = ("Arial", 24, "bold"))
my_label.grid(row = 0, column= 0)

#Button
button = Button(text = "Button", command=button_clicked)
button.grid(row=0, column=2)

new_button = Button(text = "new Button",)
new_button.grid(row=2, column=1)

# Entry
input = Entry(width = 10)
print(input.get())
input.grid(row = 3, column = 3)




window.mainloop()