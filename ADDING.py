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




import tkinter as tk
d = _Display()


def exit():
    root.destroy()

class Table:
    def __init__(self,root):
        for i in range(total_rows):
            for j in range(total_columns):
                if i==0:
                    self.e = tk.Entry(root, width=15, bg='LightSteelBlue',fg='Black',font=('Arial',16,'bold'))

                else:
                    self.e = tk.Entry(root, width=15, fg='blue',font=('Arial',16))
                 
                self.e.grid(row=i, column=j)
                self.e.insert(tk.END, details[i][j])

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
    root = tk.Tk()
    t = Table(root)
    but =tk.Button(root,text = 'CLOSE', command = lambda:[exit()]).grid(row=total_rows+1,column=2)
    root.mainloop
window = tk.Tk()
window.geometry('800x450+300+300')
window.title("ventor shop")
greeting2= tk.Label(window,text="enter the product as a list:",font=('Arial',16,'bold'))
entry1= tk.Entry(window,fg = "black",bg="white",width=50)
greeting2.grid()
entry1.grid()
greeting3 = tk.Label(window,text="enter the quantity of the product as a list",font=('Arial',16,'bold'))
entry2 = tk.Entry(window,fg = "black",bg="white",width=50)
greeting3.grid()
entry2.grid()
def display():
    

    k=0
    n=entry1.get()
    m=entry2.get()
    l1=n.split(",")
    l2=m.split(",")
    h = []
    j=[]
    for i in l1:
        h.append(i)
    for k in l2:
        j.append(k)
    
    for i in range(len(h)):
        l = h.pop()
        z =j.pop()
        d.insert(l,z)
        
    with open("product.txt","r+") as fh: 
        n=len(fh.readlines())

    with open("product.txt","r+") as fh: 
        details={}
        for i in range(n):
            prod=(fh.readline()).split()
            key=prod[1]
            prod.remove(prod[1])
            details[key]=prod
        print(details)
    for i in range(len(l1)):
        if l1[i] in details and l2[i] <= details[l1[i]][2] and int(l2[i])>0:
            g =int(details[l1[i]][2])-int(l2[i])
            details[l1[i]][2] = str(g)
            print(details)
            d._Sdictionary()
            """with open("order.txt","w") as fs:
                for i in d._Sdictionary:
                    fs.write(str(i)+" "+str(details[i][0]))
                    fs.write("\n")"""


            new1=tk.Toplevel()
            #new1.title("Displaying the products")
            new1.geometry('800x450+300+300')                
            gre4 = tk.Label(new1,text="your order is placed succcessfully",font=('Arial',16,'bold'))
            #entry3 = tk.Entry(fg = "black",bg="white",width=50)                
            #entry3.insert(0,l1[i])
            gre4.grid()
            new1.mainloop()
        else:
            root1 = tk.Toplevel()
            gre5 = tk.Label(root1,text="please enter a valid input",font=('Arial',16,'bold'))
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
    with open("product.txt","w") as fh:
        for i in details:
            fh.write(str(details[i][0])+" "+str(i)+" "+str(details[i][1])+" "+str(details[i][2]))
            fh.write("\n")



button=tk.Button(window,text="submit",width=25,height=5,bg="blue",fg="yellow",command=lambda:[display()])
#button2 = tk.Button(window,text="close",width=25,height=5,bg="blue",fg="yellow",command=lambda:[exit()])
button.grid()
#button2.grid()

    



window.mainloop()


                
                
                

 
