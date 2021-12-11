#Om Gam Ganapataye Namah
import tkinter
import importlib
import mainwindow
from tkinter import messagebox
import command

mainwindow = importlib.import_module('mainwindow')
def check():
    if (e1.get()=="" and e2.get()=="") or (e1.get()=="" or e2.get()==""):
        tkinter.messagebox.showerror("ERROR","ERROR! Blank values not accepted!")
        
    elif e1.get()=="arshwini" and e2.get()=="rk":
        window.destroy()
        mainwindow.main()

    else:
        tkinter.messagebox.showwarning("WARNING","Login Unsuccessful")
         
window=tkinter.Tk()
window.geometry("300x200")
window.configure(bg="Yellow")
window.title("Library Management System")
window.iconbitmap('Icon.ico')
window.resizable(0, 0)
img=tkinter.PhotoImage(file="room.png")
w = img.width()
h = img.height()
window.geometry("%dx%d" % (w, h))
tkinter.Label(window,image=img).pack()

l=tkinter.Label(window, text="Library Management System",font=("Arial", 30, "bold", "italic"),fg="#0000FF",bg="Yellow")
l.place(x=38,y=0)
l1=tkinter.Label(window, text="LOGIN",font=("Arial", 27, "bold", ),fg="Red",bg="Yellow")
l1.place(x=260,y=70)
l2=tkinter.Label(window, text="Enter your name      :",font=("Arial", 18),bg="Yellow")
l2.place(x=65,y=150)
l3=tkinter.Label(window, text="Enter your password:",font=("Arial", 18),bg="Yellow")
l3.place(x=65,y=220)
e2=tkinter.Entry(window,relief="sunken",width=30,bd=10,font=("Arial", 10),show="*")
e2.place(x=330,y=217)         
e1=tkinter.Entry(window,relief="sunken",width=30,bd=10,font=("Arial", 10))
e1.place(x=330,y=148)
b2=tkinter.Button(window,command=check,text="Submit",font=("Arial",18),bg="Red")
b2.place(x=270,y=280)
i=tkinter.PhotoImage(file="HogwartsLibrarycopy.png")
I=tkinter.PhotoImage(file="bookshelf.png")
tc = tkinter.ttk.Notebook(width=600,height=600)
Im=tkinter.PhotoImage(master=tc,file="bs2.png")
Img=tkinter.PhotoImage(master=tc,file="t3.png")
ima=tkinter.PhotoImage(file="room2.png")
Ma=tkinter.PhotoImage(file="rroom.png")
window.mainloop()