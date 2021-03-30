from tkinter import *
import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',password="",database='banking')
mycursor=mydb.cursor()

root=Tk(className=' Akin Bank System')
root.geometry('1200x1200')
root['background']='#007BA7'
l0=Label(root,text='AKIN BANK',bg='cyan',cursor='star',fg='silver',width=100,relief='groove',underline='0',font='helvetica 16 bold italic').place(x='0',y='0')
l1=Label(text='Command Section of Bank',fg='indigo',bg='lime',width=20,font=('times',15,'bold'))
l1.place(x=200,y=50)

def createaccount():
    def insertdatabyentry():
        n=e4.get()
        a=e5.get()
        b=e6.get()
        p=e7.get()
        adr=e8.get()
        mob=e9.get()
        ins='insert into akininfo(name,age,balance,password,address,mobile_no) values (%s,%s,%s,%s,%s,%s)'
        datas=(n,a,b,p,adr,mob)
        mycursor.execute(ins,datas)
        mydb.commit()


    

    top=Toplevel()
    top.geometry('1200x1200')
    top['background']='#007BA7'
    l2=Label(top,text='AKIN BANK',bg='cyan',cursor='star',fg='silver',width=100,relief='groove',underline='0',font='helvetica 16 bold italic').place(x='0',y='0')    
    l3=Label(top,text='CREATE AN ACCOUNT',fg='purple',bg='lime',width=60,relief='ridge',font='bold').place(x='400',y='30')
    l4=Label(top,text='Name',bg='crimson',width=15,fg='orange',relief='sunken',pady=10,font='calibri 12 bold italic').place(x='20',y='80')
    l5=Label(top,text='Age',bg='crimson',width=15,fg='orange',relief='sunken',pady=10,font='calibri 12 bold italic').place(x='20',y='130')
    l6=Label(top,text='Balance',bg='crimson',width=15,fg='orange',relief='sunken',pady=10,font='calibri 12 bold italic').place(x='20',y='180')
    l7=Label(top,text='Password',bg='crimson',width=15,fg='orange',relief='sunken',pady=10,font='calibri 12 bold italic').place(x='20',y='230')
    l8=Label(top,text='Address',bg='crimson',width=15,fg='orange',relief='sunken',pady=10,font='calibri 12 bold italic').place(x='20',y='280')
    l9=Label(top,text='Mobile No.',bg='crimson',width=15,fg='orange',relief='sunken',pady=10,font='calibri 12 bold italic').place(x='20',y='330')
    
    e4=Entry(top,width=40,bd=10)
    e4.place(x='150',y='80')
    e5=Entry(top,width=40,bd=10)
    e5.place(x='150',y='130')
    e6=Entry(top,width=40,bd=10)
    e6.place(x='150',y='180')
    e7=Entry(top,show='*',width=40,bd=10)
    e7.place(x='150',y='230')
    e8=Entry(top,width=40,bd=10)
    e8.place(x='150',y='280')
    e9=Entry(top,width=40,bd=10)
    e9.place(x='150',y='330')
    b9=Button(top,text='Submit',bg='blue',fg='yellow',font='Arial 12 bold roman',height=2,width=20,command=insertdatabyentry).place(x='400',y='400')
   
    

    top.mainloop()

def showdetails():
    call=Toplevel()
    call.geometry('1200x1200')
    call['background']='#007BA7'
    def show():
        n=e1.get()
        p=e2.get()
        mycursor.execute("select * from akininfo where name='"+str(n)+"'and password='"+str(p)+"'")
        print(list(mycursor))

    def acc():
        n=e1.get()
        p=e2.get()
        mycursor.execute("select account_no from akininfo where name='"+str(n)+ "'and password='"+str(p)+"'")
        print(list(mycursor))
    def bal():
        n=e1.get()
        p=e2.get()
        mycursor.execute("select balance from akininfo where name='"+str(n)+"' and password='"+str(p)+"'")
        print(list(mycursor))
    l10=Label(call,text='AKIN BANK',bg='cyan',cursor='star',fg='silver',width=100,relief='groove',underline='0',font='helvetica 16 bold italic').place(x='0',y='0')    
    l11=Label(call,text='Name',bg='crimson',width=15,fg='orange',relief='ridge',pady=10,font='constantia 12 bold italic').place(x='20',y='80')
    l12=Label(call,text='Password',bg='crimson',width=15,fg='orange',relief='ridge',pady=10,font='constantia 12 bold italic').place(x='20',y='140')
    e1=Entry(call,width=40,bd=12)
    e1.place(x='180',y='80')
    e2=Entry(call,show='*',width=40,bd=12)
    e2.place(x='180',y='140')
    b10=Button(call,text='Show Full Account Details',bg='blue',fg='yellow',height=2,width=20,font='ebrima 10 bold italic',command=show).place(x='200',y='240')
    b11=Button(call,text='Show Account No.',bg='blue',fg='yellow',height=2,width=20,font='ebrima 10 bold italic',command=acc).place(x='200',y='300')
    b12=Button(call,text='Show Balance',bg='blue',fg='yellow',height=2,width=20,font='ebrima 10 bold italic',command=bal).place(x='200',y='360')
    call.mainloop()

def wbal():
    def withdraw():
        acc=e14.get()
        n=e15.get()
        p=e16.get()
        b=int(e17.get())
        mycursor.execute("update akininfo set balance=balance-"+str(b)+" where name='"+str(n)+"' and password='"+str(p)+"' and account_no="+str(acc))
        mydb.commit()
    tree=Toplevel()
    tree.geometry('1200x1200')
    tree['background']='#007BA7'
    l13=Label(tree,text='AKIN BANK',bg='cyan',cursor='star',fg='silver',width=100,relief='groove',underline='0',font='helvetica 16 bold italic').place(x='0',y='0')
    l14=Label(tree,text='Enter Account No.',bg='crimson',width=15,fg='orange',relief='ridge',pady=10,padx=50).place(x='20',y='80')
    l15=Label(tree,text='Enter Name',bg='crimson',width=15,fg='orange',relief='ridge',pady=10,padx=50).place(x='20',y='120')
    l16=Label(tree,text='Enter Password',bg='crimson',width=15,fg='orange',relief='ridge',pady=10,padx=50).place(x='20',y='160')    
    l17=Label(tree,text='Enter Amount to be Withdrawn',bg='crimson',width=15,fg='orange',relief='ridge',pady=10,padx=50).place(x='20',y='200') 


    e14=Entry(tree,width=40,bd=10)
    e14.place(x=250,y=80)
    e15=Entry(tree,width=40,bd=10)
    e15.place(x=250,y=120)
    e16=Entry(tree,width=40,bd=10)
    e16.place(x=250,y=160)
    e17=Entry(tree,width=40,bd=10)
    e17.place(x=250,y=200)
    b13=Button(tree,text='Initiate Transaction',bg='blue',fg='yellow',height=2,width=20,command=withdraw).place(x='200',y='360')
    tree.mainloop()

def dep():
    def deposit():
        acc=e14.get()
        n=e15.get()
        p=e16.get()
        b=int(e17.get())
        mycursor.execute("update akininfo set balance=balance+"+str(b)+" where name='"+str(n)+"' and password='"+str(p)+"' and account_no="+str(acc))
        mydb.commit()
    trek=Toplevel()
    trek.geometry('1200x1200')
    trek['background']='#007BA7'
    l13=Label(trek,text='AKIN BANK',bg='cyan',cursor='star',fg='silver',width=100,relief='groove',underline='0',font='helvetica 16 bold italic').place(x='0',y='0')
    l14=Label(trek,text='Enter Account No.',bg='crimson',width=15,fg='orange',relief='ridge',pady=10,padx=50).place(x='20',y='80')
    l15=Label(trek,text='Enter Name',bg='crimson',width=15,fg='orange',relief='ridge',pady=10,padx=50).place(x='20',y='120')
    l16=Label(trek,text='Enter Password',bg='crimson',width=15,fg='orange',relief='ridge',pady=10,padx=50).place(x='20',y='160')    
    l17=Label(trek,text='Enter Amount to be Deposited',bg='crimson',width=15,fg='orange',relief='ridge',pady=10,padx=50).place(x='20',y='200') 


    e14=Entry(trek,width=40,bd=10)
    e14.place(x=250,y=80)
    e15=Entry(trek,width=40,bd=10)
    e15.place(x=250,y=120)
    e16=Entry(trek,width=40,bd=10)
    e16.place(x=250,y=160)
    e17=Entry(trek,width=40,bd=10)
    e17.place(x=250,y=200)
    b14=Button(trek,text='Initiate Transaction',bg='blue',fg='yellow',height=2,width=20,command=deposit).place(x='200',y='360')
    trek.mainloop()

def delacc():
    tell=Toplevel()
    tell.geometry('1200x1200')
    tell['background']='#007BA7'
    def removeacc():
        acc=e14.get()
        n=e15.get()
        p=e16.get()
        b=int(e17.get())
        mycursor.execute("delete from akininfo where name='"+str(n)+"' and password='"+str(p)+"' and account_no='"+str(acc))
        mydb.commit()
    l13=Label(tell,text='AKIN BANK',bg='cyan',cursor='star',fg='silver',width=100,relief='groove',underline='0',font='helvetica 16 bold italic').place(x='0',y='0')
    l14=Label(tell,text='Enter Account No.',bg='crimson',width=15,fg='orange',relief='ridge',pady=10,padx=50).place(x='20',y='80')
    l15=Label(tell,text='Enter Name',bg='crimson',width=15,fg='orange',relief='ridge',pady=10,padx=50).place(x='20',y='120')
    l16=Label(tell,text='Enter Password',bg='crimson',width=15,fg='orange',relief='ridge',pady=10,padx=50).place(x='20',y='160')
    
    e14=Entry(tell,width=40,bd=10)
    e14.place(x=250,y=80)
    e15=Entry(tell,width=40,bd=10)
    e15.place(x=250,y=120)
    e16=Entry(tell,width=40,bd=10)
    e16.place(x=250,y=160)
    b14=Button(tell,text='Remove Account',bg='blue',fg='yellow',height=2,width=20,command=removeacc).place(x='200',y='360')
    tell.mainloop()

def Trmoney():
    tin=Toplevel()
    tin.geometry('1200x1200')
    tin['background']='#007BA7'
    def transfer():
        acc=e14.get()
        n=e15.get()
        p=e16.get()
        b=int(e17.get())
        mycursor.execute("update akininfo set balance=balance-"+str(b)+" where name='"+str(n)+"' and password='"+str(p)+"' and account_no="+str(acc))
        mydb.commit()
        acd=e18.get()
        na=e19.get()
        mycursor.execute("update akininfo set balance=balance+"+str(b)+" where name='"+str(na)+"' and account_no="+str(acd))
        mydb.commit()
    l13=Label(tin,text='AKIN BANK',bg='cyan',cursor='star',fg='silver',width=100,relief='groove',underline='0',font='helvetica 16 bold italic').place(x='0',y='0')
    l3=Label(tin,text='Enter Account Details of Sender',fg='purple',bg='lime',width=60,relief='ridge',font='bold').place(x='100',y='40')
    l14=Label(tin,text='Enter Account No.',bg='crimson',width=15,fg='orange',relief='ridge',pady=10,padx=50).place(x='20',y='80')
    l15=Label(tin,text='Enter Name',bg='crimson',width=15,fg='orange',relief='ridge',pady=10,padx=50).place(x='20',y='120')
    l16=Label(tin,text='Enter Password',bg='crimson',width=15,fg='orange',relief='ridge',pady=10,padx=50).place(x='20',y='160')
    l17=Label(tin,text='Enter Amount to be Transferred',bg='crimson',width=15,fg='orange',relief='ridge',pady=10,padx=50).place(x='20',y='200')
    
    e14=Entry(tin,width=40,bd=10)
    e14.place(x=250,y=80)
    e15=Entry(tin,width=40,bd=10)
    e15.place(x=250,y=120)
    e16=Entry(tin,width=40,bd=10)
    e16.place(x=250,y=160)
    e17=Entry(tin,width=40,bd=10)
    e17.place(x=250,y=200)
   
    l4=Label(tin,text='Enter Account Details of Reciever',fg='purple',bg='lime',width=60,relief='ridge',font='bold').place(x='100',y='240')
    l18=Label(tin,text='Enter Account No.',bg='crimson',width=15,fg='orange',relief='ridge',pady=10,padx=50).place(x='20',y='280')
    l19=Label(tin,text='Enter Name',bg='crimson',width=15,fg='orange',relief='ridge',pady=10,padx=50).place(x='20',y='320')
    
    e18=Entry(tin,width=40,bd=10)
    e18.place(x=250,y=280)
    e19=Entry(tin,width=40,bd=10)
    e19.place(x=250,y=320)
    b14=Button(tin,text='Initiate Transaction',bg='blue',fg='yellow',height=2,width=20,command=transfer).place(x='600',y='360')
    tin.mainloop()

    
    
b1=Button(text='Create New Account',bg='crimson',fg='gold',relief='raised',font=('courier',10,'bold'),command=createaccount)
b1.place(x=200,y=100)
b2=Button(text='Show My Account Details',bg='crimson',fg='gold',relief='raised',font=('courier',10,'bold'),command=showdetails)
b2.place(x=200,y=150)
b3=Button(text='Check Account No.',bg='crimson',fg='gold',relief='raised',font=('courier',10,'bold'),command=showdetails)
b3.place(x=200,y=200)
b4=Button(text="Check Balance",bg='crimson',fg='gold',relief='raised',font=('courier',10,'bold'),command=showdetails)
b4.place(x=200,y=250)
b5=Button(text="Withdraw From Account",bg='crimson',fg='gold',relief='raised',font=('courier',10,'bold'),command=wbal)
b5.place(x=200,y=300)
b6=Button(text='Deposit Into Account',bg='crimson',fg='gold',relief='raised',font=('courier',10,'bold'),command=dep)
b6.place(x=200,y=350)
b7=Button(text='Drop Account',bg='crimson',fg='gold',relief='raised',font=('courier',10,'bold'),command=delacc)
b7.place(x=200,y=400)
b8=Button(text="Transfer Money",bg='crimson',fg='gold',relief='raised',font=('courier',10,'bold'),command=Trmoney)
b8.place(x=200,y=450)

root.mainloop()

