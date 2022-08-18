from sys import path
from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
import os
import mysql.connector
import cv2
import numpy as np
from tkinter import messagebox


class train:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        title_lbl=Label(self.root,text="DO YOU WANT TO TRAIN DATA",font=("times new roman",35 ,"bold"),bg="blue",fg="white")
        title_lbl.place(x=0,y=0,width=1530,height=45)
        # This part is image labels setting start 
        # first header image  
        img_top=Image.open(r"College img\TRAN.jpg")
        img_top=img_top.resize((1530,325),Image.ANTIALIAS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        # set image as lable
        f_lb1 = Label(self.root,image=self.photoimg_top)
        f_lb1.place(x=0,y=55,width=1530,height=325)

        # backgorund image
        title_lbl=Button(self.root,text="Train Data",cursor="hand2",command=self.train_classifier,font=("times new roman",35 ,"bold"),bg="GREEN",fg="white")
        title_lbl.place(x=0,y=380,width=1530,height=60)
 


        img_botton=Image.open(r"College img\t_bg1.jpg")
        img_botton=img_botton.resize((1530,325),Image.ANTIALIAS)
        self.photobg_botton=ImageTk.PhotoImage(img_botton)

        # set image as lable
        f_lb1 = Label(self.root,image=self.photobg_botton)
        f_lb1.place(x=0,y=440,width=1530,height=325)
# ==================Create Function of Traing===================
    def train_classifier(self):
        data_dir=("data")
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]
        
        faces=[]
        ids=[]

        for image in path:
            img=Image.open(image).convert('L') # conver in gray scale 
            imageNp = np.array(img,'uint8')
            id=int(os.path.split(image)[1].split('.')[1])

            faces.append(imageNp)
            ids.append(id)

            cv2.imshow("Training",imageNp)
            cv2.waitKey(1)==13
        
        ids=np.array(ids)

#=================Train Classifier=============
        recogniger= cv2.face.LBPHFaceRecognizer_create()
        recogniger.train(faces,ids)
        recogniger.write("classifier.xml")

        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training Dataset Complated!",parent=self.root)



        
        
        



        # main class object

if __name__ == "__main__":
    root=Tk()
    obj=train(root)
    root.mainloop()
