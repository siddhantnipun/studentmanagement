from tkinter import*
from tkinter import ttk,messagebox
from PIL import Image,ImageTk,ImageDraw
import sqlite3
class Login_window:
    def __init__(self,root):
        self.root=root
        self.root.title("Login")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="#344a58")

        #----backgroundcolor----

        #left_lbl=Label(self.root,bg="#006192",bd=0)
        #left_lbl.place(x=0,y=0,relheight=1,width=600)

        #right_lbl=Label(self.root,bg="#000c12",bd=0)
        #right_lbl.place(x=600,y=0,relheight=1,relwidth=1)

        #bgimage
        self.bg=ImageTk.PhotoImage(file="img3.png")
        bg=Label(self.root,image=self.bg).place(x=0,y=0,relwidth=1,relheight=1)

        #------Frame------
        #login_frame=Frame(self.root,bg="white")
        l_frame=Frame(self.root,bg="#99a5ab")
        l_frame.place(x=250,y=100,width=800,height=500)

        #------left frame----
        #self.lbl=Label(self.root,text="\nShashi Kant Project",font=("Gabriola",25,"bold"),fg="white",compound=BOTTOM,bg="#000609",bd=0)
        #self.lbl.place(x=90,y=120,height=450,width=350)
        self.left=ImageTk.PhotoImage(file="img12.png")
        left=Label(self.root,image=self.left,bg="#99a5ab").place(x=100,y=100,width=360,height=500)
        
        #title=Label(self.root,text="Shashi Kant Project",font=("Gabriola",25,"bold"),bg="green",fg="white").place(x=120,y=140)

        title=Label(l_frame,text="LOGIN HERE",font=("times new roman",30,"bold"),bg="#99a5ab",fg="#006192").place(x=250,y=50)

        email=Label(l_frame,text="E-MAIL ADDRESS",font=("times new roman",18,"bold"),bg="#99a5ab",fg="black").place(x=250,y=150)
        self.txt_email=Entry(l_frame,font=("times new roman",15),bg="lightgray")
        self.txt_email.place(x=250,y=182,width=350,height=35)

        password=Label(l_frame,text="PASSWORD",font=("times new roman",18,"bold"),bg="#99a5ab",fg="black").place(x=250,y=250)
        self.txt_password=Entry(l_frame,font=("times new roman",15),bg="lightgray")
        self.txt_password.place(x=250,y=282,width=350,height=35)

        btn_register=Button(l_frame,text="Register new Account?",command=self.register_window,font=("times new roman",14),fg="red",bg="#99a5ab",bd=0,cursor="hand2").place(x=250,y=330)

        self.btnimg=ImageTk.PhotoImage(file="img10.png")
        btn_login=Button(l_frame,image=self.btnimg,command=self.login,bd=0,cursor="hand2",bg="#99a5ab").place(x=250,y=370)
       # btn_login=Button(l_frame,text="SHOW RESULT",command=self.login,font=("times new roman",20),fg="white",bg="#5f003f",cursor="hand2").place(x=250,y=385,width=200,height=40)
    def register_window(self):
        self.root.destroy()
        import regis
        
    def login(self):
        if self.txt_email.get()=="" or self.txt_password.get()=="":
             messagebox.showerror("Error","All Fields Are Required",parent=self.root)
        else:
            try:
                con = sqlite3.connect('registration.db')
                cur = con.cursor()
                cur.execute("select * from registration1 where email=? and password=?",[self.txt_email.get(),self.txt_password.get()]) # if record found give none, if not found fetch the record(give one record)
                row=cur.fetchone()
                #print(row)
                if row==None:
                    messagebox.showerror("Error","Invalid USERNAME & PASSWORD!",parent=self.root)
                    
                else:
                    cur.execute("select M1,M2,M3,M4,f_name,l_name,email from registration1 where email=? and password=?",[self.txt_email.get(),self.txt_password.get()])
                    m1=int(row[5])
                    m2=int(row[6])
                    m3=int(row[7])
                    m4=int(row[8])
                    m5=(m1+m2+m3+m4)/4

                    a1=str(row[1])
                    a2=str(row[2])
                    a3=str(row[3])
                    a4 =a1+a2
                
                    #print("NAME:",a4,"\nE-MAIL:",a3)
                    messagebox.showinfo("Name", a4)
                        
                    
                    if m5>=90:
                        messagebox.showinfo("Success","You got grade O")
                    elif m5>=80:
                        messagebox.showinfo("Success","You got grade A+ ")
                    elif m5>=70:
                        messagebox.showinfo("Success","You got grade A ")
                    elif m5>=60:
                        messagebox.showinfo("Success","You got grade B ")
                    elif m5>=50:
                        messagebox.showinfo("Success","You got grade C ")
                    
                    #messagebox.showinfo("Success","WELCOME",parent=self.root)
                    
                con.close()
                    
            except Exception as es:
                                        
                   messagebox.showerror("Error",f"Error due to: {str(es)}",parent=self.root)
                                        
                                        
                   
                   
root=Tk()
obj=Login_window(root)
root.mainloop()
