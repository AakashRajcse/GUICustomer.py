
from tkinter import *

def addCustomerHandler():
    id = var_id.get()
    name = var_name.get()
    age = var_age.get()
    mob = var_mob.get()
    print(id, name, age, mob)

root = Tk()
root.geometry("500x400")

# Labels
lblId = Label(root, text="Enter Your Id", font=1)
lblId.grid(row=0, column=0, padx=20, pady=10)

lblName = Label(root, text="Enter Your Name", font=1)
lblName.grid(row=1, column=0, padx=20, pady=10)

lblAge = Label(root, text="Enter Your Age", font=1)
lblAge.grid(row=2, column=0, padx=20, pady=10)

lblMob = Label(root, text="Enter Your Mobile", font=1)
lblMob.grid(row=3, column=0, padx=20, pady=10)

# Entry Variables
var_id = IntVar()
entry_id = Entry(root, font=1, textvariable=var_id)
entry_id.grid(row=0, column=1)

var_name = StringVar()
entry_name = Entry(root, font=1, textvariable=var_name)
entry_name.grid(row=1, column=1)

var_age = IntVar()
entry_age = Entry(root, font=1, textvariable=var_age)
entry_age.grid(row=2, column=1)

var_mob = StringVar()  # Change to StringVar for mobile numbers
entry_mob = Entry(root, font=1, textvariable=var_mob)
entry_mob.grid(row=3, column=1)

# Button
btn_addCustomer = Button(root, text="Add Cust", font=1, command=addCustomerHandler)
btn_addCustomer.grid(row=4, column=1, pady=20)

root.mainloop()
