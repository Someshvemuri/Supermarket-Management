import tkinter
from tkinter import *
from tkinter.ttk import Button

def exit():
    global root
    root.destroy()

def searchp():
    s1=s.get()

class Table:
    def __init__(self,total_rows,total_columns,details,root):
        for i in range(total_rows):
            for j in range(total_columns):
                if i==0:
                    self.e = Entry(root, width=15, bg='LightSteelBlue',fg='Black',font=('Arial',16,'bold'))
                else:
                    self.e = Entry(root, width=15, fg='blue',font=('Arial',16))
                self.e.grid(row=i, column=j)
                self.e.insert(END, details[i][j])

def search(s):
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
        if i.upper()==s.get().upper():
            detail=[]
            sp=[]
            detail.insert(0,["CODE","NAME","PRICE","STOCK"])
            sp.append(details[i][0])
            sp.append(i)
            sp.append(details[i][1])
            sp.append(details[i][2])
            detail.append(sp)
    total_rows = len(detail)
    total_columns = len(detail[0])
    root = Tk()
    t = Table(total_rows,total_columns,detail,root)
    root.mainloop()

root=Tk()
root.geometry("400x200")
s=StringVar()
n = Label(root, text = 'Enter the product name to be searched: ', font=('calibre',10, 'bold')).grid(row=1,column=0)
e1= Entry(root,textvariable = s, font=('calibre',10,'normal')).grid(row=1,column=1)
but =Button(root,text = 'Search', command = lambda:[searchp(),exit()]).grid(row=2,column=0)
root.mainloop()
search(s)
