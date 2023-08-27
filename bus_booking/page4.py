from tkinter import *
import mysql.connector
root=Tk()
(h,w)=root.winfo_screenwidth(),root.winfo_screenheight()
root.geometry('%dx%d+0+0'%(h,w))
bus= PhotoImage(file='.\\Bus_for_project.png')
Label(root,image=bus).grid(column=0,row=0,columnspan=10,padx=w/2)
Label(root,text='Online Bus Booking System',bg='lightblue',fg='red',font='Arial 20 bold').grid(row=1,column=0,columnspan=10,padx=w/2,pady=20)
Label(root, text ="Bus Ticket").grid(row=2,column=0,columnspan=10,padx=w/2,pady=20)
conn = mysql.connector.connect(host='localhost',user='root',database='211b420_bus',password='M@n@n123')
cur=conn.cursor()
cur.execute('select max(Reference_Id) from Booking_history')
res1=cur.fetchall()
m=res1[0][0]
cur.execute('select Name ,Phone,Age ,Gender ,Boarding ,Upto ,Travelling_Date ,Booking_date, Seates_booked,Bus_Id,fare from Booking_history where reference_id={}'.format(m))
a=cur.fetchall()
final = LabelFrame(root)
final.grid(row=8, column =0, columnspan=5,padx=w/2)
Label(final, text = "Passenger: {}".format(a[0][0])).grid(row =8, column=0)
Label(final, text = "No of seats: {}".format(a[0][8])).grid(row =9, column=0)
Label(final, text = "Age: {}".format(a[0][2])).grid(row =10, column=0)
Label(final, text = "Booking Ref.").grid(row =11, column=0)
Label(final, text = "Travels on: {}".format(a[0][6])).grid(row =12, column=0)
Label(final, text = "No of Seats: {}".format(a[0][8])).grid(row =13, column=0)
Label(final, text = "Gender: {}".format(a[0][3])).grid(row =8, column=1)
Label(final, text = "Phone: {}".format(a[0][1])).grid(row =9, column=1)
Label(final, text = "Fare Rs: {} ".format(a[0][10]*a[0][8])).grid(row =10, column=1)
Label(final, text = "Bus Detail: {}".format(a[0][9])).grid(row =11, column=1)
Label(final, text = "Booked On: {}".format(a[0][7])).grid(row =12, column=1)
Label(final, text = "Boarding Point: {}".format(a[0][4])).grid(row =13, column=1)
Label(final, text = "Total amount Rs{} to be paid at the time of boarding the bus".format(a[0][10]),fg='grey').grid(row =14, column=0,columnspan=2)
