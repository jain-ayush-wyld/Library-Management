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
from issuek import book_issue,Quit3,submit4,book_return,Quit4,submit5
from memberk import go1,go,quit9,search,q4,new,q3,sub1,sub,delete,q2,modify,q1,submit3,q6,s1,renew,q5,member_regis,q8
from bookk import book_regis,Quit9,addbook,testVal,submit1,Quit,deletebook,submit2,Quit1,book_details,submit6,searchin2,Quit6,submit7,searchin1,Quit7
def submit():
    global username,passcode,cur,con
    username = info1.get()
    passcode = info2.get()        
    '''
    con=mysql.connector.connect(host='localhost',user=username,password=passcode)
    messagebox.showinfo("logged in","YOU HAVE SUCCESSFULLY LOGGED IN ")
    cur=con.cursor() 
    cur.execute("create database if not exists db")
    cur.execute("use db")
    vroot.destroy()
    btn1.destroy()
    cursor=con.cursor()
    btn2 = Button(root,text="MEMBERSHIP REGISTER",bg='black', fg='white',command=member_regis)
    btn2.place(relx=0.28,rely=0.4, relwidth=0.45,relheight=0.1)
    btn3 = Button(root,text="BOOK REGISTER",bg='black', fg='white',command=book_regis)
    btn3.place(relx=0.28,rely=0.5, relwidth=0.45,relheight=0.1)
    btn4 = Button(root,text="ISSUE",bg='black', fg='white',command=book_issue)
    btn4.place(relx=0.28,rely=0.6, relwidth=0.45,relheight=0.1)
    btn5 = Button(root,text="RETURN",bg='black', fg='white',command=book_return)
    btn5.place(relx=0.28,rely=0.7, relwidth=0.45,relheight=0.1)
    QuitBtn=Button(root,text="QUIT",bg='#d1ccc0', fg='black',command=Quit8)
    QuitBtn.place(relx=0.4,rely=0.9, relwidth=0.18,relheight=0.08)
    '''
    try:
        con=mysql.connector.connect(host='localhost',user=username,password=passcode)
        messagebox.showinfo("logged in","YOU HAVE SUCCESSFULLY LOGGED IN ")

        cur=con.cursor() 
        cur.execute("create database if not exists db")
        cur.execute("use db")
        cur.execute("show tables")
        t1=cur.fetchall()
        
        if (("issue"),) in t1:
            cur.execute("describe issue")
            t12=cur.fetchall()
            if t12==[('bid', b'char(20)', 'NO', None, ''), ('memid', b'char(20)', 'YES', '', None, ''), ('date_of_issue', b'date', 'YES', '', None, ''), ('due_date_of_return', b'date', 'YES', '', None, ''), ('returned_date', b'date', 'YES', '', None, '')]:
                qwertyuiosdfghj=0
                
            else:
                cur.execute("delete from issue")
                con.commit()
                cur.execute("drop table issue")
                cur.execute("create table issue(bid char(20),memid char(20),date_of_issue date,due_date_of_return date,returned_date date)")
        else:
            cur.execute("create table issue(bid char(20),memid char(20),date_of_issue date,due_date_of_return date,returned_date date)")    

        
        if (("book"),) in t1:
            cur.execute("describe book")
            t2=cur.fetchall()
            if t2[0][0]=='id' and t2[0][1]==b'char(20)'and t2[1][0]=='title' and t2[1][1]==b'char(20)' and t2[2][0]=='author' and t2[2][1]==b'char(20)' and t2[3][0]=='publication' and t2[3][1]==b'char(20)' and t2[4][0]=='yr_publi' and t2[4][1]==b'char(20)' and t2[5][0]=='status' and t2[5][1]==b'char(9)' and t2[5][4]==b'avialable':
                vgsvdfvfdvdfvdbmhjbdfjhvdfjhvbdjhehj=0
                print("check 3")
            
            else:
                cur.execute("delete from book")
                
                cur.execute("drop table book")
                con.commit()
                cur.execute("create table book(id char(20) primary key,title char(20),author char(20),publication char(20),yr_publi char(20),status char(9) default 'avialable')")
        else:
            cur.execute("create table book(id char(20) primary key,title char(20),author char(20),publication char(20),yr_publi char(20),status char(9) default 'avialable')")

        if (("membership_register"),) in t1:
            cur.execute("describe membership_register")
            t3=cur.fetchall()
            if t3==[('MembershipNo', b'char(25)', 'NO', 'PRI', None, ''), ('Member_Name', b'varchar(25)', 'YES', '', None, ''), ('Member_address', b'varchar(60)', 'NO', '', None, ''), ('Phone_number', b'decimal(10,0)', 'NO', '', None, ''), ('Mobile_number', b'decimal(10,0)', 'YES', '', None, ''), ('Dateof_start_of_membership', b'date', 'NO', '', None, ''), ('Date_of_expiry_of_membership', b'date', 'NO', '', None, ''), ('Membership_Fees', b'decimal(10,0)', 'YES', '', None, '')]:
                asdfghjksdfghjdfgh=0
            else:
                cur.execute("delete from membership_register")
                cur.execute("drop table membership_register")
                cur.execute("create table membership_register(MembershipNo char(25) primary key,Member_Name varchar(25) null,Member_address varchar(60) not null,Phone_number decimal(10,0) not null,Mobile_number decimal(10,0) null,Dateof_start_of_membership date  not null,Date_of_expiry_of_membership date not null,Membership_Fees decimal(10,0) null)")
                cur.execute("commit")
                
        else:
            cur.execute("create table membership_register(MembershipNo char(25) primary key,Member_Name varchar(25) null,Member_address varchar(60) not null,Phone_number decimal(10,0) not null,Mobile_number decimal(10,0) null,Dateof_start_of_membership date  not null,Date_of_expiry_of_membership date not null,Membership_Fees decimal(10,0) null)")
        
        vroot.destroy()
        btn1.destroy()
        cursor=con.cursor()
        btn2 = Button(root,text="MEMBERSHIP REGISTER",bg='black', fg='white',command=cmd1)
        btn2.place(relx=0.28,rely=0.4, relwidth=0.45,relheight=0.1)
        btn3 = Button(root,text="BOOK REGISTER",bg='black', fg='white',command=cmd2)
        btn3.place(relx=0.28,rely=0.5, relwidth=0.45,relheight=0.1)
        btn4 = Button(root,text="ISSUE",bg='black', fg='white',command=cmd3)
        btn4.place(relx=0.28,rely=0.6, relwidth=0.45,relheight=0.1)
        btn5 = Button(root,text="RETURN",bg='black', fg='white',command=cmd4)
        btn5.place(relx=0.28,rely=0.7, relwidth=0.45,relheight=0.1)
        QuitBtn=Button(root,text="QUIT",bg='#d1ccc0', fg='black',command=Quit8)
        QuitBtn.place(relx=0.4,rely=0.9, relwidth=0.18,relheight=0.08)
    except:
        messagebox.showerror("ERROR","PASSWORD/USERNAME IS INCORRECT")
        vroot.destroy()

def cmd1():
    member_regis(cur,con)
def cmd2():
    book_regis(cur,con)
def cmd3():
    book_issue(cur,con)
def cmd4():
    book_return(cur,con)

def Quit8():
    root.destroy()

def test():
    
    
   
    #ANY VARIABLE OR NAME TO BE PUT HERE
    global info1,info2,lb1,lb2,root,vroot,username,passcode,cursor,btn1,xroot

    vroot=Tk()
    vroot.title("library 1")
    vroot.minsize(width=400,height=400)
    vroot.geometry("600x500")
    
    labelFrame = Frame(vroot,bg='black')
    labelFrame.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.5)   
        
    lb1 = Label(labelFrame,text="USER ID ", bg='black', fg='white')
    lb1.place(relx=0.05,rely=0.5)
    info1 = Entry(labelFrame)
    info1.place(relx=0.3,rely=0.5, relwidth=0.62)

    lb2 = Label(labelFrame,text="PASSWORD ", bg='black', fg='white')
    lb2.place(relx=0.05,rely=0.6)
    info2 = Entry(labelFrame)
    info2.place(relx=0.3,rely=0.6, relwidth=0.62)
    SubmitBtn = Button(vroot,text="Login",bg='#d1ccc0', fg='black',command=submit)
    SubmitBtn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)
    QuitBtn=Button(vroot,text="CLOSE",bg='#d1ccc0', fg='black',command=Quit2)
    QuitBtn.place(relx=0.6,rely=0.9, relwidth=0.18,relheight=0.08)
    root.mainloop()

def Quit2():
    vroot.destroy()


############################################################################################################################

    
############################################################################################################################

root=Tk()
root.title("library")
root.minsize(width=400,height=400)
root.geometry("600x500")
same=True
n=0.25
str1='download1.jpg'
background_image = immage.open('download1.jpg')
canvas = Canvas(width=700, height=500)
canvas.pack(expand=YES, fill=BOTH)
image = ImageTk.PhotoImage(file="download1.jpg")
canvas.create_image(0, 0, image=image, anchor=NW)
headingFrame1 = Frame(root,bg="#FFBB00",bd=5)
headingFrame1.place(relx=0.2,rely=0.1,relwidth=0.6,relheight=0.16)
headingLabel = Label(headingFrame1, text="Welcome to \n Library Of Congress", bg='black', fg='white', font=('Courier',15))
headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
btn1 = Button(root,text="LOG IN TO MY SQL",bg='black', fg='white',command=test)
btn1.place(relx=0.28,rely=0.4, relwidth=0.45,relheight=0.1)
