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
def go1():
    global name1,add,pno,mno,name,entry3,entry4,entry5,entry1,entry12,membershipno
    add=entry3.get()
    pno=entry4.get()
    mno=entry5.get()
    name1=entry12.get()
    c1.execute('update membership_register set Member_Name=\''+(str(name1)).upper()+'\',Member_address=\''+str(add)+'\',Mobile_number='+str(mno)+',Phone_number='+(pno)+' where MembershipNo=\''+str(membershipno)+'\'')
    c2.commit()
    messagebox.showinfo('SUCCESS','Succesfully Updated')
    vroot2.destroy()
    
def go():
    global en1,en2,m,n,ad,ds,de,fees,v5
    nam2=en1.get()
    me=en2.get()
    print(nam2)
    print(me)
    nam2=nam2.upper()
    me=str(me)
    c1.execute('select Member_Name,MembershipNo from membership_register')
    data4=c1.fetchall()
    t=(nam2,me)
    v3.destroy()
    if t in data4:
        c1.execute('select * from membership_register where MembershipNo = '+me)
        d=c1.fetchall()
        for i in d:
            m,n,ad,pn,mn,ds,de,fees=i
        v5=Tk()
        v5.title('Search Member Details')
        v5.geometry('600x500')
        hfr5=Frame(master=v5,bg="#FFBB00",bd=5)
        hfr5.place(relx=0.3,rely=0,relwidth=0.4,relheight=0.17)
        head1=Label(text='Member Details',master=hfr5,bg='black',fg='white',font=('Courier',15))
        fr1=Frame(master=v5,bg='black')
        head1.place(relx=0,rely=0,relwidth=1,relheight=1)
        labe2=Label(text='Membership No:',master=fr1,bg='black',fg='white')
        head1.place(relx=0,rely=0,relwidth=1,relheight=1)
        entr1=Label(text=m,master=fr1)
        labe2.place(relx=0.01,rely=0.05)
        entr1.place(relx=0.28,rely=0.05,relwidth=0.7)
        labe3=Label(text='Name:',master=fr1,bg='black',fg='white')
        labe3.place(relx=0.01,rely=0.19)
        entr2=Label(text=n,master=fr1)
        entr2.place(relx=0.28,rely=0.19,relwidth=0.7)
        labe4=Label(text='Address:',master=fr1,bg='black',fg='white')
        entr3=Label(text=ad,master=fr1)
        labe5=Label(text='Phone No:',master=fr1,bg='black',fg='white')
        entr4=Label(text=pn,master=fr1)
        labe6=Label(text='Mobile No:',master=fr1,bg='black',fg='white')
        entr5=Label(text=mn,master=fr1)
        labe7=Label(text='Date of start of membership',master=fr1,bg='black',fg='white')
        entr6=Label(fr1,text=ds)
        labe8=Label(fr1,text='Date of expiry of membership',bg='black',fg='white')
        entr7=Label(fr1,text=de)
        labe4.place(relx=0.02,rely=0.33)
        entr3.place(relx=0.28,rely=0.33,relwidth=0.5)
        labe5.place(relx=0.02,rely=0.47)
        entr4.place(relx=0.28,rely=0.47,relwidth=0.5)
        labe6.place(relx=0.02,rely=0.61)
        entr5.place(relx=0.28,rely=0.61,relwidth=0.5)
        labe7.place(relx=0.02,rely=0.75)
        entr6.place(relx=0.28,rely=0.75,relwidth=0.5)
        labe8.place(relx=0.02,rely=0.89)
        entr7.place(relx=0.28,rely=0.89,relwidth=0.5)
        fr1.place(relx=0.05,rely=0.2,relwidth=0.9,relheight=0.7)
        qbtn1=Button(text='QUIT',master=v5,bg='#d1ccc0', fg='black',command=quit9)
        qbtn1.place(relx=0.4,rely=0.92, relwidth=0.18,relheight=0.06)
        #messagebox.showinfo('','Member Details Found')
    else:
        messagebox.showerror('Error!',' Member Name NOT Found')
def quit9():
    v5.destroy()
def search():
    global nam2,me,en1,en2,v3
    window.destroy()
    v3=Tk()
    v3.title('Searching Member Details')
    v3.minsize(height=400,width=400)
    v3.geometry('600x500')
    fc=Frame(master=v3,bg='black')
    hfr4=Frame(v3,bg="#FFBB00",bd=5)
    h1=Label(text='Search Member Details',master=hfr4,bg='black',fg='white',font=('Courier',15))
    h1.place(relx=0,rely=0,relwidth=1,relheight=1)
    hfr4.place(relx=0.25,rely=0,relwidth=0.5,relheight=0.2)
    fc.place(relx=0.15,rely=0.4,relwidth=0.75,relheight=0.25)
    la2=Label(text='Name:',master=fc,bg='black',fg='white')
    en1=Entry(master=fc)
    la3=Label(text='Membership No:',master=fc,bg='black',fg='white')
    en2=Entry(master=fc)
    bt0=Button(text='SUBMIT',master=v3,command=go,bg='#d1ccc0', fg='black')
    qb=Button(text='QUIT',master=v3,bg='#d1ccc0', fg='black',command=q4)
    la2.place(relx=0.05,rely=0.25)
    en1.place(relx=0.3,rely=0.25, relwidth=0.62)
    la3.place(relx=0.05,rely=0.5)
    en2.place(relx=0.3,rely=0.5, relwidth=0.62)
    bt0.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)
    qb.place(relx=0.5,rely=0.9, relwidth=0.18,relheight=0.08)
    
def q4():
    v3.destroy()
    
def new():
    global name,add,mno,pno,e1,e3,e4,e5,v4
    v4=Tk()
    v4.title('New Membership')
    v4.minsize(height=400,width=400)
    v4.geometry('600x500')
    hfr3=Frame(v4,bg="#FFBB00",bd=5)
    l1=Label(text='New Membership',master=hfr3,bg='black',fg='white',font=('Courier',18))
    l1.place(relx=0,rely=0,relwidth=1,relheight=1)
    hfr3.place(relx=0.25,rely=0,relwidth=0.5,relheight=0.2)
    f1=Frame(master=v4,bg='black')
    l3=Label(text='Name:',master=f1,bg='black',fg='white',font=(10))
    e1=Entry(master=f1)
    l3.place(relx=0.02,rely=0.1)
    e1.place(relx=0.3,rely=0.1,relwidth=0.65)
    l4=Label(text='Address:',master=f1,bg='black',fg='white',font=(10))
    e3=Entry(master=f1)
    l5=Label(text='Phone No:',master=f1,bg='black',fg='white',font=(10))
    e4=Entry(master=f1)
    l6=Label(text='Mobile No:',master=f1,bg='black',fg='white',font=(10))
    e5=Entry(master=f1)
    l4.place(relx=0.02,rely=0.25)
    e3.place(relx=0.3,rely=0.25,relwidth=0.65)
    l5.place(relx=0.02,rely=0.4)
    e4.place(relx=0.3,rely=0.4,relwidth=0.65)
    l6.place(relx=0.02,rely=0.55)
    e5.place(relx=0.3,rely=0.55,relwidth=0.65)
    f1.place(relx=0.2,rely=0.4,relwidth=0.65,relheight=0.4)
    btn6=Button(text='SUBMIT',master=v4,bg='#d1ccc0', fg='black',command=sub1)
    qbtn=Button(text='QUIT',master=v4,bg='#d1ccc0', fg='black',command=q3)
    btn6.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)
    qbtn.place(relx=0.5,rely=0.9, relwidth=0.18,relheight=0.08)
    name=e1.get()
    add=e3.get()
    pno=e4.get()
    mno=e5.get()
    

def q3():
    v4.destroy()
    q8()
    
def sub1():
    
    global name,add,pno,mno,memno,e1,e3,e4,e5
    q8()
    name=e1.get()
    add=e3.get()
    pno=e4.get()
    mno=e5.get()
    v4.destroy()
    c1.execute('select Member_Name from membership_register')
    names=c1.fetchall()
    if (name,) in names:
        messagebox.showerror('ERROR','Existing Member')
        
    else:
        
        c1.execute('select max(MembershipNo) from membership_register')
        memno=c1.fetchall()
        if memno[0][0]==None:
            m=10000000
        else:
            m=int(memno[0][0])+1
        date0=date.today()
        date1=str(date0.year)+'-'+str(date0.month)+'-'+str(date0.day)
        date2=str((date0.year)+2)+'-'+str(date0.month)+'-'+str(date0.day)
        com='insert into membership_register values('+str(m)+',\''+str(name.upper())+'\',\''+str(add.upper())+'\','+str(pno)+','+str(mno)+',\''+date1+"','"+date2+'\',3000)'
        c1.execute(com)
        c1.execute('commit')
        messagebox.showinfo('SUCCESS','Successfully Added')
        

def sub():
    global name2,mem
    name2=ent1.get()
    name2=name2.upper()
    mem=str(ent2.get())
    c1.execute('select Member_Name,MembershipNo from membership_register')
    data3=c1.fetchall()
    t=(name2,mem)
    if t in data3:
        c1.execute('delete from membership_register where MembershipNo='+str(mem))
        c1.execute('Commit')
        messagebox.showinfo('SUCCESS','Successfully Deleted')
        vroot3.destroy()
    else:
        messagebox.showerror('ERROR','Wrong Credentials')
        vroot3.destroy()

def delete():
    global name2,memno,ent1,ent2,vroot3
    vroot3=Tk()
    vroot3.title('Deleting Member Details')
    vroot3.minsize(height=400,width=400)
    vroot3.geometry('600x500')
    framec=Frame(master=vroot3,bg='black')
    hfr2=Frame(vroot3,bg="#FFBB00",bd=5)
    headinglab1=Label(text='DELETE MEMBER DETAILS',master=hfr2,bg='black',fg='white',font=(15))
    headinglab1.place(relx=0,rely=0,relwidth=1,relheight=1)
    hfr2.place(relx=0.25,rely=0,relwidth=0.5,relheight=0.2)
    framec.place(relx=0.15,rely=0.4,relwidth=0.75,relheight=0.25)
    lab2=Label(text='Name:',master=framec,bg='black',fg='white',font=(8))
    ent1=Entry(master=framec)
    lab3=Label(text='Membership No:',master=framec,bg='black',fg='white',font=(8))
    ent2=Entry(master=framec)
    btn0=Button(text='SUBMIT',master=vroot3,command=sub,bg='#d1ccc0', fg='black')
    qtbtn=Button(text='QUIT',master=vroot3,bg='#d1ccc0', fg='black',command=q2)
    lab2.place(relx=0.02,rely=0.2)
    ent1.place(relx=0.4,rely=0.2, relwidth=0.5)
    lab3.place(relx=0.02,rely=0.4)
    ent2.place(relx=0.4,rely=0.45, relwidth=0.5)
    btn0.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)
    qtbtn.place(relx=0.5,rely=0.9, relwidth=0.18,relheight=0.08)
    
    window.destroy()

def q2():
    vroot3.destroy()
    window.destroy()

def modify():
    global entry1,membershipno,entry2,vroot1
    vroot1=Tk()
    vroot1.title('Modify Memeber Details')
    vroot1.minsize(height=400,width=400)
    vroot1.geometry('600x500')
    hefr1=Frame(vroot1,bg="#FFBB00",bd=5)
    hefr1.place(relx=0.25,rely=0,relwidth=0.5,relheight=0.2)
    label=Label(text='MODIFY USER DETAILS',master=hefr1,bg='black',fg='white',font=('Courier',15))
    label.place(relx=0,rely=0,relwidth=1,relheight=1)
    framea=Frame(master=vroot1,bg='black')
    framea.place(relx=0.15,rely=0.4,relwidth=0.75,relheight=0.25)
    label1=Label(text='Name:',master=framea,bg='black',fg='white',font=(10))
    entry1=Entry(master=framea)
    label2=Label(text='Membership No:',master=framea,bg='black',fg='white',font=(10))
    entry2=Entry(master=framea)
    label1.place(relx=0.02,rely=0.2)
    entry1.place(relx=0.4,rely=0.2, relwidth=0.4)
    label2.place(relx=0.02,rely=0.4)
    entry2.place(relx=0.4,rely=0.45, relwidth=0.4)
    btn5=Button(text='SUMBIT',master=vroot1,command=submit3,bg='#d1ccc0', fg='black')
    quitbtn1=Button(text='QUIT',master=vroot1,bg='#d1ccc0', fg='black',command=q1)
    btn5.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)
    quitbtn1.place(relx=0.5,rely=0.9, relwidth=0.18,relheight=0.08)

def q1():
    vroot1.destroy()

def submit3():
    global name,add,mno,pno,name1,membershipno,entry3,entry4,entry5,entry12,vroot2
    name=entry1.get()
    name=name.upper()
    membershipno=str(entry2.get())
    c1.execute('Select Member_Name,MembershipNo from membership_register')
    data1=c1.fetchall()
    if (name,membershipno) in data1:
        messagebox.showinfo('','Member Found')
        vroot1.destroy()
        vroot2=Tk()
        vroot2.title('Modify')
        vroot2.minsize(height=400,width=400)
        vroot2.geometry('600x500')
        hfr6=Frame(vroot2,bg="#FFBB00",bd=5)
        hfr6.place(relx=0.25,rely=0,relwidth=0.5,relheight=0.2)
        strvar1=StringVar()
        frameb=Frame(master=vroot2,bg='black')
        label2=Label(text='Enter New Details',master=hfr6,bg='black',fg='white',font=('Courier',15))
        label2.place(relx=0,rely=0,relwidth=1,relheight=1)
        label3=Label(text='Name:',master=frameb,bg='black',fg='white')
        label3.place(relx=0.05,rely=0.1)
        entry12=Entry(master=frameb)
        entry12.place(relx=0.3,rely=0.1,relwidth=0.65)
        label4=Label(text='Address:',master=frameb,bg='black',fg='white')
        entry3=Entry(master=frameb)
        label5=Label(text='Phone No:',master=frameb,bg='black',fg='white')
        entry4=Entry(master=frameb)
        label6=Label(text='Mobile No:',master=frameb,bg='black',fg='white')
        entry5=Entry(master=frameb)
        label4.place(relx=0.05,rely=0.3)
        entry3.place(relx=0.3,rely=0.3,relwidth=0.65)
        label5.place(relx=0.05,rely=0.5)
        entry4.place(relx=0.3,rely=0.5,relwidth=0.65)
        label6.place(relx=0.05,rely=0.7)
        entry5.place(relx=0.3,rely=0.7,relwidth=0.65)
        frameb.place(relx=0.2,rely=0.4,relwidth=0.65,relheight=0.4)
        btn6=Button(text='SUBMIT',master=vroot2,command=go1,bg='#d1ccc0', fg='black')
        qbtn3=Button(vroot2,text='QUIT',bg='#d1ccc0', fg='black',command=q6)
        btn6.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)
        qbtn3.place(relx=0.5,rely=0.9, relwidth=0.18,relheight=0.08)
        add=entry3.get()
        pno=entry4.get()
        mno=entry5.get()
        name1=entry12.get()
        window.destroy()
    else:
        messagebox.showerror('Error!',' WRONG CREDENTIALS')
        window.destroy()
        

def q6():
    vroot2.destroy()

def s1():
    global mmm,n2
    q8()
    n2=(et1.get()).upper()
    mmm=(et2.get())
    t1=(mmm,n2)
    dat0=date.today()
    dat1=str(dat0.year)+'-'+str(dat0.month)+'-'+str(dat0.day)
    dat2=str((dat0.year)+2)+'-'+str(dat0.month)+'-'+str(dat0.day)
    d1=c1.execute('select MembershipNo,Member_Name from membership_register')
    d2=c1.fetchall()
    print(d2,t1)
    if t1 in d2:
        c1.execute('update membership_register set Dateof_start_of_membership=\''+str(dat1)+'\',Date_of_expiry_of_membership=\''+str(dat2)+'\' where MembershipNo='+str(mmm))
        c1.execute('commit')
        messagebox.showinfo('','Membership Renewed')
        v6.destroy()
    else:
        messagebox.showerror('ERROR','Wrong Credentials')
        v6.destroy()

def renew():
    global n2,memn,et1,et2,v6
    v6=tk.Tk()
    v6.title('Renew Membership')
    v6.minsize(height=400,width=400)
    v6.geometry('600x500')
    hfr2=Frame(master=v6,bg="#FFBB00",bd=5)
    hlab1=Label(text='Renew Membership',master=hfr2,bg='black',fg='white',font=('Courier',15))

    hlab1.place(relx=0,rely=0,relwidth=1,relheight=1)
    hfr2.place(relx=0.25,rely=0,relwidth=0.5,relheight=0.2)
    fr2=Frame(v6,bg='black')
    fr2.place(relx=0.2,rely=0.4,relwidth=0.6,relheight=0.25)
    lb2=Label(text='Name:',master=fr2,bg='black',fg='white')
    et1=Entry(master=fr2)
    lb3=Label(text='Membership No:  ',master=fr2,bg='black',fg='white')
    et2=Entry(master=fr2)
    b0=Button(text='SUBMIT',master=v6,bg='#d1ccc0', fg='black',command=s1)
    quitbtn=Button(text='QUIT',master=v6,bg='#d1ccc0', fg='black',command=q5)
    lb2.place(relx=0.05,rely=0.2)
    et1.place(relx=0.3,rely=0.2, relwidth=0.62)
    lb3.place(relx=0.03,rely=0.4)
    et2.place(relx=0.3,rely=0.4, relwidth=0.62)
    b0.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)
    quitbtn.place(relx=0.5,rely=0.9, relwidth=0.18,relheight=0.08)
    n2=et1.get()
    memn=et2.get()

def q5():
    v6.destroy()

def member_regis(cur,con):
    global window,c1,c2
    c1=cur
    c2=con
    window=Tk()
    window.title('Library')
    window.geometry('600x500')
    window.minsize(width=400,height=400)
    frame1=Frame(master=window,bg="#FFBB00",bd=5)
    text=Label(text='Membership Register',master=frame1,bg='black',fg='white',font=('Courier',15))
    text.place(relx=0,rely=0,relwidth=1,relheight=1)
    frame1.place(relx=0.2,rely=0.1,relwidth=0.6,relheight=0.16)
    btn1=Button(text='Modify User Details',master=window,command=modify,bg='black',fg='white')
    btn2=Button(text='New Memebership',master=window,command=new,bg='black',fg='white')
    btn3=Button(text='Delete Membership',master=window,command=delete,bg='black',fg='white')
    btn4=Button(text='Search Member',master=window,command=search,bg='black',fg='white')
    btn=Button(text='Renew Membership',master=window,command=renew,bg='black',fg='white')
    btn1.place(relx=0.28,rely=0.7, relwidth=0.45,relheight=0.1)
    btn2.place(relx=0.28,rely=0.4, relwidth=0.45,relheight=0.1)
    btn3.place(relx=0.28,rely=0.8, relwidth=0.45,relheight=0.1)
    btn4.place(relx=0.28,rely=0.6, relwidth=0.45,relheight=0.1)
    btn.place(relx=0.28,rely=0.5, relwidth=0.45,relheight=0.1)
    qtbt=Button(window,text='QUIT',bg='#d1ccc0', fg='black',command=q8)
    qtbt.place(relx=0.45,rely=0.93,relwidth=0.1,relheight=0.06)

def q8():
    window.destroy()
