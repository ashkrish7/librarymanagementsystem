#Om Gam Ganapataye Namah

import tkinter
from tkinter.ttk import *
import datetime as dt
from tkinter import ttk
import mysql.connector as sql
from tkinter import messagebox
from tkinter import ttk

mydb=sql.connect(user="root",host="localhost",password="yourmysqlpassword",database="databasename")
cursor= mydb.cursor()
def search():   
    global I,Im, Img
    m = tkinter.Tk()
    m.geometry("600x670")
    m.title("Library Management System")
    m.iconbitmap('assets\LMS_Icon.ico')
    m.resizable(0, 0)
    
    
    topframe=tkinter.Frame(m,bg="#FFD700",width = 600,height=70,relief="raised",borderwidth=10)
    topframe.pack(side="top") 
    la=tkinter.Label(topframe, text=" Library   Management   System",font=("ALGERIAN", 25, "bold"),fg="Black",bg="#FFD700")
    la.place(x=0,y=0)
    tc = tkinter.ttk.Notebook(m,width=600,height=600)
    t1 = tkinter.ttk.Frame(tc)
    t2 = tkinter.ttk.Frame(tc)
    t3 = tkinter.ttk.Frame(tc)
    tc.add(t1, text ='Search Book')
    tc.add(t2, text ='Add New Book')
    tc.add(t3, text ="Delete Book")
    tc.place(x=0,y=70)
    I=tkinter.PhotoImage(master=tc,file="assets\\bookshelf.png")
    canvas=tkinter.Canvas(t1,width=600,height=600)
    canvas.place(x=0,y=0)
    canvas.create_image(1,1,image=I,anchor="nw")
    Im=tkinter.PhotoImage(master=tc,file="assets\\bookshelf2.png")
    canvas=tkinter.Canvas(t2,width=600,height=600)
    canvas.place(x=0,y=0)
    canvas.create_image(1,1,image=Im,anchor="nw")
    Img=tkinter.PhotoImage(master=tc,file="assets\\bookshelf3.png")
    canvas=tkinter.Canvas(t3,width=600,height=600)
    canvas.place(x=0,y=0)
    canvas.create_image(1,1,image=Img,anchor="nw")

    scroll = tkinter.Scrollbar(t1, orient="vertical")
    scroll.pack(side = "right", fill = "y" ) 
    management_box = tkinter.Listbox(t1, width=66, height=8, font='times 12 bold')
    management_box.place(x=30,y=215)
    bdetails = tkinter.Listbox(t1, width=66,height = 8, font= 'times 12 bold')
    bdetails.place(x=30,y=390)
    management_box.config(yscrollcommand = scroll.set)
    scroll.config(command = management_box.yview) 
    management_box.delete(0,"end")

    choice = tkinter.IntVar(master=t1)
    all_books = Radiobutton(t1, text='List all books', variable = choice,value=1)
    all_books.place(x=100,y=115)
    instock = Radiobutton(t1, text='Books available', variable =choice,value=2)
    instock.place(x=250,y=115)
    issued_books = Radiobutton(t1, text='Books issued', variable =choice,value=3)
    issued_books.place(x=420,y=115)
    
    
    
    def selection(evt):
        if (tc.tab(tc.select(), "text")) == "Add New Book":
            pass
        else:
            w = evt.widget
            ind =int(w.curselection()[0])
            value = w.get(ind)
            al = value.split('-')
            l= int(al[0])
    
            bdetails.delete(0,'end')
            cursor.execute('SELECT * FROM books WHERE S_NO=%s',(l,))
            book=cursor.fetchall()
        
            bdetails.insert(0, 'Book Name:'+book[0][1])
            bdetails.insert(1, 'Book Number:'+book[0][2])
            bdetails.insert(2, 'Author Name:'+book[0][3])
            bdetails.insert(3,'Availablility:'+book[0][4])
    
    def cshowbooks():
        f = choice.get()
        query = " "
        if f==0:
            query="SELECT * FROM books"
        elif f==1:
            query = "SELECT * FROM books ORDER BY S_NO"
        elif f==2:
            query = "select * from books where Availability='Yes' "
        elif f==3:
            query = "select * FROM books where Availability = 'No'"
        management_box.delete(0,"end")
        c = 0
        cursor.execute(query)
        searchquery = cursor.fetchall()
        for book in searchquery:
            management_box.insert(c, str(book[0])+'-'+str(book[1]))
            c += 1
        management_box.bind('<<ListboxSelect>>',selection)
    bshow=tkinter.Button(t1,text="Show Books",command=cshowbooks,font=("Octin Vintage B R", 15,"bold"),relief="raised",borderwidth=5,fg="Black",bg="#FFD700")
    bshow.place(x=230,y=150)
    
        
    def S():
        value = ent_search.get()
        if (value=='') or (value==' '):
            tkinter.messagebox.showerror("ERROR","ERROR! Blank values not accepted!")
        else:
            cursor.execute("SELECT * FROM books WHERE BOOK_NO LIKE %s",(value,))
            data=cursor.fetchall()
            management_box.delete(0,"end")
            cr = 0
            for book in data:
                 management_box.insert(cr, str(book[0])+"-"+str(book[1]))
                 cr+=1
            ent_search.delete(0,'end')
            management_box.bind('<<ListboxSelect>>',selection)
        
    L=tkinter.Label(t1, text="Enter Book Number:",font=("Arial", 15),fg="Black")
    L.place(x=10,y=75)
    cursor.execute("SELECT BOOK_NO FROM books")
    bs = cursor.fetchall()
    bl = []
    for b in bs:
        bl.append(b[0])

    bn = tkinter.StringVar()
    ent_search = ttk.Combobox(t1, textvariable=bn,width=30)
    ent_search.place(x= 200,y=78)
    ent_search['values'] = bl
    bsearch=tkinter.Button(t1,text="Search Now",command=S,font=("Octin Vintage B R", 11,"bold"),relief="raised",borderwidth=5,fg="Black",bg="#FFD700")
    bsearch.place(x=470,y=70)
        
    l=tkinter.Label(t1, text="SEARCH BOOK",font=("ALGERIAN", 30, "bold"),fg="White",bg="Black")
    l.place(x=165,y=2)
    l1=tkinter.Label(t2, text="ADD NEW BOOK",font=("ALGERIAN", 30, "bold"),fg="White",bg="Black")
    l1.place(x=160,y=2)
    L1=tkinter.Label(t2, text="Serial Number        :",font=("Arial", 15),fg="Black")
    L1.place(x=60,y=85)
    eL1 = tkinter.Entry(t2, width=30,bd=10)
    eL1.place(x=279,y=80)
    
    L2=tkinter.Label(t2, text="Enter Book Name   :",font=("Arial", 15),fg="Black")
    L2.place(x=60,y=155)
    eL2 = tkinter.Entry(t2, width=30,bd=10)
    eL2.place(x=279,y=150)
    
    L3=tkinter.Label(t2, text="Enter Book Number:",font=("Arial", 15),fg="Black")
    L3.place(x=60,y=225)
    eL3 = tkinter.Entry(t2, width=30,bd=10)
    eL3.place(x=279,y=220)
    
    L4=tkinter.Label(t2, text="Enter Author Name :",font=("Arial", 15),fg="Black")
    L4.place(x=60,y=295)
    eL4 = tkinter.Entry(t2, width=30,bd=10)
    eL4.place(x=279,y=290)
    
    L5=tkinter.Label(t2, text="Availability              :",font=("Arial", 15),fg="Black")
    L5.place(x=60,y=365)
    eL5 = tkinter.Entry(t2, width=30,bd=10)
    eL5.place(x=279,y=360)

    def add():
        sno = eL1.get()
        bookname = eL2.get()
        booknum = eL3.get()
        author = eL4.get()
        availability = eL5.get()

        if(bookname != '' and booknum!= '' and author != '' and availability != ''): 
            try:
                cursor.execute("INSERT INTO books(S_NO,BOOK_Name,BOOK_NO,Author,Availability) VALUES(%s, %s, %s, %s, %s)",(sno,bookname,booknum,author,availability))
                messagebox.showinfo('SUCCESS','Book has been added successfully')
                eL1.delete(0,'end')
                eL2.delete(0,'end')
                eL3.delete(0,'end')
                eL4.delete(0,'end')
                eL5.delete(0,'end')
                mydb.commit()
            except:
                messagebox.showerror('ERROR','Transaction failed!')
        
        elif(sno==0 or bookname == '' or booknum== '' or author == '' or availability == ''):
            messagebox.showerror('ERROR','Blank Values not accepted!')

    badd=tkinter.Button(t2,text="Add Now",command=add,font=("Octin Vintage B R", 15,"bold"),relief="raised",borderwidth=5,fg="Black",bg="#FFD700")
    badd.place(x=250,y=420)
    
   

    label2=tkinter.Label(t3, text="DELETE BOOK",font=("ALGERIAN", 30, "bold"),fg="White",bg="Black")
    label2.place(x=160,y=2)
    ll1=tkinter.Label(t3, text="Enter Book Number:",font=("Arial", 15),fg="Black")
    ll1.place(x=210,y=110)
    
    cursor.execute("SELECT BOOK_NO, BOOK_Name FROM books")
    BS = cursor.fetchall()
    BL = []
    for B in BS:
        BL.append(B[0]+'-'+B[1])

    BN = tkinter.StringVar()
    ell1 = ttk.Combobox(t3, textvariable=BN,width=45)
    ell1.place(x= 115,y=230)
    ell1['values'] = BL

    def Delete():
        bn=ell1.get().split('-')[0]
        if(bn!= ''): 
            try:
                cursor.execute("DELETE FROM books WHERE BOOK_NO = %s", (bn, ))
                messagebox.showinfo('SUCCESS','Book has been deleted successfully')
                ell1.delete(0,'end')
                mydb.commit()
            except:
               messagebox.showerror('ERROR','Transaction failed!')
        
        elif(bn== ''):
            messagebox.showerror('ERROR','Blank Values not accepted!') 
    
    bdelete=tkinter.Button(t3,text="Delete Now",command=Delete,font=("Octin Vintage B R", 15,"bold"),relief="raised",borderwidth=5,fg="Black",bg="#FFD700")
    bdelete.place(x=230,y=340)
    m.mainloop()

 
def issueorreturn():
    
    global ima
    t = tkinter.Tk()
    t.title("Library Management System")
    t.geometry("1198x651")
    t.iconbitmap('assets\LMS_Icon.ico')
    t.resizable(0, 0)
    ima=tkinter.PhotoImage(master=t,file="assets\Library2.png")
    canvas=tkinter.Canvas(t,width=1198,height=591)
    canvas.place(x=0,y=70)
    canvas.create_image(1,1,image=ima,anchor="nw")
    
    tframe=tkinter.Frame(t,bg="#FFD700",width = 1198,height=70,relief="raised",borderwidth=10)
    tframe.pack(side="top") 
    La=tkinter.Label(tframe, text="        L i b r a r y       M a n a g e m e n t       S y s t e m          ",font=("ALGERIAN", 30, "bold"),fg="Black",bg="#FFD700")
    La.place(x=0,y=0)
    l=tkinter.Label(t, text=" ISSUE BOOK ",font=("ALGERIAN", 30, "bold"),fg="White",bg="Black")
    l.place(x=170,y=71)
    l1=tkinter.Label(t, text="Serial Number         :",font=("Arial", 15),fg="Black")
    l1.place(x=20,y=165)
    el1 = tkinter.Entry(t, width=40,bd=10)
    el1.place(x=229,y=160)
    
    l2=tkinter.Label(t, text="Enter Book Number :",font=("Arial", 15),fg="Black")
    l2.place(x=20,y=235)
    
    l3=tkinter.Label(t, text="Enter ID                 :",font=("Arial", 15),fg="Black")
    l3.place(x=20,y=305)
    
    l4=tkinter.Label(t, text="Issue Date             :",font=("Arial", 15),fg="Black")
    l4.place(x=20,y=375)
    el4 = tkinter.Entry(t, width=40,bd=10)
    el4.place(x=229,y=370)

    l5=tkinter.Label(t, text="Due Date               :",font=("Arial", 15),fg="Black")
    l5.place(x=20,y=445)
    el5 = tkinter.Entry(t, width=40,bd=10)
    el5.place(x=229,y=440)

    l6=tkinter.Label(t, text="Status                   :",font=("Arial", 15),fg="Black")
    l6.place(x=20,y=515)#(x=680,y=515)
    el6 = tkinter.Entry(t, width=40,bd=10)
    el6.place(x=229,y=510)#(x=889,y=510)

    cursor.execute("SELECT * FROM books WHERE Availability='Yes'")
    books = cursor.fetchall()
    booklist = []
    for book in books:
        booklist.append(str(book[2])+'-'+book[1])

    bname = tkinter.StringVar()
    el2 = ttk.Combobox(t, textvariable=bname,width=40)
    el2.place(x= 229,y=240)
    el2['values'] = booklist

    cursor.execute("SELECT ID_NO FROM users")
    users = cursor.fetchall()
    userlist = []
    for user in users:
        userlist.append(user[0])  
    username = tkinter.StringVar()
    el3 = ttk.Combobox(t,textvariable=username,width=40)
    el3.place(x= 229,y=310)

    el3['values'] = userlist

    def issue():
        """
            Issues book to the given member and updates DB
        """
        sn = el1.get()
        bk = el2.get().split('-')[0]
        usr = el3.get()
        isdate=el4.get()
        duedate=el5.get()
        status=el6.get()
        if(bk != '' and usr!= '' and isdate != '' and duedate != '' and status!=''): 
            try:
                cursor.execute("select * from status where ID_NO=%s",(usr,))
                p=cursor.fetchone()
                
                if p[5]=="RETURNED":
                    query="update status set BOOK_NO=%s,IssueDate=%s,DueDate=%s,Status=%s where ID_NO=%s"
                    cursor.execute(query, (bk,isdate,duedate,status,usr))
                    messagebox.showinfo('SUCCESS','Book has been issued successfully')
                    el1.delete(0,'end')
                    el2.set("")
                    el3.set("")
                    el4.delete(0,'end')
                    el5.delete(0,'end')
                    el6.delete(0,'end')
                    mydb.commit()
                    cursor.execute("UPDATE books SET Availability='No' WHERE BOOK_NO=%s",(bk,))
                    mydb.commit()
                else:
                    query = "INSERT INTO status (S_NO,BOOK_NO,ID_NO,IssueDate,DueDate,Status) VALUES(%s,%s,%s,%s,%s,%s)"
                    cursor.execute(query, (sn,bk, usr,isdate,duedate,status))
                    messagebox.showinfo('SUCCESS','Book has been issued successfully')
                    el1.delete(0,'end')
                    el2.set("")
                    el3.set("")
                    el4.delete(0,'end')
                    el5.delete(0,'end')
                    el6.delete(0,'end') 
                    mydb.commit()
                    cursor.execute("UPDATE books SET Availability='No' WHERE BOOK_NO=%s",(bk,))
                    mydb.commit()
            except:
                messagebox.showerror('ERROR','Transaction not commit')

     
        else:
            messagebox.showerror('ERROR','Blank Values not accepted!')
            
    ibtn=tkinter.Button(t,text=" Issue Now ",command=issue,font=("Octin Vintage B R", 15,"bold"),relief="raised",borderwidth=5,fg="Black",bg="#FFD700")
    ibtn.place(x=230,y=580)

    label1=tkinter.Label(t, text=" RETURN BOOK ",font=("ALGERIAN", 30, "bold"),fg="White",bg="Black")
    label1.place(x=745,y=71)
    
    _L1=tkinter.Label(t, text="Enter ID                 :",font=("Arial", 15),fg="Black")
    _L1.place(x=630,y=165)

    _L2=tkinter.Label(t, text="Enter Book Number:",font=("Arial", 15),fg="Black")
    _L2.place(x=630,y=305)
    
    _L3=tkinter.Label(t, text="Status                   :",font=("Arial", 15),fg="Black")
    _L3.place(x=630,y=445)
    Le3 = tkinter.Entry(t, width=40,bd=10)
    Le3.place(x=838,y=440)

    cursor.execute("SELECT ID_NO FROM status WHERE Status = 'LENT'")
    USERS = cursor.fetchall()
    USERlist = []
    for USER in USERS:
        USERlist.append(USER[0])
    USERname = tkinter.StringVar()
    Le1 = ttk.Combobox(t,textvariable=USERname,width=40)
    Le1.place(x= 838,y=166)

    Le1['values'] = USERlist

    cursor.execute("SELECT BOOK_NO FROM status")
    Books = cursor.fetchall()
    
    Booklist = []
    for Book in Books:
        Booklist.append(Book[0])

    Bname = tkinter.StringVar()
    Le2 = ttk.Combobox(t, textvariable=Bname,width=40)
    Le2.place(x= 838,y=307)
    Le2['values'] = Booklist
    rbtn=tkinter.Button(t,text=" Return Now ",font=("Octin Vintage B R", 15,"bold"),relief="raised",borderwidth=5,fg="Black",bg="#FFD700")
    rbtn.place(x=805,y=560)

    
    
    def call(evt):
        def rn():
            us = Le1.get()
            stat=Le3.get()
            b=Le2.get()
            if(b != '' and us!= '' and stat!=''):
                try:
                    cursor.execute("UPDATE status SET BOOK_NO=NULL, IssueDate=NULL, DueDate=NULL, Status=%s WHERE ID_NO=%s",(stat,us))
                    messagebox.showinfo('SUCCESS','Book has been returned successfully')    
                    Le1.set("")
                    Le2.set("")
                    Le3.delete(0,'end')
                    mydb.commit()
                    cursor.execute("UPDATE books SET Availability='Yes' WHERE BOOK_NO=%s",(b,))
                    mydb.commit()
                except:
                    messagebox.showerror('ERROR','Transaction not commit')
            elif(us== '' or stat==''):
                messagebox.showerror('ERROR','Blank Values not accepted!')
            else:
                messagebox.showerror('ERROR','Blank Values not accepted!')    
        global Le1,rbtn,Le2
        Le1 = ttk.Combobox(t,textvariable=USERname,width=40)
        us = Le1.get()
        cursor.execute("SELECT BOOK_NO FROM status WHERE ID_NO=%s",(us,))
        Books = cursor.fetchall()
        Booklist = []
        for Book in Books:
            Booklist.append(Book[0])
        
        Bname = tkinter.StringVar()
        Le2 = ttk.Combobox(t, textvariable=Bname,width=40)
        Le2.place(x= 838,y=307)
        Le2['values'] = Booklist
        rbtn=tkinter.Button(t,text=" Return Now ",command=rn,font=("Octin Vintage B R", 15,"bold"),relief="raised",borderwidth=5,fg="Black",bg="#FFD700")
        rbtn.place(x=805,y=560)
    Le1.bind("<<ComboboxSelected>>", call)
    t.mainloop()

    
def status():
    global Ma
    s = tkinter.Tk()
    s.title("Library Management System")
    s.geometry("1198x652")
    s.iconbitmap('assets\LMS_Icon.ico')
    s.resizable(0, 0)
    Ma=tkinter.PhotoImage(master=s,file="assets\Library3.png")
    canvas=tkinter.Canvas(s,width=1198,height=592)
    canvas.place(x=0,y=70)
    canvas.create_image(1,1,image=Ma,anchor="nw")
    Tframe=tkinter.Frame(s,bg="#FFD700",width = 1198,height=70,relief="raised",borderwidth=10)
    Tframe.pack(side="top") 
    LA=tkinter.Label(Tframe, text="        L i b r a r y       M a n a g e m e n t       S y s t e m          ",font=("ALGERIAN", 30, "bold"),fg="Black",bg="#FFD700")
    LA.place(x=0,y=0)
    v=ttk.Treeview(s, columns=(1,2,3,4,5,6), show="headings", height="25")
    v.place(x=0,y=115)
    v.heading(1, text="Serial Number")
    v.heading(2, text="Book Number")
    v.heading(3, text="ID")
    v.heading(4, text="Issue Date")
    v.heading(5, text="Due Date")
    v.heading(6, text="Status")
    cursor.execute("select * from status")
    rows=cursor.fetchall()
    for i in rows:
        v.insert("","end",values=i)
    def refresh():
        v.delete(*v.get_children())
        cursor.execute("select * from status")
        rows=cursor.fetchall()
        for row in rows:
            v.insert('','end', values =row )
    refreshbtn=tkinter.Button(s,text="Refresh",command=refresh,font=("Octin Vintage B R", 10,"bold"),relief="raised",borderwidth=5,fg="Black",bg="#FFD700")
    refreshbtn.place(x=560,y=78)
    s.mainloop()
