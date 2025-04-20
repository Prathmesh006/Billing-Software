from tkinter import*
import math
import random
from tkinter import messagebox
import os
import  sys
import win32print
import win32api
import PIL as p
import PIL.ImageTk as ptk
import subprocess

subprocess.call(['install_modules.bat'], shell=True)

import os
import sys

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        base_path = sys._MEIPASS  # temp folder used by PyInstaller
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

class Bill_App:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1920x1080+0+0")
        self.root.title("Krishna Juice Center")
        pic=(r"assets\\but1.png")
        pic1= p.Image.open(pic)
        photo=ptk.PhotoImage(pic1)
        bg_color="RoyalBlue2"
        title=Label(self.root,text="KRISHNA JUICE CENTER",bd=12,relief=FLAT,bg=bg_color,fg="white",font=("times new roman",30,"bold"),pady=2).pack(fill=X)
        #--------------------------------------variables declare-----------------------------------------------
        #=================================FIRST ENTRIES============================
        self.content_1=IntVar()
        self.content_2=IntVar()
        self.content_3=IntVar()
        self.content_4=IntVar()
        self.content_5=IntVar()
        self.content_6=IntVar()
        #=================================SECOND ENTRIES==============================
        self.content2_1=IntVar()
        self.content2_2=IntVar()
        self.content2_3=IntVar()
        self.content2_4=IntVar()
        self.content2_5=IntVar()
        self.content2_6=IntVar()
        #=================================THIRD ENTRIES================================
        self.content3_1=IntVar()
        self.content3_2=IntVar()
        self.content3_3=IntVar()
        self.content3_4=IntVar()
        self.content3_5=IntVar()
        self.content3_6=IntVar()
        #================================TOTAL PRICE AND TAX VARIABLES==================
        self.n1=StringVar()
        self.n2=StringVar()
        self.n3=StringVar()
        self.n4=StringVar()
        self.n5=StringVar()
        self.n6=StringVar()
        #================================CUSTOMER DETAILS VARIABLES==============================================
        self.cname=StringVar()
        self.cphone=StringVar()
        self.cbillno=StringVar()
        x= random.randint(1000,9999)
        self.cbillno.set(str(x))
        #=====================================================SEARCH BUTTON VARIABLE===================================
        self.searchbtn=StringVar()


 

        #-----------------------------------------------CUSTOMER DETAILS----------------------------------------------------------------------------
        F1=LabelFrame(self.root,bd=10,relief=FLAT,text="Customer Details",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        F1.place(x=0,y=75,relwidth=1)
        
        cname_lbl=Label(F1,text="Customer name",bg=bg_color,fg="white",font=("times new roman",18,"bold")).grid(row=0,column=0,padx=20,pady=5)
        cname_text=Entry(F1,width=20,textvariable=self.cname,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=1,pady=5,padx=10)

        cphone_lbl=Label(F1,text="Phone Number",bg=bg_color,fg="white",font=("times new roman",18,"bold")).grid(row=0,column=2,padx=20,pady=5)
        cphone_text=Entry(F1,width=20,textvariable=self.cphone,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=3,pady=5,padx=10)

        cbillno_lbl=Label(F1,text="Bill Number",bg=bg_color,fg="white",font=("times new roman",18,"bold")).grid(row=0,column=4,padx=20,pady=5)
        cbillno_text=Entry(F1,width=20,textvariable=self.searchbtn,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=5,pady=5,padx=10)



        # ------------------------------------------------SEARCH BUTTON--------------------------------------------
        btn = Button(F1,text="SEARCH",command=self.findbill,width=14,bd=5,font="aarial 12 bold").grid(row=0,column=6,padx=10,pady=10)




        #--------------------------------------FIRST ENTERIES---------------------------------------------------
        F2=LabelFrame(self.root,bd=10,relief=FLAT,text="Fruit juices ",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        F2.place(x=0,y=170,width=325,height=408)

        content_1=Label(F2,text="Apple juice",font=("times new roman",16,"bold"),bg=bg_color,fg="lightblue").grid(row=0,column=0,padx=10,pady=10,sticky="w")
        content_1_txt=Entry(F2,width=10,textvariable=self.content_1,font=("times new roman",16,"bold"),bd=5,relief=GROOVE).grid(row=0,column=1,padx=10,pady=10)

        content_2=Label(F2,text="Avocado juice",font=("times new roman",16,"bold"),bg=bg_color,fg="lightblue").grid(row=1,column=0,padx=10,pady=10,sticky="w")
        content_2_txt=Entry(F2,width=10,textvariable=self.content_2,font=("times new roman",16,"bold"),bd=5,relief=GROOVE).grid(row=1,column=1,padx=10,pady=10)

        content_3=Label(F2,text="Blackberry juice",font=("times new roman",16,"bold"),bg=bg_color,fg="lightblue").grid(row=2,column=0,padx=10,pady=10,sticky="w")
        content_3_txt=Entry(F2,width=10,textvariable=self.content_3,font=("times new roman",16,"bold"),bd=5,relief=GROOVE).grid(row=2,column=1,padx=10,pady=10)

        content_4=Label(F2,text="Dragonfruit juice",font=("times new roman",16,"bold"),bg=bg_color,fg="lightblue").grid(row=3,column=0,padx=10,pady=10,sticky="w")
        content_4_txt=Entry(F2,width=10,textvariable=self.content_4,font=("times new roman",16,"bold"),bd=5,relief=GROOVE).grid(row=3,column=1,padx=10,pady=10)

        content_5=Label(F2,text="Grape juice",font=("times new roman",16,"bold"),bg=bg_color,fg="lightblue").grid(row=4,column=0,padx=10,pady=10,sticky="w")
        content_5_txt=Entry(F2,width=10,textvariable=self.content_5,font=("times new roman",16,"bold"),bd=5,relief=GROOVE).grid(row=4,column=1,padx=10,pady=10)

        content_6=Label(F2,text="Watermelon juice",font=("times new roman",16,"bold"),bg=bg_color,fg="lightblue").grid(row=5,column=0,padx=10,pady=10,sticky="w")
        content_6_txt=Entry(F2,width=10,textvariable=self.content_6,font=("times new roman",16,"bold"),bd=5,relief=GROOVE).grid(row=5,column=1,padx=10,pady=10)

        #------------------------------------SECOND ENTERIES-----------------------------------------------------
        F3=LabelFrame(self.root,bd=10,relief=FLAT,text="Milkshakes",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        F3.place(x=326,y=170,width=325,height=408)

        content2_1=Label(F3,text="Chocolate MS",font=("times new roman",16,"bold"),bg=bg_color,fg="lightblue").grid(row=0,column=0,padx=10,pady=10,sticky="w")
        content2_1_txt=Entry(F3,width=10,textvariable=self.content2_1,font=("times new roman",16,"bold"),bd=5,relief=GROOVE).grid(row=0,column=1,padx=10,pady=10)

        content2_2=Label(F3,text="Vanilla MS",font=("times new roman",16,"bold"),bg=bg_color,fg="lightblue").grid(row=1,column=0,padx=10,pady=10,sticky="w")
        content2_2_txt=Entry(F3,width=10,textvariable=self.content2_2,font=("times new roman",16,"bold"),bd=5,relief=GROOVE).grid(row=1,column=1,padx=10,pady=10)

        content2_3=Label(F3,text="Strawberry MS",font=("times new roman",16,"bold"),bg=bg_color,fg="lightblue").grid(row=2,column=0,padx=10,pady=10,sticky="w")
        content2_3_txt=Entry(F3,width=10,textvariable=self.content2_3,font=("times new roman",16,"bold"),bd=5,relief=GROOVE).grid(row=2,column=1,padx=10,pady=10)

        content2_4=Label(F3,text="Butterscotch MS",font=("times new roman",16,"bold"),bg=bg_color,fg="lightblue").grid(row=3,column=0,padx=10,pady=10,sticky="w")
        content2_4_txt=Entry(F3,width=10,textvariable=self.content2_4,font=("times new roman",16,"bold"),bd=5,relief=GROOVE).grid(row=3,column=1,padx=10,pady=10)

        content2_5=Label(F3,text="Caramel MS",font=("times new roman",16,"bold"),bg=bg_color,fg="lightblue").grid(row=4,column=0,padx=10,pady=10,sticky="w")
        content2_5_txt=Entry(F3,width=10,textvariable=self.content2_5,font=("times new roman",16,"bold"),bd=5,relief=GROOVE).grid(row=4,column=1,padx=10,pady=10)

        content2_6=Label(F3,text="Blueberry MS",font=("times new roman",16,"bold"),bg=bg_color,fg="lightblue").grid(row=5,column=0,padx=10,pady=10,sticky="w")
        content2_6_txt=Entry(F3,width=10,textvariable=self.content2_6,font=("times new roman",16,"bold"),bd=5,relief=GROOVE).grid(row=5,column=1,padx=10,pady=10)


        #------------------------------------------------------third enteries---------------------------------------------
        F4=LabelFrame(self.root,bd=10,relief=FLAT,text="Soda Drinks",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        F4.place(x=652,y=170,width=325,height=408)

        content3_1=Label(F4,text="Coca-Cola",font=("times new roman",16,"bold"),bg=bg_color,fg="lightblue").grid(row=0,column=0,padx=10,pady=10,sticky="w")
        content3_1_txt=Entry(F4,width=10,textvariable=self.content3_1,font=("times new roman",16,"bold"),bd=5,relief=GROOVE).grid(row=0,column=1,padx=10,pady=10)

        content3_2=Label(F4,text="Sprite",font=("times new roman",16,"bold"),bg=bg_color,fg="lightblue").grid(row=1,column=0,padx=10,pady=10,sticky="w")
        content3_2_txt=Entry(F4,width=10,textvariable=self.content3_2,font=("times new roman",16,"bold"),bd=5,relief=GROOVE).grid(row=1,column=1,padx=10,pady=10)

        content3_3=Label(F4,text="Pepsi",font=("times new roman",16,"bold"),bg=bg_color,fg="lightblue").grid(row=2,column=0,padx=10,pady=10,sticky="w")
        content3_3_txt=Entry(F4,width=10,textvariable=self.content3_3,font=("times new roman",16,"bold"),bd=5,relief=GROOVE).grid(row=2,column=1,padx=10,pady=10)

        content3_4=Label(F4,text="7UP",font=("times new roman",16,"bold"),bg=bg_color,fg="lightblue").grid(row=3,column=0,padx=10,pady=10,sticky="w")
        content3_4_txt=Entry(F4,width=10,textvariable=self.content3_4,font=("times new roman",16,"bold"),bd=5,relief=GROOVE).grid(row=3,column=1,padx=10,pady=10)

        content3_5=Label(F4,text="Lemon Soda",font=("times new roman",16,"bold"),bg=bg_color,fg="lightblue").grid(row=4,column=0,padx=10,pady=10,sticky="w")
        content3_5_txt=Entry(F4,width=10,textvariable=self.content3_5,font=("times new roman",16,"bold"),bd=5,relief=GROOVE).grid(row=4,column=1,padx=10,pady=10)

        content3_6=Label(F4,text="Orange soda",font=("times new roman",16,"bold"),bg=bg_color,fg="lightblue").grid(row=5,column=0,padx=10,pady=10,sticky="w")
        content3_6_txt=Entry(F4,width=10,textvariable=self.content3_6,font=("times new roman",16,"bold"),bd=5,relief=GROOVE).grid(row=5,column=1,padx=10,pady=10)



        #---------------------------bill area-----------------------------------------------
        F5=Frame(self.root,bg="white",bd=10,relief=GROOVE)
        F5.place(x=980,y=170,width=400,height=408)
        bill_title=Label(F5,text="Bill Invoice",font="arial 15 bold",bg="gray",bd=7,relief=FLAT).pack(fill=X)
        scrollbar_1=Scrollbar(F5,orient=VERTICAL)
        self.textarea=Text(F5,yscrollcommand=scrollbar_1.set)
        scrollbar_1.pack(side=RIGHT,fill=Y)
        scrollbar_1.config(command=self.textarea.yview)
        self.textarea.pack(fill=BOTH,expand=1)



        #-----------------------------------------------logo design--------------------------------------------------------------
        F7=Label(self.root,bd=1,relief=SUNKEN,bg="gray",image=photo)
        F7.place(x=1380,y=170,width=145,height=408)







        #----------------------------------------------------------frame for total price in BILL MENU----------------------------------------------------
        F6=LabelFrame(self.root,bd=2,relief=GROOVE,text="BILL DETAILS",font=("times new roman",20,"bold"),fg="gold",bg=bg_color)
        F6.place(x=0,y=580,relwidth=1,height=180)
        n1_lbl=Label(F6,bg=bg_color,text="Total Fruit Juices price",font=("times new roman",15,"bold")).grid(row=0,column=0,padx=20,pady=8,sticky="w")
        n1_txt=Entry(F6,width=18,textvariable=self.n1,font="arial 10 bold",bd=3,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=1)

        n2_lbl=Label(F6,bg=bg_color,text="Total Milkshakes price",font=("times new roman",15,"bold")).grid(row=2,column=0,padx=20,pady=8,sticky="w")
        n2_txt=Entry(F6,width=18,textvariable=self.n2,font="arial 10 bold",bd=3,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=1)

        n3_lbl=Label(F6,bg=bg_color,text="Total Soda drinks price",font=("times new roman",15,"bold")).grid(row=4,column=0,padx=20,pady=8,sticky="w")
        n3_txt=Entry(F6,width=18,textvariable=self.n3,font="arial 10 bold",bd=3,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=1)


        #--------------------------------------------------------PRODUCT TAX SYSTEM----------------------------------------------------------------
        n4_lbl=Label(F6,bg=bg_color,text="Fruit Juices TAX",font=("times new roman",15,"bold")).grid(row=0,column=3,padx=20,pady=8,sticky="w")
        n4_txt=Entry(F6,width=18,textvariable=self.n4,font="arial 10 bold",bd=3,relief=SUNKEN).grid(row=0,column=4,padx=10,pady=1)

        n5_lbl=Label(F6,bg=bg_color,text="Milkshakes TAX",font=("times new roman",15,"bold")).grid(row=2,column=3,padx=20,pady=8,sticky="w")
        n5_txt=Entry(F6,width=18,textvariable=self.n5,font="arial 10 bold",bd=3,relief=SUNKEN).grid(row=2,column=4,padx=10,pady=1)

        n6_lbl=Label(F6,bg=bg_color,text="Soda drinks TAX",font=("times new roman",15,"bold")).grid(row=4,column=3,padx=20,pady=8,sticky="w")
        n6_txt=Entry(F6,width=18,textvariable=self.n6,font="arial 10 bold",bd=3,relief=SUNKEN).grid(row=4,column=4,padx=10,pady=1)



        #-------------------------------------------------------total , bill generate, clear, print BUTTONS------------------------------------------------
        BTN_FRAME=Frame(F6,bg=bg_color,bd=7,relief=GROOVE)
        BTN_FRAME.place(x=775,width=745,height=135)

        tot_btn=Button(BTN_FRAME,command=self.total,text="TOTAL",bg="cadetblue",fg="white",bd=2,pady=15,width=11,font="arial 15 bold").grid(row=0,column=0,padx=15,pady=25)
        bill_btn=Button(BTN_FRAME,text="GENERATE BILL",command=self.bill_area,bg="cadetblue",fg="white",bd=2,pady=15,width=15,font="arial 15 bold").grid(row=0,column=1,padx=15,pady=25)
        clr_btn=Button(BTN_FRAME,text="CLEAR",command=self.clear_data,bg="cadetblue",fg="white",bd=2,pady=15,width=11,font="arial 15 bold").grid(row=0,column=2,padx=15,pady=25)
        print_btn=Button(BTN_FRAME,text="PRINT",command=self.print_bill,bg="cadetblue",fg="white",bd=2,pady=15,width=11,font="arial 15 bold").grid(row=0,column=3,padx=15,pady=25)



        #---------------------------------------------------------EXIT BUTTON-------------------------------------------------------------------------
        F8=LabelFrame(self.root,bd=2,relief=GROOVE,bg=bg_color)
        F8.place(x=0,y=760,relwidth=1,height=32)

        exit_btn=Button(F8,text="EXIT",command=self.exit_soft,bg="gray",fg="black",bd=2,pady=10,width=169,height=1,font="arial 11 bold").grid(row=0,column=0,padx=0,pady=0)
        self.welcome_bill()


    #=====================================================================TOTAL ADDING CONTENT 1=====================================
    def total(self):
        self.c_1_p=(self.content_1.get()*40)
        self.c_2_p=(self.content_2.get()*50)
        self.c_3_p=(self.content_3.get()*50)
        self.c_4_p=(self.content_4.get()*60)
        self.c_5_p=(self.content_5.get()*40)
        self.c_6_p=(self.content_6.get()*30)
        self.total_content_1_price=float(self.c_1_p+self.c_2_p+self.c_3_p+self.c_4_p+self.c_5_p+self.c_6_p)
        self.n1.set("Rs. "+str(self.total_content_1_price))
        self.c1_tax=round((self.total_content_1_price*0.05),2)
        self.n4.set("Rs. "+str(self.c1_tax))
    #====================================================================TOTAL ADDING CONTENT 2=======================================
        self.c2_1_p=(self.content2_1.get()*100)
        self.c2_2_p=(self.content2_2.get()*100)
        self.c2_3_p=(self.content2_3.get()*100)
        self.c2_4_p=(self.content2_4.get()*100)
        self.c2_5_p=(self.content2_5.get()*100)
        self.c2_6_p=(self.content2_6.get()*100)
        self.total_content_2_price=float(self.c2_1_p+self.c2_2_p+self.c2_3_p+self.c2_4_p+self.c2_5_p+self.c2_6_p)
        self.n2.set("Rs. "+str(self.total_content_2_price))
        self.c2_tax=round((self.total_content_2_price*0.1),2)
        self.n5.set("Rs. "+str(self.c2_tax))
    #====================================================================TOTAL ADDING CONTENT 3======================================
        self.c3_1_p=(self.content3_1.get()*20)
        self.c3_2_p=(self.content3_2.get()*20)
        self.c3_3_p=(self.content3_3.get()*20)
        self.c3_4_p=(self.content3_4.get()*20)
        self.c3_5_p=(self.content3_5.get()*20)
        self.c3_6_p=(self.content3_6.get()*20)
        self.total_content_3_price=float(self.c3_1_p+self.c3_2_p+self.c3_3_p+self.c3_4_p+self.c3_5_p+self.c3_6_p)
        self.n3.set("Rs. "+str(self.total_content_3_price))
        self.c3_tax=round((self.total_content_3_price*0.05),2)
        self.n6.set("Rs. "+str(self.c3_tax))


        self.Total_bill=float(self.total_content_1_price+self.total_content_2_price+self.total_content_3_price+self.c1_tax+self.c2_tax+self.c3_tax)






    #===================================================================BILL AREA LOGIC==============================================
    def welcome_bill(self):
        self.textarea.delete('1.0',END)
        self.textarea.insert(END,"\t     Welcome Krishna Juice Center\n")
        self.textarea.insert(END,f"\nBill No: {self.cbillno.get()}")
        self.textarea.insert(END,f"\nCustomer Name: {self.cname.get()}")
        self.textarea.insert(END,f"\nPhone No: {self.cphone.get()}")
        self.textarea.insert(END,f"\n\n============================================")
        self.textarea.insert(END,f"\n  Products\t\t    QTY\t\t  Price")
        self.textarea.insert(END,f"\n============================================")

    def bill_area(self):
        if self.cname.get()=="" or self.cphone.get()=="":
            messagebox.showerror("ERROR!","PLEASE ENTER CUSTOMER DETAILS..")
        elif self.n1.get()=="Rs. 0.0" and self.n2.get()=="Rs. 0.0" and self.n3.get()=="Rs. 0.0":
            messagebox.showerror("ERROR!","NO PRODUCTS SELECTED..")
        else:
            self.welcome_bill()
            if self.content_1.get()!=0:
                self.textarea.insert(END,f"\n Apple juice\t\t    {self.content_1.get()}\t\tRs. {self.c_1_p}")
            if self.content_2.get()!=0:
                self.textarea.insert(END,f"\n Avocado juice\t\t    {self.content_2.get()}\t\tRs. {self.c_2_p}")
            if self.content_3.get()!=0:
                self.textarea.insert(END,f"\n Blackberry juice\t\t    {self.content_3.get()}\t\tRs. {self.c_3_p}")
            if self.content_4.get()!=0:
                self.textarea.insert(END,f"\n Dragonfruit juice\t\t    {self.content_4.get()}\t\tRs. {self.c_4_p}")
            if self.content_5.get()!=0:
                self.textarea.insert(END,f"\n Grape juice\t\t    {self.content_5.get()}\t\tRs. {self.c_5_p}")
            if self.content_6.get()!=0:
                self.textarea.insert(END,f"\n Watermelon juice\t\t    {self.content_6.get()}\t\tRs. {self.c_6_p}")


            if self.content2_1.get()!=0:
                self.textarea.insert(END,f"\n Chocolate MS\t\t    {self.content2_1.get()}\t\tRs. {self.c2_1_p}")
            if self.content2_2.get()!=0:
                self.textarea.insert(END,f"\n Vanilla MS\t\t    {self.content2_2.get()}\t\tRs. {self.c2_2_p}")
            if self.content2_3.get()!=0:
                self.textarea.insert(END,f"\n Strawberry MS\t\t    {self.content2_3.get()}\t\tRs. {self.c2_3_p}")
            if self.content2_4.get()!=0:
                self.textarea.insert(END,f"\n Butterscotch MS\t\t    {self.content2_4.get()}\t\tRs. {self.c2_4_p}")
            if self.content2_5.get()!=0:
                self.textarea.insert(END,f"\n Caramel MS\t\t    {self.content2_5.get()}\t\tRs. {self.c2_5_p}")
            if self.content2_6.get()!=0:
                self.textarea.insert(END,f"\n Blueberry MS\t\t    {self.content2_6.get()}\t\tRs. {self.c2_6_p}")


            if self.content3_1.get()!=0:
                self.textarea.insert(END,f"\n Coca-Cola\t\t    {self.content3_1.get()}\t\tRs. {self.c3_1_p}")
            if self.content3_2.get()!=0:
                self.textarea.insert(END,f"\n Sprite\t\t    {self.content3_2.get()}\t\tRs. {self.c3_2_p}")
            if self.content3_3.get()!=0:
                self.textarea.insert(END,f"\n Pepsi\t\t    {self.content3_3.get()}\t\tRs. {self.c3_3_p}")
            if self.content3_4.get()!=0:
                self.textarea.insert(END,f"\n 7UP\t\t    {self.content3_4.get()}\t\tRs. {self.c3_4_p}")
            if self.content3_5.get()!=0:
                self.textarea.insert(END,f"\n Lemon Soda\t\t    {self.content3_5.get()}\t\tRs. {self.c3_5_p}")
            if self.content3_6.get()!=0:
                self.textarea.insert(END,f"\n Orange soda\t\t    {self.content3_6.get()}\t\tRs. {self.c3_6_p}")
        
            self.textarea.insert(END,f"\n\n------------------------------------------")
            if self.n4.get()!="Rs. 0.0":
                self.textarea.insert(END,f"\n  Fruit juices TAX\t\t\t\t{self.n4.get()}")
            if self.n5.get()!="Rs. 0.0":
                self.textarea.insert(END,f"\n  Milkshakes TAX\t\t\t\t{self.n5.get()}")
            if self.n6.get()!="Rs. 0.0":
                self.textarea.insert(END,f"\n  Soda Drinks TAX\t\t\t\t{self.n6.get()}")
            self.textarea.insert(END,f"\n--------------------------------------------")
            self.textarea.insert(END,f"\n  TOTAL BILL\t\t\t\tRs. {str(self.Total_bill)}")
            self.textarea.insert(END,f"\n--------------------------------------------")
            self.save_bill()


    #-----------------------------------------------TO SAVE BILL IN FILE------------------------------------------------------------------
    def save_bill(self):
        op=messagebox.askyesno("Save Bill","Do you want to save bill?")
        if op>0:
            self.bill_data=self.textarea.get('1.0',END)
            f1=open("Bills\\"+str(self.cbillno.get())+".txt","w")
            f1.write(self.bill_data)
            f1.close()
            messagebox.showinfo("SAVED",f"Bill {self.cbillno.get()} saved succcessfully")
        else:
            return

    #-----------------------------------------------TO SEARCH BILL------------------------------------------------------------------------
    def findbill(self):
        present="no"
        for i in os.listdir("Bills"):
            if i.split('.')[0]==self.searchbtn.get():
                f1=open(f"Bills\\{i}","r")
                self.textarea.delete('1.0',END)
                for d in f1:
                    self.textarea.insert(END,d)
                f1.close()
                present="yes"
        if present=="no":
            messagebox.showerror("ERROR","Invalid bill number")

    #-----------------------------------------------TO CLEAR DATA------------------------------------------------------------------
    def clear_data(self):
        op=messagebox.askyesno("CLEAR","Do you really want to clear the Data")
        if op>0:
            #=================================FIRST ENTRIES============================
            self.content_1.set(0)
            self.content_2.set(0)
            self.content_3.set(0)
            self.content_4.set(0)
            self.content_5.set(0)
            self.content_6.set(0)
            #=================================SECOND ENTRIES==============================
            self.content2_1.set(0)
            self.content2_2.set(0)
            self.content2_3.set(0)
            self.content2_4.set(0)
            self.content2_5.set(0)
            self.content2_6.set(0)
            #=================================THIRD ENTRIES================================
            self.content3_1.set(0)
            self.content3_2.set(0)
            self.content3_3.set(0)
            self.content3_4.set(0)
            self.content3_5.set(0)
            self.content3_6.set(0)
            #================================TOTAL PRICE AND TAX VARIABLES==================
            self.n1.set("")
            self.n2.set("")
            self.n3.set("")
            self.n4.set("")
            self.n5.set("")
            self.n6.set("")
            #================================CUSTOMER DETAILS VARIABLES==============================================
            self.cname.set("")
            self.cphone.set("")
            self.cbillno.set("")
            x= random.randint(1000,9999)
            self.cbillno.set(str(x))
            #=====================================================SEARCH BUTTON VARIABLE===================================
            self.searchbtn.set("")
            self.welcome_bill()
        else:
            return


    #------------------------------------------------------EXIT THE SOFTWARE---------------------------------------------
    def exit_soft(self):
        op=messagebox.askyesno("EXIT","Do you really want to exit?")
        if op>0:
            self.root.destroy()
        else:
            return

    #-----------------------------------------------------PRINTING THE BILL-----------------------------------------------
    def print_bill(self):
        # Save bill content to a temporary file
        bill_content = self.textarea.get('1.0', END)
        file_path = f"Bills\\temp_bill_{self.cbillno.get()}.txt"
        with open(file_path, "w") as temp_file:
            temp_file.write(bill_content)

        # Get default printer and send the file to print
        try:
            win32api.ShellExecute(
                0,
                "print",
                file_path,
                None,
                ".",
                0
            )
        except Exception as e:
            messagebox.showerror("Printing Error", f"Could not print the bill:\n{e}")



    




root = Tk()
obj = Bill_App(root)
root.mainloop()                                                     