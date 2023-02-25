from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from register import reg
from login import log
def open_reg():
    reg()

def open_log():
    log()

root=Tk()
root.title("HOME!")
root.geometry("1366x768+0+0")
root.config(bg="white")
    

#---BG_IMAGE---
bg=Label(root)
img=Image.open(r"images\bg.jpg")
img=ImageTk.PhotoImage(img)
bg.config(image=img)
bg.image=img
bg.place(x=0,y=0,relheight=1,relwidth=1)

#---ICON_IMAGE---
icon=Label(root)
icon.place(x=80,y=100)


frame1=Frame(root,bg="white")
frame1.place(x=585,y=100,width=700,height=586)

#---INTRODUCTION---
title=Label(frame1,text="FACIAL RECOGNITION SYSTEM",font=("Californian FB",30,"bold"),bg="white",fg="red").place(x=50,y=30)

desc1=Label(frame1,text="This is a Facial Recognition System for students. Here",font=("Californian FB",18),bg="white").place(x=80,y=100)
desc2=Label(frame1,text="students can mark attendance and detect mask by recognising",font=("Californian FB",18),bg="white").place(x=55,y=150)
desc3=Label(frame1,text="recognising individual faces.",font=("Californian FB",18),bg="white").place(x=210,y=200)

desc4=Label(frame1,text="New User!",font=("Californian FB",18),bg="white").place(x=120,y=350)
desc5=Label(frame1,text="Existing User!",font=("Californian FB",18),bg="white").place(x=450,y=350)

#---REGISTER_BUTTON---
reg_btn=Button(frame1)
img=Image.open(r"images\reg.jpg")
img=ImageTk.PhotoImage(img)
reg_btn.config(image=img,bd=0,cursor="hand2",command=open_reg)
reg_btn.image=img
reg_btn.place(x=80,y=400,height=50,width=240)

#---LOGIN_BUTTON---
log_btn=Button(frame1)
img=Image.open(r"images\log.jpg")
img=ImageTk.PhotoImage(img)
log_btn.config(image=img,bd=0,cursor="hand2",command=open_log)
log_btn.image=img
log_btn.place(x=400,y=400,height=50,width=240)

#---QUIT_BUTTON---
q_btn=Button(frame1)
img=Image.open(r"images\quit.jpg")
img=ImageTk.PhotoImage(img)
q_btn.config(image=img,bd=0,cursor="hand2",command=root.destroy)
q_btn.image=img
q_btn.place(x=230,y=500,height=50,width=240)

x=1
def a():
    global x
    img=Image.open(r"images\x"+str(x)+".png")
    img=ImageTk.PhotoImage(img)
    icon.config(image=img)
    icon.image=img
    x=x+1
    root.after(2000,a)
    if x==3:
        x=1
a()
root.mainloop()
