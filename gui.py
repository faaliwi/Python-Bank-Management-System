import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import re
import Bank_DB

#-------1) Create User Account ----------------------
def Create_Account():
    create_window = tk.Toplevel(window)
    create_window.title("Create Account")
    create_window.geometry("600x500")
    title = tk.Label(create_window, text="Create User Account", font=("Arial", 15, "bold"))
    title.pack(pady=5)

    form_frame = tk.Frame(create_window)
    form_frame.pack(pady=30)

    tk.Label(form_frame, text= "User Name").grid(row=1, column=0, padx=20, pady=10, sticky="e")
    username_entry = tk.Entry(form_frame, width=30)
    username_entry.grid(row=1, column=1, padx=20,pady=10)

    tk.Label(form_frame, text= "Password").grid(row=2, column=0, padx=20, pady=10, sticky="e")
    password_entry = tk.Entry(form_frame, width=30)
    password_entry.grid(row=2, column=1, padx=20,pady=10)

    tk.Label(form_frame, text= "First Name").grid(row=3, column=0, padx=20, pady=10, sticky="e")
    fname_entry = tk.Entry(form_frame, width=30)
    fname_entry.grid(row=3, column=1, padx=20,pady=10)

    tk.Label(form_frame, text= "Last Name").grid(row=4, column=0, padx=20, pady=10, sticky="e")
    lname_entry = tk.Entry(form_frame, width=30)
    lname_entry.grid(row=4, column=1, padx=20,pady=10)

    tk.Label(form_frame, text= "Phone").grid(row=5, column=0, padx=20, pady=10, sticky="e")
    phone_entry = tk.Entry(form_frame, width=30)
    phone_entry.grid(row=5, column=1, padx=20,pady=10)

    tk.Label(form_frame, text= "Email").grid(row=6, column=0, padx=20, pady=10, sticky="e")
    email_entry = tk.Entry(form_frame, width=30)
    email_entry.grid(row=6, column=1, padx=20,pady=10)

    tk.Label(form_frame, text= "Job Title").grid(row=7, column=0, padx=20, pady=10, sticky="e")
    Job_entry = tk.Entry(form_frame, width=30)
    Job_entry.grid(row=7, column=1, padx=20,pady=10)

    tk.Label(form_frame, text= "Balance").grid(row=8, column=0, padx=20, pady=10, sticky="e")
    balance_entry = tk.Entry(form_frame, width=30)
    balance_entry.grid(row=8, column=1, padx=20,pady=10)

    def add_from_gui():
        Username = username_entry.get()
        Password = password_entry.get()
        Fname = fname_entry.get()
        Lname = lname_entry.get()
        Phone = phone_entry.get()
        email = email_entry.get()
        JobTitle = Job_entry.get()
        Balance = balance_entry.get()

        if Username == "" or Password == "" or Fname == "" or Lname == "" or Phone == ""or email == ""or JobTitle == "" or Balance == "":
            messagebox.showwarning("Warning", "Please fill in the required fields")

        # Password validation    
        if len(Password) < 6:
            messagebox.showerror("Error", "Password must be at least 6 characters")
            return
        
        # Phone validation
        if not Phone.isdigit():
            messagebox.showerror("Error", "Phone must contain numbers only")
            return

        # Email validation
        email_pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        if not re.match(email_pattern, email):
            messagebox.showerror("Error", "Invalid email address")
            return

        # Balance validation
        try:
            Balance = float(Balance)
        except ValueError:
            messagebox.showerror("Error", "Balance must be a number")
            return

        Bank_DB.CreateAccountDB(Username, Password, Fname, Lname, Phone, email, JobTitle, Balance)
        messagebox.showinfo("Success", "Account created successfully")

        username_entry.delete(0,tk.END)
        password_entry.delete(0,tk.END)
        fname_entry.delete(0, tk.END)
        lname_entry.delete(0, tk.END)
        phone_entry.delete(0, tk.END)
        email_entry.delete(0, tk.END)
        Job_entry.delete(0, tk.END)
        balance_entry.delete(0, tk.END)

    button_frame = tk.Frame(create_window)
    button_frame.pack()
    Add_button = tk.Button(button_frame, text="Create Account", width= 20, font=("Arial", 10, "bold"), command=add_from_gui)
    Add_button.pack(side="left", padx=5)

    back_button = tk.Button(button_frame, text="Back", width= 10, font=("Arial", 10, "bold"), command=create_window.destroy)
    back_button.pack(side="left", padx=5)

#-------2) Login to Account ----------------------
def LogIn (UserName, Password):
# check user name and passord from DB
# window to show option : 
# 1) Transfer
# 2) show balance 
# 3) show user detials and update
# 4) Exit

    result = Bank_DB.LogIn(UserName, Password)
    if result:
        User_window = tk.Toplevel(window)
        User_window.title("User Account")
        User_window.geometry("500x300")
        title = tk.Label(User_window, text="User Account", font=("Arial", 15, "bold"))
        title.pack(pady=5)

    
        tk.Button(User_window, text="Transfer", command= lambda: Transfer(UserName), width= 20, font=("Arial", 10, "bold")).pack(pady=15)
        tk.Button(User_window, text="Show Balance", command= lambda: Show_Balance(UserName), width= 20, font=("Arial", 10, "bold")).pack(pady=15)
        tk.Button(User_window, text="Show User Profile", command= lambda: Show_Update_Profile(UserName), width= 20, font=("Arial", 10, "bold")).pack(pady=15)
        tk.Button(User_window, text="Exit", command= User_window.destroy, width= 20, font=("Arial", 10, "bold")).pack(pady=15)
        
    else:
        messagebox.showerror("Login Error","Usernamer or Password is Invaild" )
        print("Usernamer or Password is Invaild")

#-------2.1) Transfer ----------------------
def Transfer (UserName):
    Transfer_window = tk.Toplevel(window)
    Transfer_window.title("Transfer from Your Account to another")
    Transfer_window.geometry("700x300")
    
    title = tk.Label(Transfer_window, text="Transfer from Your Account to another", font=("Arial", 15, "bold"))
    title.grid(row=10, column=0, padx=20, pady=10, sticky="e")
    
    tk.Label(Transfer_window, text="Enter account no").grid(row=15, column=0, padx=20, pady=10, sticky="e")
    account_entry = tk.Entry(Transfer_window, width=30)
    account_entry.grid(row=15, column=1, padx=20,pady=10)

    tk.Label(Transfer_window, text="Enter amount").grid(row=20, column=0, padx=20, pady=10, sticky="e")
    amount_entry = tk.Entry(Transfer_window, width=30)
    amount_entry.grid(row=20, column=1, padx=20,pady=10)

    def transfer_from_gui():
        id = account_entry.get()
        amount = amount_entry.get()

        if id == "" or amount == "":
            messagebox.showwarning("Warning", "Please fill all fields")
            return
        try:
            amount = float (amount)
        except ValueError:
            messagebox.showerror("Error", "Amount must be a numbrt")
            return
        if amount <= 0:
            messagebox.showwarning ("Warning", "Amount must be greater than Zero")
            return

        result = Bank_DB.Transfer(UserName, id, amount)
        if result:
            messagebox.showinfo("Success", "Transfer Completed Successfully")
            account_entry.delete(0, tk.END)
            amount_entry.delete(0, tk.END)
        else:
            messagebox.showerror("Error", "Transfer Failed")


     # Frame
    button_frame = tk.Frame(Transfer_window)
    button_frame.grid(row=25, column=0, columnspan=2, pady=20)
    
    transfer_button = tk.Button(button_frame, text="Transfer",command= transfer_from_gui, width= 15, font=("Arial", 10, "bold"))
    transfer_button.grid(row=25, column=0, padx=10)
    cancel_button = tk.Button(button_frame, text="Cancel", command=Transfer_window.destroy, width= 15, font=("Arial", 10, "bold"))
    cancel_button.grid(row=25, column=1, padx=10)
    
#-------2.2) Show Balance ----------------------
def Show_Balance (UserName):
    Balance_window = tk.Toplevel(window)
    Balance_window.title("User Balance Account")
    Balance_window.geometry("500x200")

    title = tk.Label(Balance_window, text="User Balance Account", font=("Arial", 15, "bold"))
    title.grid(row=15, column=0, padx=20, pady=10, sticky="e")

    tk.Label(Balance_window, text="User Balance").grid(row=30, column=0, padx=20, pady=10, sticky="e")
    balance_entry = tk.Entry(Balance_window, width=30)
    balance_entry.grid(row=30, column=1, padx=20,pady=10)

    balance = Bank_DB.Show_BalanceDB(UserName)

    if balance is not None:
        balance_entry.insert(0, str(balance))
    else:
        print("Error")

    
#-------2.3) Show user profile and update ----------------------
def Show_Update_Profile(UserName):
    Profile_window = tk.Toplevel(window)
    Profile_window.title("Usr Profile Account")
    Profile_window.geometry("500x400")
    
    title = tk.Label(Profile_window, text="User Profile Account", font=("Arial", 15, "bold"))
    title.grid(row=0, column=0, padx=20, pady=10, sticky="e")
    
    tk.Label(Profile_window, text="First Name").grid(row=1, column=0, padx=10, pady=10, sticky="e")
    Fname_entry = tk.Entry(Profile_window, width=30)
    Fname_entry.grid(row=1, column=1, padx=10,pady=10)

    tk.Label(Profile_window, text="Last Name").grid(row=2, column=0, padx=20, pady=10, sticky="e")
    Lname_entry = tk.Entry(Profile_window, width=30)
    Lname_entry.grid(row=2, column=1, padx=20,pady=10)

    tk.Label(Profile_window, text="Phone").grid(row=3, column=0, padx=20, pady=10, sticky="e")
    Phone_entry = tk.Entry(Profile_window, width=30)
    Phone_entry.grid(row=3, column=1, padx=20,pady=10)

    tk.Label(Profile_window, text="Email").grid(row=4, column=0, padx=20, pady=10, sticky="e")
    email_entry = tk.Entry(Profile_window, width=30)
    email_entry.grid(row=4, column=1, padx=20,pady=10)

    tk.Label(Profile_window, text="Job Title").grid(row=5, column=0, padx=20, pady=10, sticky="e")
    Job_entry = tk.Entry(Profile_window, width=30)
    Job_entry.grid(row=5, column=1, padx=20,pady=10)

    tk.Label(Profile_window, text="Account No").grid(row=6, column=0, padx=20, pady=10, sticky="e")
    accountNo_entry = tk.Entry(Profile_window, width=30)
    accountNo_entry.grid(row=6, column=1, padx=20,pady=10)
    
    entry = Bank_DB.Show_Profile(UserName)
    print(entry)
    print(type(entry))
    if entry is not None:
        Fname_entry.insert(0, str(entry[3]))
        Lname_entry.insert(0, str(entry[4]))
        Phone_entry.insert(0, str(entry[5]))
        email_entry.insert(0, str(entry[6]))
        Job_entry.insert(0, str(entry[7]))
        accountNo_entry.insert(0, str(entry[0]))
    else:
        print("Error")

    def update_from_gui():
        fname = Fname_entry.get()
        lname = Lname_entry.get()
        phone = Phone_entry.get()
        email = email_entry.get()
        job = Job_entry.get()

        Bank_DB.Update_profile(UserName, fname, lname, phone, email, job)

        messagebox.showinfo(
        "Success",
        "Profile updated successfully")

    # Frame
    button_frame = tk.Frame(Profile_window)
    button_frame.grid(row=7, column=0, columnspan=2, pady=20)

    update_button = tk.Button(button_frame, text="Update",command= update_from_gui, width= 15, font=("Arial", 10, "bold"))
    update_button.grid(row=0, column=0, padx=10)
    cancel_button = tk.Button(button_frame, text="Cancel", command=Profile_window.destroy, width= 15, font=("Arial", 10, "bold"))
    cancel_button.grid(row=0, column=1, padx=10)

def Show_detials ():
    display_window = tk.Toplevel(window)
    display_window.title("Disply ACount Detials")
    display_window.geometry("1000x500")

    columns = ("ID","Username", "Password","First Name", "Last Name", "Phone","Email","Job Title","Balance")

    table = ttk.Treeview( display_window, columns=columns,show="headings")

    # أسماء الأعمدة
    for column in columns:
        table.heading(column, text=column)
        table.column(column, width=120, stretch=False)

    # الحصول على البيانات من قاعدة البيانات
    accounts = Bank_DB.Show_DetialsDB()

    # إضافة البيانات إلى الجدول
    for account in accounts:
        table.insert("", tk.END, values=account)

    table.pack(fill="both", expand=True, side="right")


#------------------------------Main Window------------------------------------------
window = tk.Tk()
window.title("Banak Managment System")
window.geometry("500x300")

title = tk.Label(window, text="Bank Managment System", font=("Arial", 10, "bold"))
title.grid(row=1, column=0, padx=20, pady=10, sticky="e")

tk.Label(window, text= "User Name").grid(row=15, column=0, padx=20, pady=10, sticky="e")
user_entry = tk.Entry(window, width=30)
user_entry.grid(row=15, column=1, padx=20,pady=10)

tk.Label(window, text= "Password").grid(row=30, column=0, padx=20, pady=10, sticky="e")
passwoed_entry = tk.Entry(window, width=30, show="*")
passwoed_entry.grid(row=30, column=1, padx=20,pady=10)

button_fram = tk.Frame(window)
button_fram.grid(row=40, column=0, columnspan=2, pady=20)     

tk.Button(button_fram, text="Create Account",command= Create_Account, 
          width= 15, font=("Arial", 10, "bold")).pack(side= "left",padx=5)#grid(row=40, column=0, pady=20, padx=5)

tk.Button(button_fram, text="logIn",command= lambda: LogIn(user_entry.get(), passwoed_entry.get()), 
          width= 15, font=("Arial", 10, "bold")).pack(side= "right",padx=5)#grid(row=40, column=1, pady=20, padx=5)

window.mainloop()
