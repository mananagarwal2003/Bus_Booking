from tkinter import *
root=Tk()
(h,w)=root.winfo_screenheight(),root.winfo_screenwidth()
root.geometry('%dx%d+0+0'%(w,h))
bus= PhotoImage(file='.\\Bus_for_project.png')
Label(root,image=bus).pack()
Label(root,text='Online Bus Booking System',bg='lightblue',fg='red',font='Arial 26 bold').pack(pady=40)
Label(root,text='Name: Manan Agarwal',fg='blue',font='Arial 16 bold').pack(pady=10)
Label(root,text='Enrollment: 211b420',fg='blue',font='Arial 16 bold').pack(pady=10)
Label(root,text='Mobile No.: 7627081914',fg='blue',font='Arial 16 bold').pack(pady=20)
Label(root,text='Submitted To: Dr. Mahesh Kumar',bg='lightblue',fg='red',font='Arial 16 bold').pack()
Label(root,text='Project Based Learning',fg='red',font='Arial 12 bold').pack()
def close(e=1):
    root.destroy()
    import page2
root.bind('<KeyPress>',close)
root.mainloop()
