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
Label(root,text='Add Bus Running Details',fg='green',font='Arial 14 bold').grid(row=2,column=0,padx=w/2,columnspan=10,pady=30)
Label(root,text='Bus id',fg='black',font='Arial 10 bold').grid(row=3,column=0,padx=10,pady=30)
a=Entry(root)
a.grid(row=3,column=1)
Label(root,text='Running Date',fg='black',font='Arial 10 bold').grid(row=3,column=2,padx=10,pady=30)
b=Entry(root)
b.grid(row=3,column=3)
Label(root,text='Seat Available',fg='black',font='Arial 10 bold').grid(row=3,column=4,padx=10,pady=30)
c=Entry(root)
c.grid(row=3,column=5)

def pop():
    if len(b.get())==0 or len(c.get())==0 or len(f.get())==0 or len(o.get())==0 or len(r.get())==0:
        showerror("Error","Enter Details Properly")
    else:
        conn = sqlite3.connect("bus_reservation_211b420.db")
        cur=conn.cursor()
        cur.execute('insert into Runs values(?,?,?)',(a.get(),b.get(),c.get()))
        conn.commit()
        conn.close
        showinfo("opertor entry","New record added")

def Home():
    root.destroy()
    import page2

Button(root,text='Add Run',fg='black',bg='lightgreen',font='Arial 10 bold',command=pop).grid(row=3,column=6,padx=10,pady=30)
Button(root,text='Delete Run',fg='black',bg='lightgreen',font='Arial 10 bold').grid(row=3,column=17,padx=10,pady=30)
home=PhotoImage(file='.\\home.png')
Button(root,image=home,command=Home).grid(row=4,column=5,padx=10,pady=30)
root.mainloop()
