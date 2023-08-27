from tkinter import *
from tkinter.messagebox import *
import sqlite3
conn = sqlite3.connect("bus_reservation_211b420.db")

root=Tk()
(h,w)=root.winfo_screenwidth(),root.winfo_screenheight()
root.geometry('%dx%d+0+0'%(h,w))
bus= PhotoImage(file='.\\Bus_for_project.png')
Label(root,image=bus).grid(column=0,row=0,columnspan=10,padx=w/2)
Label(root,text='Online Bus Booking System',bg='lightblue',fg='red',font='Arial 20 bold').grid(row=1,column=0,pady=20,padx=w/2,columnspan=10)
Label(root,text='Add Bus Operator Details',fg='green',font='Arial 14 bold').grid(row=2,column=0,padx=w/2,columnspan=10,pady=30)
Label(root,text='Operator id',fg='black',font='Arial 10 bold').grid(row=3,column=0,padx=10,pady=30)
o=Entry(root)
o.grid(row=3,column=1)
Label(root,text='Name',fg='black',font='Arial 10 bold').grid(row=3,column=2,padx=10,pady=30)
n=Entry(root)
n.grid(row=3,column=3)
Label(root,text='Address',fg='black',font='Arial 10 bold').grid(row=3,column=4,padx=10,pady=30)
a=Entry(root)
a.grid(row=3,column=5)
Label(root,text='Phone',fg='black',font='Arial 10 bold').grid(row=3,column=6,padx=10,pady=30)
p=Entry(root)
p.grid(row=3,column=7)
Label(root,text='Email',fg='black',font='Arial 10 bold').grid(row=3,column=8,padx=10,pady=30)
e=Entry(root)
e.grid(row=3,column=9)
def pop():
    if len(o.get())==0 or len(n.get())==0 or len(a.get())==0 or len(p.get())==0:
        showerror("Error","Enter Details Properly")
    else:
        conn = sqlite3.connect("bus_reservation_211b420.db")
        cur=conn.cursor()
        cur.execute('insert into Operator values(?,?,?,?,?)',(n.get(),o.get(),a.get(),p.get(),e.get()))
        conn.commit()
        conn.close
        showinfo("opertor entry","New record added")

Button(root,text='Add',fg='black',bg='lightgreen',font='Arial 10 bold',command= pop).grid(row=3,column=10,padx=10,pady=30)
Button(root,text='Edit',fg='black',bg='lightgreen',font='Arial 10 bold').grid(row=3,column=11,padx=10,pady=30)
home=PhotoImage(file='.\\home.png')
def Home():
    root.destroy()
    import page2
Button(root,image=home,command=Home).grid(row=4,column=9,padx=10,pady=30)

root.mainloop()
