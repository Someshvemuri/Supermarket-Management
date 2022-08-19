import string
import tkinter
from tkinter import *
from functools import partial
from tkinter.messagebox import askyesno
from tkinter import StringVar
from datetime import datetime, timedelta

import random

import os
from tkinter import font
import smtplib
import time
from tkinter.ttk import Button




def cancel(e):   
        
           kl=e.get()       
           k=open("pro.txt","r+")
           n=[]
           x=len(k.readlines())#counting no of elements in
           k.close()
           k=open("pro.txt","r+")
  

           for i in range(x):
            g=(k.readline()).split()
            
            n.append(g)

          
           
        
          # c=input("enter")
          
       
          
           print(len(n))
           for j in range(len(n)):
                 print(j)
                 print(n[j][0])
                 if n[j][0]==kl:
                  kk=(n[j][2]).split(",")
                  ll=n[j][3].split(",")
                  print(kk,ll)
                  
                  n.remove(n[j])
                  break
                     
              
           k.close()
           k=open("pro.txt","w")      
           for i in n:
               for j in i:
               
                   k.write(j)
                   k.write(' ')
               k.write("\n")
           k.close()
           k=open("products.txt","r")    
           m=[]
           g=len(k.readlines())
           k.close()
           k=open("products.txt","r")
           for i in range(g):
            v=(k.readline()).split()
            m.append(v)
           k.close() 
          # print(m) 
           for i  in range (len(kk)):
            for j in range (len(m)):
                if kk[i]==m[j][1]:
                    print(kk[i],m[j][1],ll[i])
                    m[j][3]=str(int(m[j][3])+int(ll[i]))
                    break
            k=open("products.txt","w") 
            
           for i in m:
               for j in i:
               
                   k.write(j)
                   k.write(' ')
               k.write("\n")
                       
def tk():               
           ee=Tk()
           ee.geometry("480x500")
           kl=StringVar()
           g=tkinter.Label(ee,text="enter the order id").grid(row=0,column=0)
           f=tkinter.Entry(ee,width=20,textvariable=kl).grid(row=0,column=1)
           Cancel=partial(cancel,kl)
           but=Button(ee,text="ok",command=Cancel)
          
          
           but.place(relx=0.5,rely=0.5,anchor="center")
         
           ee.mainloop()
                      



tk()           