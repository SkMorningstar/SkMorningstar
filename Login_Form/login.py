from tkinter import *
import mysql.connector as db                              

mydb=db.connect(host="localhost",username="root",password="",database="tk")
cursor=mydb.cursor()

def add_data(e1,e2):
    try:
        statement="INSERT INTO pytk(e1,e2) VALUES (%s,%s)"
        data=(e1,e2)
        cursor.execute(statement,data)
        mydb.commit()
        print("SUCCESSFULLY ADDED ENTRY TO THE DATABASE")
        res=Label(gui,text="SUCCESS",foreground="green",font=('ariel',40))
        res.pack(side="bottom")
        gui.after(3000,lambda:gui.destroy())
    except db.Error as e:
        print(f"Error adding entry to database: {e}")
        res=Label(gui,text="Failure",foreground="red",font=('ariel',40))
        res.pack(side="bottom")
   
def entry():
    e1=a1.get()
    e2=int(a2.get())
    display.insert(0,f'The data of Mr/Ms.{e1} of age {e2} is stored...')
    add_data(e1,e2)
   
def destroy():
    res=Label(gui,text="BYE",foreground="black",font=('ariel',40))
    res.pack(side="bottom")
    gui.after(1000,lambda:gui.destroy())
   
def reset():
    try:
        statement="TRUNCATE TABLE pytk"
        cursor.execute(statement)
        mydb.commit()
        print("DATABASE IS ALL CLEARED")
        res=Label(gui,text="ALL CLEAR",foreground="green",font=('ariel',40))
        res.pack(side="bottom")
    except db.Error as e:
        print(f"Can't clear the database: {e}")
        res=Label(gui,text="CAN NOT CLEAR",foreground="red",font=('ariel',40))
        res.pack(side="bottom")

gui=Tk()
gui.title("Bio Data")
gui.geometry("800x450")
gui['bg']="light blue"

a1=Entry(gui,background="sky blue",foreground="black",font="bold")
a1.place(x=350,y=50)
a2=Entry(gui,background="sky blue",foreground="black",font="bold")
a2.place(x=350,y=130)
q1=Label(gui,text="Enter your name ",background="white",foreground="blue",font="bold")
q1.place(x=150,y=50)
q2=Label(gui,text="Enter your age ",background="white",foreground="blue",font="bold")
q2.place(x=150,y=130)
submit=Button(gui,text="SUBMIT",width=40,command=entry,background="blue",foreground="white",activeforeground="white",activebackground="dark blue")
submit.place(x=230,y=200)
display=Entry(gui,width=40)
display.place(x=240,y=250)
reset=Button(gui,text="RESET",width=20,command=reset,background="sky blue",foreground="black",activeforeground="white",activebackground="dark blue")
reset.place(x=100,y=320)
exit=Button(gui,text="EXIT",width=20,command=destroy,background="sky blue",foreground="black",activeforeground="white",activebackground="dark blue")
exit.place(x=500,y=320)

mainloop()