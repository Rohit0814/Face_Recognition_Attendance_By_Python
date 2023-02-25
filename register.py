from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import numpy as np
import face_recognition

def reg():
    
    path=""
    #---REGISTER---
    def save():
        def clear():
            txt_name.delete(0,END)
            txt_dept.delete(0,END)
            txt_email.delete(0,END)
            txt_pswd.delete(0,END)
            root.destroy()
            
        global path
        d1=txt_name.get()
        d2=txt_dept.get()
        d3=txt_email.get()
        d4=txt_pswd.get()
        d5=str(0)
        
        if d1=="" or d2=="" or d3=="" or d4=="" or d5=="" or str=="":
            messagebox.showerror("ERROR!","All Fields Are Required!")
        else:
            try:
                conn = mysql.connector.connect(host='127.0.0.1',user='root',password='')
                cur = conn.cursor()
                cur.execute("use face")
                cur.execute("insert into info values("+"'"+d1+"'"+","+"'"+d2+"'"+","+"'"+d3+"'"+","+"'"+d4+"'"+","+"'"+path+"'"+","+"'"+d5+"'"+")")
                conn.commit()
                conn.close()
                messagebox.showinfo("SUCCESS","Data Saved Successfully!")
                clear()
            except:
                messagebox.showerror("ERROR!","Error Occured!Try Again!")
        
    #---UPLOAD_IMAGE---
    def cam():
        global path
        cap=cv2.VideoCapture(0)
        conn=mysql.connector.connect(host="127.0.0.1",user="root",password="")
        my=conn.cursor()
        my.execute("use face")
        res=my.execute("select count(*) from info")
        rows=my.fetchall()
        for i in rows:
            x=i[0]
            break
        x=x+1
        while True:
            rect,frame=cap.read()
            cv2.imshow("CAPTURE FACE",frame)
            cv2.imwrite(r"user_image/pic"+str(x)+".jpg",frame)
            if cv2.waitKey(1)& 0xff==ord('q'):
                break
        cap.release()
        cv2.destroyAllWindows()

        img_lb=Label(img_fr)
        img_lb.place(x=0,y=0)
        path="user_image/pic"+str(x)+".jpg"
        img=Image.open(r"user_image/pic"+str(x)+".jpg")
        img=img.resize((280,170),Image.ANTIALIAS)
        img=ImageTk.PhotoImage(img)
        img_lb.config(image=img)
        img_lb.image=img
        
    root=Toplevel()
    root.title("REGISTER!")
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
    img=Image.open(r"images\x1.png")
    img=ImageTk.PhotoImage(img)
    icon.config(image=img)
    icon.image=img
    icon.place(x=80,y=100)

    
    #---REGISTER_FRAME---
    frame1=Frame(root,bg="white")
    frame1.place(x=585,y=100,width=700,height=586)

    title=Label(frame1,text="REGISTER HERE",font=("Californian FB",20,"bold"),bg="white",fg="red").place(x=50,y=30)

    img_lbl=Label(frame1,text="Image",font=("Californian FB",15,"bold"),bg="white",fg="gray").place(x=380,y=100)

    name=Label(frame1,text="Username",font=("Californian FB",15,"bold"),bg="white",fg="gray").place(x=50,y=100)
    txt_name=Entry(frame1,font=("Californian FB",15),bg="lightgray")
    txt_name.place(x=50,y=130,width=300)

    email=Label(frame1,text="Email",font=("Californian FB",15,"bold"),bg="white",fg="gray").place(x=50,y=180)
    txt_email=Entry(frame1,font=("Californian FB",15),bg="lightgray")
    txt_email.place(x=50,y=210,width=300)

    dept=Label(frame1,text="Department",font=("Californian FB",15,"bold"),bg="white",fg="gray").place(x=50,y=260)
    txt_dept=Entry(frame1,font=("Californian FB",15),bg="lightgray")
    txt_dept.place(x=50,y=290,width=300)

    pswd=Label(frame1,text="Password",font=("Californian FB",15,"bold"),bg="white",fg="gray").place(x=50,y=340)
    txt_pswd=Entry(frame1,show="*",font=("Californian FB",15),bg="lightgray")
    txt_pswd.place(x=50,y=370,width=300)
    
    #---HOME_BUTTON---
    h_btn=Button(frame1)
    img=Image.open(r"images\home.jpg")
    img=ImageTk.PhotoImage(img)
    h_btn.config(image=img,bd=0,cursor="hand2",command=root.destroy)
    h_btn.image=img
    h_btn.place(x=600,y=30,height=50,width=50)
    
    #---IMAGE_FRAME---
    img_fr=Frame(frame1,highlightthickness=2,highlightbackground = "black", highlightcolor= "black")
    img_fr.place(x=380,y=130,height=180,width=290)

    #---REGISTER_BUTTON---
    reg_btn=Button(frame1)
    img=Image.open(r"images\reg.jpg")
    img=ImageTk.PhotoImage(img)
    reg_btn.config(image=img,bd=0,cursor="hand2",command=save)
    reg_btn.image=img
    reg_btn.place(x=230,y=450,height=50,width=240)

    #---UPLOAD_IMAGE_BUTTON---
    upl_btn=Button(frame1)
    img=Image.open(r"images\upload.jpg")
    img=ImageTk.PhotoImage(img)
    upl_btn.config(image=img,bd=0,cursor="hand2",command=cam)
    upl_btn.image=img
    upl_btn.place(x=453,y=370,height=30,width=144)

    root.mainloop()
