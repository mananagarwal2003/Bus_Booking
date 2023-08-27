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
Label(root,text='Add Bus Details',fg='green',font='Arial 14 bold').grid(row=2,column=0,padx=w/2,columnspan=10,pady=30)
Label(root,text='Bus id',fg='black',font='Arial 10 bold').grid(row=3,column=0,padx=10,pady=30)
b=Entry(root)
b.grid(row=3,column=1)

bustype=StringVar()
option=("AC 2X2", "AC 3X2", "Non AC2X2", "Non AC 3X2", "AC-Sleeper 2X1", "Non-AC SLeeper 2X1" )
menu=OptionMenu(root,bustype,* option).grid(row=3, column=3,padx=10,pady=30)
bustype.set("select bus")

Label(root,text='Capacity',fg='black',font='Arial 10 bold').grid(row=3,column=4,padx=10,pady=30)
c=Entry(root)
c.grid(row=3,column=5)
Label(root,text='Fare Rs',fg='black',font='Arial 10 bold').grid(row=3,column=6,padx=10,pady=30)
f=Entry(root)
f.grid(row=3,column=7)
Label(root,text='Operator id',fg='black',font='Arial 10 bold').grid(row=3,column=8,padx=10,pady=30)
o=Entry(root)
o.grid(row=3,column=9)
Label(root,text='Route id',fg='black',font='Arial 10 bold').grid(row=3,column=10,padx=10,pady=30)
r=Entry(root)
r.grid(row=3,column=11)

def pop():
    if len(b.get())==0 or len(c.get())==0 or len(f.get())==0 or len(o.get())==0 or len(r.get())==0:
        showerror("Error","Enter Details Properly")
    else:
        conn = sqlite3.connect("bus_reservation_211b420.db")
        cur=conn.cursor()
        cur.execute('insert into Bus values(?,?,?,?,?,?)',(b.get(),bustype.get(),c.get(),f.get(),r.get(),o.get()))
        conn.commit()
        conn.close
        showinfo("opertor entry","New record added")
def Home():
    root.destroy()
    import page2

Button(root,text='Add',fg='black',bg='lightgreen',font='Arial 10 bold',command=pop).grid(row=4,column=7,padx=10,pady=30)
Button(root,text='Edit',fg='black',bg='lightgreen',font='Arial 10 bold').grid(row=4,column=8,padx=10,pady=30)
home=PhotoImage(file='.\\home.png')
Button(root,image=home,command=Home).grid(row=4,column=9,padx=10,pady=30)
root.mainloop()


