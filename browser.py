import webbrowser
from tkinter import *

root =Tk()
root.geometry('400x200')
root.title('ibr20100')
root.resizable(False,False)
root.config(background='#4C4646')

#====== انشاء ادالة ======
def search():
    t=e.get()
    webbrowser.open(t)
#=========
lb1 = Label(root,text='Web Browser',fg='white',bg='black',font=('Courier',12,'bold'))
lb1.pack(fill=X)

e =Entry(root, width=60,fg='red',font='bold')
e.pack()

btn=Button(root,text='Search',activebackground='black',activeforeground='white',fg='green' ,font=('Courier',14,'bold'),command=search)
btn.pack()
root.mainloop()


