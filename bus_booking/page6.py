from tkinter import *
root=Tk()
(h,w)=root.winfo_screenwidth(),root.winfo_screenheight()
root.geometry('%dx%d+0+0'%(h,w))
bus= PhotoImage(file='.\\Bus_for_project.png')
Label(root,image=bus).grid(column=0,row=0,columnspan=10,padx=w/2)

def next(e=1):
    root.destroy()
    import page7
def next1(e=1):
    root.destroy()
    import page8
def next2(e=1):
    root.destroy()
    import page9
def next3(e=1):
    root.destroy()
    import page10

Label(root,text='Online Bus Booking System',bg='lightblue',fg='red',font='Arial 20 bold').grid(row=1,column=0,pady=20,padx=w/2,columnspan=10)
Label(root,text='Add New Details To Database',fg='green',font='Arial 14 bold').grid(row=2,column=0,padx=w/2,columnspan=10)
Button(root,text='New Operator',fg='black',bg='green',font='Arial 10 bold',command=next).grid(row=3,column=0,padx=20,pady=20)
Button(root,text='New Bus',bg='orange',fg='black',font='Arial 10 bold',command=next1).grid(row=3,column=2,padx=20)
Button(root,text='New Route',bg='blue',fg='black',font='Arial 10 bold',command=next2).grid(row=3,column=4,padx=20)
Button(root,text='New Run',bg='brown',fg='black',font='Arial 10 bold',command=next3).grid(row=3,column=6,padx=5)
root.mainloop()
