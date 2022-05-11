from tkinter import *
from subprocess import call

def Login():
    call(["python", "login.py"])
def Registration():
    call(["python", "registration.py"])

main_screen = Tk()   # create a GUI window 

def main_account_screen():
    
    main_screen.geometry("300x500") # set the configuration of GUI window 
    main_screen.title("Account Login") # set the title of GUI window
 

# create a Form label 
Label(text="Choose Login Or Register", fg='white', bg="blue", width="50", height="2", font=("Calibri", 13)).pack() 
Label(text="").pack() 
 
# create Login Button 
Button(text="Login", height="2", width="15",command=Login).pack() 
Label(text="").pack() 
 
# create a register button
Button(text="Register", height="2", width="15",command=Registration).pack()


main_screen.mainloop() # start the GUI
 
main_account_screen() # call the main_account_screen() function