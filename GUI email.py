import tkinter
from tkinter import font
import smtplib
import time
from tkinter.ttk import Button

start=time.time()

def bill():
 order={"apple":3,"tomato":2,"onion":4,"brinjal":2,"drumstick":1,"pumpkin":0}#inputs from user in dict form(example)


 d=[i for i in order.keys()]

 e=[i for i in order.values()]
 f=open("products.txt","r")




 g=len(f.readlines())
 f.close()
 f=open("products.txt","r")
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
 k="receiver@gmail.com"
 x=k[0:-10]
# Authentication
 s.login("cuedelacci@gmail.com", "rrnhihgezznhtdxy")
 sub="CONFORAMTION OF YOUR VEGETABLE ORDER"
 body=("HELLO!!!,"+x+"\n\t{}".format("your order has sucessfully placed and it will be delivered soon\n")+"invoice for your order\n\n\n"+l+"\n\n\n\t{}".format("have a nice day :)"))
  
# message to be sent
 message = "Subject:{}\n\n{}".format(sub,body)

  
# sending the mail
 s.sendmail("cuedelacci@gmail.com", "vemula2110137@ssn.edu.in", message)
 

# terminating the session
 s.quit()
 window=tkinter.Tk()
 
 window.geometry("700x1000")
 l=tkinter.Label(window,text=d,font=("arial",12,"italic")).grid(column=0,row=0)
 end=time.time()
 print("time taken to compile",end-start)


 bt=tkinter.Button(window,text="exit",command=window.destroy,fg="red",bg="green",height=3,width=5).grid(column=0,row=1)
 
 window.mainloop()
 
bill() 
