from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import numpy as np
import face_recognition


def log():
        
    def auth():

        #---HOME---
        def home():
            dash.destroy()
            root.destroy()

        def out():
            dash.destroy()
            txt_email.delete(0,END)
            txt_pswd.delete(0,END)

        #---ATTENDANCE_MARKER---
        def att():

            #---CAPTURE_IMAGE---
            def click():
                global cam
                cap=cv2.VideoCapture(0)
                while True:
                    rect,frame=cap.read()
                    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
                    cv2.imshow("CAPTURE - Press 'q' key!",frame)
                    cv2.imwrite(r"C:\Users\singh\OneDrive\Desktop\face recoginaion attendance by python\images\att.jpg",frame)
                    cam=(r"C:\Users\singh\OneDrive\Desktop\face recoginaion attendance by python\images\att.jpg")
                    imgc=Image.open(cam)
                    imgc=imgc.resize((480,330),Image.ANTIALIAS)
                    imgc=ImageTk.PhotoImage(imgc)
                    c_img.config(image=imgc)
                    c_img.image=imgc
                    if cv2.waitKey(1)& 0xff==ord('q'):
                        break
                cap.release()
                cv2.destroyAllWindows()
                
            #---MATCH_FACES---    
            def match():
                def mess():
                    mes.destroy()
                    at.destroy()
                global path1
                x=0
                img1=face_recognition.load_image_file(path1)
                img1=cv2.cvtColor(img1,cv2.COLOR_BGR2RGB)
                faceloc=face_recognition.face_locations(img1)[0]
                encode1=face_recognition.face_encodings(img1)[0]
                cv2.rectangle(img1,(faceloc[3],faceloc[0]),(faceloc[1],faceloc[2]),(255,0,0),2)

                img2=face_recognition.load_image_file(r"C:\Users\singh\OneDrive\Desktop\face recoginaion attendance by python\images\att.jpg")
                img2=cv2.cvtColor(img2,cv2.COLOR_BGR2RGB)
                faceloc1=face_recognition.face_locations(img2)[0]
                encode2=face_recognition.face_encodings(img2)[0]
                cv2.rectangle(img2,(faceloc1[3],faceloc1[0]),(faceloc1[1],faceloc1[2]),(255,0,0),2)
                
                res=face_recognition.compare_faces([encode1],encode2)
                if res[0] == True :
                    conn=mysql.connector.connect(host="127.0.0.1",user="root",password="")
                    cur=conn.cursor()
                    cur.execute("use face")
                    cur.execute("select * from info where email="+"'"+d1+"'"+" and pswd="+"'"+d2+"'"+"")
                    res=cur.fetchall()
                    for row in res:
                        no = row[5]
                    x=x+1
                    dash.destroy()
                    at.destroy()
                    no = no+1
                    cur.execute("update info set att="+"'"+str(no)+"'"+" where email="+"'"+d1+"'"+"")
                    auth()
                    conn.commit()
                    conn.close()
                    mes = Toplevel()
                    mes.geometry("250x80+602+200")
                    mes.title("SUCCESS")
                    er=Label(mes,text="Marked Successfully!",font=("bold")).place(x=15,y=15)
                    bt=Button(mes,text="Close",command=mess).place(x=105,y=45)
                    mes.lift()
                    
                else:
                    mes = Toplevel()
                    mes.geometry("250x80+602+200")
                    mes.title("ERROR")
                    er=Label(mes,text="Marking Failed!",font=("bold")).place(x=15,y=15)
                    bt=Button(mes,text="Close",command=mess).place(x=105,y=45)
                    
                
            #---ATTENDANCE_TOPLEVEL---    
            global path1
            at=Toplevel()
            at.title("ATTENDANCE!")
            at.geometry("1205x550+80+100")
            at.config(bg="white")
            c=0
            #---BG_IMAGE---
            
            bg=Label(at)
            img=Image.open(r"C:\Users\singh\OneDrive\Desktop\face recoginaion attendance by python\images\bg.jpg")
            img=img.resize((1205,550),Image.ANTIALIAS)
            img=ImageTk.PhotoImage(img)
            bg.config(image=img)
            bg.image=img
            bg.place(x=0,y=0,relheight=1,relwidth=1)

            #---Frame_Image---
            fr1=Frame(at,bg="white")
            fr1.place(x=66,y=50,width=500,height=400)

            fi = Frame(fr1,bg="red")
            fi.place(x=0,y=0,width=500,height=350)

            u_img=Label(fi)
            img=Image.open(r""+path1+"")
            img=img.resize((480,330),Image.ANTIALIAS)
            img=ImageTk.PhotoImage(img)
            u_img.config(image=img)
            u_img.image=img
            u_img.place(x=8,y=8)
            
            lb=Label(fr1,text="Your Profile Image",font=("Californian FB",15,"bold"),bg="white",fg="red").place(x=170,y=360)

            #---Frame_Camera---
            fr2=Frame(at,bg="white")
            fr2.place(x=632,y=50,width=500,height=400)

            fc = Frame(fr2,bg="skyblue")
            fc.place(x=0,y=0,width=500,height=350)

            c_img=Label(fc)
            imgc=Image.open(r"C:\Users\singh\OneDrive\Desktop\face recoginaion attendance by python\images\cam.jpg")
            imgc=imgc.resize((480,330),Image.ANTIALIAS)
            imgc=ImageTk.PhotoImage(imgc)
            c_img.config(image=imgc)
            c_img.image=imgc
            c_img.place(x=8,y=8)
            
            #---UPLOAD_IMAGE_BUTTON---
            upl_btn=Button(fr2)
            img=Image.open(r"C:\Users\singh\OneDrive\Desktop\face recoginaion attendance by python\images\upload.jpg")
            img=ImageTk.PhotoImage(img)
            upl_btn.config(image=img,bd=0,cursor="hand2",command=click)
            upl_btn.image=img
            upl_btn.place(x=178,y=360,height=30,width=144)

            #---MARK_ATTENDANCE---
            att_btn=Button(at)
            img=Image.open(r"C:\Users\singh\OneDrive\Desktop\face recoginaion attendance by python\images\mark.jpg")
            img=ImageTk.PhotoImage(img)
            att_btn.config(image=img,bd=0,cursor="hand2",command=match)
            att_btn.image=img
            att_btn.place(x=502,y=475,height=50,width=200)
            
        #---LOGIN_TOPLEVEL---
        global path1
        c=0
        d1=txt_email.get()
        d2=txt_pswd.get()
        
        dash=Toplevel()
        dash.title("DASHBOARD!")
        dash.geometry("1366x768+0+0")
        dash.config(bg="white")
                
        #---BG_IMAGE---
        bg=Label(dash)
        img=Image.open(r"C:\Users\singh\OneDrive\Desktop\face recoginaion attendance by python\images\bg.jpg")
        img=ImageTk.PhotoImage(img)
        bg.config(image=img)
        bg.image=img
        bg.place(x=0,y=0,relheight=1,relwidth=1)

        #---ICON_IMAGE---
        icon=Label(dash)
        img=Image.open(r"C:\Users\singh\OneDrive\Desktop\face recoginaion attendance by python\images\x2.png")
        img=ImageTk.PhotoImage(img)
        icon.config(image=img)
        icon.image=img
        icon.place(x=80,y=100)
            
        #---DASHBOARD_FRAME---
        frame1=Frame(dash,bg="white")
        frame1.place(x=585,y=100,width=700,height=586)

        #---HOME_BUTTON---
        h_btn=Button(frame1)
        img=Image.open(r"C:\Users\singh\OneDrive\Desktop\face recoginaion attendance by python\images\home.jpg")
        img=ImageTk.PhotoImage(img)
        h_btn.config(image=img,bd=0,cursor="hand2",command=home)
        h_btn.image=img
        h_btn.place(x=600,y=30,height=50,width=50)

        title=Label(frame1,text="Student Dashboard",font=("Californian FB",30,"bold"),bg="white",fg="red").place(x=50,y=30)

        conn=mysql.connector.connect(host="127.0.0.1",user="root",password="")
        cur=conn.cursor()
        cur.execute("use face")
        cur.execute("select * from info where email="+"'"+d1+"'"+" and pswd="+"'"+d2+"'"+"")
        res=cur.fetchall()
        for data in res:
            c=c+1
            path1=data[4]
            
            #---DEATIL_SECTION---
            det=Frame(frame1,bg="white",highlightthickness=2,highlightbackground = "black", highlightcolor= "black")
            det.place(x=0,y=150,height=200,width=700)
                
            det1=Label(det,text="Username : "+data[0],font=("Californian FB",20,"bold"),bg="white",fg="blue").place(x=50,y=20)
            det2=Label(det,text="Department : "+data[1],font=("Californian FB",20,"bold"),bg="white",fg="blue").place(x=50,y=60)
            det3=Label(det,text="Email : "+data[2],font=("Californian FB",20,"bold"),bg="white",fg="blue").place(x=50,y=100)
            det3=Label(det,text="Attendance : "+str(data[5]),font=("Californian FB",20,"bold"),bg="white",fg="blue").place(x=50,y=140)
            det4=Label(det)
            img1=Image.open(r""+data[4]+"")
            img1=img1.resize((250,160),Image.ANTIALIAS)
            img1=ImageTk.PhotoImage(img1)
            det4.config(image=img1)
            det4.image=img1
            det4.place(x=400,y=20)
            
            #---MARK_ATTENDANCE---
            att_btn=Button(frame1)
            img=Image.open(r"C:\Users\singh\OneDrive\Desktop\face recoginaion attendance by python\images\tick.jpg")
            img=ImageTk.PhotoImage(img)
            att_btn.config(image=img,bd=0,cursor="hand2",command=att)
            att_btn.image=img
            att_btn.place(x=250,y=390,height=50,width=200)

            #---LOGOUT_BUTTON---
            out_btn=Button(frame1)
            img=Image.open(r"C:\Users\singh\OneDrive\Desktop\face recoginaion attendance by python\images\logout.jpg")
            img=ImageTk.PhotoImage(img)
            out_btn.config(image=img,bd=0,cursor="hand2",command=out)
            out_btn.image=img
            out_btn.place(x=250,y=480,height=50,width=200)

            #---CLOSE_CONNECTION---
            conn.close()
        if c==0:
            out()
            mes = Toplevel()
            mes.geometry("250x80+785+200")
            mes.title("ERROR")
            er=Label(mes,text="Invalid Login Credentials!",font=("bold")).place(x=15,y=15)
            bt=Button(mes,text="Close",command=mes.destroy).place(x=105,y=45)
        
    #---LOGIN_TOPLEVEL---
    root=Toplevel()
    root.title("LOGIN!")
    root.geometry("1366x768+0+0")
    root.config(bg="white")
    

    #---BG_IMAGE---
    bg=Label(root)
    img=Image.open(r"C:\Users\singh\OneDrive\Desktop\face recoginaion attendance by python\images\bg.jpg")
    img=ImageTk.PhotoImage(img)
    bg.config(image=img)
    bg.image=img
    bg.place(x=0,y=0,relheight=1,relwidth=1)

    #---ICON_IMAGE---
    icon=Label(root)
    img=Image.open(r"C:\Users\singh\OneDrive\Desktop\face recoginaion attendance by python\images\x2.png")
    img=ImageTk.PhotoImage(img)
    icon.config(image=img)
    icon.image=img
    icon.place(x=80,y=100)

    
    #---LOGIN_FRAME---
    frame1=Frame(root,bg="white")
    frame1.place(x=585,y=100,width=700,height=586)

    title=Label(frame1,text="LOGIN HERE",font=("Californian FB",20,"bold"),bg="white",fg="red").place(x=50,y=30)

    email=Label(frame1,text="Email",font=("Californian FB",15,"bold"),bg="white",fg="gray").place(x=200,y=210)
    txt_email=Entry(frame1,font=("Californian FB",15),bg="lightgray")
    txt_email.place(x=200,y=240,width=300)

    pswd=Label(frame1,text="Password",font=("Californian FB",15,"bold"),bg="white",fg="gray").place(x=200,y=290)
    txt_pswd=Entry(frame1,show="*",font=("Californian FB",15),bg="lightgray")
    txt_pswd.place(x=200,y=320,width=300)
    
    #---HOME_BUTTON---
    h_btn=Button(frame1)
    img=Image.open(r"C:\Users\singh\OneDrive\Desktop\face recoginaion attendance by python\images\home.jpg")
    img=ImageTk.PhotoImage(img)
    h_btn.config(image=img,bd=0,cursor="hand2",command=root.destroy)
    h_btn.image=img
    h_btn.place(x=600,y=30,height=50,width=50)

    #---LOGIN_BUTTON---
    log_btn=Button(frame1)
    img=Image.open(r"C:\Users\singh\OneDrive\Desktop\face recoginaion attendance by python\images\log.jpg")
    img=ImageTk.PhotoImage(img)
    log_btn.config(image=img,bd=0,cursor="hand2",command=auth)
    log_btn.image=img
    log_btn.place(x=230,y=400,height=50,width=240)


    root.mainloop()
