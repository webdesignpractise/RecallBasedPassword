from tkinter import *
from functools import partial
from tkinter import messagebox
import mysql.connector
db=mysql.connector.connect(

    host="localhost",
    username="root",
    password="Manish@1998!"
)

cur=db.cursor()

cur.execute('use projclg')

password=""

def validateLogin(username):
    
    sql="select password from registration where username=%s"
    val=username.get()
    cur.execute(sql,[val])

    passdb=cur.fetchone()[0]

    if passdb==password :
        messagebox.showinfo('information', 'Login Successfully !!!')
        #print("Login Successfully !!!")
    else:
        messagebox.showinfo('information', 'Invalid Credentials, Please try again')
        #print("Invalid Credentials, Please try again")
    
	# print("username entered :", username.get())
	# print("password entered :", password)
	#return

def get_button(t):
    global password
    password+=str(t)
    return

#window
tkWindow = Tk()  
tkWindow.geometry('500x300')  
tkWindow.title('Login')

#username label and text entry box
usernameLabel = Label(tkWindow, text="Enter Email").grid(row=0, column=0)
username = StringVar()
usernameEntry = Entry(tkWindow, textvariable=username).grid(row=0, column=1)  

#password label and password entry box
passwordLabel = Label(tkWindow,text="Password").grid(row=1, column=0)  
# password = StringVar()
# passwordEntry = Entry(tkWindow, textvariable=password, show='*').grid(row=1, column=1)  
passwordLabel = Label(tkWindow,text="        Select Password").grid(row=1, column=0)  
password =""
#passwordEntry = Entry(tkWindow, textvariable=password, show='*').grid(row=1, column=1)  
button1 = Button(tkWindow, fg='black', bg='red', height=1, width=7, command= lambda t= "red": get_button(t))
button1.grid(row=2, column=0,padx=2,pady=3)

button2 = Button(tkWindow, fg='black', bg='blue',height=1, width=7, command= lambda t= "blue": get_button(t))
button2.grid(row=2, column=1)
 
button3 = Button(tkWindow, fg='black', bg='orange', height=1, width=7, command= lambda t= "orange": get_button(t))
button3.grid(row=2, column=2)
 
button4 = Button(tkWindow, fg='black', bg='yellow', height=1, width=7, command= lambda t= "yellow": get_button(t))
button4.grid(row=3, column=0,padx=2,pady=3)
 
button5 = Button(tkWindow, fg='black', bg='pink',height=1, width=7, command= lambda t= "pink": get_button(t))
button5.grid(row=3, column=1)
 
button6 = Button(tkWindow, fg='black', bg='purple', height=1, width=7, command= lambda t= "purple": get_button(t))
button6.grid(row=3, column=2)
 
button7 = Button(tkWindow, fg='black', bg='green', height=1, width=7, command= lambda t= "green": get_button(t))
button7.grid(row=4, column=0,padx=2,pady=3)
 
button8 = Button(tkWindow, fg='black', bg='black',height=1, width=7, command= lambda t= "black": get_button(t))
button8.grid(row=4, column=1)
 
button9 = Button(tkWindow, fg='black', bg='brown', height=1, width=7, command= lambda t= "brown": get_button(t))
button9.grid(row=4, column=2)

validateLogin = partial(validateLogin, username)

#login button
loginButton = Button(tkWindow, text="Login", command=validateLogin,fg='black',bg='sky blue',height=1, width=7)  
loginButton.grid(row=5, column=1,pady=2)
tkWindow.mainloop()