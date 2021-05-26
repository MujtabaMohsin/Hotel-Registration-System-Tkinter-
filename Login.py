import tkinter as tk
from tkinter import messagebox

import Register as register
import UserTab as usertab
from UserModel import User

main_font = "Verdana 20"
sub_font = "Verdana 18"
color = 'gray77'
username1 = ""


class Login(tk.Frame):



    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)
        self.pack(fill='both', expand=1)

        # ============ variables =============
        username = tk.StringVar()
        password = tk.StringVar()


        self.configure(bg=color)


        wel = tk.Label(self, text="Welcome to Hotel Registration System", bg=color, font="Verdana 23 ")
        wel.place(anchor="center", x=400, y=75)

        log = tk.Label(self, text="Login:", bg=color, font=main_font)
        log.place(anchor="center", x=400, y=125)

        tk.Label(self, text="Username:", bg=color, font=sub_font).place(anchor="center", x=270, y=205)
        tk.Label(self, text="Password:", bg=color, font=sub_font).place(anchor="center", x=270, y=265)

        userentry = tk.Entry(self, textvariable=username, width=30, bd=3, bg='white', insertwidth=2)
        userentry.place(anchor="center", x=450,y=205)

        passentry = tk.Entry(self, textvariable=password, width=30, bd=3, show="*", bg='white', insertwidth=2)
        passentry.place(anchor="center", x=450,y=265)


        login_btn = tk.Button(self, text="Login", padx=12, pady=8, highlightbackground=color
        ,command=lambda: self.showUserTab(controller, username.get(), password.get()))


        login_btn.place(anchor="center", x=340, y=325)

        reset_btn = tk.Button(self, text="Reset", command=lambda: self.reset(self, username, password), padx=12, pady=8,
                   highlightbackground=color)
        reset_btn.place(anchor="center", x=430, y=325)

        reg = tk.Label(self, cursor="hand2", text="Don't you have an account? Register now.", bg=color,
                    font="Helvetica 12 bold underline")
        reg.place(anchor="center", x=400, y=390)
        reg.bind('<Button-1>', lambda x: controller.show_frame(register.Register))



    @staticmethod
    def reset(self, username, password):
        username.set("")
        password.set("")

    # =================== check login function =========================

    @staticmethod
    def checklogin(username, password):

        file = open('files\\database.txt', 'r')
        lines = file.read().splitlines()
        checkuser = False;
        tempint = 0;

        #check if username is in
        for x in range(0,len(lines),1):
            if x == 0 or x % 2 == 0:
                if username == lines[x]:
                    checkuser = True
                    tempint = x+1
                    break
                    
    
        if checkuser and lines[tempint] == password:
            return True;
        else:
            return False;

        file.close()


    @staticmethod
    def showUserTab(controller, username, password):

        check = Login.checklogin(username, password)


        if check:
            usertab.UserTab.createframes(controller, username)
            controller.show_frame(usertab.UserTab)
        else:
            messagebox.showwarning("No Match", "Uncorrect data. Please try again.")