from tkinter import *
root=Tk()
(h,w)=root.winfo_screenwidth(),root.winfo_screenheight()
root.geometry('%dx%d+0+0'%(h,w))
bus= PhotoImage(file='.\\Bus_for_project.png')
Label(root,image=bus).grid(column=0,row=0,columnspan=10,padx=w//2)
Label(root,text='Online Bus Booking System',bg='lightblue',fg='red',font='Arial 26 bold').grid(row=1,column=0,columnspan=10,padx=w//2,pady=40)

def next(e=1):
    root.destroy()
    import page3

def next1(e=1):
    root.destroy()
    import page6

def next2(e=1):
    root.destroy()
    import page5

Button(root,text='Seat Booking',bg='lightgreen',fg='black',font='Arial 16 bold',command=next).grid(row=2,column=3,padx=20,pady=50)
Button(root,text='Checked Booked Seat',bg='lightgreen',fg='black',font='Arial 16 bold',command=next2).grid(row=2,column=5,padx=20)
Button(root,text='Add Bus Details',bg='lightgreen',fg='black',font='Arial 16 bold',command=next1).grid(row=2,column=7,padx=20)
Label(root,text='For Admin Only',fg='red',font='Arial 12 bold').grid(row=3,column=7)
root.mainloop()
