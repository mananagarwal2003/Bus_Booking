from tkinter import *
from tkinter.messagebox import *
import mysql.connector
conn = mysql.connector.connect(host='localhost',user='root',database='211b420_bus',password='M@n@n123')
root=Tk()
(h,w)=root.winfo_screenwidth(),root.winfo_screenheight()
root.geometry('%dx%d+0+0'%(h,w))
bus= PhotoImage(file='.\\Bus_for_project.png')
Label(root,image=bus).grid(column=0,row=0,columnspan=10,padx=w/2)
Label(root,text='Online Bus Booking System',bg='lightblue',fg='red',font='Arial 20 bold').grid(row=1,column=0,columnspan=10,padx=w/2,pady=20)
Label(root, text ="Check Your Booking",bg='green',fg='black',font='Arial 14 bold').grid(row=2,column=0,columnspan=10,padx=w/2,pady=20)
Label(root, text = "Enter Your Mobile No: ").grid(row =7, column =0,padx=w/3)
mob = Entry(root)
mob.grid(row =7, column=1)

def check():
    if len(mob.get())==0:
        showerror("Value Missing","Enter Mobile No.")
    else:
        cur=conn.cursor()
        cur.execute('select Name ,Phone,Age ,Gender ,Boarding ,Upto ,Travelling_Date ,Booking_date, Seates_booked,Bus_Id,fare,reference_id from Booking_history where Phone={}'.format(mob.get()))
        res=cur.fetchall()
        final = LabelFrame(root)
        final.grid(row = 8, column =0, columnspan=5,padx=w/2)
        Label(final, text = "Passenger: {}".format(res[0][0])).grid(row =8, column=0)
        Label(final, text = "No of seats: {}".format(res[0][8])).grid(row =9, column=0)
        Label(final, text = "Age: {}".format(res[0][2])).grid(row =10, column=0)
        Label(final, text = "Booking Ref.{}".format(res[0][11])).grid(row =11, column=0)
        Label(final, text = "Travels on: {}".format(res[0][6])).grid(row =12, column=0)
        Label(final, text = "No of Seats: {}".format(res[0][8])).grid(row =13, column=0)
        Label(final, text = "Gender: {}".format(res[0][3])).grid(row =8, column=1)
        Label(final, text = "Phone: {}".format(res[0][1])).grid(row =9, column=1)
        Label(final, text = "Fare Rs: {} ".format(res[0][10]*res[0][8])).grid(row =10, column=1)
        Label(final, text = "Bus Detail: {}".format(res[0][9])).grid(row =11, column=1)
        Label(final, text = "Booked On: {}".format(res[0][7])).grid(row =12, column=1)
        Label(final, text = "Boarding Point: {}".format(res[0][4])).grid(row =13, column=1)
        Label(final, text = "Total amount Rs {} to be paid at the time of boarding the bus".format(res[0][10]),fg='grey').grid(row =14, column=0,columnspan=2)
        

Button(root, text = "Check Booking", command = check).grid(row = 7, column=2,padx=w/3)

root.mainloop()


