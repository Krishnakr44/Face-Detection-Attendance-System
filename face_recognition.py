from sys import path
from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
import os
import mysql.connector
from datetime import datetime
import cv2
import numpy as np
from tkinter import messagebox


class Face_recognition:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        title_lbl=Label(self.root,text="FACE RECOGNITION ",font=("times new roman",35 ,"bold"),bg="blue",fg="white")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        img_top=Image.open(r"College img\Fac1.jpg")
        img_top=img_top.resize((650,700),Image.ANTIALIAS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        # set image as lable
        f_lb1 = Label(self.root,image=self.photoimg_top)
        f_lb1.place(x=0,y=55,width=650,height=700)


        img_botton=Image.open(r"College img\fac.jpg")
        img_botton=img_botton.resize((950,700),Image.ANTIALIAS)
        self.photobg_botton=ImageTk.PhotoImage(img_botton)

        # set image as lable
        f_lb1 = Label(self.root,image=self.photobg_botton)
        f_lb1.place(x=650,y=55,width=950,height=700)


        # Create buttons below the section 
        # ------------------------------------------------------------------------------------------------------------------- 
        # Training button 1
        std_b1 = Button(f_lb1,text="Face Recognition",command=self.recognition,cursor="hand2",font=("times new roman",18 ,"bold"),bg="dark green",fg="white")
        std_b1.place(x=280,y=620,width=360,height=60)

        #=====================Attendance===================


    def mark_attendance(self,i,r,n,d):
        with open("attendance.csv","r+",newline="\n") as f:
            myDatalist=f.readlines()
            name_list=[]
            for line in myDatalist:
                entry=line.split((","))
                name_list.append(entry[0])

            if((i not in name_list)) and ((r not in name_list)) and ((n not in name_list)):
                now=datetime.now()
                d1=now.strftime("%d/%m/%Y")
                dtString=now.strftime("%H:%M:%S")
                f.writelines(f"\n{i}, {r}, {n}, {dtString}, {d1}, Present")
                
                messagebox.showinfo("Result","Attendance successfully recorded",parent=self.root)
                cv2.system("cls")
            
            




        #================face recognition==================
    def recognition(self):
        def draw_boundray(img,classifier,scaleFactor,minNeighbors,color,text,clf):
            gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            featuers=classifier.detectMultiScale(gray_image,scaleFactor,minNeighbors)

            coord=[]
            
            for (x,y,w,h) in featuers:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                id,predict=clf.predict(gray_image[y:y+h,x:x+w])

                confidence=int((100*(1-predict/300)))

                conn = mysql.connector.connect(username='root', password='Shivam123',host='localhost',database='face_recognition_system')
                cursor = conn.cursor()

                cursor.execute("select Name from student where Student_ID="+str(id))
                n=cursor.fetchone()
                n="+".join(n)

                cursor.execute("select Roll_No from student where Student_ID="+str(id))
                r=cursor.fetchone()
                r="+".join(r)

                cursor.execute("select Department from student where Student_ID="+str(id))
                d=cursor.fetchone()
                d="+".join(d)


                if confidence > 77:
                    cv2.putText(img,f"Roll_No:{r}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(64,15,223),2)
                    cv2.putText(img,f"Name:{n}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(64,15,223),2)
                    cv2.putText(img,f"Department:{d}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(64,15,223),2)
                    self.mark_attendance( id,r,n,d)
                    
            
                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                    cv2.putText(img,"Unknown Face",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,0),3)    

                coord=[x,y,w,y]
            
            return coord   

            #==========
        def recognize(img,clf,faceCascade):
            coord=draw_boundray(img,faceCascade,1.1,10,(255,25,255),"Face",clf)
            return img
        
        faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        videoCap=cv2.VideoCapture(0)

        while True:
            ret,img=videoCap.read()
            img=recognize(img,clf,faceCascade)
            cv2.imshow("Welcome To face Recognition",img)

            if cv2.waitKey(1) == 13:
                break
        videoCap.release()
        cv2.destroyAllWindows() 


 # main class object

if __name__ == "__main__":
    root=Tk()
    obj=Face_recognition(root)
    root.mainloop()
