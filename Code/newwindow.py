#RADHEKRISHNA
import tkinter
import datetime as dt
import commands

def main():
    global i
    w=tkinter.Tk()
    w.geometry("300x200")
    w.configure(bg="Yellow")
    w.title("Library Management System")
    w.iconbitmap('Icon.ico')
    w.resizable(0, 0)
    
    i=tkinter.PhotoImage(file="HogwartsLibrarycopy.png")
    wid = i.width()
    h = i.height()
    w.geometry("%dx%d" % (wid, h))
    tkinter.Label(w,image=i).pack()
    l=tkinter.Label(w, text="  T H E     L I B R A R Y     W O R L D  ",font=("ALGERIAN", 40, "bold"),fg="White",bg="Black", relief='raised',borderwidth=15)
    l.place(x=0,y=0)
    T1="""  Search  
  Book  """
    btn=tkinter.Button(w,text=T1,command=commands.search,font=("Octin Vintage B R", 20,"bold"),relief="raised",borderwidth=5,fg="Black",bg="#FFD700")
    btn.place(x=95,y=180)
    tid = tkinter.Label(w, text=f"{dt.datetime.now():%a, %b %d %Y}", fg="white", bg="black", font=("Georgia", 25),relief="raised",borderwidth=9)#helvetica
    tid.place(x=640,y=744)
    T="""Issue / Return
Book"""
    b=tkinter.Button(w,text=T,command=commands.issueorreturn,font=("Octin Vintage B R", 20,"bold"),relief="raised",borderwidth=5,fg="Black",bg="#FFD700")
    b.place(x=60,y=400)
    T2="""  Show  
  Status  """
    b=tkinter.Button(w,text=T2,command=commands.status,font=("Octin Vintage B R", 20,"bold"),relief="raised",borderwidth=5,fg="Black",bg="#FFD700")
    b.place(x=95,y=630)
    I=tkinter.PhotoImage(file="bookshelf.png")
    tc = tkinter.ttk.Notebook(width=600,height=600)
    Im=tkinter.PhotoImage(master=tc,file="bs2.png")
    Img=tkinter.PhotoImage(master=tc,file="t3.png")
    ima=tkinter.PhotoImage(file="room2.png")
    Ma=tkinter.PhotoImage(file="rroom.png")
    txt=""" ABOUT

The Library
Management System,
has been deisnged
and developed
by Ashwini and Arsha,
studying in class XII B
in Amrita Vidyalayam,
Ettimadai.
This System,
allows the user,
a Librarian,
an easy and
efficient way of maintaining
a database that is useful
to enter new books,
new members,
and much more
without the burden of
manual record keeping
by the user.""" 
    lr=tkinter.Label(w,text=txt,height=22,width=22, font=("Octin Vintage B R",15,"bold"),relief="groove",borderwidth=9,bg="#FFD700",fg="Black")
    lr.place(x=610,y=145)
    w.mainloop()
