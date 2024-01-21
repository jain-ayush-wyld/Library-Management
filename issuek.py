from ctypes import *
from tkinter import *
from tkinter import messagebox
import mysql
import mysql.connector
from tkinter import *
from tkinter import messagebox
import datetime as dt
from datetime import date
from datetime import timedelta
def book_issue(cur,con):
    
    global info1,info2,eroot,c1,c2
    c1=cur
    c2=con
    eroot=Tk()
    eroot.title("library")
    eroot.minsize(width=400,height=400)
    eroot.geometry("600x500")
    headingFrame1 = Frame(eroot,bg="#FFBB00",bd=5)
    headingFrame1.place(relx=0.2,rely=0.1,relwidth=0.6,relheight=0.16)

    headingLabel = Label(headingFrame1, text="ISSUE BOOK", bg='black', fg='white', font=('Courier',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
    labelFrame = Frame(eroot,bg='black')
    labelFrame.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.5)
    lb1 = Label(labelFrame,text="Book ID", bg='black', fg='white')
    lb1.place(relx=0.05,rely=0.3)
    info1 = Entry(labelFrame)
    info1.place(relx=0.3,rely=0.3, relwidth=0.62)
    lb2 = Label(labelFrame,text="Member ID", bg='black', fg='white')
    lb2.place(relx=0.05,rely=0.4)
    info2 = Entry(labelFrame)
    info2.place(relx=0.3,rely=0.4, relwidth=0.62)
    SubmitBtn = Button(eroot,text="ISSUE",bg='#d1ccc0', fg='black',command=submit4)
    SubmitBtn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)
    QuitBtn=Button(eroot,text="QUIT",bg='#d1ccc0', fg='black',command=Quit3)
    QuitBtn.place(relx=0.5,rely=0.9, relwidth=0.18,relheight=0.08)

def Quit3():
    eroot.destroy()

def submit4():
    global c1,c2
    v1=info1.get()
    v2=info2.get()
    v2=v2.upper()
    print(v1)
    print(v2)
    Quit3()
    if v1=='' or v2=='':
        messagebox.showerror("ERROR","PL. ENTER BOTH THE ENTRIES")
    else:
        c1.execute("use db")
        c1.execute("select id from book")
        t8=c1.fetchall()
        c1.execute("select MembershipNo from membership_register")
        t9=c1.fetchall()
        
        temp1=(v1,)
        temp2=(v2,)
        
        if temp2 in t9:
            if temp1 in t8:
                
        
                c1.execute("select status from book where id="+v1)
                t10=c1.fetchall()
                print(t10)
                temp3=('avialable'),
                c1.execute("select Date_of_expiry_of_membership from membership_register where MembershipNo="+v2)
                t11=c1.fetchall()
                if date.today() <= t11[0][0]:
                    date0=date.today()
                    date2=date0 + timedelta(days=15)
                    if date2 <= t11[0][0]:
                            
                        if temp3 in t10 :
                            c1.execute("update book set status='issued' where id="+v1)
                            c2.commit()
                            date0=str(date0.year)+'-'+str(date0.month)+'-'+str(date0.day)
                            date2=str(date2.year)+'-'+str(date2.month)+'-'+str(date2.day)
                            c1.execute("select max(SerialNumber) from issue")
                            j=c1.fetchall()
                            print(j)
                            if j[0][0]==None:
                                j=1
                            else:
                                j=int(j[0][0])+1
                            str1=str(j)
                            print(j)
                            c1.execute("insert into issue values('"+v1+"','"+v2+"','"+date0+"','"+date2+"','"+date2+"','"+str1+"')") 
                            c2.commit()
                            messagebox.showinfo("s","book has been success fully issued")
                        else:
                            messagebox.showinfo("s","book has been ALREADY issued")
                    else:
                        messagebox.showinfo("error","BOOK CAN'T BE ISSUED AS \nDATE OF BOOK RETURN \nMORE THAN DATE OF EXPIRY OF MEMBERSHIP")
                else:
                    messagebox.showinfo("error","member has expired")
            else:
                messagebox.showerror("error","CHECK THE ENTERED DETAILS")
        else:
            messagebox.showerror("error","CHECK THE ENTERED DETAILS")
def book_return(cur,con):
    global info1,info2,froot,c1,c2
    c1=cur
    c2=con
    
    froot=Tk()
    froot.title("library")
    froot.minsize(width=400,height=400)
    froot.geometry("600x500")
    headingFrame1 = Frame(froot,bg="#FFBB00",bd=5)
    headingFrame1.place(relx=0.2,rely=0.1,relwidth=0.6,relheight=0.16)

    headingLabel = Label(headingFrame1, text="RETURN BOOK", bg='black', fg='white', font=('Courier',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
    labelFrame = Frame(froot,bg='black')
    labelFrame.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.5)
    lb1 = Label(labelFrame,text="BOOK ID", bg='black', fg='white')
    lb1.place(relx=0.05,rely=0.3)
    info1 = Entry(labelFrame)
    info1.place(relx=0.3,rely=0.3, relwidth=0.62)
    lb2 = Label(labelFrame,text="MEMBER ID", bg='black', fg='white')
    lb2.place(relx=0.05,rely=0.4)
    info2 = Entry(labelFrame)
    info2.place(relx=0.3,rely=0.4, relwidth=0.62)
    SubmitBtn = Button(froot,text="RETURN",bg='#d1ccc0', fg='black',command=submit5)
    SubmitBtn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)
    QuitBtn=Button(froot,text="QUIT",bg='#d1ccc0', fg='black',command=Quit4)
    QuitBtn.place(relx=0.5,rely=0.9, relwidth=0.18,relheight=0.08)

def Quit4():
    froot.destroy()
    
def submit5():
    v1=info1.get()
    v2=info2.get()
    
    froot.destroy()
    init=30
    if v1=='' or v2=='':
        messagebox.showerror("ERROR","PL. ENTER BOTH THE ENTRIES")
    else:
        c1.execute("use db")
        c1.execute("select id from book")
        t14=c1.fetchall()
        c1.execute("select MembershipNo from membership_register")
        t15=c1.fetchall()
        
        temp1=(v1),
        temp2=(v2),
        
        if temp2 in t15:
            if temp1 in t14:
                c1.execute("select bid from issue")
                t16=c1.fetchall()
                if t16==None:
                    messagebox.showerror("error","NO BOOKS HAVE BEEN ISSUED YET")
                else:
                    c1.execute("select status from book where id = "+v1)
                    t18=c1.fetchall()
                    temp5=("issued"),
                    if temp5 in t18:
                        date0=date.today()
                        date2=date(int(date0.year),int(date0.month),int(date0.day))
                        c1.execute("select due_date_of_return from issue where bid="+v1+" and due_date_of_return = returned_date")
                        t17=c1.fetchall()
                        print(t17)
                        st1=str(t17[0][0])
                        date1=date(int(st1[0:4]),int(st1[5:7]),int(st1[8:10]))
                        print("date 1",date1)
                        print("date 2",date2)
                        delta = date2 - date1
                        print(delta)
                        if delta.days <=0:
                            fine=0
                            date3=str(date0.year)+'-'+str(date0.month)+'-'+str(date0.day)
                            messagebox.showinfo("fine","YOUR FINE IS RUPPEES : "+str(fine))
                            c1.execute("update issue set returned_date = '"+date3+"' where bid = "+v1)
                            c2.commit()
                            c1.execute("update book set status = 'avialable' where id="+v1)
                            c2.commit()
                        else:
                            date3=str(date0.year)+'-'+str(date0.month)+'-'+str(date0.day)
                            fine=init*delta.days
                            messagebox.showinfo("fine","YOUR FINE IS RUPPEES :"+str(fine))
                            c1.execute("update issue set returned_date = '"+date3+"' where bid = "+v1)
                            c2.commit()
                            c1.execute("update book set status = 'avialable' where id="+v1)
                            c2.commit()
                    else:
                        messagebox.showerror("error","THE BOOK HAS NOT BEEN ISSUED YET")
            else:
                messagebox.showerror("error","CHECK THE ENTERED DETAILS")
        else:
            messagebox.showerror("error","CHECK THE ENTERED DETAILS")
