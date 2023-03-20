from ctypes import *
from tkinter import *
from PIL import ImageTk
from PIL import Image as immage
from tkinter import messagebox
import mysql
import mysql.connector
import tkinter as tk
from tkinter import *
from tkinter import messagebox
import mysql.connector as sqlt
import datetime as dt
from datetime import date
from datetime import timedelta
def book_regis(cur,con):
    global c1,c2,broot
    c1=cur
    c2=con
    broot=Tk()
    broot.title("book regis")
    broot.minsize(width=400,height=400)
    broot.geometry("600x500")
    headingFrame1 = Frame(broot,bg="#FFBB00",bd=5)
    headingFrame1.place(relx=0.2,rely=0.1,relwidth=0.6,relheight=0.16)

    headingLabel = Label(headingFrame1, text="BOOK REGISTER", bg='black', fg='white', font=('Courier',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)

    btn7 = Button(broot,text="NEW BOOK ENTRY",bg='black', fg='white', command=addbook)
    btn7.place(relx=0.28,rely=0.4, relwidth=0.45,relheight=0.1)
        
    btn8 = Button(broot,text="DELETE BOOK",bg='black', fg='white', command=deletebook)
    btn8.place(relx=0.28,rely=0.5, relwidth=0.45,relheight=0.1)
        
    btn9 = Button(broot,text="VIEW BOOK LIST",bg='black', fg='white', command=book_details)
    btn9.place(relx=0.28,rely=0.6, relwidth=0.45,relheight=0.1)
        
    btn10 = Button(broot,text="SEARCH A BOOK",bg='black', fg='white', command=searchin1)
    btn10.place(relx=0.28,rely=0.7, relwidth=0.45,relheight=0.1)

    QuitBtn=Button(broot,text="QUIT",bg='#d1ccc0', fg='black',command=Quit9)
    QuitBtn.place(relx=0.5,rely=0.9, relwidth=0.18,relheight=0.08)

def Quit9():
    broot.destroy()
    
def addbook():
    global c2,c1,info3,info4,info5,info6,croot
    Quit9()
    #broot.destroy()
    croot=Tk()
    croot.title("add book")
    croot.minsize(width=400,height=400)
    croot.geometry("600x500")
    
    headingFrame1 = Frame(croot,bg="#FFBB00",bd=5)
    headingFrame1.place(relx=0.2,rely=0.1,relwidth=0.6,relheight=0.16)

    headingLabel = Label(headingFrame1, text="ADD BOOK", bg='black', fg='white', font=('Courier',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
    
    z=75400022
    
    labelFrame = Frame(croot,bg='black')
    labelFrame.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.5)
    
    
    lb3 = Label(labelFrame,text="TITLE", bg='black', fg='white')
    lb3.place(relx=0.05,rely=0.3)
    info3 = Entry(labelFrame)
    info3.place(relx=0.3,rely=0.3, relwidth=0.62)
    lb4 = Label(labelFrame,text="AUTHOR", bg='black', fg='white')
    lb4.place(relx=0.05,rely=0.4)
    info4 = Entry(labelFrame)
    info4.place(relx=0.3,rely=0.4, relwidth=0.62)
    lb5 = Label(labelFrame,text="PUBLISHER", bg='black', fg='white')
    lb5.place(relx=0.05,rely=0.5)
    info5 = Entry(labelFrame)
    info5.place(relx=0.3,rely=0.5, relwidth=0.62)
    '''
    ####
    name = StringVar(croot)
    name.trace("w", lambda l, idx, mode: writefile())

    croot.config(cursor="none")
    #######
    '''
    lb6 = Label(labelFrame,text="Yr. OF PUBLICATION", bg='black', fg='white')
    lb6.place(relx=0.05,rely=0.6)
    info6 = Entry(labelFrame, validate="key")
    info6['validatecommand'] = (info6.register(testVal),'%P','%d')
    
    info6.place(relx=0.3,rely=0.6, relwidth=0.62)
    
    SubmitBtn = Button(croot,text="SUBMIT",bg='#d1ccc0', fg='black',command=submit1)
    SubmitBtn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)
    QuitBtn=Button(croot,text="QUIT",bg='#d1ccc0', fg='black',command=Quit)
    QuitBtn.place(relx=0.5,rely=0.9, relwidth=0.18,relheight=0.08)

def testVal(inStr,acttyp):
    if acttyp == '1': #insert
        if not inStr.isdigit():
            return False
    return True

    
def submit1():
    v1 = info3.get()
    v2 = info4.get()
    v3 = info5.get()
    v4 = info6.get()
    a=1
    v21=v1.upper()
    v22=v2.upper()
    v23=v3.upper()
    if len(v4)<=4:
        if v4.isdigit():
            a=0
    v2=v2.replace(" ",'')
    v2=v2.replace(".",'')
    v3=v3.replace(" ",'')
    v3=v3.replace(".",'')
    
    
    if  v2.isalpha() and v3.isalpha() and a==0:
        #print(type(v4))
        c1=c2.cursor()
        c1.execute("use db")
        c1.execute("select * from book")
        t1=c1.fetchall()
        
        c1.execute("select max(id) from book")
        j=c1.fetchall()
        print(j)
        if j[0][0]==None:
            j=75400022
        else:
            j=int(j[0][0])+1
        str1=str(j)
        print(j)
        st1="insert into book values('"+str1+"','"+v21+"','"+v22+"','"+v23+"','"+v4+"','avialable')"
        print(st1)
        c1.execute(st1)
        c2.commit()
        messagebox.showinfo("logged in","NEW BOOK SUCCESSFULLY ADDED")
        croot.destroy()
        broot.mainloop()
    
    else:
        messagebox.showerror("ERROR","PLEASE CHECK THAT\n AUTHOR DOES NOT HAVE NUMBERS\nPUBLICATION DOES NOT HAVE NUMBERS\nYR. OF PUBLI. IS A VALID YEAR")
        croot.mainloop()

def Quit():
    croot.destroy()
    
def deletebook():
    global info1,c1,c2,droot
    Quit9()
    droot=Tk()
    droot.title("delete")
    droot.minsize(width=400,height=400)
    droot.geometry("600x500")
    headingFrame1 = Frame(droot,bg="#FFBB00",bd=5)
    headingFrame1.place(relx=0.2,rely=0.1,relwidth=0.6,relheight=0.16)

    headingLabel = Label(headingFrame1, text="DELETE BOOK", bg='black', fg='white', font=('Courier',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)

    labelFrame = Frame(droot,bg='black')
    labelFrame.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.5)
    lb1 = Label(labelFrame,text="BOOK ID", bg='black', fg='white')
    lb1.place(relx=0.05,rely=0.3)
    info1 = Entry(labelFrame)
    info1.place(relx=0.3,rely=0.3, relwidth=0.62)
    SubmitBtn = Button(droot,text="DELETE",bg='#d1ccc0', fg='black',command=submit2)
    SubmitBtn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)
    QuitBtn=Button(droot,text="QUIT",bg='#d1ccc0', fg='black',command=Quit1)
    QuitBtn.place(relx=0.5,rely=0.9, relwidth=0.18,relheight=0.08)

def submit2():
    v1=info1.get()
    c1.execute("use db")
    c1.execute("select id from book")
    t1=c1.fetchall()
    if ((v1),) in t1:
        st1="delete from book where id="+v1
        c1.execute(st1)
        c2.commit()
        droot.destroy()
        messagebox.showinfo("ERROR","THE GIVEN BOOK IS DELETED")
    else:
        messagebox.showerror("ERROR","THE GIVEN BOOK ID DOES NOT EXIST")
        droot.destroy()
def Quit1():
    droot.destroy()

def book_details():
    Quit9()
    groot=Tk()
    groot.title("library")
    groot.minsize(width=400,height=400)
    groot.geometry("600x500")
    h = Scrollbar(groot, orient = 'horizontal')
    h.pack(side = BOTTOM, fill = X)
    v = Scrollbar(groot)
    v.pack(side = RIGHT, fill = Y)
    t = Text(groot, width = 20, height = 20, wrap = NONE,xscrollcommand = h.set,yscrollcommand = v.set)
    c1.execute("use db")
    c1.execute("select * from book")
    t19=c1.fetchall()
    i=0
    c1.execute("select count(id) from book")
    t20=c1.fetchall()
    print(t20)
    v1=int(t20[0][0])
    print(v1)
    for i in range(0,v1):
        t.insert(END,t19[i][0]+'\t'+t19[i][1]+'\t'+t19[i][2]+'\t'+t19[i][3]+'\t'+t19[i][4]+"\n")
    t.pack(side=TOP, fill=X)
    h.config(command=t.xview)
    v.config(command=t.yview)

def submit6():
    global c1,c2,lb2
    v1=info1.get()
    if v1.isdigit():
        c1.execute("use db")
        c1.execute("select id from book")
        t22=c1.fetchall()
        if ((v1),) in t22:
            c1.execute("select * from book where id = "+v1)
            t21=c1.fetchall()
            print(t21)
            lb2 = Label(labelFrame,text="BOOK ID : "+v1+"\nTITLE : "+t21[0][1]+"\nAUTHOR : "+t21[0][2]+"\nPUBLICATION : "+t21[0][3]+"\nYR. OF PUBLICATION : "+t21[0][4]+"\nSTATUS : "+t21[0][5], bg='black', fg='white', font=('Courier',15))
            lb2.place(relx=0.2,rely=0.2)
        else:
            messagebox.showerror("error","THE BOOK ID DOES NOT EXIST")
    else:
        messagebox.showerror("error","ENTER A VALID BOOK ID")

def searchin2():
    global c1,c2,info2,labelFrame1,hroot
    labelFrame1 = Frame(hroot,bg='black')
    labelFrame1.place(relx=0.05,rely=0.2,relwidth=0.9,relheight=0.6)
    lb3 = Label(labelFrame1,text="TITLE", bg='black', fg='white')
    lb3.place(relx=0.02,rely=0.1)
    info2 = Entry(labelFrame1)
    info2.place(relx=0.14,rely=0.1, relwidth=0.62)
    btn2=Button(hroot,text="CLICK ME TO SEARCH BY BOOK ID",bg='#d1ccc0', fg='black',command=searchin1)
    btn2.place(relx=0.23,rely=0.9, relwidth=0.3,relheight=0.08)
    SubmitBtn1 = Button(labelFrame1,text="SEARCH",bg='#d1ccc0', fg='black',command=submit7)
    SubmitBtn1.place(relx=0.8,rely=0.1, relwidth=0.18,relheight=0.075)
    QuitBtn1=Button(hroot,text="QUIT",bg='#d1ccc0', fg='black',command=Quit6)
    QuitBtn1.place(relx=0.6,rely=0.9, relwidth=0.18,relheight=0.08)

def Quit6():
    hroot.destroy()

def submit7():
    v2=info2.get()
    v2=v2.upper()
    print(v2,"\n")
    c1.execute("use db")
    c1.execute("select title from book")
    t22=c1.fetchall()
    print(t22)
    if (((v2),),) in t22:
        print("yes")
        c1.execute("select * from book where title = "+v2)
        t21=c1.fetchall()
        lb4 = Label(labelFrame1,text="BOOK ID : "+t21[0][0]+"\nTITLE : "+t21[0][1]+"\nAUTHOR : "+t21[0][2]+"\nPUBLICATION : "+t21[0][3]+"\nYR. OF PUBLICATION : "+t21[0][4]+"\nSTATUS : "+t21[0][5], bg='black', fg='white', font=('Courier',15))
        lb4.place(relx=0.2,rely=0.2)
    else:
        messagebox.showerror("error","THE BOOK TITLE DOES NOT EXIST")
    
def searchin1():
    global hroot,info1,labelFrame,lb1,info1,btn1,SubmitBtn,QuitBtn
    #Quit9()
    hroot=Tk()
    hroot.title("delete")
    hroot.minsize(width=400,height=400)
    hroot.geometry("600x500")
    headingFrame1 = Frame(hroot,bg="#FFBB00",bd=5)
    headingFrame1.place(relx=0.2,rely=0.01,relwidth=0.6,relheight=0.16)
    headingLabel = Label(headingFrame1, text="SEARCH BOOK BY ID", bg='black', fg='white', font=('Courier',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
    labelFrame = Frame(hroot,bg='black')
    labelFrame.place(relx=0.05,rely=0.2,relwidth=0.9,relheight=0.6)
    lb1 = Label(labelFrame,text="BOOK ID", bg='black', fg='white')
    lb1.place(relx=0.02,rely=0.1)
    info1 = Entry(labelFrame)
    info1.place(relx=0.14,rely=0.1, relwidth=0.62)
    btn1=Button(hroot,text="CLICK ME TO SEARCH BY TITLE",bg='#d1ccc0', fg='black',command=searchin2)
    btn1.place(relx=0.23,rely=0.9, relwidth=0.3,relheight=0.08)
    SubmitBtn = Button(labelFrame,text="SEARCH",bg='#d1ccc0', fg='black',command=submit6)
    SubmitBtn.place(relx=0.8,rely=0.1, relwidth=0.18,relheight=0.075)
    QuitBtn=Button(hroot,text="QUIT",bg='#d1ccc0', fg='black',command=Quit7)
    QuitBtn.place(relx=0.6,rely=0.9, relwidth=0.18,relheight=0.08)

def Quit7():
    hroot.destroy()

