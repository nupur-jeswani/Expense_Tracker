import tkinter as tk
from tkinter import *
from tkinter import messagebox, Tk, ttk
from tkcalendar import DateEntry
import matplotlib.pyplot as plt
import mysql.connector
from PIL import ImageTk

db = mysql.connector.connect(
    host="localhost",
    port=3306,
    user="root",
    passwd="root",
    database="expense_users"
)

my_cursor = db.cursor()


def raise_frame(frame):
    frame.tkraise()


main_win = Tk()
main_win.title("Paisa Tracker")
main_win.geometry("1024x683+250+60")
main_win.resizable(False, False)

# setting icon
p = tk.PhotoImage(file='wallet.png')
main_win.iconphoto(False, p)

# paisa tracker main page frame declaration
pt = Frame(main_win)

# registration form frame declaration
reg = Frame(main_win)

# adding expenditure
opt1 = Frame(main_win)

# view expenditure
opt2 = Frame(main_win)

# edit expenditure
opt3 = Frame(main_win)

# delete expenditure
opt4 = Frame(main_win)

# graphical analysis
opt5 = Frame(main_win)

# login page gui start

login = Frame(main_win)
login.place(x=0, y=0, width=1024, height=683)

# setting background image for the login frame

bg = ImageTk.PhotoImage(file="background2.jpg")
login.bg_image = Label(login, image=bg).place(x=0, y=0, relwidth=1, relheight=1)

Frame(login, bg="white", borderwidth=9, relief="raised").place(x=265, y=150, height=400, width=500)

Label(login, bg="white", bd=1, relief="solid", padx="10", pady="10", text="Enter your Credentials to Login", font=("Lato", 15, "bold"), fg="dark slate gray").place(x=353, y=190)

Label(login, text="Enter your Username: ", font=("Times", 13), bg="white").place(x=316, y=275)
luser = StringVar()
ltxt_user = Entry(login, textvariable=luser, width=25, bg="snow2", fg="black", font=("Times", 13), bd=2, relief="ridge")
ltxt_user.focus_set()
ltxt_user.place(x=480, y=275)

Label(login, text="Enter your Password: ", font=("Times", 13), bg="white").place(x=320, y=330)
lpaswd = StringVar()
ltxt_pass = Entry(login, textvariable=lpaswd, show='*', width=25, bg="snow2", fg="black", font=("Times", 13), bd=2, relief="ridge")
ltxt_pass.place(x=480, y=330)


def login_checker():
    luser_verification = ltxt_user.get()
    lpass_verification = ltxt_pass.get()

    sql = "SELECT * FROM users WHERE USERNAME = %s AND PASSWORD = %s"
    my_cursor.execute(sql, [luser_verification, lpass_verification])
    result = my_cursor.fetchall()

    if ltxt_pass.get() == "" and ltxt_user.get() == "":
        messagebox.showerror("Error", "All fields are Empty. Login Unsuccessful", parent=login)

    elif ltxt_pass.get() == "" or ltxt_user.get() == "":
        messagebox.showerror("Error", "One of the fields above is Empty. Login Unsuccessful", parent=login)

    elif result:
        messagebox.showinfo("Welcome to Expense Tracker", f"Welcome {luser_verification} \nYou have successfully Logged in.", parent=login)
        login.lower()
        raise_frame(pt)

        # paisa tracker main page gui start

        pt.place(x=0, y=0, width=1024, height=683)
        pt.configure(bg="#5f8368")

        Frame(pt, bg="white", height=70, width=1024).place(x=0, y=613)
        Frame(pt, bg="white", height=550, width=3).place(x=20, y=123)
        Frame(pt, bg="white", height=500, width=3).place(x=1004, y=0)
        Frame(pt, bg="white", height=3, width=800).place(x=100, y=120)

        Label(pt, text="PAISA TRACKER", font=("Luthier", 23, "bold"), bg="#5f8368").place(x=380, y=45)
        Label(pt, text="~ we make money work in your favour", font=("Luthier", 13, "italic"), bg="#5f8368").place(x=540,
                                                                                                                  y=80)

        Label(pt, text="Click on what you want to do next: ", font=("Times", 15), bg="#5f8368", fg="white").place(x=250,
                                                                                                                  y=170)

        def adding_expense():
            pt.lower()
            raise_frame(opt1)

        def view_data():
            a = "SELECT * FROM expenses WHERE USERNAME = %s"
            my_cursor.execute(a, [luser_verification])
            l_result = my_cursor.fetchall()

            if not l_result:
                messagebox.showinfo("No Records", "You dont have any records saved with Paisa Tracker.\nAdd expenditure details first and then continue.")
            else:
                pt.lower()
                raise_frame(opt2)

        def edit_go():
            a = "SELECT * FROM expenses WHERE USERNAME = %s"
            my_cursor.execute(a, [luser_verification])
            l_result = my_cursor.fetchall()

            if not l_result:
                messagebox.showinfo("No Records", "You dont have any records saved with Paisa Tracker.\nAdd expenditure details first and then continue.")
            else:
                pt.lower()
                raise_frame(opt3)

        def delete_go():
            a = "SELECT * FROM expenses WHERE USERNAME = %s"
            my_cursor.execute(a, [luser_verification])
            l_result = my_cursor.fetchall()

            if not l_result:
                messagebox.showinfo("No Records", "You dont have any records saved with Paisa Tracker.\nAdd expenditure details first and then continue.")
            else:
                pt.lower()
                raise_frame(opt4)

        def logging_out():
            ltxt_user.delete(0, 'end')
            ltxt_user.focus_set()
            ltxt_pass.delete(0, 'end')

            pt.lower()
            raise_frame(login)

        def graph_go():
            a = "SELECT * FROM expenses WHERE USERNAME = %s"
            my_cursor.execute(a, [luser_verification])
            l_result = my_cursor.fetchall()

            if not l_result:
                messagebox.showinfo("No Records", "You dont have any records saved with Paisa Tracker.\nAdd expenditure details first and then continue.")
            else:
                pt.lower()
                raise_frame(opt5)

        add_expenditure = Button(pt, padx=8, pady=8, width=25, height=1, text="Add my Daily Expense", bg="white",
                                 font=("Times", 13), command=adding_expense)
        add_expenditure.place(x=400, y=220)

        view_expenditure = Button(pt, padx=8, pady=8, width=25, height=1, text="View expenses of a specific date",
                                  bg="white", font=("Times", 13), command=view_data)
        view_expenditure.place(x=400, y=280)

        edit_expenditure = Button(pt, padx=8, pady=8, width=25, height=1, text="Edit expenses of a specific date",
                                  bg="white", font=("Times", 13), command=edit_go)
        edit_expenditure.place(x=400, y=340)

        delete_expenditure = Button(pt, padx=8, pady=8, width=25, height=1, text="Delete expenses of a specific date",
                                    bg="white", font=("Times", 13), command=delete_go)
        delete_expenditure.place(x=400, y=400)

        graphical_visual = Button(pt, padx=8, pady=8, width=25, height=1, text="Graphical View of Expenses", bg="white", font=("Times", 13), command=graph_go)
        graphical_visual.place(x=400, y=460)

        logout = Button(pt, padx=8, pady=8, width=10, height=1, text="Logout", bg="#5f8368", fg="white", command=logging_out,
                        font=("Times", 12))
        logout.place(x=890, y=625)

        Label(pt, text=f"{luser_verification}'s Expenses", font=("Luthier", 13), bg="white").place(x=15, y=635)

        # paisa tracker main page gui finish

        # saving expense gui start

        # if user clicks add expenditures button

        opt1.place(x=0, y=0, width=1024, height=683)
        opt1.configure(bg="LightSteelBlue")

        Frame(opt1, bg="black", height=1, width=545).place(x=245, y=80)
        Frame(opt1, bg="black", height=1, width=545).place(x=245, y=520)
        Frame(opt1, bg="black", height=455, width=1).place(x=255, y=73)
        Frame(opt1, bg="black", height=455, width=1).place(x=780, y=73)

        Label(opt1, bg="LightSteelBlue", fg="black", text="Enter your details of the transaction",
              font=("Lato", 15, "bold")).place(x=350, y=110)

        # change date data type to char data type in expenses database in order to insert uniform data and searching will be easy.
        Label(opt1, text="Enter the Date of Expense: ", font=("Times", 13), bg="LightSteelBlue").place(x=300, y=200)
        date_entry = DateEntry(opt1, width=24, background="black", foreground="white", font=("Times", 13), dateformat=2,
                               date_pattern='yyyy/mm/dd')
        date_entry.place(x=500, y=197)

        Label(opt1, text="[Select appropriate date by clicking on the arrow key near the entry field]",
              font=("Times", 11), bg="LightSteelBlue").place(x=300, y=240)

        Label(opt1, text="Category/description: ", font=("Times", 13), bg="LightSteelBlue").place(x=331, y=285)
        desc = StringVar()
        desc_entry = Entry(opt1, textvariable=desc, width=26, bg="ghost white", fg="black", font=("Times", 13), bd=2,
                           relief="ridge")
        desc_entry.place(x=500, y=285)

        Label(opt1, text="Enter the amount payed: ", font=("Times", 13), bg="LightSteelBlue").place(x=318, y=340)
        amt = StringVar()
        amt_entry = Entry(opt1, textvariable=amt, width=26, bg="ghost white", fg="black", font=("Times", 13), bd=2,
                          relief="ridge")
        amt_entry.place(x=500, y=340)

        def save_exp():
            de = date_entry.get()
            desc_of_item = desc.get()
            amount_paid = amt.get()

            x = "SELECT * FROM users WHERE USERNAME = %s"
            my_cursor.execute(x, [luser_verification])
            r = my_cursor.fetchall()

            if de == "" and amount_paid == "":
                messagebox.showerror("Error", "Please enter required details in order to save them.")
            elif de == "" or amount_paid == "":
                messagebox.showerror("Error", "One of the fields above is Empty. Login Unsuccessful", parent=opt1)
            elif r:
                # save details in the database which are entered by the user
                y = "INSERT INTO expenses (DATE_OF_EXPENSE, AMOUNT, DESCRIPTION, USERNAME) VALUES (%s, %s, %s, %s)"
                data_insert = (de, amount_paid, desc_of_item, luser_verification)
                my_cursor.execute(y, data_insert)

                db.commit()
                messagebox.showinfo("Expenditure Saved.",
                                    "Your details have been saved successfully!")

                resetting()

        def resetting():
            date_entry.delete(0, 'end')
            desc_entry.delete(0, 'end')
            amt_entry.delete(0, 'end')

        def call_main():
            resetting()
            opt1.lower()
            raise_frame(pt)

        Button(opt1, text="Save this expenditure", padx=14, pady=8, bg="Lavender", fg="black",
               font=("Times", 13), command=save_exp).place(x=330, y=430)
        Button(opt1, text="Clear Fields", padx=35, pady=8, bg="grey30", fg="white", font=("Times", 13),
               command=resetting).place(x=550, y=430)
        Button(opt1, text="Return Back", padx=10, pady=5, bg="black", fg="white", font=("Times", 13),
               command=call_main).place(x=880, y=610)

        Label(opt1, text=f"{luser_verification}'s Expenses", font=("Luthier", 13), bg="LightSteelBlue").place(x=35, y=620)

        # adding expense gui finish

        # viewing expense gui start

        opt2.place(x=0, y=0, width=1024, height=683)
        opt2.configure(bg="white")

        Frame(opt2, bd=2, relief="ridge", bg="white", height=150, width=950).place(x=35, y=55)

        Label(opt2, text="You can search your expenses by the Date of Expense: ", font=("Times", 12), bg="black",
              fg="white", padx=10, pady=2).place(x=45, y=42)

        Label(opt2, text="Enter the Date of Expense: ", font=("Times", 13), bg="white").place(x=280, y=120)
        date_entry_of_view = DateEntry(opt2, width=25, background="black", foreground="white", font=("Times", 13), bd=3, dateformat=2, date_pattern='yyyy/mm/dd', relief="ridge")
        date_entry_of_view.place(x=500, y=122)

        Frame(opt2, bd=2, relief="ridge", bg="white", height=320, width=950).place(x=35, y=280)

        Label(opt2, text="Expenditures: ", font=("Times", 13), bg="white").place(x=45, y=268)

        # style for table
        style_view = ttk.Style()

        # theme for the table
        style_view.theme_use('default')

        # tree view colors
        style_view.configure("Treeview", background="#D3D3D3", foreground="black", rowheight=25,
                             fieldbackground="#D3D3D3", height=500, width=800)

        # CHANGING SELECT ROW'S COLORS
        style_view.map("Treeview", background=[('selected', "#347083")])

        # treeview frame
        view_tree_frame = Frame(opt2, bg="#D3D3D3", height=250, width=800, relief="ridge")
        view_tree_frame.place(x=120, y=300)

        # scrollbar
        view_tree_scroll = Scrollbar(view_tree_frame, orient="vertical")
        view_tree_scroll.pack(side=RIGHT, fill=Y)

        # creating treeview
        view_my_tree = ttk.Treeview(view_tree_frame, yscrollcommand=view_tree_scroll.set, selectmode="extended")
        view_my_tree.pack()

        view_tree_scroll.configure(command=view_my_tree.yview)

        # defining columns
        view_my_tree['columns'] = ("ITEM ID", "DATE_OF_EXPENSE", "AMOUNT", "DESCRIPTION")

        # for the data inside the treeview table
        view_my_tree.column("#0", width=0, stretch=NO)
        view_my_tree.column("ITEM ID", anchor=CENTER, width=111, minwidth=60)
        view_my_tree.column("DATE_OF_EXPENSE", anchor=CENTER, width=220, minwidth=110)
        view_my_tree.column("AMOUNT", width=200, anchor=CENTER, minwidth=80)
        view_my_tree.column("DESCRIPTION", width=250, anchor=CENTER, minwidth=100)

        # CREATING HEADINGS OF THE TABLE
        view_my_tree.heading("#0", text="", anchor=W)
        view_my_tree.heading("ITEM ID", text="ITEM ID", anchor=CENTER)
        view_my_tree.heading("DATE_OF_EXPENSE", text="DATE_OF_EXPENSE", anchor=CENTER)
        view_my_tree.heading("AMOUNT", text="AMOUNT", anchor=CENTER)
        view_my_tree.heading("DESCRIPTION", text="DESCRIPTION", anchor=CENTER)

        # striped rows
        view_my_tree.tag_configure('oddrow', background="white")
        view_my_tree.tag_configure('evenrow', background="lightblue")

        def view_by_specific_date():
            view2_output = "SELECT ITEM_ID, DATE_OF_EXPENSE, AMOUNT, DESCRIPTION FROM expenses WHERE USERNAME = %s AND DATE_OF_EXPENSE = %s "
            vd = date_entry_of_view.get()
            if vd == "":
                messagebox.showerror("No date selected", "You have to select a date in order to search expenditures by date.",
                                     parent=opt2)
            else:
                my_cursor.execute(view2_output, [luser_verification, vd])
                view2_result = my_cursor.fetchall()

                if not view2_result:
                    messagebox.showinfo("No Records", f"You don't have any expenditures saved on the date {vd}.", parent=opt2)
                else:
                    view_my_tree['display'] = '#all'
                    view_my_tree.delete(*view_my_tree.get_children())

                    # displaying it in treeview
                    global count
                    count = 0

                    for record2 in view2_result:
                        if count % 2 == 0:
                            view_my_tree.insert(parent="", index='end', iid=count, text="", values=(record2[0], record2[1], record2[2], record2[3]), tags=('evenrow',))
                        else:
                            view_my_tree.insert(parent="", index='end', iid=count, text="", values=(record2[0], record2[1], record2[2], record2[3]), tags=('oddrow',))
                        count += 1

        Button(opt2, text="Search for Expenditures", padx=8, bg="#347083", fg="white", font=("Times", 13),
               relief="ridge", bd=3, command=view_by_specific_date).place(x=409, y=185)

        def searching_tilldate():
            # getting data from database
            view_my_tree.delete(*view_my_tree.get_children())

            view_output = "SELECT ITEM_ID, DATE_OF_EXPENSE, AMOUNT, DESCRIPTION FROM expenses WHERE USERNAME = %s ORDER BY DATE_OF_EXPENSE DESC"
            my_cursor.execute(view_output, [luser_verification])
            view_result = my_cursor.fetchall()

            # displaying it in treeview
            count = 0

            for record in view_result:
                if count % 2 == 0:
                    view_my_tree.insert(parent="", index='end', iid=count, text="",
                                        values=(record[0], record[1], record[2], record[3]), tags=('evenrow',))
                else:
                    view_my_tree.insert(parent="", index='end', iid=count, text="",
                                        values=(record[0], record[1], record[2], record[3]), tags=('oddrow',))
                count += 1

        Button(opt2, text="Search for my Expenditures till date", padx=8, bg="#347083", fg="white", font=("Times", 13),
               relief="ridge", bd=3, command=searching_tilldate).place(x=380, y=585)

        def return_from_view():
            date_entry_of_view.delete(0, 'end')
            view_my_tree.delete(*view_my_tree.get_children())

            opt2.lower()
            raise_frame(pt)

        Button(opt2, text="Return Back", padx=8, bg="black", fg="white", font=("Times", 13), relief="ridge", bd=3,
               command=return_from_view).place(x=873, y=630)

        Label(opt2, text=f"{luser_verification}'s Expenses", font=("Luthier", 13), bg="white").place(x=35, y=635)

        # viewing expense gui finish

        # editing expenditures gui start

        opt3.place(x=0, y=0, width=1024, height=683)
        opt3.configure(bg="white")

        Frame(opt3, bd=2, relief="ridge", bg="white", height=320, width=950).place(x=35, y=15)

        Label(opt3, text="Expenditures: ", font=("Times", 13), bg="white").place(x=45, y=5)

        # style for table
        edit_style = ttk.Style()

        # theme for the table
        edit_style.theme_use('default')

        # tree view colors
        edit_style.configure("Treeview", background="#D3D3D3", foreground="black", rowheight=25,
                             fieldbackground="#D3D3D3", height=500, width=800)

        # CHANGING SELECT ROW'S COLORS
        edit_style.map("Treeview", background=[('selected', "#347083")])

        # treeview frame
        edit_tree_frame = Frame(opt3, bg="#D3D3D3", height=250, width=800, relief="ridge")
        edit_tree_frame.place(x=120, y=35)

        # scrollbar
        edit_tree_scroll = Scrollbar(edit_tree_frame, orient="vertical")
        edit_tree_scroll.pack(side=RIGHT, fill=Y)

        # creating treeview
        edit_my_tree = ttk.Treeview(edit_tree_frame, yscrollcommand=edit_tree_scroll.set, selectmode="extended")
        edit_my_tree.pack()

        edit_tree_scroll.configure(command=edit_my_tree.yview)

        # defining columns
        edit_my_tree['columns'] = ("ITEM ID", "DATE_OF_EXPENSE", "AMOUNT", "DESCRIPTION")

        # for the data inside the treeview table
        edit_my_tree.column("#0", width=0, stretch=NO)
        edit_my_tree.column("ITEM ID", anchor=CENTER, width=111, minwidth=60)
        edit_my_tree.column("DATE_OF_EXPENSE", anchor=CENTER, width=220, minwidth=110)
        edit_my_tree.column("AMOUNT", width=200, anchor=CENTER, minwidth=80)
        edit_my_tree.column("DESCRIPTION", width=250, anchor=CENTER, minwidth=100)

        # CREATING HEADINGS OF THE TABLE
        edit_my_tree.heading("#0", text="", anchor=W)
        edit_my_tree.heading("ITEM ID", text="ITEM ID", anchor=CENTER)
        edit_my_tree.heading("DATE_OF_EXPENSE", text="DATE_OF_EXPENSE", anchor=CENTER)
        edit_my_tree.heading("AMOUNT", text="AMOUNT", anchor=CENTER)
        edit_my_tree.heading("DESCRIPTION", text="DESCRIPTION", anchor=CENTER)

        # striped rows
        edit_my_tree.tag_configure('oddrow', background="white")
        edit_my_tree.tag_configure('evenrow', background="lightblue")

        Frame(opt3, bd=2, relief="ridge", bg="white", height=260, width=950).place(x=35, y=370)

        Label(opt3, text="Search and Edit Expenditures by Date", padx=10, bg="black", fg="white", bd=3,
              font=("Times", 13)).place(x=45, y=360)

        Label(opt3, text="Enter the Date of Expense: ", font=("Times", 13), bg="white").place(x=215, y=400)
        date_entry_of_edit = DateEntry(opt3, width=25, background="black", foreground="white", font=("Times", 13), bd=3, dateformat=2, date_pattern='yyyy/mm/dd', relief="ridge")
        date_entry_of_edit.place(x=410, y=401)

        def searching_till_date_edit():
            # getting data from database
            edit_output = "SELECT ITEM_ID, DATE_OF_EXPENSE, AMOUNT, DESCRIPTION FROM expenses WHERE USERNAME = %s ORDER BY DATE_OF_EXPENSE DESC "
            my_cursor.execute(edit_output, [luser_verification])
            edit_result = my_cursor.fetchall()

            edit_my_tree.delete(*edit_my_tree.get_children())

            # displaying it in treeview
            count = 0

            for record4 in edit_result:
                if count % 2 == 0:
                    edit_my_tree.insert(parent="", index='end', iid=count, text="",
                                        values=(record4[0], record4[1], record4[2], record4[3]), tags=('evenrow',))
                else:
                    edit_my_tree.insert(parent="", index='end', iid=count, text="",
                                        values=(record4[0], record4[1], record4[2], record4[3]), tags=('oddrow',))
                count += 1

        Button(opt3, text="Search for my Expenditures till date", padx=4, bg="grey65", fg="black", font=("Times", 13),
               relief="ridge", bd=3, command=searching_till_date_edit).place(x=380, y=315)

        def searching():
            d = date_entry_of_edit.get()

            # getting data from database
            o = "SELECT ITEM_ID, DATE_OF_EXPENSE, AMOUNT, DESCRIPTION FROM expenses WHERE USERNAME = %s AND DATE_OF_EXPENSE = %s"
            my_cursor.execute(o, [luser_verification, d])
            res = my_cursor.fetchall()

            if not res:
                messagebox.showinfo("No Records", f"You don't have any expenditures saved till now on the date {d}.",
                                    parent=opt3)
            else:
                edit_my_tree.delete(*edit_my_tree.get_children())

                # displaying it in treeview
                global count
                count = 0

                for i in res:
                    if count % 2 == 0:
                        edit_my_tree.insert(parent="", index='end', iid=count, text="", values=(i[0], i[1], i[2], i[3]),
                                            tags=('evenrow',))
                    else:
                        edit_my_tree.insert(parent="", index='end', iid=count, text="", values=(i[0], i[1], i[2], i[3]),
                                            tags=('oddrow',))
                    count += 1

        Button(opt3, text="Search for results", bg="#D3D3D3", fg="black", font=("Times", 11), relief="ridge", bd=3,
               command=searching).place(x=670, y=395)

        def selected_record(e):
            if edit_date.get() != "" or edit_desc.get != "" or edit_amt.get() != "":
                edit_date.delete(0, 'end')
                edit_desc.delete(0, 'end')
                edit_amt.delete(0, 'end')

            selected = edit_my_tree.focus()
            values = edit_my_tree.item(selected, 'values')

            edit_date.insert(0, values[1])
            edit_amt.insert(0, values[2])
            edit_desc.insert(0, values[3])

            def updating():
                nonlocal selected, values
                ed = edit_date.get()
                ea = edit_amt.get()
                ede = edit_desc.get()

                edit_my_tree.item(selected, values=(values[0], ed, ea, ede))

                if ed == "" or ea == "":
                    messagebox.showerror("Null Error",
                                         "Please check your details before saving, Date of exepense or amount cannot be empty.",
                                         parent=opt3)
                else:
                    my_cursor.execute(
                        "UPDATE expenses SET DATE_OF_EXPENSE = %s, AMOUNT = %s, DESCRIPTION = %s WHERE ITEM_ID = %s",
                        (ed, float(ea), ede, values[0]))
                    db.commit()

                    messagebox.showinfo("Changes Saved", "Your changes were successfully saved.", parent=opt3)

                    edit_date.delete(0, 'end')
                    edit_desc.delete(0, 'end')
                    edit_amt.delete(0, 'end')

            Button(opt3, text="Save Changes", padx=8, bg="#347083", fg="white", font=("Times", 13), relief="ridge",
                   bd=3, command=updating).place(x=450, y=560)

        edit_my_tree.bind("<ButtonRelease-1>", selected_record)

        Label(opt3,
              text="To Edit, Select an expenditure from the table, perform the changes you want and click on 'Save Changes'.",
              font=("Times", 13), bg="white").place(x=140, y=450)

        Label(opt3, text="Date of expense: ", font=("Times", 13), bg="white").place(x=43, y=500)
        edit_date = DateEntry(opt3, width=25, background="black", foreground="white", font=("Times", 13), bd=3, dateformat=2, date_pattern='yyyy/mm/dd', relief="ridge")
        edit_date.place(x=170, y=502)

        Label(opt3, text="Description: ", font=("Times", 13), bg="white").place(x=375, y=500)
        edit_d = StringVar()
        edit_desc = Entry(opt3, textvariable=edit_d, width=20, bg="snow2", fg="black", font=("Times", 13), bd=3,
                          relief="ridge")
        edit_desc.place(x=470, y=500)

        Label(opt3, text="Amount: ", font=("Times", 13), bg="white").place(x=715, y=500)
        edit_a = StringVar()
        edit_amt = Entry(opt3, textvariable=edit_a, width=20, bg="snow2", fg="black", font=("Times", 13), bd=3,
                         relief="ridge")
        edit_amt.place(x=785, y=500)

        def returning_to_main():
            edit_date.delete(0, 'end')
            edit_desc.delete(0, 'end')
            edit_amt.delete(0, 'end')
            date_entry_of_edit.delete(0, 'end')

            edit_my_tree.delete(*edit_my_tree.get_children())

            opt3.lower()
            raise_frame(pt)

        Button(opt3, text="Return Back", padx=12, bg="black", fg="white", font=("Times", 13), relief="ridge", bd=3,
               command=returning_to_main).place(x=862, y=640)

        Label(opt3, text=f"{luser_verification}'s Expenses", font=("Luthier", 13), bg="white").place(x=35, y=645)

        # editing expense gui finish

        # deleting expense gui start

        opt4.place(x=0, y=0, width=1024, height=683)
        opt4.configure(bg="white")

        Frame(opt4, bd=2, relief="ridge", bg="white", height=320, width=950).place(x=35, y=30)
        Label(opt4, text="Expenditures: ", font=("Times", 13), bg="white").place(x=45, y=20)

        # style for table
        delete_style = ttk.Style()

        # theme for the table
        delete_style.theme_use('default')

        # tree view colors
        delete_style.configure("Treeview", background="#D3D3D3", foreground="black", rowheight=25,
                               fieldbackground="#D3D3D3", height=250, width=800)

        # CHANGING SELECT ROW'S COLORS
        delete_style.map("Treeview", background=[('selected', "#347083")])

        # treeview frame
        delete_tree_frame = Frame(opt4)
        delete_tree_frame.place(x=120, y=48)

        delete_tree_scroll = Scrollbar(delete_tree_frame)
        delete_tree_scroll.pack(side=RIGHT, fill=Y)

        delete_my_tree = ttk.Treeview(delete_tree_frame, yscrollcommand=delete_tree_scroll.set, selectmode='extended')
        delete_my_tree.pack()

        delete_tree_scroll.configure(command=delete_my_tree.yview)

        # defining columns
        delete_my_tree['columns'] = ("ITEM ID", "DATE_OF_EXPENSE", "AMOUNT", "DESCRIPTION")

        # for the data inside the treeview table
        delete_my_tree.column("#0", width=0, stretch=NO)
        delete_my_tree.column("ITEM ID", anchor=CENTER, width=111, minwidth=60)
        delete_my_tree.column("DATE_OF_EXPENSE", anchor=CENTER, width=220, minwidth=110)
        delete_my_tree.column("AMOUNT", width=200, anchor=CENTER, minwidth=80)
        delete_my_tree.column("DESCRIPTION", width=250, anchor=CENTER, minwidth=100)

        # CREATING HEADINGS OF THE TABLE
        delete_my_tree.heading("#0", text="", anchor=W)
        delete_my_tree.heading("ITEM ID", text="ITEM ID", anchor=CENTER)
        delete_my_tree.heading("DATE_OF_EXPENSE", text="DATE_OF_EXPENSE", anchor=CENTER)
        delete_my_tree.heading("AMOUNT", text="AMOUNT", anchor=CENTER)
        delete_my_tree.heading("DESCRIPTION", text="DESCRIPTION", anchor=CENTER)

        # striped rows
        delete_my_tree.tag_configure('oddrow', background="white")
        delete_my_tree.tag_configure('evenrow', background="lightblue")

        def searching_till_date_delete():
            # getting data from database
            delete_output = "SELECT ITEM_ID, DATE_OF_EXPENSE, AMOUNT, DESCRIPTION FROM expenses WHERE USERNAME = %s ORDER BY DATE_OF_EXPENSE DESC "
            my_cursor.execute(delete_output, [luser_verification])
            delete_result = my_cursor.fetchall()

            delete_my_tree.delete(*delete_my_tree.get_children())

            # displaying it in treeview
            count = 0

            for record6 in delete_result:
                if count % 2 == 0:
                    delete_my_tree.insert(parent="", index='end', iid=count, text="",
                                          values=(record6[0], record6[1], record6[2], record6[3]), tags=('evenrow',))
                else:
                    delete_my_tree.insert(parent="", index='end', iid=count, text="",
                                          values=(record6[0], record6[1], record6[2], record6[3]), tags=('oddrow',))
                count += 1

        Button(opt4, text="Search for my Expenditures till date", padx=4, bg="grey65", fg="black", font=("Times", 13),
               relief="ridge", bd=3, command=searching_till_date_delete).place(x=380, y=330)

        Frame(opt4, bd=2, relief="ridge", bg="white", height=230, width=950).place(x=35, y=380)

        Label(opt4, text="Enter the Date of Expense: ", font=("Times", 13), bg="white").place(x=215, y=420)
        date_entry_of_delete = DateEntry(opt4, width=25, background="black", foreground="white", font=("Times", 13), bd=3, dateformat=2, date_pattern='yyyy/mm/dd', relief="ridge")
        date_entry_of_delete.place(x=410, y=421)

        def searching():
            d = date_entry_of_delete.get()

            # getting data from database
            o = "SELECT ITEM_ID, DATE_OF_EXPENSE, AMOUNT, DESCRIPTION FROM expenses WHERE USERNAME = %s AND DATE_OF_EXPENSE = %s"
            my_cursor.execute(o, [luser_verification, d])
            res = my_cursor.fetchall()

            if not res:
                messagebox.showinfo("No Records", f"You don't have any expenditures saved till now on the date {d}.",
                                    parent=opt4)
            else:
                delete_my_tree.delete(*delete_my_tree.get_children())

                # displaying it in treeview
                global count
                count = 0

                for i in res:
                    if count % 2 == 0:
                        delete_my_tree.insert(parent="", index='end', iid=count, text="",
                                              values=(i[0], i[1], i[2], i[3]),
                                              tags=('evenrow',))
                    else:
                        delete_my_tree.insert(parent="", index='end', iid=count, text="",
                                              values=(i[0], i[1], i[2], i[3]),
                                              tags=('oddrow',))
                    count += 1

        Button(opt4, text="Search for results", bg="#D3D3D3", fg="black", font=("Times", 11), relief="ridge", bd=3,
               command=searching).place(x=670, y=415)

        Label(opt4, text="Search and Edit Expenditures by Date", padx=10, bg="black", fg="white", bd=3,
              font=("Times", 13)).place(x=45, y=367)

        def selected_record(e):
            selected = delete_my_tree.focus()
            values = delete_my_tree.item(selected, 'values')

            def deleting():
                nonlocal selected, values
                delete_my_tree.item(selected, values=(values[0]))

                my_cursor.execute("DELETE FROM expenses WHERE ITEM_ID = %s", (values[0],))
                db.commit()

                delete_my_tree.delete(selected)

                messagebox.showinfo("Deletion Successful", "Your Record was deleted successfully.", parent=opt4)

            Button(opt4, text="Delete Selected Expenditure", padx=8, bg="#347083", fg="white", font=("Times", 13),
                   relief="ridge", bd=3, command=deleting).place(x=390, y=550)

        delete_my_tree.bind("<ButtonRelease-1>", selected_record)

        Label(opt4,
              text="To Delete an expenditure: \n \t  -- Select an expenditure from the table, \n \t  -- Click on 'Delete Selected Expenditure' which will appear after selection.",
              justify="left", font=("Times", 13), bg="white").place(x=215, y=460)

        def returning_to_main_from_delete():
            date_entry_of_delete.delete(0, 'end')
            delete_my_tree.delete(*delete_my_tree.get_children())

            opt4.lower()
            raise_frame(pt)

        Button(opt4, text="Return Back", padx=12, bg="black", fg="white", font=("Times", 13), relief="ridge", bd=3,
               command=returning_to_main_from_delete).place(x=862, y=625)

        Label(opt4, text=f"{luser_verification}'s Expenses", font=("Luthier", 13), bg="white").place(x=35, y=630)

        # deleting expense gui finish

        # graph gui start

        opt5.place(x=0, y=0, width=1024, height=683)
        opt5.configure(bg="honeydew3")

        def showing_help():
            messagebox.showinfo("How to see Expense graphs",
                                "Click on the button 'View daily expense chart'\nIn this chart you will find analysis of your daily expenditures i.e. Total amount you spend on a daily basis.\n\nYou can use the toolbar to navigate throught the graph.\n\nThe table will display detailed information about your expenditures")

        Label(opt5, text="Click on the button to view your daily expense graph and your expenditures in the table",
              font=("Times", 12), bg="white", padx=5, pady=6, relief="solid", bd=1).place(x=60, y=55)
        Button(opt5, text="Help?", padx=10, bg="white", command=showing_help).place(x=950, y=10)
        Frame(opt5, height=450, width=900, bg="white", relief="ridge", bd=2).place(x=60, y=180)

        # style for table
        graph_style = ttk.Style()

        # theme for the table
        graph_style.theme_use('default')

        # tree view colors
        graph_style.configure("Treeview", background="#D3D3D3", foreground="black", rowheight=25,
                              fieldbackground="#D3D3D3", height=250, width=800)

        # CHANGING SELECT ROW'S COLORS
        graph_style.map("Treeview", background=[('selected', "#347083")])

        # treeview frame
        graph_tree_frame = Frame(opt5)
        graph_tree_frame.place(x=110, y=250)

        graph_tree_scroll = Scrollbar(graph_tree_frame)
        graph_tree_scroll.pack(side=RIGHT, fill=Y)

        graph_my_tree = ttk.Treeview(graph_tree_frame, yscrollcommand=graph_tree_scroll.set, selectmode='extended')
        graph_my_tree.pack()

        graph_tree_scroll.configure(command=graph_my_tree.yview)

        # defining columns
        graph_my_tree['columns'] = ("ITEM ID", "DATE_OF_EXPENSE", "AMOUNT", "DESCRIPTION")

        # for the data inside the treeview table
        graph_my_tree.column("#0", width=0, stretch=NO)
        graph_my_tree.column("ITEM ID", anchor=CENTER, width=111, minwidth=60)
        graph_my_tree.column("DATE_OF_EXPENSE", anchor=CENTER, width=220, minwidth=110)
        graph_my_tree.column("AMOUNT", width=200, anchor=CENTER, minwidth=80)
        graph_my_tree.column("DESCRIPTION", width=250, anchor=CENTER, minwidth=100)

        # CREATING HEADINGS OF THE TABLE
        graph_my_tree.heading("#0", text="", anchor=W)
        graph_my_tree.heading("ITEM ID", text="ITEM ID", anchor=CENTER)
        graph_my_tree.heading("DATE_OF_EXPENSE", text="DATE_OF_EXPENSE", anchor=CENTER)
        graph_my_tree.heading("AMOUNT", text="AMOUNT", anchor=CENTER)
        graph_my_tree.heading("DESCRIPTION", text="DESCRIPTION", anchor=CENTER)

        # striped rows
        graph_my_tree.tag_configure('oddrow', background="white")
        graph_my_tree.tag_configure('evenrow', background="lightblue")

        def showing_graph():
            # getting data from database
            graph_output = "SELECT ITEM_ID, DATE_OF_EXPENSE, AMOUNT, DESCRIPTION FROM expenses WHERE USERNAME = %s ORDER BY DATE_OF_EXPENSE DESC"
            my_cursor.execute(graph_output, [luser_verification])
            graph_result = my_cursor.fetchall()

            graph_my_tree.delete(*graph_my_tree.get_children())

            # displaying it in treeview
            count = 0

            for record7 in graph_result:
                if count % 2 == 0:
                    graph_my_tree.insert(parent="", index='end', iid=count, text="",
                                         values=(record7[0], record7[1], record7[2], record7[3]), tags=('evenrow',))
                else:
                    graph_my_tree.insert(parent="", index='end', iid=count, text="",
                                         values=(record7[0], record7[1], record7[2], record7[3]), tags=('oddrow',))
                count += 1

            y = "SELECT DATE_OF_EXPENSE, SUM(AMOUNT) AS TOTAL_AMOUNT FROM expenses WHERE USERNAME = %s GROUP BY DATE_OF_EXPENSE DESC"
            my_cursor.execute(y, [luser_verification])
            result = my_cursor.fetchall()

            Dates = []
            amounts = []

            for i in result:
                Dates.append(i[0])
                amounts.append(i[1])

            f = plt.figure()
            f.set_figwidth(8)
            f.set_figheight(6)
            plt.plot(Dates, amounts)
            plt.title('My Expenses')
            plt.ylabel('Amount')
            plt.xlabel('Date')
            plt.xticks(rotation=30)
            plt.grid(True, color='#f1f1f1')
            plt.show()

        Button(opt5, text="View Daily Expense Chart", padx=15, pady=8, bg="dark slate gray", fg="white",
               command=showing_graph, font=("Times", 13)).place(x=400, y=100)
        Button(opt5, text="Return Back", padx=10, bg="black", fg="white", command=showing_help,
               font=("Times", 13)).place(x=843, y=640)

        Label(opt5, text="Expenditures: ", font=("Times", 13), bg="white").place(x=75, y=200)

        def returning_from_graph():
            graph_my_tree.delete(*graph_my_tree.get_children())
            opt5.lower()
            raise_frame(pt)

        Button(opt5, text="Return Back", padx=10, bg="black", fg="white", command=returning_from_graph,
               font=("Times", 13)).place(x=843, y=640)

        Label(opt5, text=f"{luser_verification}'s Expenses", font=("Luthier", 13), bg="honeydew3").place(x=58, y=643)

        # graphical gui finish

    else:
        messagebox.showinfo("Authentication Error", "Please recheck your entered details. \nIf you haven't registered, Register yourself first in order to use our System.", parent=login)


Button(login, padx=10, pady=10, width=23, bg="forest green", fg="white", height=1, text="Login", command=login_checker).place(x=320, y=390)


def reset_field():
    ltxt_user.delete(0, 'end')
    ltxt_pass.delete(0, 'end')


Button(login, padx=10, pady=10, width=23, bg="brown3", fg="white", height=1, text="Reset Fields", command=reset_field).place(x=520, y=390)


def Register():
    login.lower()
    raise_frame(reg)


Button(login, padx=10, pady=10, width=52, bg="SteelBlue4", fg="white", height=1, text="Don't Have an Account?", command=Register).place(x=320, y=450)

# login for gui finish

# Registration form gui start

reg.place(x=0, y=0, width=1024, height=683)

# setting background image for the form

reg.bg = PhotoImage(file="regbgtry2.png")
reg.bg_image = Label(reg, image=reg.bg).place(x=0, y=0, relwidth=1, relheight=1)

ruser = StringVar()
rtxt_user = Entry(reg, textvariable=ruser, width=25, bg="white", fg="grey21", font=("Bell MT", 13), bd=1, relief="sunken")
rtxt_user.place(x=675, y=283)

rpaswd = StringVar()
rtxt_pass = Entry(reg, textvariable=rpaswd, show='*', width=25, bg="white", fg="grey21", font=("Bell MT", 13), bd=1, relief="sunken")
rtxt_pass.place(x=675, y=335)

rcpaswd = StringVar()
rtxt_cpass = Entry(reg, textvariable=rcpaswd, show='*', width=25, bg="white", fg="grey21", font=("Bell MT", 13), bd=1, relief="sunken")
rtxt_cpass.place(x=675, y=388)


def reg_check():
    user_verify = ruser.get()
    pass_insert = rpaswd.get()

    a = "SELECT * FROM users WHERE USERNAME = %s "
    my_cursor.execute(a, [user_verify])
    res = my_cursor.fetchall()

    if rpaswd.get() == "" and ruser.get() == "" and rcpaswd.get() == "":
        messagebox.showerror("Error", "All fields are Empty. Login Unsuccessful", parent=reg)
    elif rpaswd.get() == "" or ruser.get() == "" or rcpaswd.get() == "":
        messagebox.showerror("Error", "Some of the above fields are Empty. Login Unsuccessful", parent=reg)
    elif rcpaswd.get() != rpaswd.get():
        messagebox.showerror("Error", "Password fields Don't match", parent=reg)
    elif res:
        messagebox.showerror("Error", f"Username '{user_verify}' already taken, Please Change.", parent=reg)
    else:
        s = "INSERT INTO users (USERNAME, PASSWORD) VALUES (%s, %s)"
        data = (user_verify, pass_insert)
        my_cursor.execute(s, data)

        db.commit()
        messagebox.showinfo("Paisa Tracker", f"Welcome {user_verify} to Paisa Tracker. \nLogin to Begin.")

        reg.lower()
        raise_frame(login)


reg_button = tk.Button(reg, padx=10, pady=10, width=23, bg="forest green", fg="white", height=1, text="Submit Details", command=reg_check)
reg_button.place(x=620, y=450)


def reset():
    rtxt_user.delete(0, 'end')
    rtxt_pass.delete(0, 'end')
    rtxt_cpass.delete(0, 'end')


reset_button = tk.Button(reg, padx=5, pady=5, width=23, bg="azure4", fg="white", height=1, text="Reset Fields", command=reset)
reset_button.place(x=625, y=510)


def backtologin():
    reg.lower()
    reset_field()
    raise_frame(login)


Back_button = tk.Button(reg, padx=1, pady=2, bg="old lace", fg="black", height=1, text="Back to Login window", command=backtologin)
Back_button.place(x=880, y=25)

# Registration form gui finish

main_win.mainloop()
# application code finish
