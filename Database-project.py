from tkinter import Tk, Label, Button, messagebox, Image,ttk
from PIL import ImageTk, Image
from tkinter import *
from tkcalendar import DateEntry
import sqlite3
from tkinter import *

root = Tk()
root.title("Python: Simple Inventory System")
root.geometry("1000x500+250+130")
root.config(background='red')

def Database():
    global conn, cursor
    conn = sqlite3.connect("data.db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS StudentNames(id INTEGER PRIMARY KEY, Name TEXT, address TEXT, number TEXT, YEARName TEXT, Dob TEXT, Gender TEXT)")
    
def Exit():
    result = tkMessageBox.askquestion('System', 'Are you sure you want to exit?', icon="warning")
    if result == 'yes':
        root.destroy()
        exit()
        
#=============================================VARIABLES======================================================#
Name = StringVar()        
Address = StringVar()  
Number = StringVar()    
v = StringVar()   
Dob = StringVar()    
v1 = StringVar()   
#===============================================METHODS=====================================================#   
        
def register():
    global registerFrame ,lbl_result1
    registerFrame = Frame(root)
    registerFrame.config(background='red')
    registerFrame.place(x= 10, y= 10, height=580, width=980) 
    
    #img=PhotoImage(file='img2.png')
    #L=Label(registerFrame,image=img)
    #L.place(x= 80, y= 100)
    
    name = Label(registerFrame, text="Full Name:",bg="red",foreground="Yellow",font=("Helvetica",12))
    name.place(relx=0.442, rely=0.100, height=20, width=80)    
         
    name_box = Entry(registerFrame, textvariable=Name,font=("Helvetica",12))
    name_box.place(relx=0.552, rely=0.100, height=30, width=250)
              
    
    address = Label(registerFrame, text="Address:",bg="red",foreground="Yellow",font=("Helvetica",12))
    address.place(relx=0.442, rely=0.200, height=20, width=80)
              
    address_box = Entry(registerFrame, textvariable =Address,font=("Helvetica",12))
    address_box.place(relx=0.552, rely=0.200, height=30, width=250)
              
    number = Label(registerFrame, text="Phone no.:",bg="red",foreground="Yellow",font=("Helvetica",12))
    number.place(relx=0.442, rely=0.300, height=30, width=80)
              
    number_box = Entry(registerFrame, textvariable=Number,font=("Helvetica",12))
    number_box.place(relx=0.552, rely=0.300, height=30, width=150)
              
    branch = Label(registerFrame, text="Year:",bg="red",foreground="Yellow",font=("Helvetica",12))
    branch.place(relx=0.442, rely=0.400, height=20, width=75)
              
    v.set("FE")
    button= Radiobutton(registerFrame, text="FE", variable=v, value="FE",bg="red",foreground="Black",font=("Helvetica",12))
    button.place(relx=0.552, rely=0.400, height=20, width=75)
              
    button= Radiobutton(registerFrame, text="SE", variable=v, value ="SE",bg="red",foreground="Black",font=("Helvetica",12))
    button.place(relx=0.625, rely=0.400, height=20, width=75)
              
    button= Radiobutton(registerFrame, text="TE", variable=v, value ="TE",bg="red",foreground="Black",font=("Helvetica",12))
    button.place(relx=0.700, rely=0.400, height=20, width=75)
              
    button= Radiobutton(registerFrame, text="BE", variable=v, value ="BE",bg="red",foreground="Black",font=("Helvetica",12))
    button.place(relx=0.775, rely=0.400, height=20, width=75)
              
    
    birth_date = Label(registerFrame, text="DateofBirth:",bg="red",foreground="Yellow",font=("Helvetica",12))
    birth_date.place(relx=0.420, rely=0.500)
              
    dob_box = DateEntry(registerFrame, textvariable=Dob,font=("Helvetica",12))
    dob_box.place(relx=0.552, rely=0.500, height=30, width=150)

              
    gender = Label(registerFrame, text="Gender:",bg="red",foreground="Yellow",font=("Helvetica",12))
    gender.place(relx=0.452, rely=0.600)
              
    
    v1.set("Female")
    button1= Radiobutton(registerFrame, text="Male", variable=v1, value = "Male",bg="red",foreground="Black",font=("Helvetica",12))
    button1.place(relx=0.552, rely=0.600, height=20, width=75)
              
    button1= Radiobutton(registerFrame, text="Female", variable=v1, value = "Female",bg="red",foreground="Black",font=("Helvetica",12))
    button1.place(relx=0.652, rely=0.600, height=20, width=75)
              
    submit_button = Button(registerFrame, text="Save",bg="#800000",foreground="Yellow",font=("Helvetica",12),command=submit)
    submit_button.place(relx=0.450, rely=0.700, height=40, width=70)
               
    submit_button3 = Button(registerFrame, text="Show",bg="#800000",foreground="Yellow",font=("Helvetica",12),command=show)
    submit_button3.place(relx=0.750, rely=0.700, height=40, width=80)   
    
    lbl_result1 = Label(registerFrame, text="", font=("Helvetica",12),background='red')
    lbl_result1.place(relx=0.750, rely=0.620, height=40, width=100) 

def submit():
    Database()
    cursor.execute("SELECT * FROM StudentNames WHERE Name = ?", (Name.get(),))
    if cursor.fetchone() is not None:
            lbl_result1.config(text="Username is already taken", fg="red")
    else:
            cursor.execute("INSERT INTO StudentNames (Name, address, number, YEARName,Dob, Gender) VALUES(?, ?, ?, ?,?,?)", (str(Name.get()), str(Address.get()), str(Number.get()), str(v.get()),str(Dob.get()),str(v1.get())))
            conn.commit()
            Name.set("")
            Address.set("")
            Number.set("")
            v.set("")
            Dob.set("")
            v1.set("")
            lbl_result1.config(text= "Your record is successfully saved!",fg="blue")
    cursor.close()
    conn.close()       


def show():
    global showFrame, tree
    showFrame = Frame(root)
    showFrame.config(background='red')
    showFrame.place(x= 10, y= 10, height=580, width=980) 
    
    style = ttk.Style(showFrame)
    style.theme_use("clam")
    style.configure("Treeview", background="black", fieldbackground="black", foreground="white")
    
    tree= ttk.Treeview(showFrame, column=(1,2,3,4,5,6,7), show='headings')
    tree.heading("#1", text="ID")
    tree.column("#1", anchor="center",width=70)
    tree.heading("#2", text="Name")
    tree.column("#2", anchor="center")
    tree.heading("#3", text="Address")
    tree.column("#3", anchor="center")
    tree.heading("#4", text="Phone")
    tree.column("#4", anchor="center")
    tree.heading("#5", text="YEARName")
    tree.column("#5", anchor="center")
    tree.heading("#6", text="Dob")
    tree.column("#6", anchor="center")
    tree.heading("#7", text="Gender")
    tree.column("#7", anchor="center")
    tree.place(x=40, y=10,height=330, width=890)
             
              
    conn=sqlite3.connect('data.db')
    cursor=conn.cursor()
    cursor.execute('SELECT * FROM  StudentNames')
    r = cursor.fetchall()
              
    for i in r:
        item=tree.insert("", END, values=i)
        tree.item(item,tags=item)
                     
    ysb = Scrollbar(showFrame, orient='vertical', command=tree.yview)
    xsb = Scrollbar(showFrame, orient='horizontal', command=tree.xview)
    tree.configure(yscroll=ysb.set, xscroll=xsb.set)
    ysb.place(x=40 + 900 + 1, y=10, height=310 + 20)  
    xsb.place(x=60 , y=150+200+1, width=870 + 20)
    
#========================================INITIALIZATION===================================
if __name__ == '__main__':
    root.mainloop()
