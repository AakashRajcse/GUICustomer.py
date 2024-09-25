from googletrans import Translator
from tkinter import*
def handler_hindi(e):
    res = t.translate("Good Morning", dest="Hi")  # 'hi' is the code for Hindi
    src_data=var.get()
    data = res.text
    lbl_dest=Label(root,text=data,font=1)
    lbl_dest.grid(row=2,column=1)
root=Tk()
root.geometry("500x400")
t = Translator()
lblSrc=Label(root,text="Enter Your Text",font=1)
lblSrc.grid(row=0,column=0)
var=StringVar()
entr1=Entry(root,textvariable=var,font=1)
entr1.grid(row=0,column=0)
btnHi=Button(root,text="Convert Hindi",font=1)
btnHi.bind("<Button>",handler_hindi)
btnHi.grid(row=1,column=1)



# Correctly specifying the destination language code
res=t.translate("Good Morning", dest="Hi")  # 'hi' is the code for Hindi

data = res.text
print(data)
root.mainloop()
