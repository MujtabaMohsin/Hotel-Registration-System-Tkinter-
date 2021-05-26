import tkinter as tk
import Login as login


main_font = "Verdana 20"
sub_font = "Verdana 18"
color = 'gray77'

class Register(tk.Frame):


    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.configure(bg=color)

        # ============ variables =============
        username_txt = tk.StringVar()
        password_txt = tk.StringVar()
        phone_txt = tk.StringVar()

        title = tk.Label(self, text="Register", bg=color, font=main_font)
        title.grid(row=1, column=1, padx=10, pady=11, sticky='SW')

        username = tk.Label(self, text="Name:", bg=color,font=sub_font)
        username.grid(row=2, column=0, padx=10, pady=10,sticky='E')

        username_entry = tk.Entry(self, width=30, bd=3, bg='white',textvariable=username_txt)
        username_entry.grid(row=2, column=1, padx=10, pady=10,sticky='W')

        phone = tk.Label(self, text="Phone:", bg=color,font=sub_font)
        phone.grid(row=3, column=0, padx=10, pady=10,sticky='E')

        phone_entry = tk.Entry(self, width=30, bd=3, bg='white',textvariable=phone_txt)
        phone_entry.grid(row=3, column=1, padx=10, pady=10,sticky='W')

        password = tk.Label(self, text="Password:", bg=color,font=sub_font)
        password.grid(row=4, column=0, padx=10, pady=10,sticky='E')

        password_entry = tk.Entry(self, width=30, bd=3, bg='white',textvariable=password_txt)
        password_entry.grid(row=4, column=1, padx=10, pady=10,sticky='W')


        reg_btn = tk.Button(self, text="Register", padx=12, pady=8, highlightbackground=color,
        command=lambda: self.register(self,username_txt, password_txt, phone_txt,controller))
        reg_btn.grid(row=5, column=0, padx=10, pady=10,sticky='E')

        reset_btn = tk.Button(self, text="Reset", padx=12, pady=8,
                   highlightbackground=color,
                    command=lambda: self.reset(self, username_txt, password_txt, phone_txt))
        reset_btn.grid(row=5, column=1, padx=30, pady=20,sticky='WN')

        back_btn = tk.Button(self, text="<-", padx=5, pady=5, highlightbackground=color,
                            command=lambda: controller.show_frame(login.Login))
        back_btn.grid(row=0, column=0, padx=10, pady=10,sticky='NW')

    @staticmethod
    def reset(self, username, password, phone):
        username.set("")
        password.set("")
        phone.set("")

    @staticmethod
    def register(self,username, password, phone,controller):

        if self.checkDuplicate(username.get()):
            file = 'files\\users\\'
            type = ".txt"
            file = open(file+username.get()+type, 'w')
            file.write(username.get() +'\n' + password.get() +'\n' + phone.get() +'\n')
            file.close()

            file2 = open('files\\database.txt', 'a')
            file2.write(username.get() + '\n' + password.get() + '\n')
            file2.close()
            controller.show_frame(login.Login)



    @staticmethod
    def checkDuplicate(username):
        file = open('files\\database.txt', 'r')
        lines = file.read().splitlines()
        checkuser = False;
        #check if username is in
        for x in range(0,len(lines),1):
            if x == 0 or x % 2 == 0:
                if username == lines[x]:
                    checkuser = True
                    break

        if checkuser:
            tk.messagebox.showwarning("Try again","The username is duplicated.")
            return False
        else:
            tk.messagebox.showinfo("Done", "Thanks, you can log in now")
            return True

        file.close()





