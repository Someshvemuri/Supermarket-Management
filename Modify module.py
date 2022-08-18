from tkinter import *
from tkinter.messagebox import askyesno

def submit():
    x=r.get()

def exit():
    root.destroy()

def Code():
    p=pcode.get()
    n=ncode.get()

def modifyC():

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
                win = Tk()    
                win.geometry("150x150")
                Label(win, text= "New code entered! ",font=('Helvetica 10 bold')).pack(pady=20)
                win.after(3000,lambda:win.destroy())
                win.mainloop()
                break  
          
    else:
        win = Tk()    
        win.geometry("200x200")
        Label(win, text= "Entered code not found ",font=('Helvetica 10 bold')).pack(pady=20)
        win.after(3000,lambda:win.destroy())
        win.mainloop()
        
    with open("product.txt","w") as fh:
        for i in details:
            fh.write(str(details[i][0])+" "+str(i)+" "+str(details[i][1])+" "+str(details[i][2]))
            fh.write("\n") 

def name():
    w=pname.get()
    
def modifyN():
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
                win = Tk()    
                win.geometry("150x150")
                Label(win, text= "New name entered! ",font=('Helvetica 10 bold')).pack(pady=20)
                win.after(3000,lambda:win.destroy())
                win.mainloop()
                break  
          
    else:
        win = Tk()    
        win.geometry("200x200")
        Label(win, text= "Entered name not found ",font=('Helvetica 10 bold')).pack(pady=20)
        win.after(3000,lambda:win.destroy())
        win.mainloop()

    with open("product.txt","w") as fh:
        for i in details:
            fh.write(str(i)+" "+str(details[i][0])+" "+str(details[i][1])+" "+str(details[i][2]))
            fh.write("\n")

def price():
    z=namep.get()

def modifyP():
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
                win = Tk()    
                win.geometry("150x150")
                Label(win, text= "New price entered! ",font=('Helvetica 10 bold')).pack(pady=20)
                win.after(3000,lambda:win.destroy())
                win.mainloop()
                break  
          
    else:
        win = Tk()    
        win.geometry("200x200")
        Label(win, text= "Entered name not found ",font=('Helvetica 10 bold')).pack(pady=20)
        win.after(3000,lambda:win.destroy())
        win.mainloop()
       
    with open("product.txt","w") as fh:
        for i in details:
            fh.write(str(details[i][0])+" "+str(i)+" "+str(details[i][1])+" "+str(details[i][2]))
            fh.write("\n")

def stock():
    s1=namep.get()
    s2=nstock.get()

def modifyS():
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
                win = Tk()    
                win.geometry("200x150")
                Label(win, text= "New Stock value entered! ",font=('Helvetica 10 bold')).pack(pady=20)
                win.after(3000,lambda:win.destroy())
                win.mainloop()
                break  
          
    else:
        win = Tk()    
        win.geometry("200x200")
        Label(win, text= "Entered name not found ",font=('Helvetica 10 bold')).pack(pady=20)
        win.after(3000,lambda:win.destroy())
        win.mainloop()
    
    with open("product.txt","w") as fh:
        for i in details:
            fh.write(str(details[i][0])+" "+str(i)+" "+str(details[i][1])+" "+str(details[i][2]))
            fh.write("\n")

def addp():
    y=r1.get()
    
def add():

    with open("product.txt","r+") as fh: 
            n=len(fh.readlines())
    with open("product.txt","r+") as fh: 
        details={}
        for i in range(n):
            prod=(fh.readline()).split()
            key=prod[1]
            prod.remove(prod[1])
            details[key]=prod
    np=[]
    np.append(r1.get())  
    np.append(r3.get())  
    np.append(r4.get())  
    details[r2.get().upper()]=np
    with open("product.txt","w") as fh:
        for i in details:
            fh.write(str(details[i][0])+" "+str(i)+" "+str(details[i][1])+" "+str(details[i][2]))
            fh.write("\n")
    win = Tk()    
    win.geometry("300x200")
    Label(win, text= "Product successfully added! ",font=('Helvetica 10 bold')).pack(pady=20)
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
            win = Tk()    
            win.geometry("300x200")
            Label(win, text= "Product successfully deleted! ",font=('Helvetica 10 bold')).pack(pady=20)
            win.after(3000,lambda:win.destroy())
            win.mainloop()
            break
    else:
        win = Tk()    
        win.geometry("300x200")
        Label(win, text= "Product not found! ",font=('Helvetica 10 bold')).pack(pady=20)
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
    def __init__(self,root):
        for i in range(total_rows):
            for j in range(total_columns):
                if i==0:
                    self.e = Entry(root, width=15, bg='LightSteelBlue',fg='Black',font=('Arial',16,'bold'))

                else:
                    self.e = Entry(root, width=15, fg='blue',font=('Arial',16))
                 
                self.e.grid(row=i, column=j)
                self.e.insert(END, details[i][j])

#main program
while True:
    root=Tk()
    root.geometry("400x200")
    myLabel1=Label(root,text="Choices are: ").grid(row=0,column=0)
    myLabel2=Label(root,text="1 for Modifying existing product").grid(row=1,column=0)
    myLabel3=Label(root,text="2 for Adding a new product").grid(row=2,column=0)
    myLabel4=Label(root,text="3 for Deleting existing product").grid(row=3,column=0)
    myLabel5=Label(root,text="4 for Displaying the products").grid(row=4,column=0)
    myLabel6=Label(root,text="5 for Exit").grid(row=5,column=0)
    choice = Label(root, text = 'Enter your Choice: ', font=('calibre',10, 'bold')).grid(row=6,column=0)
    option=[1,2,3,4,5]
    r=IntVar(root)
    r.set("Select an Option")
    question_menu = OptionMenu(root, r, *option).grid(row=6,column=1)
    but =Button(root,text = 'Submit', command = lambda:[submit(), exit()]).grid(row=7,column=0)
    root.mainloop()
    if r.get()==1:
        
        root=Tk()
        root.geometry("400x200")
        myLabel1=Label(root,text="Choices are: ").grid(row=0,column=0)
        myLabel2=Label(root,text="A for modifying product code").grid(row=1,column=0)
        myLabel3=Label(root,text="B for modifying product name").grid(row=2,column=0)
        myLabel4=Label(root,text="C for modifying product price").grid(row=3,column=0)
        myLabel5=Label(root,text="D for modifying product stock").grid(row=4,column=0)
        choice = Label(root, text = 'Enter your Choice: ', font=('calibre',10, 'bold')).grid(row=5,column=0)
        option=["A","B","C","D"]
        r=StringVar(root)
        r.set("Select an Option")
        question_menu = OptionMenu(root, r, *option).grid(row=5,column=1)
        but =Button(root,text = 'Submit', command = lambda:[submit(), exit()]).grid(row=6,column=0)

        root.mainloop()
        if r.get()=="A":

           root=Tk()
           root.geometry("300x300")
           pcode=StringVar()
           ncode=StringVar()
           code1 = Label(root, text = 'Enter the existing code: ', font=('calibre',10, 'bold')).grid(row=0,column=0)
           e = Entry(root,textvariable = pcode, font=('calibre',10,'normal')).grid(row=0,column=1)
           code2 = Label(root, text = 'Enter the new code: ', font=('calibre',10, 'bold')).grid(row=1,column=0)
           e = Entry(root,textvariable = ncode, font=('calibre',10,'normal')).grid(row=1,column=1)
           but =Button(root,text = 'Submit', command = lambda:[Code(), exit()]).grid(row=2,column=0)
  
           root.mainloop()
           modifyC()

        elif r.get()=="B":
           root=Tk()
           root.geometry("300x300")
           pname=StringVar()
           nname=StringVar()
           name1 = Label(root, text = 'Enter the existing name: ', font=('calibre',10, 'bold')).grid(row=0,column=0)
           e = Entry(root,textvariable = pname, font=('calibre',10,'normal')).grid(row=0,column=1)
           name2 = Label(root, text = 'Enter the new name: ', font=('calibre',10, 'bold')).grid(row=1,column=0)
           e = Entry(root,textvariable = nname, font=('calibre',10,'normal')).grid(row=1,column=1)
           but =Button(root,text = 'Submit', command = lambda:[name(), exit()]).grid(row=2,column=0)
  
           root.mainloop()
           modifyN()

        elif r.get()=="C":
           root=Tk()
           root.geometry("300x300")
           namep=StringVar()
           nprice=StringVar()
           name1 = Label(root, text = 'Enter the product name: ', font=('calibre',10, 'bold')).grid(row=0,column=0)
           e = Entry(root,textvariable = namep, font=('calibre',10,'normal')).grid(row=0,column=1)
           name2 = Label(root, text = 'Enter the new price: ', font=('calibre',10, 'bold')).grid(row=1,column=0)
           e = Entry(root,textvariable = nprice, font=('calibre',10,'normal')).grid(row=1,column=1)
           but =Button(root,text = 'Submit', command = lambda:[price(), exit()]).grid(row=2,column=0)
  
           root.mainloop()
           modifyP()

        elif r.get()=="D":
           root=Tk()
           root.geometry("300x300")
           namep=StringVar()
           nstock=IntVar()
           name1 = Label(root, text = 'Enter the product name: ', font=('calibre',10, 'bold')).grid(row=0,column=0)
           e = Entry(root,textvariable = namep, font=('calibre',10,'normal')).grid(row=0,column=1)
           name2 = Label(root, text = 'Enter the new stock value: ', font=('calibre',10, 'bold')).grid(row=1,column=0)
           e = Entry(root,textvariable = nstock, font=('calibre',10,'normal')).grid(row=1,column=1)
           but =Button(root,text = 'Submit', command = lambda:[stock(), exit()]).grid(row=2,column=0)
  
           root.mainloop()
           modifyS()
    
    elif r.get()==2:
        root=Tk()
        root.geometry("400x200")
        r1=StringVar()
        r2=StringVar()
        r3=StringVar()
        r4=StringVar()
        
        myLabel1=Label(root,text="Enter the product detsils below: ",font=('calibre',10, 'bold')).grid(row=0,column=0)
        c = Label(root, text = 'Code: ', font=('calibre',10, 'bold')).grid(row=1,column=0)
        e1= Entry(root,textvariable = r1, font=('calibre',10,'normal')).grid(row=1,column=1)
        n = Label(root, text = 'Name: ', font=('calibre',10, 'bold')).grid(row=2,column=0)
        e2= Entry(root,textvariable = r2, font=('calibre',10,'normal')).grid(row=2,column=1)
        p = Label(root, text = 'Price per unit: ', font=('calibre',10, 'bold')).grid(row=3,column=0)
        e3= Entry(root,textvariable = r3, font=('calibre',10,'normal')).grid(row=3,column=1)
        s = Label(root, text = 'Stock available: ', font=('calibre',10, 'bold')).grid(row=4,column=0)
        e4= Entry(root,textvariable = r4, font=('calibre',10,'normal')).grid(row=4,column=1)
        but =Button(root,text = 'Submit', command = lambda:[addp(), exit()]).grid(row=6,column=0)
        root.mainloop()
        add()
    
    elif r.get()==3:
        root=Tk()
        root.geometry("400x200")
        r=StringVar()
        n = Label(root, text = 'Enter the product name to be deleted: ', font=('calibre',10, 'bold')).grid(row=1,column=0)
        e1= Entry(root,textvariable = r, font=('calibre',10,'normal')).grid(row=1,column=1)
        but =Button(root,text = 'Delete', command = lambda:[confirm()]).grid(row=2,column=0)
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
        t = Table(root)
        but =Button(root,text = 'CLOSE', command = lambda:[exit()]).grid(row=total_rows+1,column=2)
        root.mainloop()

    elif r.get()==5:
        break
    