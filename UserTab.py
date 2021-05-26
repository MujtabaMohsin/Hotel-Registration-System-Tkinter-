import tkinter as tk
from tkinter import *
import Login as login
from tkcalendar import DateEntry
from datetime import date
import random

from UserModel import User

main_font = "Verdana 18 bold"
sub_font = "Verdana 13"
sub_font2 = "Verdana 14"
color = 'gray77'
 

class UserTab(tk.Frame):
    left_frame = None
    right_frame = None
    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)
        self.configure(bg=color)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=4)

        UserTab.left_frame = tk.Frame(self, bg='#00008B')
        UserTab.left_frame.grid(row=0, column=0, sticky='NSEW', ipadx=1,ipady=500)

        UserTab.right_frame = tk.Frame(self, bg=color)

        UserTab.right_frame.grid(row=0, column=1, padx=15, sticky='NSEW')

    def createframes(controller,username):
        # ============ variables =============
        username_txt = tk.StringVar()
        password_txt = tk.StringVar()
        phone_txt = tk.StringVar()



        # =================== Left Frame =========================
        welcome = tk.Label(UserTab.left_frame, text="Welcome "+username, bg='#00008B',fg='white', font=sub_font)
        welcome.grid(row=0, column=0, padx=5, pady=5, sticky='NSEW')

        reserve_btn = tk.Button(UserTab.left_frame, text="Reserve a Room", width=15, padx=22, pady=8, highlightbackground=color
                                , command=lambda: reserve_frame.tkraise())
        reserve_btn.grid(row=1, column=0, padx=10, pady=10)

        myrooms_btn = tk.Button(UserTab.left_frame, text="My Rooms",width=15, padx=22, pady=8, highlightbackground=color
                                , command=lambda: myrooms_frame.tkraise())
        myrooms_btn.grid(row=2, column=0, padx=10, pady=10)

        update_btn = tk.Button(UserTab.left_frame, text="Update profile",width=15, padx=22, pady=8, highlightbackground=color
                               , command=lambda: update_frame.tkraise())
        update_btn.grid(row=3, column=0, padx=10, pady=10)

        logout_btn = tk.Button(UserTab.left_frame, text="Log out",width=15, padx=22, pady=8, highlightbackground=color
                               , command=lambda: controller.show_frame(login.Login))
        logout_btn.grid(row=4, column=0, padx=10, pady=10)

        # =================== Update Frame =========================
        data = UserTab.getUpdateData(username)
        username_txt = data[0]

        password_txt = data[1]
        phone_txt = data[2]

        update_frame = tk.Frame(UserTab.right_frame, bg=color)
        update_frame.grid(row=0, column=0, sticky='NSEW')
        # update_frame.columnconfigure(1, weight=5)

        title2 = tk.Label(update_frame, text="Update Profile", bg=color, font=main_font)
        title2.grid(row=0, column=0, padx=10, pady=10, sticky='w')

        tempframe = tk.Frame(update_frame, bg=color)
        tempframe.grid(row=1, column=0, padx=10, pady=10, sticky='w')

        username_lb = tk.Label(tempframe, text="Name:", bg=color, font=sub_font2)
        username_lb.grid(row=0, column=0, padx=3, pady=10, sticky='W')

        username_entry = tk.Entry(tempframe, width=30, bd=3, bg='white', textvariable=username_txt)
        username_entry.grid(row=0, column=1, padx=10, pady=10, sticky='W')
        username_entry.delete(0, 'end')
        username_entry.insert(0, username_txt)

        phone = tk.Label(tempframe, text="Phone:", bg=color, font=sub_font2)
        phone.grid(row=1, column=0, padx=3, pady=10, sticky='W')

        phone_entry = tk.Entry(tempframe, width=30, bd=3, bg='white', textvariable=phone_txt)
        phone_entry.grid(row=1, column=1, padx=10, pady=10, sticky='W')
        phone_entry.delete(0, 'end')
        phone_entry.insert(0, phone_txt)

        password = tk.Label(tempframe, text="Password:", bg=color, font=sub_font2)
        password.grid(row=2, column=0, padx=3, pady=10, sticky='W')

        password_entry = tk.Entry(tempframe, width=30, bd=3, bg='white', textvariable=password_txt)
        password_entry.grid(row=2, column=1, padx=10, pady=10, sticky='W')
        password_entry.delete(0, 'end')
        password_entry.insert(0, password_txt)

        login_btn = tk.Button(update_frame, text="Update", padx=12, pady=8, highlightbackground=color)
        login_btn.grid(row=2, column=0, padx=10, pady=10, sticky='W')

        # =================== My rooms =========================

        myrooms_frame = tk.Frame(UserTab.right_frame, bg=color)
        myrooms_frame.grid(row=0, column=0, sticky='NSEW')

        title_frame = tk.Frame(myrooms_frame, bg=color)
        title_frame.grid(row=0, column=0, sticky='NSEW')

        table_frame = tk.Frame(myrooms_frame, bg=color)
        table_frame.grid(row=1, column=0, sticky='NSEW')

        # myrooms_frame.forget()
        title3 = tk.Label(title_frame, text="My Rooms", bg=color, font=main_font)
        title3.grid(row=0, column=0, padx=10, pady=10, sticky='w')

        rooms = UserTab.getRooms(username)

        #add first row
        UserTab.createFirstRow(table_frame)

        for i in range(0,len(rooms),1):
            for j in range(0,6,1):
                if j == 2 or j == 3 or j == 4:
                    width = 11
                else:
                    width = 9
                e = Entry(table_frame, width=width, fg='blue',
                          font=('Arial', 12, 'bold'), justify='center')

                e.grid(row=i+1, column=j)
                if j == 0:
                    e.insert(END, str(i+1))

                else:
                    e.insert(END, rooms[i].__getitem__(j))
                e.config(state=DISABLED)

        # =================== Reserve Frame =========================

        reserve_frame = tk.Frame(UserTab.right_frame, bg=color)
        reserve_frame.grid(row=0, column=0, sticky='NSEW')

        reserve_frame.columnconfigure(0, weight=3)

        title1 = tk.Label(reserve_frame, text="Reserve a Room", bg=color, font=main_font)
        title1.grid(row=0, column=0, padx=10, pady=10, sticky='w')

        type_frame = tk.Frame(reserve_frame, bg=color)
        type_frame.grid(row=1, column=0, padx=10, pady=10, sticky='w')

        type = tk.Label(type_frame, text="Type:", bg=color, font=sub_font2)
        type.grid(row=0, column=0, sticky='w')

        v = tk.IntVar()
        res = tk.IntVar()

        choices_frame = tk.Frame(type_frame, bg=color)
        choices_frame.grid(row=0, column=1, sticky='w')

        choice1 = tk.Radiobutton(choices_frame, text="Room", padx=5, variable=v, value=0, bg=color)
        choice2 = tk.Radiobutton(choices_frame, text="Apartment", padx=5, variable=v, value=1, bg=color)
        v.set(0)
        choice1.grid(row=0, column=0, padx=5, pady=0)
        choice2.grid(row=0, column=1, padx=5, pady=0)

        strdate_frame = tk.Frame(reserve_frame, bg=color)
        strdate_frame.grid(row=3, column=0, padx=5, pady=5, sticky='w')

        enddate_frame = tk.Frame(reserve_frame, bg=color)
        enddate_frame.grid(row=4, column=0, padx=5, pady=5, sticky='w')

        str_label = tk.Label(strdate_frame, text="Start Date:", bg=color, font=sub_font2)
        str_label.grid(row=0, column=0, padx=5, pady=10, sticky='w')

        strdate = DateEntry(strdate_frame, width=12, background='darkblue', foreground='white', borderwidth=2)
        strdate.grid(row=0, column=1, padx=5, pady=10, sticky='w')

        end_label = tk.Label(enddate_frame, text="End Date:", bg=color, font=sub_font2)
        end_label.grid(row=1, column=0, padx=5, pady=10, sticky='w')

        enddate = DateEntry(enddate_frame, width=12, background='darkblue', foreground='white', borderwidth=2)
        enddate.grid(row=1, column=1, padx=5, pady=10, sticky='w')

        resv_btn = tk.Button(reserve_frame, text="Reserve Now", padx=22, pady=8, highlightbackground=color
                    ,command=lambda: UserTab.reserve(username,v.get(),strdate.get_date(),enddate.get_date(),result))
        resv_btn.grid(row=7, column=0, padx=15, pady=10, sticky='w')

        result = tk.Label(reserve_frame, text="", fg="red", bg=color, font=sub_font2)
        result.grid(row=8, column=0, padx=15, pady=10, sticky='w')



    @staticmethod
    def reserve(username, type, strd, end,result):
        today = date.today()

        #check if the date is valid
        if strd >= today and strd <= end:
            file = open('files\\users\\'+username+'.txt', 'a')
            room = random.randint(1, 500)
            str2 = strd.strftime("%m-%d-%Y")
            end2 = end.strftime("%m-%d-%Y")
            if type == 0:
                rtype = 'Room'
            else:
                rtype = 'Apartment'

            file.write(str(room) + '\n' + rtype + '\n' + str2 + '\n' + end2 + '\n')
            file.close()
            result['text'] = 'Thank you. Your room number is ' + str(room)

        else:
            result['text'] = 'Please, select a valid date.'


    @staticmethod
    def getUpdateData(username):
        file = open('files\\users\\'+username+'.txt', 'r')
        lines = file.read().splitlines()
        file.close()

        return lines

    def getRooms(username):

        lines = UserTab.getUpdateData(username)
        lines = lines[3:]
        x = 1
        y = 1
        room = []
        rooms = []
        for n in range(0,len(lines),1):
            room.append(lines[n])
            if x == 4:
                room.insert(0,str(y))
                strd = room[3]
                end = room[4]
                room.append(UserTab.roomstatus(strd,end))


                rooms.append(room.copy())
                room.clear()
                x = 0
                y+=1
            x += 1
        

        return rooms

    def roomstatus(strd,end):
        today = date.today()
        today_ft = today.strftime("%m-%d-%Y")

        if strd <= today_ft:
            return 'started'
        elif end < today_ft:
            return 'ended'
        else:
            return 'waiting'



    def createFirstRow(frame):
        e1 = Entry(frame, width=9, bg='#FF6347', font=('Arial', 12, 'bold'), justify='center')
        e1.grid(row=0, column=0)
        e1.insert(END, "#")

        e2 = Entry(frame, width=9, bg='#FF6347', font=('Arial', 12, 'bold'), justify='center')
        e2.grid(row=0, column=1)
        e2.insert(END, "Number")

        e3 = Entry(frame, width=11, bg='#FF6347', font=('Arial', 12, 'bold'), justify='center')
        e3.grid(row=0, column=2)
        e3.insert(END, "Type")

        e4 = Entry(frame, width=11, bg='#FF6347', font=('Arial', 12, 'bold'), justify='center')
        e4.grid(row=0, column=3)
        e4.insert(END, "Start")

        e5 = Entry(frame, width=11, bg='#FF6347', font=('Arial', 12, 'bold'), justify='center')
        e5.grid(row=0, column=4)
        e5.insert(END, "End")

        e6 = Entry(frame, width=9, bg='#FF6347', font=('Arial', 12, 'bold'), justify='center')
        e6.grid(row=0, column=5)
        e6.insert(END, "Status")

