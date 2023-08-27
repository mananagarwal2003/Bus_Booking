from tkinter import *
from tkinter.messagebox import *
import mysql.connector

root=Tk()
(h,w)=root.winfo_screenwidth(),root.winfo_screenheight()
root.geometry('%dx%d+0+0'%(h,w))
bus= PhotoImage(file='.\\Bus_for_project.png')
Label(root,image=bus).grid(column=0,row=0,columnspan=10,padx=w/2)
Label(root,text='Online Bus Booking System',bg='lightblue',fg='red',font='Arial 20 bold').grid(row=1,column=0,columnspan=10,padx=w/2,pady=20)
Label(root,text='Enter Journey Details',bg='lightgreen',fg='green',font='Arial 14 bold').grid(row=2,column=0,columnspan=10,padx=w/2)
Label(root,text='To',fg='black',font='Arial 10 bold').grid(row=3,column=0,padx=10,pady=30)
a=Entry(root)
a.grid(row=3,column=1)
Label(root,text='From',fg='black',font='Arial 10 bold').grid(row=3,column=2,padx=10,pady=30)
b=Entry(root)
b.grid(row=3,column=3)
Label(root,text='Journey Date',fg='black',font='Arial 10 bold').grid(row=3,column=4,padx=10,pady=30)
c=Entry(root)
c.grid(row=3,column=5)

def abc():
    conn = mysql.connector.connect(host='localhost',user='root',database='211b420_bus',password='M@n@n123')
    cur=conn.cursor()
    cur.execute('select op.Name,b.type,r.Seat_Available,r.Seat_Available,b.fare,b.Bus_Id from Operator as op, Bus as b,runs as r, route as f,route as t where b.op_id=op.op_id and b.bus_id=r.bus_id and f.Route_id=b.Route_id and f.sname="{}" and t.sname="{}" and f.Route_id = t.route_id and F.s_id<T.s_id and r.date="{}";'.format(b.get(),a.get(),c.get()))
    resx=cur.fetchall()
    bid=resx[0][5]
    fare=resx[0][4]
    #cur.execute('insert into Booking_history(Name ,Phone,Age ,Gender ,Boarding ,Upto ,Travelling_Date ,Booking_date, Seates_booked,Bus_Id,fare)values("{}",{},{},"{}","{}","{}","{}","{}",{},{},{})'.format(n.get(),m.get(),age.get(),gender.get(),b.get(),a.get(),"29/11/22",c.get(),s.get(),bid,fare))
    cur.execute('insert into Booking_history(Name,Phone,Age,Gender,Boarding,Upto,Travelling_Date,Booking_date,Seates_booked,Bus_Id,fare) values("{}",{},{},"{}","{}","{}","{}",current_date(),{},{},{})'.format(n.get(),m.get(),age.get(),gender.get(),b.get(),a.get(),c.get(),s.get(),bid,fare))
    conn.commit()
    conn.close()
    result=askquestion("Confirmation","Are you sure to book tickets?")
    if result=="yes":
        root.destroy()
        import page4
    else:
        root.destroy()
        import page2

def book():
    Label(root,text='Fill Passenger Details To Book Tickets',bg='lightblue',fg='red',font='Arial 16 bold').grid(row=6,column=0,columnspan=10,padx=w/2,pady=20)
    Label(root,text='Name',fg='black',font='Arial 10 bold').grid(row=7,column=0,padx=10,pady=30)
    n.grid(row=7,column=1)
    Label(root,text='Gender',fg='black',font='Arial 10 bold').grid(row=7,column=2,padx=10,pady=30)

    
    option=("Male", "Female", "Others")
    menu=OptionMenu(root,gender,* option).grid(row=7, column=3,padx=10,pady=30)
    gender.set("Select Gender")
    Label(root,text='No of Seats',fg='black',font='Arial 10 bold').grid(row=7,column=4,padx=10,pady=30)
    s.grid(row=7,column=5)
    Label(root,text='Mobile No',fg='black',font='Arial 10 bold').grid(row=7,column=6,padx=10,pady=30)
    
    m.grid(row=7,column=7)
    Label(root,text='Age',fg='black',font='Arial 10 bold').grid(row=7,column=8,padx=10,pady=30)
    age.grid(row=7,column=9)
    Button(root,text='Book Seat',bg='green',fg='black',font='Arial 12 bold',command=abc).grid(row=7,column=10)
    
    
    
def show_bus():
    Label(root,text='Select Bus',fg='green',font='Arial 10 bold').grid(row=4,column=0)
    Label(root,text='Operator',fg='green',font='Arial 10 bold').grid(row=4,column=1)
    Label(root,text='Bus Type',fg='green',font='Arial 10 bold').grid(row=4,column=2)
    Label(root,text='Available',fg='green',font='Arial 10 bold').grid(row=4,column=3)
    Label(root,text='Capacity',fg='green',font='Arial 10 bold').grid(row=4,column=4)
    Label(root,text='Fare',fg='green',font='Arial 10 bold').grid(row=4,column=5)
    conn = mysql.connector.connect(host='localhost',user='root',database='211b420_bus',password='M@n@n123')
    cur=conn.cursor()
    cur.execute('select op.Name,b.type,r.Seat_Available,r.Seat_Available,b.fare from Operator as op, Bus as b,runs as r, route as f,route as t where b.op_id=op.op_id and b.bus_id=r.bus_id and f.Route_id=b.Route_id and f.sname="{}" and t.sname="{}" and f.Route_id = t.route_id and F.s_id<T.s_id and r.date="{}";'.format(b.get(),a.get(),c.get()))
    res=cur.fetchall()
    cur.execute('select sum(seates_booked) from booking_history where Travelling_date = "{}"'.format(c.get()))
    xyz=cur.fetchall()
    Radiobutton(root,text='Bus1',variable=bus_s,value=1).grid(row=5,column=0)
    Label(root,text=res[0][0]).grid(row=5,column=1)
    Label(root,text=res[0][1]).grid(row=5,column=2)
    Label(root,text=res[0][2]-xyz[0][0]).grid(row=5,column=3)
    Label(root,text=res[0][3]).grid(row=5,column=4)
    Label(root,text=res[0][4]).grid(row=5,column=5)
    Button(root,text='Proceed To Book',command=book,bg='green',fg='black',font='Arial 12 bold').grid(row=5,column=9)
    conn.commit()
    conn.close()
Button(root,text='Show Bus',command=show_bus,bg='darkgreen',fg='black',font='Arial 12 bold').grid(row=3,column=6,padx=20,pady=30)
home=PhotoImage(file='.\\home.png')
Button(root,image=home).grid(row=3,column=7,padx=20,pady=30)
bus_s=IntVar()
n=Entry(root)
s=Entry(root)
gender=StringVar()
m=Entry(root)
age=Entry(root)
root.mainloop()

#"select op.Name,b.type,r.Seat_Available,b.fare,r.Seat_Available from Operator as op, Bus as b,runs as r, route as f,route as t where b.op_id=op.op_id and b.bus_id=r.bus_id and f.Route_id=b.Route_id and f.sname="{}" and t.sname="{}" and f.Route_id = t.route_id and F.s_id<T.s_id and r.date="{}";""".format(From.get(),to.get(),date.get()))


