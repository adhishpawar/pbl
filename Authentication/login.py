from tkinter import *
from tkinter import ttk
from PIL import ImageTk
from PIL import Image
from tkinter import messagebox

class login_window:
    def __init__(self,root):
        self.root=root
        self.root.title("Login")
        self.root.geometry("1600x800+0+0")
        
        self.bg=ImageTk.PhotoImage(file=r"D:\PBL\imgs\BG1.jpg")

        lbl_bg=Label(self.root,image=self.bg)
        lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)
        frame=Frame(self.root,bg="black")
        frame.place(x=610,y=170,width=340,height=450)

        img1=Image.open(r"D:\PBL\images\login-icon.jpg")
        img1=img1.resize((100,100),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        lblimg1=Label(image=self.photoimg1,borderwidth=0)
        lblimg1.config(bg="black")
        lblimg1.place(x=730,y=175,width=100,height=100)

        getstr=Label(frame,text="Get Started",font=("times new roman",20,"bold"),fg="white",bg="black")
        getstr.place(x=95,y=100)

        #label

        username=Label(frame,text="Username:",font=("times new roman",15,"bold"),fg="white",bg="black")
        username.place(x=70,y=155)

        self.txtusr=ttk.Entry(frame,font=("times new roman",15,"bold"))
        self.txtusr.place(x=40,y=180,width=270)

        password=Label(frame,text="Password:",font=("times new roman",15,"bold"),fg="white",bg="black")
        password.place(x=70,y=225)

        self.txtpass=ttk.Entry(frame,show='x',font=("times new roman",15,"bold"))
        self.txtpass.place(x=40,y=250,width=270)

        ##icon images

        img2=Image.open(r"D:\PBL\images\login-icon.jpg")
        img2=img2.resize((25,25),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        lblimg1=Label(image=self.photoimg2,borderwidth=0)
        lblimg1.config(bg="black")
        lblimg1.place(x=650,y=323,width=25,height=25)


        img3=Image.open(r"D:\PBL\images\pass-image.png")
        img3=img3.resize((25,25),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        lblimg1=Label(image=self.photoimg3,borderwidth=0)
        lblimg1.config(bg="black")
        lblimg1.place(x=650,y=392,width=25,height=25)


        #Login Button
        loginbtn=Button(frame,command=self.login,text="LOGIN",font=("times new roman",15,"bold"),bd=3,relief=RIDGE,fg="white",bg="red",activeforeground="red",activebackground="white")
        loginbtn.place(x=110,y=300,width=120,height=35)

        ##register 
        loginbtn=Button(frame,text="NEW USER Register",font=("times new roman",10,"bold"),borderwidth=0,fg="white",bg="black",activeforeground="black",activebackground="white")
        loginbtn.place(x=10,y=350,width=160)

        #forgot pass

        loginbtn=Button(frame,text="Forgot Password",font=("times new roman",10,"bold"),borderwidth=0,fg="white",bg="black",activeforeground="black",activebackground="white")
        loginbtn.place(x=10,y=375,width=160)

    def login(self):
        if self.txtusr.get()=="" or self.txtpass.get()=="":
            messagebox.showerror("Error", "Please enter details!")
        
        elif self.txtusr.get()=="varunpatki03@gmail.com" and self.txtpass.get()=="Pune@2016":
            messagebox.showinfo("Success","Welcome To The Student DataBase System")
        else:
            messagebox.showerror("Error","Invalid Credentials!")








        


         



if __name__=="__main__":
    root=Tk()
    app=login_window(root)
    root.mainloop()