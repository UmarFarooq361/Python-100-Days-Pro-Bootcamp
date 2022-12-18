from tkinter import *

window = Tk()
window.minsize(width=250 , height= 170)
window.title( "Miles to Kilometers")
window.config(padx= 20 , pady= 20)

meter_label = Label(text= "Meter", font= ("arial", 16))
meter_label.grid(column=2, row=0)

equal_to_label = Label(text= "is equal to", font= ("arial", 16))
equal_to_label.grid(column=0, row=1)

km_label = Label(text= "0", font= ("arial", 16), background="#f3f2ff")
km_label.grid(column=1, row=1)

kilometer= Label(text= "Kilometers", font= ("arial", 16))
kilometer.grid(column=2, row=1)

def miles_to_kilometer():
    miles = float(input.get())
    kilometers = round(miles * 1.609)
    km_label.config(text=f"{kilometers}")

converter_btn = Button(text= "Convert" , command= miles_to_kilometer)
converter_btn.grid(column=1, row=2)
converter_btn.config(pady= 7, padx=10 )

input = Entry(width=8)
input.grid(column=1, row=0)







window.mainloop()