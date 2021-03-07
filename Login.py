import tkinter
from tkinter import messagebox

root = tkinter.Tk()
root.title("Login to my Email")
root.geometry("600x600")

def register():
    newUn = tkinter.Entry()
    newUn.insert(0, "Enter your username")
    newUn.pack()

    newPw = tkinter.Entry()
    newPw.insert(0, "Enter your password")
    newPw.pack()

    def write_to_file():
        getNewUn = newUn.get()
        getNewPw = newPw.get()
        with open("Users.txt", "a") as file:
            file.write(str(getNewUn) + "," + str(getNewPw) + "\n")
    
    registerBtn = tkinter.Button(text="Sign up", command=write_to_file)
    registerBtn.pack()

textUn = tkinter.Label(text="Enter Username:")
textUn.pack()
enterUn = tkinter.Entry()
enterUn.pack()

textPw = tkinter.Label(text="Enter Password:")
textPw.pack()
enterPw = tkinter.Entry()
enterPw.pack()

def login():
    username = enterUn.get()
    password = enterPw.get()
    with open("Users.txt", "r") as file:
       if (username + "," + password + "\n") in file.readlines():
            success = tkinter.Label(text="You are now logged in.")
            success.pack()
       else:
            fail = tkinter.Label(text="Invalid username or password supplied.")
            fail.pack()

loginButton = tkinter.Button(text="Login", command=login)
loginButton.pack()

registerButton = tkinter.Button(text="Sign up", command=register)
registerButton.pack()
          
root.mainloop()
