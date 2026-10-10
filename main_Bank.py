
def display_List():
    print("Select from the list: ")
    print("1. Create Account")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Transfer")
    print("5. Show Balance")
    print("6. Show Accoounts detials")
    print("7. Delete Accounts")
    print("0. Exit")

class account_info:
    def __init__(self, AccountNo, Fname, Lname, phone, email, Balance):
        self.account_No = AccountNo
        self.account_fname = Fname
        self.account_lname = Lname
        self.account_phone = phone
        self.account_email = email
        self.account_Balance = Balance

    def desiplay (self):
        with open(r"C:\\Users\\faaliwi\\Desktop\\Python\GetHup\bank_info.txt", "r") as f:
           print(f.read())

    def create_account(self):
        with open(r"C:\\Users\\faaliwi\\Desktop\\Python\GetHup\bank_info.txt", "a") as f:
            print(f.write(f"{self.account_No},"
                          f"{self.account_fname},"
                          f"{self.account_lname},"
                          f"{self.account_phone},"
                          f"{self.account_email},"
                          f"{self.account_Balance} \n"))

    def despite (self, accountNo, amount):
            path = r"C:\\Users\\faaliwi\\Desktop\\Python\GetHup\bank_info.txt"
            with open(path, "r") as f:
                lines = f.readlines()
    
            with open(path, "w") as f:
                 for line in lines:
                    data = line.strip().split(",")
                    if data [0] == str(accountNo):
                        data[5] = str (float(data[5]) + amount)
                        new_line = ",".join(data)+"\n"
                        f.write(new_line)
                        print("The new balance is : ")
                        print(data[5])
                    else:
                        f.write(line)

    def withdraw(self, accountNo, amount):
        path = r"C:\\Users\\faaliwi\\Desktop\\Python\GetHup\bank_info.txt"
        with open(path, "r") as f:
            lines = f.readlines()

        with open(path, "w") as f:
            for line in lines:
                data = line.strip().split(",")
                if data [0] == str(accountNo):
                    data[5] = str (float(data[5]) - amount)
                    new_line = ",".join(data)+"\n"
                    f.write(new_line)
                    print("The new balance is : ")
                    print(data[5])
                else:
                    f.write(line)

    def delete_Account(self, AccountNo):
        path = r"C:\\Users\\faaliwi\\Desktop\\Python\GetHup\bank_info.txt"
        with open(path, "r") as f:
            lines = f.readlines()

        with open(path, "w") as f:
            for line in lines:
                data = line.strip().split(",")
                if data [0] != str(AccountNo):
                    f.write(line)

def show_balance(accountNo):
    path = r"C:\\Users\\faaliwi\\Desktop\\Python\GetHup\bank_info.txt"
    found = False
    with open(path, "r") as f:
        for line in f: 
            #print("Bebug: ", line)
            data = line.strip().split(",")
            #if len(data) < 6:
            #    continue
            if data [0] == str(accountNo):
                print("Bebug: ", line)
                data = line.strip().split(",")
                print("The balance is : ", data[5])
                found = True
                break
    if not found:
        print("Account not found.")

def show_Account(accountNo):
    path = r"C:\\Users\\faaliwi\\Desktop\\Python\GetHup\bank_info.txt"
    found = False
    with open(path, "r") as f:
        #lines = f.readlines()
        for line in f: 
            data = line.strip().split(",")
            if data [0] == str(accountNo):
                #print("The balance is : ", data[5])
                print("Bebug: ", line)
                found = True
                break
    if not found:
        print("Account not found.")

#------Main--------

loop = True
while loop:
    display_List()
    try: 
        selectNum = int(input("Enter your choice: "))
    except ValueError:
        print("Please enter a number ")
        continue

    match selectNum:
        case 1: #create account
            AccountNo = input("Enter Account No. : ")
            Fname = input("Enter First Name : ")
            Lname = input("Enter Last Name : ")
            Phone = input("Enter Phone Number : ")
            email = input("Enter email : ")
            Balance = float(input("Enter initial Balance : "))
            account1 = account_info(AccountNo, Fname, Lname, Phone, email, Balance)
            account1.create_account()
            account1.desiplay()
            print("Account created successfuly.")

        case 2: #despite
            AccountNo = int(input("Enter Account No "))
            despite_amount = float(input("Enter a despite amount "))
            account2 = account_info("","","","","","")
            account2.despite(AccountNo, despite_amount)
            print("Despite completed successfuly.")
            

        case 3: #withdraw 
            AccountNo = int(input("Enter Account No "))
            withdraw_amount = float(input("Enter a withdraw amount "))
            account3 = account_info("","","","","","")
            account3.withdraw(AccountNo, withdraw_amount)
            print("Withdraw completed successfuly.")

        case 4: #transfer
            AccountNo1 = input("Enter Account No 1: ")
            AccountNo2 = input("Enter Account No 2: ")
            transfer_amount = float(input("Enter a transfer amount "))
            account1 = account_info("","","","","","")
            account2 = account_info("","","","","","") 
             #print("the Account : ", repr(AccountNo))
            account1.withdraw(AccountNo1, transfer_amount)
            account2.despite(AccountNo2, transfer_amount)
           # transfer(AccountNo, AccountNo2)

        case 5: #balance 
            AccountNo = input("Enter Account No ")
            #print("the Account : ", repr(AccountNo))
            show_balance(AccountNo)

        case 6: # Show account information
            AccountNo = input("Enter Account No ")
            print("the Account : ", repr(AccountNo))
            show_Account(AccountNo)
    
        case 7:  #delete
            print("Enter Account No to delete it ")
            AccountNo = input()
            account5 = account_info("","","","","","")
            account5.delete_Account(AccountNo)
            print("Account deleted successfuly.")
    
       
        case 0:  
            print("Program Ended.")  
            break
        case _:
            print("Error, The Number is not from the list")

    print("do you want to select another choice : just type 1 for Yes or 0 for No")
    Choise = int(input())
    if Choise == 0:
        loop = False
        print("Program Ended.")


