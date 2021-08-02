from tkinter import*
from tkinter import ttk,messagebox
from PIL import Image,ImageTk
import sqlite3
class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Registration Window")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="white")

         #bgimage
        self.bg=ImageTk.PhotoImage(file="img.jpg")
        bg=Label(self.root,image=self.bg).place(x=0,y=0,relwidth=1,relheight=1)

         #leftimage
        self.left=ImageTk.PhotoImage(file="img9.jpg")
        left=Label(self.root,image=self.left).place(x=80,y=100,width=400,height=500)
         
         #Register frame
        frame1=Frame(self.root,bg="white")
        frame1.place(x=480,y=100,width=700,height=500)

        title=Label(frame1,text="REGISTER HERE",font=("times new roman",20,),bg="white",fg="green").place(x=50,y=30)

        
        f_name=Label(frame1,text="FIRST NAME",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=50,y=100)
        self.txt_fname=Entry(frame1,font=("times new roman",15),bg="lightgray")
        self.txt_fname.place(x=50,y=130,width=250)
        

        l_name=Label(frame1,text="LAST NAME",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=370,y=100)
        self.txt_lname=Entry(frame1,font=("times new roman",15),bg="lightgray")
        self.txt_lname.place(x=370,y=130,width=250)

        l_email=Label(frame1,text="E-MAIL",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=50,y=170)
        self.txt_email=Entry(frame1,font=("times new roman",15),bg="lightgray")
        self.txt_email.place(x=50,y=200,width=250)

        password=Label(frame1,text="PASSWORD",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=370,y=170)
        self.txt_password=Entry(frame1,font=("times new roman",15),bg="lightgray")
        self.txt_password.place(x=370,y=200,width=250)

       # contact=Label(frame1,text="CONTACT No:",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=50,y=170)
       # self.txt_contact=Entry(frame1,font=("times new roman",15),bg="lightgray")
       # self.txt_contact.place(x=50,y=200,width=250)

    
        M1=Label(frame1,text="MARKS OF SUBJECT 1",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=50,y=240)
        self.txt_M1=Entry(frame1,font=("times new roman",15),bg="lightgray")
        self.txt_M1.place(x=50,y=270,width=250)


        #question=Label(frame1,text="SECURITY QUESTION",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=50,y=240)

        #self.cmb_quest=ttk.Combobox(frame1,font=("times new roman",13),state='readonly',justify=CENTER)
        #self.cmb_quest['values']=("Select","Your Best Friend","Your Pet Name","Your Nickname")
        #self.cmb_quest.place(x=50,y=270,width=250)
        #self.cmb_quest.current(0)

        M2=Label(frame1,text="MARKS OF SUBJECT 2",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=370,y=240)
        self.txt_M2=Entry(frame1,font=("times new roman",15),bg="lightgray")
        self.txt_M2.place(x=370,y=270,width=250)

        M3=Label(frame1,text="MARKS OF SUBJECT 3",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=50,y=310)
        self.txt_M3=Entry(frame1,font=("times new roman",15),bg="lightgray")
        self.txt_M3.place(x=50,y=340,width=250)

        M4=Label(frame1,text="MARKS OF SUBJECT 4",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=370,y=310)
        self.txt_M4=Entry(frame1,font=("times new roman",15),bg="lightgray")
        self.txt_M4.place(x=370,y=340,width=250)

        #terms and condition
        self.var_chk=IntVar()
        chk=Checkbutton(frame1,text="I Agree The Terms & Conditions",variable=self.var_chk,onvalue=1,offvalue=0 ,bg="white" ,font =("times new roman",12)).place(x=50,y=380)
        
        self.btnimg=ImageTk.PhotoImage(file="img6.png")
        btnregister=Button(frame1,image=self.btnimg,bd=0,cursor="hand2",command=self.register_data).place(x=230,y=400)

        login=Label(self.root,text="Already a Member Click on Sign In !",font=("times new roman",14,),fg="red").place(x=135,y=550)
        
        btn_login=Button(self.root,text="Sign In",command=self.login_window,font=("times new roman",20),bd=1,bg="lightgray",cursor="hand2").place(x=206,y=450,width=150)
    def login_window(self):
        self.root.destroy()
        import sign_in

    def clear(self):
        self.txt_fname.delete(0,END)
        self.txt_lname.delete(0,END)
        self.txt_email.delete(0,END)
        self.txt_password.delete(0,END)
        self.txt_M1.delete(0,END)
        #self.cmb_quest.current(0)
        self.txt_M2.delete(0,END)
        self.txt_M3.delete(0,END)
        self.txt_M4.delete(0,END)

    def register_data(self):
        #print(self.var_fname.get(),self.txt_lname.get())
           if self.txt_fname.get()=="" or self.txt_lname.get()=="" or self.txt_email.get()=="" or self.txt_password.get()=="Select" or self.txt_M1.get()=="" or self.txt_M2.get()==""or self.txt_M3.get()=="" or self.txt_M4.get()=="":
              messagebox.showerror("Error","All Fields Are Required",parent=self.root)
          # elif self.txt_password.get()!= self.txt_cpassword.get():
              # messagebox.showerror("Error","Password and Confirm Password Should be same",parent=self.root)
           #elif self.var_chk.get()==0:
              # messagebox.showerror("Error","Please Agree our terms & Condition",parent=self.root)
           else:
               try:
                   con = sqlite3.connect('registration.db')
                   #con = sqlite3.connect(host="localhost",user="RISHI PAL",password="nock",database="registration")
                   cur = con.cursor()
                   cur.execute("select * from registration1 where email=?",[self.txt_email.get()]) # if record found give none, if not found fetch the record(give one record)
                   row=cur.fetchone()
                   #print(row)
                   if row!=None:
                       messagebox.showerror("Error","!User already Exist,Please try with another email",parent=self.root)
                   else:
                       cur.execute("insert into registration1(f_name,l_name,email,password,M1,M2,M3,M4)values(?,?,?,?,?,?,?,?)",
                               (self.txt_fname.get(),
                                self.txt_lname.get(),
                                self.txt_email.get(),
                                self.txt_password.get(),
                                self.txt_M1.get(),
                                self.txt_M2.get(),
                                self.txt_M3.get(),
                                self.txt_M4.get()
                                ))
                       con.commit()
                       con.close()
                                
                       messagebox.showinfo("Success","Register Successful",parent=self.root)
                       self.clear()
                   

               except Exception as es:
                   messagebox.showerror("Error",f"Error due to: {str(es)}",parent=self.root)
                   
               
           
    

root=Tk()
obj=Register(root)
root.mainloop()


