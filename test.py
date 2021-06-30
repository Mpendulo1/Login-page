 def login(self):

        hospital = mysql.connector.connect(user='lifechoices', password='@Lifechoices1234', host='127.0.0.1', database='hospital',
                              auth_plugin='mysql_native_password')
        mycursor=hospital.cursor()
        xy=mycursor.execute('Select * from Login')
        for x in mycursor:
            if x[1] == self.password_entry.get() and x[0] == self.username_entry.get():
                messagebox.showinfo("PERMISSION", "LOGIN SUCCESSFUL")
                root.destroy()
        if x[1] != self.password_entry.get() or x[0] != self.username_entry.get():
                    messagebox.showerror("STATUS", "ACCESS DENIED")
                    self.username_entry.delete(0, END)
                    self.password_entry.delete(0, END)

    def register(self):
        mydb = mysql.connector.connect(user='lifechoices', password='@Lifechoices1234', host='127.0.0.1', database='hospital',
                              auth_plugin='mysql_native_password')

        mycursor = mydb.cursor()
        sql = "INSERT INTO Login (user, password) VALUE (%s, %s)"
        val = (self.username_entry.get(), self.password_entry.get())
        mycursor.execute(sql, val)
        messagebox.showinfo("PERMISSION", "YOU HAVE REGISTERED SUCCESSFULLY")
        self.username_entry.delete(0, END)
        self.password_entry.delete(0, END)
        mydb.commit()
