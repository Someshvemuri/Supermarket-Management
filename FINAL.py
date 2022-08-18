#Login Code
import tkinter
from tkinter import *
from tkinter.messagebox import askyesno
from tkinter import StringVar
import os
from tkinter import font
import smtplib
import time
from tkinter.ttk import Button
class _Display():
    class _Node:
        __slots__ = '_Object','_Price','_prev','_next'

        def __init__(self,product,price,previ,nex):
            self._Object = product
            self._Price = price
            self._prev = previ
            self._next = nex
        
    def __init__(self):
        self._header = self._Node(None,None,None,None)
        self._trailer = self._Node(None,None,None,None)
        self._header._next = self._trailer
        self._trailer._prev=self._header
        self._size = 0

    def insert(self,r,price):
        new = self._Node(r,price,self._header,self._header._next)
        self._header._next = new
        new._prev = self._header
        self._size +=1
    
    def display(self):
        temp = self._header._next
        while (temp != self._trailer):
            print("product:", temp._Object)
            print("price:",temp._Price)
            print("-------------")
            temp = temp._next
    
    def _Sdictionary(self):
        temp = self._header._next
        dict={}
        while (temp != self._trailer):
            dict[temp._Object]=int(temp._Price)
            temp = temp._next
        print(dict)
        return dict
d = _Display()
start=time.time()
#opening tkinter
window=tkinter.Tk()
#creating window 
window.geometry("460x190")
frame = Frame(window, height=600, width=600,background='lightblue', highlightbackground='#ccffcc',highlightthickness=10)
frame.grid(row=0,column=0)
username=StringVar()
password=StringVar()
# Creating a window to get username and password for security purpose... 
window.title("LOGIN AND REGISTER")
label1=tkinter.Label(frame,text="USERNAME").grid(row=0,column=0,padx=10,pady=10)
username1=tkinter.Entry(frame,width=20,textvariable=username).grid(row=0,column=1,padx=40,pady=10)
label2=tkinter.Label(frame,text="PASSWORD").grid(row=1,column=0)
password1=tkinter.Entry(frame,width=20,textvariable=password,show="*").grid(row=1,column=1)
r=""
root=""
def searchitem():
    root1=Toplevel(window)
    siei=StringVar()
    sil=tkinter.Label(root1,text="Enter a item name to search").grid(row=0,column=0)
    sie=tkinter.Entry(root1,width=20,textvariable=siei).grid(row=0,column=1)
    sib=tkinter.Button(root1,text="Submit",command=lambda:[search(siei),root1.destroy()]).grid(row=1,column=1)
def search(s):
    detail=[]
    print(s.get())
    with open("product.txt","r+") as fh: 
            n=len(fh.readlines())
    with open("product.txt","r+") as fh: 
        details={}
        for i in range(n):
            prod=(fh.readline()).split()
            key=prod[1]
            prod.remove(prod[1])
            details[key]=prod
    for i in details:
        print(i)
        if i.upper()==s.get().upper():
            sp=[]
            detail.insert(0,["CODE","NAME","PRICE","STOCK"])
            sp.append(details[i][0])
            sp.append(i)
            sp.append(details[i][1])
            sp.append(details[i][2])
            detail.append(sp)
    print(detail)
    total_rows = len(detail)
    total_columns = len(detail[0])
    root = Tk()
    t = Table(total_rows,total_columns,detail,root)
    root.mainloop()
def searchp(s):
    s1=s.get()
def submit():
    global r
    x=r.get()

def exit():
    global root
    root.destroy()

def Code(pcode,ncode):
    p=pcode.get()
    n=ncode.get()

def modifyC(pcode,ncode):

    with open("product.txt","r+") as fh: 
         n=len(fh.readlines())

    with open("product.txt","r+") as fh: 
        details={}
        for i in range(n):
            prod=(fh.readline()).split()
            key=prod[1]
            prod.remove(prod[1])
            details[key]=prod

    for i in details:
        if details[i][0]==pcode.get():
                details[i][0]=ncode.get()
                win=Tk()
                win.geometry("200x150")
                win.config(bg='lightgreen')
                window2=Label(win,text= "New code entered! ",font=('Helvetica 10 bold'),bg='lightgreen').grid(row=2,column=2,pady=40,padx=13)
                win.after(3000,lambda:win.destroy())
                win.mainloop()
                break  
          
    else:
        win = Tk()    
        win.geometry("200x200")
        Label(win, text= "Entered code not found ",font=('Helvetica 10 bold')).pack(pady=20)
        win.after(3000,lambda:win.destroy())
        win.mainloop()
        win=Tk()
        win.geometry("200x130")
        win.config(bg='#f7ef38')
        window2=Label(win,text= "Entered code not found! ",font=('Helvetica 10 bold'),bg='#f7ef38').grid(row=2,column=2,pady=40,padx=13)
        win.after(3000,lambda:win.destroy())
        win.mainloop()
        
    with open("product.txt","w") as fh:
        for i in details:
            fh.write(str(details[i][0])+" "+str(i)+" "+str(details[i][1])+" "+str(details[i][2]))
            fh.write("\n") 

def name(pname):
    w=pname.get()
    
def modifyN(pname,nname):
    with open("product.txt","r+") as fh: 
        n=len(fh.readlines())

    with open("product.txt","r+") as fh: 
        details={}
        for i in range(n):
            prod=(fh.readline()).split()
            key=prod[0]
            prod.remove(prod[0])
            details[key]=prod
            
    for i in details:
        if details[i][0]==pname.get().upper():
                details[i][0]=nname.get().upper()
                win=Tk()
                win.geometry("200x150")
                win.config(bg='lightgreen')
                window2=Label(win,text= "New name entered! ",font=('Helvetica 10 bold'),bg='lightgreen').grid(row=2,column=2,pady=40,padx=13)
                win.after(3000,lambda:win.destroy())
                win.mainloop()
                break  
          
    else:
        win=Tk()
        win.geometry("200x130")
        win.config(bg='#f7ef38')
        window2=Label(win,text= "Entered name not found! ",font=('Helvetica 10 bold'),bg='#f7ef38').grid(row=2,column=2,pady=40,padx=13)
        win.after(3000,lambda:win.destroy())
        win.mainloop()

    with open("product.txt","w") as fh:
        for i in details:
            fh.write(str(i)+" "+str(details[i][0])+" "+str(details[i][1])+" "+str(details[i][2]))
            fh.write("\n")

def price(namep):
    z=namep.get()

def modifyP(namep,nprice):
    with open("product.txt","r+") as fh: 
        n=len(fh.readlines())

    with open("product.txt","r+") as fh: 
        details={}
        for i in range(n):
            prod=(fh.readline()).split()
            key=prod[1]
            prod.remove(prod[1])
            details[key]=prod

    for i in details:
        if i==namep.get().upper():
                details[i][1]=nprice.get()
                win=Tk()
                win.geometry("200x150")
                win.config(bg='lightgreen')
                window2=Label(win,text= "New price entered!  ",font=('Helvetica 10 bold'),bg='lightgreen').grid(row=2,column=2,pady=40,padx=13)
                win.after(3000,lambda:win.destroy())
                win.mainloop()
                break  
          
    else:
        win=Tk()
        win.geometry("200x130")
        win.config(bg='#f7ef38')
        window2=Label(win,text= "Entered name not found! ",font=('Helvetica 10 bold'),bg='#f7ef38').grid(row=2,column=2,pady=40,padx=13)
        win.after(3000,lambda:win.destroy())
        win.mainloop()
       
    with open("product.txt","w") as fh:
        for i in details:
            fh.write(str(details[i][0])+" "+str(i)+" "+str(details[i][1])+" "+str(details[i][2]))
            fh.write("\n")

def stock(namep,nstock):
    s1=namep.get()
    s2=nstock.get()

def modifyS(namep,nstock):
    with open("product.txt","r+") as fh: 
        n=len(fh.readlines())

    with open("product.txt","r+") as fh: 
        details={}
        for i in range(n):
            prod=(fh.readline()).split()
            key=prod[1]
            prod.remove(prod[1])
            details[key]=prod
    for i in details:
        if i==namep.get().upper():
                details[i][2]=nstock.get()
                win=Tk()
                win.geometry("200x150")
                win.config(bg='lightgreen')
                window2=Label(win,text= "New Stock value entered! ",font=('Helvetica 10 bold'),bg='lightgreen').grid(row=2,column=2,pady=40,padx=13)
                win.after(3000,lambda:win.destroy())
                win.mainloop()
                break      
    else:
        win=Tk()
        win.geometry("200x130")
        win.config(bg='#f7ef38')
        window2=Label(win,text= "Entered name not found! ",font=('Helvetica 10 bold'),bg='#f7ef38').grid(row=2,column=2,pady=40,padx=13)
        win.after(3000,lambda:win.destroy())
        win.mainloop()
    
    with open("product.txt","w") as fh:
        for i in details:
            fh.write(str(details[i][0])+" "+str(i)+" "+str(details[i][1])+" "+str(details[i][2]))
            fh.write("\n")
def addp():
    global r1
    y=r1.get()
    
def add(r1,r2,r3,r4):
    with open("product.txt","r+") as fh: 
            n=len(fh.readlines())
    with open("product.txt","r+") as fh: 
        details={}
        for i in range(n):
            prod=(fh.readline()).split()
            key=prod[1]
            print(prod[1])
            prod.remove(prod[1])
            details[key]=prod
    code=[]
    for k in details:
        code.append(details[k][0])
    if r1.get() in code:
        win=Tk()
        win.geometry("200x130")
        win.config(bg='#f7ef38')
        window2=Label(win,text= "Code already exists! ",font=('Helvetica 10 bold'),bg='#f7ef38').grid(row=2,column=2,pady=40,padx=13)
        win.after(3000,lambda:win.destroy())
        win.mainloop()
    elif not(r1 and r2 and r3 and r4):
        win=Tk()
        win.geometry("200x130")
        win.config(bg='#f7ef38')
        window2=Label(win,text= "Details not entered! ",font=('Helvetica 10 bold'),bg='#f7ef38').grid(row=2,column=2,pady=40,padx=13)
        win.after(3000,lambda:win.destroy())
        win.mainloop()
    else:
        np=[]
        print(r1.get())
        np.append(r1.get())  
        np.append(r3.get())  
        np.append(r4.get())  
        details[r2.get().upper()]=np
        print(details)
        with open("product.txt","w") as fh:
           for i in details:
               fh.write(str(details[i][0])+" "+str(i)+" "+str(details[i][1])+" "+str(details[i][2]))
               fh.write("\n")
        win=Tk()
        win.geometry("200x130")
        win.config(bg='lightgreen')
        window2=Label(win,text= "Product successfully added! ",bg='lightgreen',font=('Helvetica 10 bold')).grid(row=2,column=2,pady=40,padx=13)
        win.after(3000,lambda:win.destroy())
        win.mainloop()

def delete():
    name=r.get().upper()
    with open("product.txt","r+") as fh: 
            n=len(fh.readlines())
    with open("product.txt","r+") as fh: 
        details={}
        for i in range(n):
            prod=(fh.readline()).split()
            key=prod[1]
            prod.remove(prod[1])
            details[key]=prod

    for i in details:
        if i==name:
            del details[i]
            win=Tk()
            win.geometry("200x130")
            win.config(bg='lightgreen')
            window2=Label(win,text= "Product successfully deleted! ",bg='lightgreen',font=('Helvetica 10 bold')).grid(row=2,column=2,pady=40,padx=13)
            win.after(3000,lambda:win.destroy())
            win.mainloop()
            break
    else:
        win=Tk()
        win.geometry("200x130")
        win.config(bg='#f7ef38')
        window2=Label(win,text= "Product not found! ",font=('Helvetica 10 bold'),bg='#f7ef38').grid(row=2,column=2,pady=40,padx=13)
        win.after(3000,lambda:win.destroy())
        win.mainloop()
    with open("product.txt","w") as fh:
        for i in details:
            fh.write(str(details[i][0])+" "+str(i)+" "+str(details[i][1])+" "+str(details[i][2]))
            fh.write("\n")

def confirm():
    answer = askyesno(title='confirmation',
                    message='Are you sure that you want to delete?')
    if answer:
        root.destroy()
        delete()
    else:
        root.destroy()

class Table:
    def __init__(self,total_rows,total_columns,details,root):
        print(total_rows,total_columns,details)
        for i in range(total_rows):
            for j in range(total_columns):
                if i==0:
                    self.e = Entry(root, width=15, bg='LightSteelBlue',fg='Black',font=('Arial',16,'bold'))
                else:
                    self.e = Entry(root, width=15, fg='blue',font=('Arial',16))
                self.e.grid(row=i, column=j)
                print(details[i][j])
                self.e.insert(END, details[i][j])

def VendorOptions():
    global root
    global r1
    while True:
        root=Tk()
        root.geometry("409x246")
        f3 = Frame(root, height=600, width=600,background='#21a5cb', highlightbackground='#291d63',highlightthickness=20)
        f3.grid(row=0,column=0)
        myLabel1=Label(f3,text="Choices are: ",bg='#21a5cb',font=(7)).grid(row=0,column=0,padx=20)
        myLabel2=Label(f3,text="1 for Modifying existing product",bg='#21a5cb').grid(row=1,column=0,padx=20)
        myLabel3=Label(f3,text="2 for Adding a new product",bg='#21a5cb').grid(row=2,column=0)
        myLabel4=Label(f3,text="3 for Deleting existing product",bg='#21a5cb').grid(row=3,column=0)
        myLabel5=Label(f3,text="4 for Displaying the products",bg='#21a5cb').grid(row=4,column=0)
        myLabel6=Label(f3,text="5 for Exit",bg='#21a5cb').grid(row=5,column=0)
        choice = Label(f3, text = 'Enter your Choice: ', font=('calibre',10, 'bold'),bg='#21a5cb').grid(row=6,column=0)
        option=[1,2,3,4,5]
        global r
        r=IntVar(root)
        r.set("Select an Option")
        question_menu = OptionMenu(f3, r, *option).grid(row=6,column=1,padx=10)
        but =Button(f3,text = 'Submit', command = lambda:[submit(), exit()]).grid(row=7,column=0,pady=10)
        root.mainloop()
        if r.get()==1:
            root=Tk()
            root.geometry("350x255")
            f4 = Frame(root, height=600, width=600,background='#e9a8ee', highlightbackground='#cd87a2',highlightthickness=20)
            f4.grid(row=0,column=0)
            myLabel1=Label(f4,text="Choices are: ",bg='#e9a8ee',font=(7)).grid(row=0,column=0,pady=10)
            myLabel2=Label(f4,text="A for modifying product code",bg='#e9a8ee').grid(row=1,column=0)
            myLabel3=Label(f4,text="B for modifying product name",bg='#e9a8ee').grid(row=2,column=0)
            myLabel4=Label(f4,text="C for modifying product price",bg='#e9a8ee').grid(row=3,column=0)
            myLabel5=Label(f4,text="D for modifying product stock",bg='#e9a8ee').grid(row=4,column=0)
            choice = Label(f4, text = 'Enter your Choice: ', font=('calibre',10, 'bold'),bg='#e9a8ee').grid(row=5,column=0,pady=5)
            option=["A","B","C","D"]
            r=StringVar(root)
            r.set("Select an Option")
            question_menu = OptionMenu(f4, r, *option).grid(row=5,column=1,pady=5,padx=5)
            but =Button(f4,text = 'Submit', command = lambda:[submit(), exit()]).grid(row=6,column=0,pady=10)
            root.mainloop()
            if r.get()=="A":
               root=Tk()
               root.geometry("355x163")
               pcode=StringVar()
               ncode=StringVar()
               f5 = Frame(root, height=600, width=600,background='#ecb9c4', highlightbackground='#e089a2',highlightthickness=16)
               f5.grid(row=0,column=0)
               code1 = Label(f5, text = 'Enter the existing code: ', font=('calibre',10, 'bold'),bg='#ecb9c4').grid(row=0,column=0,padx=5,pady=10)
               e = Entry(f5,textvariable = pcode, font=('calibre',10,'normal')).grid(row=0,column=1,padx=5,pady=10)
               code2 = Label(f5, text = 'Enter the new code: ', font=('calibre',10, 'bold'),bg='#ecb9c4').grid(row=1,column=0,pady=10)
               e = Entry(f5,textvariable = ncode, font=('calibre',10,'normal')).grid(row=1,column=1,pady=10)
               but =Button(f5,text = 'Submit', command = lambda:[Code(pcode,ncode), exit()]).grid(row=2,column=0,pady=10)
               root.mainloop()
               modifyC(pcode,ncode)
            elif r.get()=="B":
               root=Tk()
               root.geometry("360x163")
               pname=StringVar()
               nname=StringVar()
               f6 = Frame(root, height=600, width=600,background='#ecb9c4', highlightbackground='#e089a2',highlightthickness=16)
               f6.grid(row=0,column=0)
               name1 = Label(f6, text = 'Enter the existing name: ', font=('calibre',10, 'bold'),bg='#ecb9c4').grid(row=0,column=0,padx=5,pady=10)
               e = Entry(f6,textvariable = pname, font=('calibre',10,'normal')).grid(row=0,column=1,padx=5,pady=10)
               name2 = Label(f6, text = 'Enter the new name: ', font=('calibre',10, 'bold'),bg='#ecb9c4').grid(row=1,column=0,pady=10)
               e = Entry(f6,textvariable = nname, font=('calibre',10,'normal')).grid(row=1,column=1,pady=10)
               but =Button(f6,text = 'Submit', command = lambda:[name(pname), exit()]).grid(row=2,column=0,pady=10)
               root.mainloop()
               modifyN(pname,nname)
            elif r.get()=="C":
               root=Tk()
               root.geometry("360x163")
               namep=StringVar()
               nprice=StringVar()
               f7 = Frame(root, height=600, width=600,background='#ecb9c4', highlightbackground='#e089a2',highlightthickness=16)
               f7.grid(row=0,column=0)
               name1 = Label(f7, text = 'Enter the product name: ', font=('calibre',10, 'bold'),bg='#ecb9c4').grid(row=0,column=0,padx=5,pady=10)
               e = Entry(f7,textvariable = namep, font=('calibre',10,'normal')).grid(row=0,column=1,padx=5,pady=10)
               name2 = Label(f7, text = 'Enter the new price: ', font=('calibre',10, 'bold'),bg='#ecb9c4').grid(row=1,column=0,pady=10)
               e = Entry(f7,textvariable = nprice, font=('calibre',10,'normal')).grid(row=1,column=1,pady=10)
               but =Button(f7,text = 'Submit', command = lambda:[price(namep), exit()]).grid(row=2,column=0,pady=10)
               root.mainloop()
               modifyP(namep,nprice)
            elif r.get()=="D":
               root=Tk()
               root.geometry("363x163")
               namep=StringVar()
               nstock=IntVar()
               f8 = Frame(root, height=600, width=600,background='#ecb9c4', highlightbackground='#e089a2',highlightthickness=16)
               f8.grid(row=0,column=0)
               name1 = Label(f8, text = 'Enter the product name: ', font=('calibre',10, 'bold'),bg='#ecb9c4').grid(row=0,column=0,padx=5,pady=10)
               e = Entry(f8,textvariable = namep, font=('calibre',10,'normal')).grid(row=0,column=1,pady=10)
               name2 = Label(f8, text = 'Enter the new stock value: ', font=('calibre',10, 'bold'),bg='#ecb9c4').grid(row=1,column=0,pady=10)
               e = Entry(f8,textvariable = nstock, font=('calibre',10,'normal')).grid(row=1,column=1,pady=10)
               but =Button(f8,text = 'Submit', command = lambda:[stock(namep,nstock), exit()]).grid(row=2,column=0,pady=10)
               root.mainloop()
               modifyS(namep,nstock)
        elif r.get()==2:
            root=Tk()
            r1=StringVar()
            r2=StringVar()
            r3=StringVar()
            r4=StringVar()
            root.geometry("415x240")
            f9 = Frame(root, height=700, width=700,background='#ffa74f', highlightbackground='#95ff95',highlightthickness=20)
            f9.grid(row=0,column=0)
            myLabel1=Label(f9,text="Enter the product detsils below: ",font=('calibre',10, 'bold'),bg='#ffa74f').grid(row=0,column=0,padx=10,pady=5)
            c = Label(f9, text = 'Code: ', font=('calibre',10, 'bold'),bg='#ffa74f').grid(row=1,column=0,padx=10,pady=5)
            e1= Entry(f9,textvariable = r1, font=('calibre',10,'normal')).grid(row=1,column=1)
            n = Label(f9, text = 'Name: ', font=('calibre',10, 'bold'),bg='#ffa74f').grid(row=2,column=0,pady=5)
            e2= Entry(f9,textvariable = r2, font=('calibre',10,'normal')).grid(row=2,column=1)
            p = Label(f9, text = 'Price per unit: ', font=('calibre',10, 'bold'),bg='#ffa74f').grid(row=3,column=0,pady=5)
            e3= Entry(f9,textvariable = r3, font=('calibre',10,'normal')).grid(row=3,column=1)
            s = Label(f9, text = 'Stock available: ', font=('calibre',10, 'bold'),bg='#ffa74f').grid(row=4,column=0,pady=5)
            e4= Entry(f9,textvariable = r4, font=('calibre',10,'normal')).grid(row=4,column=1,pady=5)
            root.mainloop()
            add(r1,r2,r3,r4)
        elif r.get()==3:
            root=Tk()
            root.geometry("438x90")
            f10 = Frame(root, height=700, width=700,background='#8ec6bb', highlightbackground='#b4faa9',highlightthickness=20)
            f10.grid(row=0,column=0)
            r=StringVar()
            n = Label(f10, text = 'Enter the product name to be deleted: ', font=('calibre',10, 'bold'),bg='#8ec6bb').grid(row=1,column=0)
            e1= Entry(f10,textvariable = r, font=('calibre',10,'normal')).grid(row=1,column=1)
            but =Button(f10,text = 'Delete', command = lambda:[confirm()]).grid(row=2,column=0)
            root.mainloop() 
        elif r.get()==4:
            with open("product.txt","r+") as fh: 
                n=len(fh.readlines())
            with open("product.txt","r+") as fh: 
                details=[]
                for i in range(n):
                    prod=(fh.readline()).split()
                    details.append(prod)
            details.insert(0,["CODE","NAME","PRICE","STOCK"])
            total_rows = len(details)
            total_columns = len(details[0])
            root = Tk()
            t = Table(total_rows,total_columns,details,root)
            but =Button(root,text = 'CLOSE', command = lambda:[exit()]).grid(row=total_rows+1,column=2)
            root.mainloop()
        elif r.get()==5:
            break
def customerregister():
    window.destroy()
    wind=tkinter.Tk()
    wind.geometry("300x130")
    frame1 = Frame(wind, height=600, width=600,background='#ADADFF', highlightbackground='#6cd5d2',highlightthickness=10)
    frame1.grid(row=0,column=0)
    gm=StringVar()
    npw=StringVar()
    ne=Label(frame1,text="Enter a new gmail ID").grid(row=1,column=0,padx=10,pady=10)
    np=Label(frame1,text="Enter a valid password").grid(row=2,column=0)
    neg=Entry(frame1,textvariable=gm).grid(row=1,column=1,padx=10,pady=10)
    npg=Entry(frame1,textvariable=npw).grid(row=2,column=1)
    negb=Button(frame1,text="submit",command = lambda:[register(gm,npw), wind.destroy()]).grid(row=3,column=1,pady=10)
def register(gm,npw):
    with open("USERNAME.txt","r+") as f1:
        n=len(f1.readlines())
    with open("USERNAME.txt","r+") as f1:
        user=[]
        for i in range(n-1):
            user.append(f1.readline().split("\n")[0])
        user.append(f1.readline())
    f1=open("USERNAME.txt","a+")
    f2=open("PASSWORD.txt","a+")
    # Appending the new user in the database table already created before...
    x=gm.get()
    y=npw.get()
    flag=False
    flag1=False
    x1=x[-len(y):-8]
    # Getting input to addd new user ...
    """for i in range(0,len(x1)):
#checking whether the input given is alphanumerical or not , if not it wont get appended...
        if x[i].isalnum():
            flag=False
            pass
        else:
            flag=True
            break"""
    print(y.isalnum())
    if y.isalnum():
        flag1=True
    else:
        flag1=False
    if x[-10:]=="@gmail.com":
        flag=True
    if flag==False:
        impg=Tk()
        impg.geometry("250x130")
        impg.config(bg='#f7ef38')
        window2=tkinter.Label(impg,text="ENTER A PROPER GMAIL ID",font=(30)).grid(row=2,column=2,pady=40,padx=13)
        impg.after(3000,lambda:impg.destroy())
        impg.mainloop()
    elif flag1==False:
        impp=Tk()
        impp.geometry("450x130")
        impp.config(bg='#f7ef38')
        window2=tkinter.Label(impp,text="USE ONLY ALPHABETS OR NUMBERS FOR PASSWORD",font=(30)).grid(row=2,column=2,pady=40,padx=13)
        impp.after(3000,lambda:impp.destroy())
        impp.mainloop()
    if x in user:
        win1=Tk()
        win1.geometry("250x130")
        win1.config(bg='#f7ef38')
        window2=tkinter.Label(win1,text="ACCOUNT ALREADY EXISTS",font=(30)).grid(row=2,column=2,pady=40,padx=13)
        win1.after(3000,lambda:win1.destroy())
        win1.mainloop()

    elif flag==True and flag1==True:
        f1.write("\n")
        f1.writelines([x])
        print("hi")
        f2.write("\n")
        f2.writelines([y])
        f1.close()
        f2.close()
        MP=tkinter.Tk()
        MP.geometry("270x165")
        MP.title("VEGETABLE SHOP")
        f = Frame(MP, height=600, width=600,background='#7dcdf9', highlightbackground='#91fa72',highlightthickness=16)
        f.grid(row=0,column=0)
        ext=tkinter.Button(f,text="EXIT",fg="Black",bg="White",command=MP.destroy).grid(row=0,column=0,padx=100,pady=20)
        hl=tkinter.Button(f,text="HELP",fg="Black",bg="White",command=help_).grid(row=1,column=0,padx=100,pady=20)
def check_usernameandpassword():
    #getiing username and password from the user...
    username2=username.get()
    password2=password.get()
    #connecting the database to access the username and password table...
    f1=open("USERNAME.txt","r+")
    f2=open("PASSWORD.txt","r+")
    up1=f1.readlines()
    ps1=f2.readlines()
    print(up1,ps1)
    print(username2,password2)
    up=[]
    ps=[]
    for i in range(0,len(up1)):
        y=up1[i].split("\n")[0]
        x=""
        for j in range(0,len(y)):
            x=x+y[j]
        up.append(x)
    for i in range(0,len(ps1)):
        a=ps1[i].split("\n")[0]
        b=""
        for j in range(0,len(a)):
            b=b+a[j]
        ps.append(b)
    dic={}
    for i in range(0,len(up)):
        dic[up[i]]=ps[i]
    for i in range(0,len(up)):
        if username2==up[i]:
            a=i
            if dic[username2]==ps[i] and password2 in ps:
                MP=tkinter.Tk()
                MP.title("VEGETABLE SHOP")
                MP.geometry("340x260")
                f1 = Frame(MP, height=600, width=600,background='#7dcdf9', highlightbackground='#91fa72',highlightthickness=16)
                f1.grid(row=0,column=0) 
                sc=tkinter.Button(f1,text="SEARCH FOR ITEM",fg="Black",bg="White",command=searchitem).grid(row=4,column=2,padx=100,pady=10)
                si=tkinter.Button(f1,text="SHOW ALL ITEMS",fg="Black",bg="White",command=cpd).grid(row=6,column=2,pady=10)
                op=tkinter.Button(f1,text="PLACE AN ORDER",fg="Black",bg="White",command=lambda:[PO()]).grid(row=2,column=2,pady=10)
                ext=tkinter.Button(f1,text="EXIT",fg="Black",bg="White",command=MP.destroy).grid(row=10,column=2,pady=10)
                hl=tkinter.Button(f1,text="HELP",fg="Black",bg="White",command=help_).grid(row=8,column=2,pady=10)
                MP.mainloop()
            else:
                window2=tkinter.Label(window,text="INVALID PASSWORD TRY AGAIN!!!").grid(row=5,column=0)
        elif username2 not in up:
            window2=tkinter.Label(window,text="INVALID USERNAME TRY AGAIN!!!").grid(row=5,column=0)
    username.set("")
    password.set("")
def check_usernameandpasswordv():
    global my_dict1
    #getiing username and password from the user...
    username2=username.get()
    print(username2)
    password2=password.get()
    print(password2)
    #connecting the database to access the username and password table...
    f1=open("USERNAMEVENDOR.txt","r+")
    f2=open("PASSWORDVENDOR.txt","r+")
    up1=f1.readlines()
    ps1=f2.readlines()
    up=[]
    ps=[]
    for i in range(0,len(up1)):
        y=up1[i].split("\n")[0]
        x=""
        for j in range(0,len(y)):
            x=x+y[j]
        up.append(x)
    for i in range(0,len(ps1)):
        a=ps1[i].split("\n")[0]
        b=""
        for j in range(0,len(a)):
            b=b+a[j]
        ps.append(b)
    dic={}
    for i in range(0,len(up)):
        dic[up[i]]=ps[i]
    print(dic,up,ps,)
    for i in range(0,len(up)):
        if username2==up[i]:
            a=i
            if dic[username2]==ps[i] and password2 in ps:
                window.destroy()
                MP=tkinter.Tk()
                MP.title("VEGETABLE SHOP")
                MP.geometry("280x170")
                f2 = Frame(MP, height=600, width=600,background='#e9a8ee', highlightbackground='#8cdbf2',highlightthickness=16)
                f2.grid(row=0,column=0)
                dis=tkinter.Button(f2,text="VENDOR OPTIONS",bg="White",command=VendorOptions).grid(row=1,column=0,padx=70,pady=10)
                ext=tkinter.Button(f2,text="EXIT",fg="Black",bg="White",command=MP.destroy).grid(row=2,column=0,pady=10)
                hl=tkinter.Button(f2,text="HELP",fg="Black",bg="White",command=help_).grid(row=3,column=0,pady=10)
            else:
                window2=tkinter.Label(window,text="INVALID PASSWORD TRY AGAIN!!!").grid(row=5,column=0)
        elif username2 not in up:
            window2=tkinter.Label(window,text="INVALID USERNAME TRY AGAIN!!!").grid(row=5,column=0)
    username.set("")
    password.set("")
# buttons for LOGIN
windowbt=tkinter.Button(frame,text="CUSTOMER LOGIN",fg="Black",bg="White",command=check_usernameandpassword).grid(row=2,column=0,pady=40)
windowbt=tkinter.Button(frame,text="VENDOR LOGIN",fg="Black",bg="White",command=check_usernameandpasswordv).grid(row=2,column=1)
bt1=tkinter.Button(frame,text="CUSTOMER REGISTER",fg="Black",bg="White",command=customerregister).grid(row=2,column=2)
def help_():
    os.startfile("HELP.txt")
def bill(gmid,order):
 print(gmid)
 print(order)
 d=[i for i in order.keys()]
 e=[i for i in order.values()]
 f=open("Product.txt","r")
 g=len(f.readlines())
 f.close()
 f=open("Product.txt","r")
 l=[]
 for i in range(g):
   h=(f.readline()).split()
   l.append(h)
 t=0
 k=[]
 for i in d:
    for j in l:
        if i==j[1]:
         k.append(j[2]) 
         a=d.index(i)
         t=t+(float(e[a])*float(j[2]))
 u=[]    
 for i in range(len(d)) :
# create a print statement for each item
         m=[d[i],k[i],e[i]]
         u.append(m)
 j=('=' * 80+'\n\t{}'.format("SSN VEGITABLE VENDORS")+'\n\t{}\t'.format(" KALAVAKKAM,")+'\n{}'.format("CHENNAI-603110.\n")+('=' * 80)+'\n\tProduct Name\tProduct Price(rs/kg)\t\tquantity\n')
 h=('*' * 60+'\n\t\t\t{}'.format("SSN VEGITABLE VENDORS")+'\n\t\t\t{}\t'.format("    KALAVAKKAM,")+'\n\t\t\t{}'.format("  CHENNAI-603110.\n")+('=' * 45)+'\n\tProduct Name\tProduct Price(rs/kg)\tquantity\n')
 m=""
 c=""
 for i in u:
   m=m+'\t{}\t\t\t\t{}\t\t\t\t{}'.format(i[0],i[1],i[2])+"\n"
   c=c+'\t{}\t\t{}\t\t\t{}'.format(i[0],i[1],i[2])+"\n"
 d=j+c+"\n"+'*' * 80+'\n\tTotal\t\t\tRS{}'.format(t)+'\n\t{}\n\n\n'.format('Thanks for shopping with us today!'+"\n\n\t{}".format("email has succesfully sent to your registered email id"))
 l=h+m+"\n"+'*' * 60+'\n\tTotal\t\t\tRS{}'.format(t)+'\n\t{}\n'.format('Thanks for shopping with us today!') 
# creates SMTP session
 s = smtplib.SMTP('smtp.gmail.com', 587)
# start TLS for security
 s.starttls()
#for i in range len(y)
 x=gmid[0:-10]
# Authentication
 s.login("cuedelacci@gmail.com", "rrnhihgezznhtdxy")
 sub="CONFORAMTION OF YOUR VEGETABLE ORDER"
 body=("HELLO!!!,"+x+"\n\t{}".format("your order has sucessfully placed and it will be delivered soon\n")+"invoice for your order\n\n\n"+l+"\n\n\n\t{}".format("have a nice day :)"))
# message to be sent
 message = "Subject:{}\n\n{}".format(sub,body)
# sending the mail
 s.sendmail("cuedelacci@gmail.com",gmid, message)
# terminating the session
 s.quit()
 window=tkinter.Tk()
 window.geometry("700x1000")
 l=tkinter.Label(window,text=d,font=("arial",12,"italic")).grid(column=0,row=0)
 end=time.time()
 print("time taken to compile",end-start)
 bt=tkinter.Button(window,text="exit",command=window.destroy,fg="red",bg="green",height=3,width=5).grid(column=0,row=1)
 window.mainloop()
def display(ent1,ent2):
    username2=username.get()
    n=ent1.get()
    m=ent2.get()
    l1=n.split(",")
    l2=m.split(",")
    h=[]
    j=[]
    for i in l1:
        h.append(i)
    for k in l2:
        j.append(k)
    for i in range(len(h)):
        l = h.pop()
        z =j.pop()
        d.insert(l,z)
    with open("Product.txt","r+") as fh: 
        n=len(fh.readlines())
    with open("Product.txt","r+") as fh: 
        details={}
        for i in range(n):
            prod=(fh.readline()).split()
            key=prod[1]
            prod.remove(prod[1])
            details[key]=prod
        print(details)
    for i in range(len(l1)):
        if (l1[i] in details) and int(l2[i])<= int(details[l1[i]][2]) and int(l2[i])>0:
            g =int(details[l1[i]][2])-int(l2[i])
            details[l1[i]][2] = str(g)
            d._Sdictionary()
            """with open("order.txt","w") as fs:
                for i in d._Sdictionary:
                    fs.write(str(i)+" "+str(details[i][0]))
                    fs.write("\n")"""
            new1=Toplevel()
            #new1.title("Displaying the products")
            new1.geometry('800x450+300+300')                
            gre4 = Label(new1,text="your order is placed succcessfully",font=('Arial',16,'bold'))
            #entry3 = tk.Entry(fg = "black",bg="white",width=50)                
            #entry3.insert(0,l1[i])
            gre4.grid()
            order=d._Sdictionary()
            bill(username2,order)
            new1.mainloop()    
        else:
            root1 = Toplevel()
            gre5 = Label(root1,text="please enter a valid input",font=('Arial',16,'bold'))
            gre5.grid()
            #entry6 = tk.Entry(fg = "black",bg= "white",width=50)
            #lab=tk.Label(window,text="enter a valid entry")
            #lab.grid()
            #entry3.pack()
            #gre5 = tk.Label(text="quantity")
            #entry4 = tk.Entry(fg = "black",bg="white",width=50)
            #entry4.insert(0,l2[i])
            #gre5.pack()
            #entry4.pack()
    with open("Product.txt","w") as fh:
        for i in details:
            fh.write(str(details[i][0])+" "+str(i)+" "+str(details[i][1])+" "+str(details[i][2]))
            fh.write("\n")
def cpd():
    with open("Product.txt","r+") as fh: 
        n=len(fh.readlines())
    with open("Product.txt","r+") as fh: 
        details=[]
        for i in range(n):
            prod=(fh.readline()).split()
            details.append(prod)
    details.insert(0,["CODE","NAME","PRICE","STOCK"])
    total_rows = len(details)
    total_columns = len(details[0])
    root = Tk()
    t = Table(total_rows,total_columns,details,root)
    but =Button(root,text = 'CLOSE', command = lambda:[root.destroy()]).grid(row=total_rows+1,column=2)
    root.mainloop()
def PO():
    windown= Toplevel(window)
    windown.geometry('638x180')
    ent1=StringVar()
    ent2=StringVar()
    f10 = Frame(windown, height=600, width=600,background='lightblue', highlightbackground='#ccffcc',highlightthickness=25)
    f10.grid(row=0,column=0)
    windown.title("Vendor shop")
    greeting2= Label(f10,text="Enter the list of products:",font=('Arial',10,'bold'),bg='lightblue').grid(row=1,column=0,padx=10,pady=10)
    entry1= Entry(f10,textvariable=ent1,width=50).grid(row=1,column=1,pady=10)
    greeting3 = Label(f10,text="enter the quantity of the product as a list",font=('Arial',10,'bold'),bg='lightblue').grid(row=2,column=0,pady=10,padx=10)
    entry2 = Entry(f10,textvariable=ent2,width=50).grid(row=2,column=1,pady=10)
    button=Button(windown,text="submit",command=lambda:[display(ent1,ent2),windown.destroy()]).grid(row=3,column=0,pady=10)
window.mainloop()
