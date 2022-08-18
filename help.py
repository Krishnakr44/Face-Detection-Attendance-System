from tkinter import*
from PIL import Image,ImageTk



class Helpsupport:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1366x768+0+0")
        self.root.title("Face_Recogonition_System")
        # This part is image labels setting start 
        # first header image  
        img=Image.open(r"College img\banner.jpg")
        img=img.resize((1366,130),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        # set image as lable
        f_lb1 = Label(self.root,image=self.photoimg)
        f_lb1.place(x=0,y=0,width=1366,height=130)

        # backgorund image 
        bg1=Image.open(r"College img\bg4.png")
        bg1=bg1.resize((1366,768),Image.ANTIALIAS)
        self.photobg1=ImageTk.PhotoImage(bg1)

        # set image as lable
        bg_img = Label(self.root,image=self.photobg1)
        bg_img.place(x=0,y=130,width=1366,height=768)


        #title section
        title_lb1 = Label(bg_img,text="Help Support",font=("verdana",30,"bold"),bg="white",fg="navyblue")
        title_lb1.place(x=0,y=0,width=1366,height=45)
# ------------------------------------------------------------------------------------------------------------------- 
        # CALL button 1
        std_img_btn=Image.open(r"College img\call1.jpg")
        std_img_btn=std_img_btn.resize((80,80),Image.ANTIALIAS)
        self.std_img1=ImageTk.PhotoImage(std_img_btn)

        std_b1 = Button(bg_img,image=self.std_img1,cursor="hand2")
        std_b1.place(x=80,y=200,width=80,height=80)

        std_b1_1 = Button(bg_img,text="8840384628",cursor="hand2",font=("tahoma",15,"bold"),bg="black",fg="white")
        std_b1_1.place(x=160,y=200,width=300,height=80)

        std_b1_1 = Button(text="FOR MORE QUERIES CONTACT US",cursor="hand2",font=("tahoma",15,"bold"),bg="black",fg="white")
        std_b1_1.place(x=80,y=180,width=1200,height=50)


        # MAP  button 2
        det_img_btn=Image.open(r"College img\map.jpg")
        det_img_btn=det_img_btn.resize((80,80),Image.ANTIALIAS)
        self.det_img1=ImageTk.PhotoImage(det_img_btn)

        det_b1 = Button(bg_img,image=self.det_img1,cursor="hand2",)
        det_b1.place(x=80,y=280,width=80,height=80)

        det_b1_1 = Button(bg_img,text="GL Bajaj Group Of Instution",cursor="hand2",font=("tahoma",15,"bold"),bg="black",fg="white")
        det_b1_1.place(x=160,y=280,width=300,height=80)

         # MAIL  button 3
        att_img_btn=Image.open(r"College img\mail.jpg")
        att_img_btn=att_img_btn.resize((80,80),Image.ANTIALIAS)
        self.att_img1=ImageTk.PhotoImage(att_img_btn)

        att_b1 = Button(bg_img,image=self.att_img1,cursor="hand2",)
        att_b1.place(x=80,y=355,width=80,height=80)

        att_b1_1 = Button(bg_img,text="glbajajgroup.org",cursor="hand2",font=("tahoma",15,"bold"),bg="black",fg="white")
        att_b1_1.place(x=160,y=355,width=300,height=80)

       # hlp_b1_1 = Button(bg_img,text="d.shivam1507@gmail.com",cursor="hand2",font=("tahoma",15,"bold"),bg="white",fg="navyblue")
        #hlp_b1_1.place(x=600,y=400)

if __name__ == "__main__":
    root=Tk()
    obj=Helpsupport(root)
    root.mainloop()