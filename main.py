import tkinter
from tkinter import *
from tkinter import ttk
import mysql.connector
from tkinter import messagebox

root = Tk()
root.title('Login Page')
root.geometry('600x400')
root.configure(bg='skyblue')

class LoginDatabase:
    def __init__(self):
        self.root = root
        self.input_text = StringVar
        self.header = Label(self.root, text='Enter Your Details', background='skyblue', foreground='black', font=('serif', 25))
        self.header.place(x=150, y=10)
        self.username = Label(self.root, text='Username', background='tomato', foreground='black', font=('Arial', 20))
        self.username.place(x=20, y=100)
        self.username_entry = ttk.Entry(self.root, textvariable=self.input_text, justify=CENTER, font=('courier', 20, 'bold'))
        self.username_entry.place(x=150, y=100)
        self.password = Label(self.root, text='Password', background='tomato', foreground='black', font=('Arial', 20))
        self.password.place(x=20, y=180)
        self.password_entry = ttk.Entry(self.root, textvariable=self.input_text, justify=CENTER, font=('Courier', 20, 'bold'), show="**")
        self.password_entry.place(x=150, y=180)

        self.login_button = tkinter.Button(self.root, text='Login', relief=GROOVE, activebackground="#33B5E5", command=self.database_login)
        self.login_button.place(x=180, y=250)
        self.signup_button = tkinter.Button(self.root, text='Sign In', relief=GROOVE, activebackground="#33B5E5", command=self.database_register)
        self.signup_button.place(x=280, y=250)

    def database_login(self):

        my_database = mysql.connector.connect(user='lifechoices', password='@Lifechoices1234', host='127.0.0.1', database='Hospitals', auth_plugin='mysql_native_password')
        mycursor = my_database.cursor()
        xy = mycursor.execute('Select * from Login')
        for x in mycursor:
            if x[1] == self.password_entry.get() and x[0] == self.username_entry.get():
                messagebox.showinfo("Permission Granted", 'Login Successful')
                root.destroy()
                return
        if x[1] != self.password_entry.get() or x[0] != self.username_entry.get():
                    messagebox.showerror("Invalid Password", "Please Enter A Valid Password")
                    self.username_entry.delete(0, END)
                    self.password_entry.delete(0, END)

    def database_register(self):
        mydb = mysql.connector.connect(user='lifechoices', password='@Lifechoices1234', host='127.0.0.1', database='Hospitals', auth_plugin='mysql_native_password')

        mycursor = mydb.cursor()
        sql = "INSERT INTO Login (NAME, PASSWORD) VALUE (%s, %s)"
        val = (self.username_entry.get(), self.password_entry.get())
        mycursor.execute(sql, val)
        messagebox.showinfo("PERMISSION", "YOU HAVE REGISTERED SUCCESSFULLY")
        self.username_entry.delete(0, END)
        self.password_entry.delete(0, END)
        mydb.commit()


x = LoginDatabase()
root.mainloop()
