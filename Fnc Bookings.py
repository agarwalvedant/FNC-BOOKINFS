import tkinter as tk 
import mysql.connector  
from tkinter import *
import pandas as pd
import webbrowser
import os
import random
import os
import tkinter.messagebox as tkMessageBox
from tkinter import BOTH, END, LEFT


from random import randint

global z
from tkinter import ttk, simpledialog
import datetime



mycon = mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="vedant",
  database="fncbookings",

)
mycursor=mycon.cursor()
    


def  ch():
    if  options1[0] and options8[0]:


        global clicked
        global options
        global root
        global popupMenu

        root = Tk()
        root.title("FNC BOOKINGS")
        root.geometry("300x300") 
        user = StringVar()

        clicked = StringVar(root)
        ds3= pd.read_sql("select * from domestics where sno =1",mycon)
        print(ds3)

        options = ['6000','8000','14000']
        clicked.set('Choose')

        popupMenu = OptionMenu(root , clicked, *options)
        Label(root, text="Ticket Price").pack()
        popupMenu.pack()
        Button(root,text="Select", command = arrays).pack()
    
        root.mainloop()
    

    elif options1[1] and options8[1]:

        global root2
        global clickedv
        global options2

        root2 = Tk()
        root2.title("FNC BOOKINGS")
        root2.geometry("300x300") 
        user = StringVar()


        global popupMenu2
        clickedv = StringVar(root2)

        options2 = ['6000','8000','14000']
        clickedv.set('Choose') # set the default option

        popupMenu2 = OptionMenu(root2 , clickedv, *options2)
        Label(root2, text="Ticket Price").pack()
        popupMenu2.pack()
        Button(root2,text="Select", command =Choose).pack()
    
        root2.mainloop()
    elif options1[2] and options8[2]:
 
        global clickedw
        global options3
        global root3
        global popupMenu3

        root3 = Tk()
        root3.title("FNC BOOKINGS")
        root3.geometry("300x300") 
        user = StringVar()
# Create a Tkinter variable
        clickedw= StringVar(root3)

# Dictionary with options
        options3= ['6000','8000','14000']
        clickedw.set('Choose') # set the default option

        popupMenu3 = OptionMenu(root3 , clickedw, *options3)
        Label(root3, text="Ticket Price").pack()
        popupMenu3.pack()
        Button(root3,text="Select", command =Choose).pack()
    
        root3.mainloop()        
    elif options1[0] and options8[2]:

        global clickedc
        global options4
        global root4
        global popupMenu4

        root4= Tk()
        root4.title("FNC BOOKINGS")
        root4.geometry("300x300") 
        user = StringVar()
# Create a Tkinter variable
        clickedc = StringVar(root4)

# Dictionary with options
        options4 = ['6000','8000','14000']
        clickedc.set('Choose') # set the default option

        popupMenu4 = OptionMenu(root4 , clickedc, *options4)
        Label(root4, text="Ticket Price").pack()
        popupMenu4.pack()
        Button(root4,text="Select", command =Choose).pack()
    
        root4.mainloop()
    elif options1[4] and options8[4]:

        global clickedz
        global options5
        global root5
        global popupMenu5

        root5 = Tk()
        root5.title("FNC BOOKINGS")
        root5.geometry("300x300") 
        user = StringVar()
# Create a Tkinter variable
        clickedz = StringVar(root5)

# Dictionary with options
        options5 = ['6000','8000','14000']
        clickedz.set('Choose') # set the default option

        popupMenu5 = OptionMenu(root5 , clickedz, *options5)
        Label(root5, text="Ticket Price").pack()
        popupMenu5.pack()
        Button(root5,text="Select", command =Choose).pack()
    
        root5.mainloop()
    elif options1[0] and options8[5]:
 
        global clickedq
        global options6
        global root6
        global popupMenu6

        root6 = Tk()
        root6.title("FNC BOOKINGS")
        root6.geometry("300x300") 
        user = StringVar()
# Create a Tkinter variable
        clickedq = StringVar(root6)

# Dictionary with options
        options6 = ['6000','8000','14000']
        clickedq.set('Choose') # set the default option

        popupMenu6 = OptionMenu(root6 , clicked6, *options6)
        Label(root6, text="Ticket Price").pack()
        popupMenu6.pack()
        Button(root6,text="Select", command =Choose).pack()
    
        root6.mainloop()
    elif options1 [6] and options8[5]:
        ds3= pd.read_sql("select * from idomestics where sno =7",mycon)
        print(ds3)
        global clickedt
        global options7
        global root7
        global popupMenu7

        root7 = Tk()
        root7.title("FNC BOOKINGS")
        root7.geometry("300x300") 
        user = StringVar()
# Create a Tkinter variable
        clickedt = StringVar(root7)

# Dictionary with options
        options7 = ['6000','8000','14000']
        clickedt.set('Choose') # set the default option

        popupMenu7 = OptionMenu(root7 , clickedt, *options7)
        Label(root7, text="Ticket Price").pack()
        popupMenu7.pack()
        Button(root7,text="Select", command =Choose).pack()
    
        root7.mainloop()


def  cha():
    if  options9[0] and options10[0]:
 
        global clicked
        global options
        global root
        global popupMenu

        root = Tk()
        root.title("FNC BOOKINGS")
        root.geometry("300x300") 
        user = StringVar()
# Create a Tkinter variable
        clicked = StringVar(root)

# Dictionary with options
        options = ['6000','8000','14000']
        clicked.set('Choose') # set the default option

        popupMenu = OptionMenu(root , clicked, *options)
        Label(root, text="Ticket Price").pack()
        popupMenu.pack()
        Button(root,text="Select", command =Choose).pack()
    
        root.mainloop()
    

    elif options9[0] and options10[1]:

        global root2
        global clickedv
        global options2

        root2 = Tk()
        root2.title("FNC BOOKINGS")
        root2.geometry("300x300") 
        user = StringVar()


        global popupMenu2
# Create a Tkinter variable
        clickedv = StringVar(root2)

# Dictionary with options
        options2 = ['6000','8000','14000']
        clickedv.set('Choose') # set the default option

        popupMenu2 = OptionMenu(root2 , clickedv, *options2)
        Label(root2, text="Ticket Price").pack()
        popupMenu2.pack()
        Button(root2,text="Select", command =Choose).pack()
    
        root2.mainloop()
    elif options9[0] and options10[2]:

        global clickedw
        global options3
        global root3
        global popupMenu3

        root3 = Tk()
        root3.title("FNC BOOKINGS")
        root3.geometry("300x300") 
        user = StringVar()
# Create a Tkinter variable
        clickedw= StringVar(root3)

# Dictionary with options
        options3= ['6000','8000','14000']
        clickedw.set('Choose') # set the default option

        popupMenu3 = OptionMenu(root3 , clickedw, *options3)
        Label(root3, text="Ticket Price").pack()
        popupMenu3.pack()
        Button(root3,text="Select", command =Choose).pack()
    
        root3.mainloop()        
    elif options9[1] and options10[3]:

        global clickedc
        global options4
        global root4
        global popupMenu4

        root4= Tk()
        root4.title("FNC BOOKINGS")
        root4.geometry("300x300") 
        user = StringVar()
# Create a Tkinter variable
        clickedc = StringVar(root4)

# Dictionary with options
        options4 = ['6000','8000','14000']
        clickedc.set('Choose') # set the default option

        popupMenu4 = OptionMenu(root4 , clickedc, *options4)
        Label(root4, text="Ticket Price").pack()
        popupMenu4.pack()
        Button(root4,text="Select", command =Choose).pack()
    
        root4.mainloop()

        global clickedz
        global options5
        global root5
        global popupMenu5

        root5 = Tk()
        root5.title("FNC BOOKINGS")
        root5.geometry("300x300") 
        user = StringVar()
# Create a Tkinter variable
        clickedz = StringVar(root5)

# Dictionary with options
        options5 = ['6000','8000','14000']
        clickedz.set('Choose') # set the default option

        popupMenu5 = OptionMenu(root5 , clickedz, *options5)
        Label(root5, text="Ticket Price").pack()
        popupMenu5.pack()
        Button(root5,text="Select", command =Choose).pack()
    
        root5.mainloop()
    elif options9[2] and options10[4]:

        global clickedq
        global options6
        global root6
        global popupMenu6

        root6 = Tk()
        root6.title("FNC BOOKINGS")
        root6.geometry("300x300") 
        user = StringVar()
# Create a Tkinter variable
        clickedq = StringVar(root6)

# Dictionary with options
        options6 = ['6000','8000','14000']
        clickedq.set('Choose') # set the default option

        popupMenu6 = OptionMenu(root6 , clicked6, *options6)
        Label(root6, text="Ticket Price").pack()
        popupMenu6.pack()
        Button(root6,text="Select", command =Choose).pack()
    
        root6.mainloop()
    elif options9 [2] and options10[5]:
        ds3= pd.read_sql("select * from idomestics where sno =7",mycon)
        print(ds3)
        global clickedt
        global options7
        global root7
        global popupMenu7

        root7 = Tk()
        root7.title("FNC BOOKINGS")
        root7.geometry("300x300") 
        user = StringVar()
# Create a Tkinter variable
        clickedt = StringVar(root7)

# Dictionary with options
        options7 = ['6000','8000','14000']
        clickedt.set('Choose') # set the default option

        popupMenu7 = OptionMenu(root7 , clickedt, *options7)
        Label(root7, text="Ticket Price").pack()
        popupMenu7.pack()
        Button(root7,text="Select", command =Choose).pack()
    
        root7.mainloop()
    
def Domestic():


    global clickeds
    global options1
    global root1
    global popupMenus
    global popupMenus8
    global clickedi
    global options8
    root1 = Tk()
    root1.title("FNC Domestic BOOKINGS")
    root1.geometry("300x300") 
    user = StringVar()
    ds2= pd.read_sql("select * from domestics",mycon)
    print(ds2)

    clickeds = StringVar(root1)
    clickedi = StringVar(root1)

    options1 = ['Jaipur','Delhi','Bombay','Jaipur','Haryana','Jaipur','Kerela']
    options8 = ['Bombay','Kashmir','Delhi','Delhi','Banglore','Goa','Goa']
    clickeds.set('From') 
    clickedi.set('Where')
    popupMenus = OptionMenu(root1 , clickeds, *options1)
    popupMenus8 = OptionMenu(root1 , clickedi, *options8)    
    popupMenus8.pack()
    popupMenus.pack()
    Button(root1,text="Select", command = ch).pack()
    
    root1.mainloop()

def Domestic():


    global clickeds
    global options1
    global root1
    global popupMenus
    global popupMenus8
    global clickedi
    global options8
    root1 = Tk()
    root1.title("FNC Domestic BOOKINGS")
    root1.geometry("300x300") 
    user = StringVar()
    ds= pd.read_sql("select * from domestics",mycon)
    print(ds)

# Create a Tkinter variable
    clickeds = StringVar(root1)
    clickedi = StringVar(root1)
# Dictionary with options
    options1 = ['Jaipur','Delhi','Bombay','Haryana','Kerela']
    options8 = ['Bombay','Kashmir','Delhi','Banglore','Goa',]
    clickeds.set('From') # set the default option
    clickedi.set('Where')
    popupMenus = OptionMenu(root1 , clickeds, *options1)
    popupMenus8 = OptionMenu(root1 , clickedi, *options8)    
    popupMenus8.pack()
    popupMenus.pack()
    Button(root1,text="Select", command = ch).pack()
    
    root1.mainloop()
def international():


    global clickedl
    global options9
    global root9
    global popupMenus9
    global popupMenus10
    global clickedl
    global options10
    root9 = Tk()
    root9.title("FNC International BOOKINGS")
    root9.geometry("300x300") 
    user = StringVar()
    ds= pd.read_sql("select * from international",mycon)
    print(ds)
# Create a Tkinter variable
    clickedp = StringVar(root9)
    clickedl= StringVar(root9)
# Dictionary with options
    options9 = ['India','Usa','Dubai']
    options10 = ['Usa','Russia','Thailand','United Kingdom','Singapore','Malayasia']
    clickedp.set('From') # set the default option
    clickedl.set('Where')
    popupMenus9 = OptionMenu(root9 , clickedp, *options9)
    popupMenus10 = OptionMenu(root9 , clickedl, *options10)    
    popupMenus9.pack()
    popupMenus10.pack()
    Button(root9,text="Select", command = cha).pack()
    
    root9.mainloop()
   
def Register_user():
    username_info = username.get()
    Password_info = Password.get()
    mail_info = mail.get()
    phone_info = phone.get()

    file=open(username_info,  'w')
    file.write(username_info+'\n')
    file.write(Password_info+'\n')
    file.write(mail_info+'\n')
    file.write(phone_info+'\n')
    file.close()
    
    username_entry.delete(0, END)
    Password_entry.delete(0, END)
    mail_entry.delete(0, END)
    phone_entry.delete(0, END)
    
    
   

    Label(screen1, text = "Welcome to Fnc Booking Registration Successfull ", fg = "orange").pack()


def login_verify():
    username1 = username_verify.get()
    password1 = password_verify.get()
    
    username_entry1.delete(0, END)
    password_entry1.delete(0, END)

    list_of_files = os.listdir()

    if username1 in list_of_files:
        file1 = open(username1, 'r')
        verify = file1.read().splitlines()
        if password1 in verify:
            print("login sucess")
            global drop
            global screen4
            global Button1
            global Button2
            screen4= Tk() 
            screen4.geometry("300x300")
            screen4.title("Welcome to Fnc Booking ")
            Button(screen4, text= "Domestic", command = Domestic ).pack()
            Button(screen4, text= "International", command = international).pack()


        

            
           
            
            
        
        else:
            print('password incorrect')
    else:
        print('username incorrect')

def registercust():
  
    L=[]
    name=input("enter name:")
    L.append(name)
    age=input("enter age:")
    L.append(age)
    email=input("enter email:")
    L.append(email)
    phone=input("enter Phone No.:")
    L.append(phone)
    adhaar=input("enter Adhaar no:")  
    L.append(adhaar)
    cust=(L)
    sql="insert into pdata(custname,age,email,phone,adhaar)values(%s,%s,%s,%s,%s)"
    mycursor.execute(sql,cust)
    mycon.commit()
def wifi():
        global ro
        global cli
        global op

        ro = Tk()
        ro.title("FNC BOOKINGS")
        ro.geometry("300x300") 
        
        

        global po
        Label(ro, text = 'Wifi').pack()
        Label (ro, text =()).pack()
# Create a Tkinter variable
        cli = StringVar(ro)

# Dictionary with options
        op= ['Yes (Cost = 500)','No']
        cli.set('Yes (Cost = 500)') # set the default option

        po= OptionMenu(ro , cli, *op)
        Label(ro, text="Wifi").pack()
        po.pack()
        Label (ro, text =()).pack()
        Button(ro,text="Select", command = services).pack()
def food():
        global roots
        global clic
        global opt

        roots = Tk()
        roots.title("FNC BOOKINGS")
        roots.geometry("300x300") 
        
        

        global pop
        Label(roots, text = 'Select Food type').pack()
        Label (roots, text =()).pack()

        clic = StringVar(roots)

        opt= ['Veg','Non-Veg']
        clic.set('Choose') 

        pop= OptionMenu(roots , clic, *opt)
        Label(roots, text="Food").pack()
        pop.pack()
        Label (roots, text =()).pack()
        Button(roots,text="Select", command = services).pack()
def seat():
        global r
        global cl
        global o

        r = Tk()
        r.title("FNC BOOKINGS")
        r.geometry("300x300") 
        
        

        global p
        Label(r, text = 'Seat').pack()
        Label (r, text =()).pack()

        cl = StringVar(r)


        o= ['Window Seat','Aisle seat', 'Middle Seat']
        cl.set('Aisle Seat') # set the default option

        p= OptionMenu(r , cl, *o)
        Label(r, text="Seat").pack()
        p.pack()
        Label (r, text =()).pack()
        Button(r,text="Select", command = services).pack()
def lugage():
    global scre
    global p
    global Password_ent
    scre= Tk()
    scre.title('Fnc Booking  Registeration')
    scre.geometry("200x200")
    Label(scre, text ='1 extra lugage is 10 kg for 3000').pack()
    Button(scre, text="Confirm", command =  services).pack()
    Password_ent= Entry(scre)

    Password_ent = simpledialog.askinteger("", "How many extra lugage")

    
    Button(scre, text="Next",command =  services).pack()


    scre.mainloop()
def openweb1():
    webbrowser.open("https://paytm.com/")
def openweb2():
    webbrowser.open("https://pay.google.com/intl/en_in/about/?gclid=Cj0KCQjw6ar4BRDnARIsAITGzlCbJi1vrRagEQHEPEVQRP3KUtB3Y1Md1lM8LOBQwqAe_xKQTLq-ghcaAsrAEALw_wcB")
def openweb3():
    webbrowser.open("https://www.icicibank.com/")
def openweb4():
    webbrowser.open("https://www.hdfcbank.com/")
def openweb5():
    webbrowser.open("https://www.onlinesbi.com/")
def ser():
    global ser
    ser = Tk()
    ser.title('Fnc Booking ')
    ser.geometry("300x300")

    Button(ser, text="Paytm",command=openweb1).pack()
    Button(ser, text="GPAY",command=openweb2).pack()
    Button(ser, text="iCIC",command=openweb3).pack()
    Button(ser, text="HDFC",command=openweb4).pack()
    Button(ser, text="SBI",command=openweb5).pack()
def nexe():
    global nexe

    nexe = Tk()
    nexe.title('Fnc Booking ')
    nexe.geometry("300x300")
    Label(nexe, text ='Select type of services if left everything will be consider basic').pack()
    if o[0] and opt[0] and op[0]:
        Label(nexe, text =("Extra lugage",Password_ent* 3000)).pack()
        Label(nexe, text ='wifi access').pack()
        Label(nexe, text =("Seat price",Password_entrys*6000)).pack()
        Label(nexe, text =("Total",(Password_entrys*6000)+(Password_ent* 3000)+500)).pack()
        Button(nexe, text="Payment Method",command =  ser).pack()
        
    else:
        print('sorry')
        
def services():
    global screend
    global p
    global Password_entrys
    screend = Tk()
    screend.title('Fnc Booking  Registeration')
    screend.geometry("300x300")  
    Label(screend, text ='Select type of services if left everything will be consider basic').pack()
    Button(screend, text="Food", command = food).pack()
    Button(screend, text="Seat Type ", command = seat).pack()
    Button(screend, text="Wifi", command = wifi).pack()
    Button(screend, text="Lugage", command = lugage).pack()
    Button(screend, text="Next", command = nexe).pack()

def arrays():
    global screens
    global p
    global Password_entrys
    screens = Tk()
    screens.title('Fnc Booking  Registeration')
    screens.geometry("200x200")
    Label(screens, text ='Entered all the detils').pack()
    Button(screens, text="Confirm", command = services).pack()
    Password_entrys= Entry(screens)

    Password_entrys = simpledialog.askinteger("", "How many Passangers")
    for i in range (Password_entrys):
        registercust()
    



    screens.mainloop()

def Register():
    global screen1
    screen1 = Toplevel(screen)
    screen1.geometry('300x400')
    
    screen1.title('Fnc Booking  Registeration')
    
    global username
    global Password
    global username_entry
    global Password_entry
    global mail
    global mail_entry
    global phone
    global phone_entry
    
    username = StringVar ()
    Password = StringVar ()
    mail = StringVar()
    phone = StringVar()
    
    Label(screen1, text = 'Please enter details bellow').pack()
    Label(screen1, text = '').pack()
    Label(screen1, text= 'username*').pack()
    username_entry= Entry(screen1, textvariable=username)
    username_entry.pack()
    Label(screen1, text= '').pack()
    Label(screen1, text= 'Password*').pack()
    Password_entry= Entry(screen1, textvariable=Password)
    Password_entry.pack()
    Label(screen1, text = '').pack()
    Label(screen1, text= 'Phone Number*').pack()
    phone_entry= Entry(screen1, textvariable=phone)
    phone_entry.pack()
    Label(screen1, text= '').pack()
    Label(screen1, text= 'MailId*').pack()
    mail_entry= Entry(screen1, textvariable=mail)
    mail_entry.pack()
    Label(text= '').pack()
    Label(screen1,text= "").pack()
    Button(screen1, text="Register", command = Register_user).pack()
    
def login():
    global screen2
    screen2 = Toplevel(screen)
    screen2.title('Fnc Bookings Login')
    screen2.geometry('300x250')
    Label(screen2, text = 'Please enter details bellow to login').pack()
    Label(screen2, text = '').pack()

    global username_verify
    global password_verify

    username_verify = StringVar()
    password_verify = StringVar()

    global username_entry1
    global password_entry1

    Label(screen2, text = 'Username * ').pack()
    username_entry1 = Entry(screen2, textvariable = username_verify)
    username_entry1.pack()
    Label(screen2, text = '').pack()
    Label(screen2, text = 'Password * ').pack()
    password_entry1 = Entry(screen2, textvariable = password_verify)
    password_entry1.pack()
    Label(screen2, text = '').pack()
    Button(screen2, text = 'Login', width = 10, height = 1, command = login_verify).pack()
    Label(screen2, text = '').pack()
    
 
    
     
def main_screen():
    global screen
    screen = Tk() 
    screen.geometry("300x300") 
    screen.title("Welcome to Fnc Booking ") 
    Label(text= "").pack()
    Button(text="Login", command =login).pack()
    Label(text= "").pack()
    Button(text="Register", command = Register).pack()
    
    screen.mainloop()
main_screen()


    
