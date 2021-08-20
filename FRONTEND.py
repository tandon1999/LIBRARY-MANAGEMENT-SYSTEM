from tkinter import *
from tkinter import messagebox
from PIL import Image,ImageTk
import backend2
def exitt():
    exit()

def bookstore():
    def customers():
        import backend3
        def get_selected_row1(event):
            global selected_tuple
            index=list2.curselection()[0]
            selected_tuple=list2.get(index)
            e1.delete(0,END)
            e1.insert(END,selected_tuple[1])
            e2.delete(0,END)
            e2.insert(END,selected_tuple[2])
            e3.delete(0,END)
            e3.insert(END,selected_tuple[3])
            e4.delete(0,END)
            e4.insert(END,selected_tuple[4])
            e5.delete(0,END)
            e5.insert(END,selected_tuple[5])
            e6.delete(0,END)
            e6.insert(END,selected_tuple[6])
            e7.delete(0,END)
            e7.insert(END,selected_tuple[7])
            e8.delete(0,END)
            e8.insert(END,selected_tuple[8])
        
        
        def view_command1():
            list2.delete(0,END)
            for row in backend3.view():
                list2.insert(END,row)
        
        def search_command1():
            list2.delete(0,END)
            for row in backend3.search(cus_id_text.get(),cus_name_text.get(),address_text.get(),city_text.get(),state_text.get(),phone_no_text.get(),a_paid_text.get(),no_books_text.get()):
                list2.insert(1,row)
        def add_command1():
            cus_id_int=int(cus_id_text.get())
            phone_no_int=int(phone_no_text.get())
            a_paid_int=int(a_paid_text.get())
            no_books_int=int(no_books_text.get())
            backend3.insert(cus_id_int,cus_name_text.get(),address_text.get(),city_text.get(),state_text.get(),phone_no_int,a_paid_int,no_books_int)
            list2.delete(0,END)
            list2.insert(END,(cus_id_int,cus_name_text.get(),address_text.get(),city_text.get(),state_text.get(),phone_no_int,a_paid_int,no_books_int))
        def delete_command1():
            backend3.delete(selected_tuple[0])
        def update_command1():
            cus_id_int=int(cus_id_text.get())
            phone_no_int=int(phone_no_text.get())
            a_paid_int=int(a_paid_text.get())
            no_books_int=int(no_books_text.get())
            backend3.update(selected_tuple[0],cus_id_int,cus_name_text.get(),address_text.get(),city_text.get(),state_text.get(),phone_no_int,a_paid_int,no_books_int)
        def total_command1():
            value=backend3.total()
            list2.delete(0,END) 
            list2.insert(1,value)
        def thanks():
            root.destroy()
            thanks=Tk()
            thanks.geometry('750x750')
            thanks.wm_title("Thanks for using .",)
            thanks.configure(background = 'AntiqueWhite1')
            imag2=Image.open("thank.jpeg")
            imag2=imag2.resize((750,750),Image.ANTIALIAS)
            photos=ImageTk.PhotoImage(imag2)
            lab2=Label(image=photos)
            lab2.place(x=0,y=0,relwidth=1,relheight=1)
            thanks.mainloop()
        window.destroy()
        root=Tk()
        root.geometry('750x750')
        root.wm_title("Customer Information",)
        root.configure(background = 'AntiqueWhite1')
        imag1=Image.open("customers.jpg")
        imag1=imag1.resize((750,750),Image.ANTIALIAS)
        photos=ImageTk.PhotoImage(imag1)
        lab1=Label(image=photos)
        lab1.place(x=0,y=0,relwidth=1,relheight=1)
        
        l1=Label(root,text="Customer ID",relief='sunken',font=("Times New Roman",12))
        l1.place(x=80,y=90)
        cus_id_text=StringVar()
        e1=Entry(root,textvariable=cus_id_text)
        e1.place(x=170,y=93)
        l2=Label(root,text="Cus_Name",relief='sunken',font=("Times New Roman",12))
        l2.place(x=80,y=120)
        cus_name_text=StringVar()
        e2=Entry(root,textvariable=cus_name_text)
        e2.place(x=170,y=123)
        l3=Label(root,text="Address",relief='sunken',font=("Times New Roman",12))
        l3.place(x=80,y=150)
        address_text=StringVar()
        e3=Entry(root,textvariable=address_text)
        e3.place(x=170,y=153)
        l4=Label(root,text="City",relief='sunken',font=("Times New Roman",12))
        l4.place(x=80,y=180)
        city_text=StringVar()
        e4=Entry(root,textvariable=city_text)
        e4.place(x=170,y=183)
        l5=Label(root,text="State",relief='sunken',font=("Times New Roman",12))
        l5.place(x=80,y=210)
        state_text=StringVar()
        e5=Entry(root,textvariable=state_text)
        e5.place(x=170,y=213)
        l6=Label(root,text="Phone_no",relief='sunken',font=("Times New Roman",12))
        l6.place(x=80,y=240)
        phone_no_text=StringVar()
        e6=Entry(root,textvariable=phone_no_text)
        e6.place(x=170,y=243)
        l7=Label(root,text="Amount Paid",relief='sunken',font=("Times New Roman",12))
        l7.place(x=80,y=270)
        a_paid_text=StringVar()
        e7=Entry(root,textvariable=a_paid_text)
        e7.place(x=170,y=273)
        l8=Label(root,text="Total books",relief='sunken',font=("Times New Roman",12))
        l8.place(x=80,y=300)
        no_books_text=StringVar()
        e8=Entry(root,textvariable=no_books_text)
        e8.place(x=170,y=303)
        list2=Listbox(root,background="light yellow", height=20,width=50)
        list2.place(x=400,y=380)

        sb1=Scrollbar(root)
        sb1.place(x=704,y=500)

        list2.configure(yscrollcommand=sb1.set)
        sb1.configure(command=list2.yview)

        list2.bind('<<ListboxSelect>>',get_selected_row1)
        b1=Button(root,text="View all", width=12,command=view_command1)
        b1.place(x=500,y=90)

        b2=Button(root,text="Search entry", width=12,command=search_command1)
        b2.place(x=500,y=120)

        b3=Button(root,text="Add entry", width=12,command=add_command1)
        b3.place(x=500,y=150)

        b4=Button(root,text="Update selected", width=12,command=update_command1)
        b4.place(x=500,y=180)

        b5=Button(root,text="Delete selected", width=12,command=delete_command1)
        b5.place(x=500,y=210)
        b7=Button(root,text="Total Books",width=12,command=total_command1)
        b7.place(x=500,y=240)
        b8=Button(root,text="Exit Bookstore",width=12,font=("Times New Roman",12),command=thanks)
        b8.place(x=500,y=280)
        root.mainloop()
    def bookseller():
        import backend4
        def get_selected_row3(event):
            global selected_tuple
            index=list3.curselection()[0]
            selected_tuple=list3.get(index)
            e1.delete(0,END)
            e1.insert(END,selected_tuple[1])
            e2.delete(0,END)
            e2.insert(END,selected_tuple[2])
            e3.delete(0,END)
            e3.insert(END,selected_tuple[3])
            e4.delete(0,END)
            e4.insert(END,selected_tuple[4])
            e5.delete(0,END)
            e5.insert(END,selected_tuple[5])
            e6.delete(0,END)
            e6.insert(END,selected_tuple[6])
            e7.delete(0,END)
            e7.insert(END,selected_tuple[7])
         
        
        def view_command3():
            list3.delete(0,END)
            for row in backend4.view():
                list3.insert(END,row)
        
        def search_command3():
            list3.delete(0,END)
          
            for row in backend4.search(booksell_id_text.get(),first_name_text.get(),middle_name_text.get(),last_name_text.get(),location_text.get(),phone_no_text.get(),revenue_text.get()):
                list3.insert(1,row)
        def add_command3():
            booksell_id_int=int(booksell_id_text.get())
            phone_no_int=int(phone_no_text.get())
            revenue_int=int(revenue_text.get())
            backend4.insert(booksell_id_int,first_name_text.get(),middle_name_text.get(),last_name_text.get(),location_text.get(),phone_no_int,revenue_int)
            list3.delete(0,END)
            list3.insert(END,(booksell_id_int,first_name_text.get(),middle_name_text.get(),last_name_text.get(),location_text.get(),phone_no_int,revenue_int))
        def delete_command3():
            backend4.delete(selected_tuple[0])
        def update_command3():
            booksell_id_int=int(booksell_id_text.get())
            phone_no_int=int(phone_no_text.get())
            revenue_int=int(revenue_text.get())
            backend4.update(selected_tuple[0],booksell_id_int,first_name_text.get(),middle_name_text.get(),last_name_text.get(),location_text.get(),phone_no_int,revenue_int)
        def total_command3():
            value=backend4.total()
            list3.delete(0,END) 
            list3.insert(1,value)
        def thanks():
            root3.destroy()
            thanks=Tk()
            thanks.geometry('750x750')
            thanks.wm_title("Thanks for using .",)
            thanks.configure(background = 'AntiqueWhite1')
            imag2=Image.open("thank.jpeg")
            imag2=imag2.resize((750,750),Image.ANTIALIAS)
            photos=ImageTk.PhotoImage(imag2)
            lab2=Label(image=photos)
            lab2.place(x=0,y=0,relwidth=1,relheight=1)
            thanks.mainloop()
        window.destroy()
        root3=Tk()
        root3.geometry('750x750')
        root3.wm_title("Bookseller Information",)
        root3.configure(background = 'AntiqueWhite1')
        imag3=Image.open("bookseller.png")
        imag3=imag3.resize((750,750),Image.ANTIALIAS)
        photos=ImageTk.PhotoImage(imag3)
        lab1=Label(image=photos)
        lab1.place(x=0,y=0,relwidth=1,relheight=1)
        
        l1=Label(root3,text="Bookseller ID",relief='sunken',font=("Times New Roman",12))
        l1.place(x=80,y=90)
        booksell_id_text=StringVar()
        e1=Entry(root3,textvariable=booksell_id_text)
        e1.place(x=175,y=93)
        l2=Label(root3,text="First_Name",relief='sunken',font=("Times New Roman",12))
        l2.place(x=80,y=120)
        first_name_text=StringVar()
        e2=Entry(root3,textvariable=first_name_text)
        e2.place(x=170,y=123)

        l3=Label(root3,text="Middle_Name",relief='sunken',font=("Times New Roman",12))
        l3.place(x=80,y=150)
        middle_name_text=StringVar()
        e3=Entry(root3,textvariable=middle_name_text)
        e3.place(x=180,y=153)
        
        l4=Label(root3,text="Last_Name",relief='sunken',font=("Times New Roman",12))
        l4.place(x=80,y=180)
        last_name_text=StringVar()
        e4=Entry(root3,textvariable=last_name_text)
        e4.place(x=170,y=183)

        
        l5=Label(root3,text="Location",relief='sunken',font=("Times New Roman",12))
        l5.place(x=80,y=210)
        location_text=StringVar()
        e5=Entry(root3,textvariable=location_text)
        e5.place(x=170,y=213)
        l6=Label(root3,text="Phone_no",relief='sunken',font=("Times New Roman",12))
        l6.place(x=80,y=240)
        phone_no_text=StringVar()
        e6=Entry(root3,textvariable=phone_no_text)
        e6.place(x=170,y=243)
        l7=Label(root3,text="Revenue",relief='sunken',font=("Times New Roman",12))
        l7.place(x=80,y=270)
        revenue_text=StringVar()
        e7=Entry(root3,textvariable=revenue_text)
        e7.place(x=170,y=273)
        list3=Listbox(root3,background='light yellow', height=20,width=50)
        list3.place(x=400,y=380)

        sb1=Scrollbar(root3)
        sb1.place(x=704,y=500)

        list3.configure(yscrollcommand=sb1.set)
        sb1.configure(command=list3.yview)

        list3.bind('<<ListboxSelect>>',get_selected_row3)
        b1=Button(root3,text="View all", width=12,command=view_command3)
        b1.place(x=500,y=90)

        b2=Button(root3,text="Search entry", width=12,command=search_command3)
        b2.place(x=500,y=120)

        b3=Button(root3,text="Add entry", width=12,command=add_command3)
        b3.place(x=500,y=150)

        b4=Button(root3,text="Update selected", width=12,command=update_command3)
        b4.place(x=500,y=180)

        b5=Button(root3,text="Delete selected", width=12,command=delete_command3)
        b5.place(x=500,y=210)
        b7=Button(root3,text="Total no.of Booksellers",width=20,command=total_command3)
        b7.place(x=500,y=240)
        b8=Button(root3,text="Exit Bookstore",width=12,font=("Times New Roman",12),command=thanks)
        b8.place(x=500,y=280)
        root3.mainloop()
    
    def get_selected_row(event):
        global selected_tuple
        index=list1.curselection()[0]
        selected_tuple=list1.get(index)
        e1.delete(0,END)
        e1.insert(END,selected_tuple[1])
        e2.delete(0,END)
        e2.insert(END,selected_tuple[2])
        e3.delete(0,END)
        e3.insert(END,selected_tuple[3])
        e4.delete(0,END)
        e4.insert(END,selected_tuple[4])

    def view_command():
        list1.delete(0,END)
        for row in backend2.view():
            list1.insert(END,row)
    
    def search_command():
        list1.delete(0,END)
        #quantity_int=int(quantity_text.get())
        #price_int=int(price_text.get())
        for row in backend2.search(title_text.get(),author_text.get(),quantity_text.get(),price_text.get()):
            list1.insert(1,row)

    def add_command():
        quantity_int=int(quantity_text.get())
        price_int=int(price_text.get())
        backend2.insert(title_text.get(),author_text.get(),quantity_int,price_int)
        list1.delete(0,END)
        list1.insert(END,(title_text.get(),author_text.get(),quantity_int,price_int))

    def delete_command():
        backend2.delete(selected_tuple[0])

    def update_command():
        quantity_int=int(quantity_text.get())
        price_int=int(price_text.get())
        backend2.update(selected_tuple[0],title_text.get(),author_text.get(),quantity_int,price_int)

    def buy_command():
        temp1=quantity_text.get()
        val1=int(temp1)
        price_int=int(price_text.get())
        if val1 == 0:
            backend2.delete(selected_tuple[0])
            messagebox.showerror("ERROR!!!","Out of stock!!!")
        else:
            new_quantity=val1-1
            backend2.update(selected_tuple[0],title_text.get(),author_text.get(),new_quantity,price_int)

    def total_command():
        value=backend2.total()
        list1.delete(0,END) 
        list1.insert(1,value)

    def max_command():
        value=backend2.maxval()
        list1.delete(0,END) 
        list1.insert(1,value)
        
    def min_command():
        value=backend2.minval()
        list1.delete(0,END) 
        list1.insert(1,value)
    def thanks2():
        window.destroy()
        thanks2=Tk()
        thanks2.geometry('750x750')
        thanks2.wm_title("Thanks for using .",)
        thanks2.configure(background = 'AntiqueWhite1')
        imag2=Image.open("thank.jpg")
        imag2=imag2.resize((750,750),Image.ANTIALIAS)
        photos=ImageTk.PhotoImage(imag2)
        lab2=Label(image=photos)
        lab2.place(x=0,y=0,relwidth=1,relheight=1)
        thanks2.mainloop()
    def head():
        def thanks1():
            head.destroy()
            thanks=Tk()
            thanks.geometry('750x750')
            thanks.wm_title("Thanks for using .",)
            thanks.configure(background = 'AntiqueWhite1')
            imag2=Image.open("thank.jpg")
            imag2=imag2.resize((750,750),Image.ANTIALIAS)
            photos=ImageTk.PhotoImage(imag2)
            lab2=Label(image=photos)
            lab2.place(x=0,y=0,relwidth=1,relheight=1)
            thanks.mainloop()
            
        window.destroy()
        head=Tk()
        head.geometry('700x650')
        head.wm_title("Bookstore Head Information.",)
        head.configure(background = 'AntiqueWhite1')
        imag3=Image.open("head.jpeg")
        imag3=imag3.resize((700,650),Image.ANTIALIAS)
        photos=ImageTk.PhotoImage(imag3)
        lab2=Label(image=photos)
        lab2.place(x=0,y=0,relwidth=1,relheight=1)
        b8=Button(head,text="Exit Bookstore",width=12,font=("Times New Roman",12),command=thanks1)
        b8.place(x=550,y=480)
        head.mainloop()
    def workers():
         def thanks2():
            worker.destroy()
            thanks2=Tk()
            thanks2.geometry('750x750')
            thanks2.wm_title("Thanks for using .",)
            thanks2.configure(background = 'AntiqueWhite1')
            imag2=Image.open("thank.jpg")
            imag2=imag2.resize((750,750),Image.ANTIALIAS)
            photos=ImageTk.PhotoImage(imag2)
            lab2=Label(image=photos)
            lab2.place(x=0,y=0,relwidth=1,relheight=1)
            thanks2.mainloop()
         window.destroy()
         worker=Tk()
         worker.geometry('800x600')
         worker.wm_title("Workers Information",)
         worker.configure(background = 'AntiqueWhite1')
         imag4=Image.open("workers.jpeg")
         imag4=imag4.resize((800,600),Image.ANTIALIAS)
         photos=ImageTk.PhotoImage(imag4)
         lab4=Label(image=photos)
         lab4.place(x=0,y=0,relwidth=1,relheight=1)
         b8=Button(worker,text="Exit Bookstore",width=12,font=("Times New Roman",12),command=thanks2)
         b8.place(x=600,y=520)
         worker.mainloop()
    
        
    root1.destroy()
    window=Tk()
    window.geometry('750x750')
    window.wm_title("BookStore",)
    imag=Image.open("bookstore.jpg")
    imag=imag.resize((750,750),Image.ANTIALIAS)
    photo=ImageTk.PhotoImage(imag)
    lab=Label(image=photo)

    l1=Label(window,text="Title",relief='groove',font=("Times New Roman",14))
    l1.grid(row=1,column=4,sticky=E)

    l2=Label(window,text="Author",relief='groove',font=("Times New Roman",14))
    l2.grid(row=1,column=6)

    l3=Label(window,text="Quantity",relief='groove',font=("Times New Roman",14))
    l3.grid(row=2,column=4)

    l4=Label(window,text="Price",relief='groove',font=("Times New Roman",14))
    l4.grid(row=2,column=6)

    title_text=StringVar()
    e1=Entry(window,textvariable=title_text)
    e1.grid(row=1,column=5,sticky=W)

    author_text=StringVar()
    e2=Entry(window,textvariable=author_text)
    e2.grid(row=1,column=7,sticky=E)

    quantity_text=StringVar()
    e3=Entry(window,textvariable=quantity_text)
    e3.grid(row=2,column=5,sticky=W)

    price_text=StringVar()
    e4=Entry(window,textvariable=price_text)
    e4.grid(row=2,column=7,sticky=E)

    list1=Listbox(window, height=12,width=40)
    list1.grid(row=3,column=0,rowspan=6,columnspan=2)

    sb1=Scrollbar(window)
    sb1.grid(row=3,column=2,rowspan=6)

    list1.configure(yscrollcommand=sb1.set)
    sb1.configure(command=list1.yview)

    list1.bind('<<ListboxSelect>>',get_selected_row)

    b1=Button(window,text="View all", width=12,command=view_command)
    b1.grid(row=3,column=7,sticky=E)

    b2=Button(window,text="Search entry", width=12,command=search_command)
    b2.grid(row=4,column=7,sticky=E)

    b3=Button(window,text="Add entry", width=12,command=add_command)
    b3.grid(row=5,column=7,sticky=E)

    b4=Button(window,text="Update selected", width=12,command=update_command)
    b4.grid(row=6,column=7,sticky=E)

    b5=Button(window,text="Delete selected", width=12,command=delete_command)
    b5.grid(row=7,column=7,sticky=E)

    b6=Button(window,text="Buy",width=12,command=buy_command)
    b6.grid(row=8,column=7,sticky=E)

    b7=Button(window,text="Total Books",width=12,command=total_command)
    b7.grid(row=9,column=0,sticky=S)

    b8=Button(window,text="Max. Price",width=12,command=max_command)
    b8.grid(row=9,column=1,columnspan=2,sticky=S)

    b9=Button(window,text="Min. Price",width=12,command=min_command)
    b9.grid(row=9,column=3,sticky=S)
    menu=Menu(window)
    window.config(menu=menu)
    subm1=Menu(menu)
    menu.add_cascade(label="File",menu=subm1)
    subm1.add_cascade(label="Bookstore Head information",command=head)
    subm1.add_cascade(label="Workers information",command=workers)
    subm1.add_cascade(label="Exit",command=thanks2)

    subm2=Menu(menu)
    menu.add_cascade(label="Options",menu=subm2)
    subm2.add_cascade(label="Customer Information",command=customers)
    subm2.add_cascade(label="Bookeller Information",command=bookseller)
    lab.place(x=0,y=0,relwidth=1,relheight=1)

    window.mainloop()
root1=Tk()
root1.geometry('700x750')
root1.wm_title("Welcome",)
imag1=Image.open("welcome.jpg")
imag1=imag1.resize((700,750),Image.ANTIALIAS)
photo1=ImageTk.PhotoImage(imag1)
lab=Label(image=photo1)
lab.place(x=0,y=0,relwidth=1,relheight=1)
b1=Button(root1,text="WELCOME", width=20,command=bookstore)
b1.place(x=510,y=400)
root1.mainloop()
    


