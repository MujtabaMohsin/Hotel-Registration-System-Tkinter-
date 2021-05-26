import tkinter as tk
import Login as login
import Register as register
import UserTab as usertab

main_font = "Verdana 20"
sub_font = "Verdana 18"

color = 'gray77'
class tkinterApp(tk.Tk):

    # __init__ function for class tkinterApp
    def __init__(self, *args, **kwargs):

        # __init__ function for class Tk
        tk.Tk.__init__(self, *args, **kwargs)

        # creating a container
        container = tk.Frame(self)
        container.configure(bg=color)
        self.geometry('800x500')
        self.iconbitmap('hotel.ico')

        self.title('Hotel Registration System')
        self.resizable(width=False, height=False)
        #container.pack(side="top", fill="both", expand=True)
        container.pack(fill='both', expand=1)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # initializing frames to an empty array
        self.frames = {}

        # iterating through a tuple consisting
        # of the different page layouts
        for F in (login.Login, register.Register, usertab.UserTab):
            frame = F(container, self)
           # print(type(frame))
            # initializing frame of that object from
            # startpage, page1, page2 respectively with
            # for loop
            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(login.Login)

    # to display the current frame passed as
    # parameter
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

app = tkinterApp()
app.mainloop()

