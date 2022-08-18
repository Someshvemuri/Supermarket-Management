#Login Code
import json
import tkinter
from tkinter import StringVar
import os
#opening tkinter
window=tkinter.Tk()
#creating window 
window.geometry("480x240")
username=StringVar()
password=StringVar()
# Creating a window to get username and password for security purpose... 
window.title("LOGIN AND REGISTER")
label1=tkinter.Label(window,text="USERNAME").grid(row=0,column=0)
username1=tkinter.Entry(window,width=20,textvariable=username).grid(row=0,column=1)
label2=tkinter.Label(window,text="PASSWORD").grid(row=1,column=0)
password1=tkinter.Entry(window,width=20,textvariable=password,show="*").grid(row=1,column=1)
def register():
    f1=open("USERNAME.txt","a+")
    f2=open("PASSWORD.txt","a+")
    # Appending the new user in the database table already created before...
    x=username.get()
    y=password.get()
    flag=True
    flag1=True
    # Getting input to addd new user ...
    for i in range(0,len(x)):
#checking whether the input given is alphanumerical or not , if not it wont get appended...
        if x[i].isalnum():
            flag=False
            pass
        else:
            flag=True
            break
    for j in range(0,len(y)):
        if y[j].isalnum():
            flag1=False
        else:
            flag1=True
            break
    if flag==True:
        window2=tkinter.Label(window,text="USE ONLY ALPHABETS OR NUMBERS FOR USERNAME").grid(row=2,column=2)
    elif flag1==True:
        window2=tkinter.Label(window,text="USE ONLY ALPHABETS OR NUMBERS FOR PASSWORD").grid(row=2,column=2)
    elif flag==False and flag1==False:
        f1.writelines([x])
        f2.writelines([y])
        MP=tkinter.Tk()
        MP.geometry("480x240")
        MP.title("VEGETABLE SHOP")
        ext=tkinter.Button(MP,text="EXIT",fg="Black",bg="White",command=MP.destroy).grid(row=6,column=2)
        hl=tkinter.Button(MP,text="HELP",fg="Black",bg="White",command=help_).grid(row=4,column=4)
        ab=tkinter.Button(MP,text="ABOUT",fg="Black",bg="White",command=about).grid(row=4,column=2)
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
    up=[]
    ps=[]
    for i in range(0,len(up1)):
        y=up1[i]
        x=""
        for j in range(0,len(y)):
            if y[j].isalnum():
                x=x+y[j]
            else:
                pass
        up.append(x)
    for i in range(0,len(ps1)):
        a=ps1[i]
        b=""
        for j in range(0,len(a)):
            if a[j].isalnum():
                b=b+a[j]
            else:
                pass
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
                MP.geometry("480x240")
                ext=tkinter.Button(MP,text="EXIT",fg="Black",bg="White",command=MP.destroy).grid(row=6,column=2)
                hl=tkinter.Button(MP,text="HELP",fg="Black",bg="White",command=help_).grid(row=4,column=4)
                ab=tkinter.Button(MP,text="ABOUT",fg="Black",bg="White",command=about).grid(row=4,column=2)
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
    password2=password.get()
    #connecting the database to access the username and password table...
    f1=open("USERNAMEVENDOR.txt","r+")
    f2=open("PASSWORDVENDOR.txt","r+")
    up1=f1.readlines()
    ps1=f2.readlines()
    up=[]
    ps=[]
    for i in range(0,len(up1)):
        y=up1[i]
        x=""
        for j in range(0,len(y)):
            if y[j].isalnum():
                x=x+y[j]
            else:
                pass
        up.append(x)
    for i in range(0,len(ps1)):
        a=ps1[i]
        b=""
        for j in range(0,len(a)):
            if a[j].isalnum():
                b=b+a[j]
            else:
                pass
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
                MP.geometry("480x240")

                ext=tkinter.Button(MP,text="EXIT",fg="Black",bg="White",command=MP.destroy).grid(row=6,column=2)
                hl=tkinter.Button(MP,text="HELP",fg="Black",bg="White",command=help_).grid(row=4,column=4)
                ab=tkinter.Button(MP,text="ABOUT",fg="Black",bg="White",command=about).grid(row=4,column=2)
            else:
                window2=tkinter.Label(window,text="INVALID PASSWORD TRY AGAIN!!!").grid(row=5,column=0)
        elif username2 not in up:
            window2=tkinter.Label(window,text="INVALID USERNAME TRY AGAIN!!!").grid(row=5,column=0)
    username.set("")
    password.set("")
# buttons for LOGIN
windowbt=tkinter.Button(window,text="CUSTOMER LOGIN",fg="Black",bg="White",command=check_usernameandpassword).grid(row=2,column=0)
windowbt=tkinter.Button(window,text="VENDOR LOGIN",fg="Black",bg="White",command=check_usernameandpasswordv).grid(row=2,column=1)
bt1=tkinter.Button(window,text="CUSTOMER REGISTER",fg="Black",bg="White",command=register).grid(row=2,column=2)
def help_():
    os.startfile("HELP.txt")
def about():
    os.startfile("ABOUT.txt")
window.mainloop()