import sqlite3 
from decimal import Decimal, InvalidOperation

DB_NAME = "BankDB.dh"

#---------------------Main Create DB-----------------------------
def createDB():
    conn = sqlite3.connect(DB_NAME)  #Connection and create 
    cursor = conn.cursor() # to execute DB

#create BankInfo Table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS BankInfo (
        id INTEGER PRIMARY KEY AUTOINCREMENT, 
        UserName TEXT NOT NULL,
        Password TEXT NOT NULL,
        Fname TEXT NOT NULL,
        Lname Text NOT NULL,
        Phone Text NOT NULL,
        email Text NOT NULL,
        JobTitle Text NOT NULL,
        Balance Float NOT NULL DEFUALT 0 )
        """)

    print("Database created successfully")


#---------------Create Account---------------

def CreateAccountDB(UserName, Password, Fname, Lname, Phone, email, JobTitle, Balance):

    try:
        balance = Decimal(str(Balance))

        if not balance.is_finite() or balance < 0:
            print("Invalid initial balance")
            return False

        if balance != balance.quantize(Decimal("0.01")):
            print("Balance must have at most 2 decimal places")
            return False

    except (InvalidOperation, ValueError, TypeError):
        print("Invalid balance")
        return False

    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()

        # Lock before checking for duplicate accounts
        cursor.execute("BEGIN IMMEDIATE")

        sql = """
        SELECT UserName, email 
        FROM BankInfo 
        WHERE UserName = ? OR email = ?
        """
        val = (UserName, email)
        cursor.execute (sql, val)
        account = cursor.fetchone()
        if account:
            print("Account already exist")
            return False
    
        sql = """
            INSERT INTO BankInfo
            (UserName, Password, Fname, Lname,
             Phone, email, JobTitle, Balance)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """

        val = (UserName, Password, Fname, Lname,
               Phone, email, JobTitle, float(balance))

        cursor.execute(sql, val)
    print("Account Information added successfully")

    return True

#---------------Log In---------------
def LogIn(UserName, Password):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor() 
    sql = """
    SELECT UserName, Password 
    FROM BankInfo 
    WHERE UserName = ? AND Password = ?
    """
    val = (UserName, Password)
    cursor.execute (sql, val)
    account = cursor.fetchone()
    if account:
        print("Login successful")
        return True
    else:
        print("Invalid username or password or Account is not available")
        return False

    
#---------------Show Account Detials---------------
def Show_DetialsDB():
    conn = sqlite3.connect("BankDB.dh")
    cursor = conn.cursor() 
    cursor.execute("SELECT * FROM BankInfo")
    accounts = cursor.fetchall()
    if accounts:
        for account in accounts:
            print(account)
    else:
        print("No accounts found")
    
    
    return accounts


#---------------Show Balance---------------
def Show_BalanceDB(UserName):
    conn = sqlite3.connect("BankDB.dh")
    cursor = conn.cursor() 
    sql = """
    SELECT Balance
        FROM BankInfo 
        WHERE UserName = ? 
        """
    val = (UserName, )
    cursor.execute (sql, val)
    result = cursor.fetchone()
    
    if result:
        print("Account Balance: ", result[0])
        return result[0]
            
    else:
        print("Account not foun")
           
        return None

#---------------Show Profile---------------
def Show_Profile(UserName):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor() 
    sql = """
    SELECT * FROM BankInfo
    WHERE UserName = ? 
    """
    val = (UserName, )
    cursor.execute(sql, val)
    account = cursor.fetchone()

    if account:
        print("Account:", account)
    else:
        print("Account not found")
    return account
#---------------Update Profile---------------
def Update_profile(UserName, Fname, Lname, Phone, email, Job):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor() 
    # Check if the email belongs to another account
    cursor.execute("BEGIN IMMEDIATE")
    cursor.execute("""
            SELECT id FROM BankInfo
            WHERE email = ? AND UserName != ?
        """, (email, UserName))

    if cursor.fetchone():
        print("Email already used by another account")
        return False
    
    sql = """UPDATE BankInfo 
          SET Fname = ?, 
            Lname = ?, 
            Phone = ?, 
            email = ?, 
            JobTitle = ? 
        WHERE UserName = ?"""
    val = (Fname, Lname, Phone, email, Job, UserName)
    cursor.execute (sql, val)

    updated = cursor.rowcount

    if updated > 0:
        print("Profile updated successfully")
        return True

    print("Account not found")
    return False

#---------------Transfer ---------------
def Transfer (UserName, id, amount):

    try:
        amount = Decimal(str(amount))

        if not amount.is_finite() or amount <= 0:
            print("Transfer amount must be greater than zero")
            return False

        if amount != amount.quantize(Decimal("0.01")):
            print("Amount must have at most 2 decimal places")
            return False

    except (InvalidOperation, ValueError, TypeError):
        print("Invalid transfer amount")
        return False

    try:
        with sqlite3.connect(DB_NAME) as conn:
            cursor = conn.cursor()

            # Lock database for safe transfer
            cursor.execute("BEGIN IMMEDIATE")

            # 1) Get sender account
            cursor.execute("""
                SELECT id, Balance
                FROM BankInfo
                WHERE UserName = ?
            """, (UserName,))

            sender = cursor.fetchone()

            if sender is None:
                print("Failed: Sender not found")
                return False

            sender_id = sender[0]
            sender_balance = Decimal(str(sender[1]))

            # 2) Get receiver account
            cursor.execute("""
                SELECT id, Balance
                FROM BankInfo
                WHERE id = ?
            """, (id,))

            receiver = cursor.fetchone()

            if receiver is None:
                print("Failed: Receiver not found")
                return False

            receiver_balance = Decimal(str(receiver[1]))

            # 3) Prevent transfer to same account
            if sender_id == receiver[0]:
                print("Cannot transfer to your own account")
                return False

            # 4) Check sender balance
            if sender_balance < amount:
                print("Failed: Insufficient balance")
                return False

            # 5) Calculate new balances
            new_sender_balance = sender_balance - amount
            new_receiver_balance = receiver_balance + amount

            # 6) Update sender
            cursor.execute("""
                UPDATE BankInfo
                SET Balance = ?
                WHERE id = ?
            """, (float(new_sender_balance), sender_id))

            # 7) Update receiver
            cursor.execute("""
                UPDATE BankInfo
                SET Balance = ?
                WHERE id = ?
            """, (float(new_receiver_balance), id))

            # Connection context commits both changes together

        print("Transfer successful")
        print("Amount transferred:", amount)
        print("New sender balance:", new_sender_balance)
        print("New receiver balance:", new_receiver_balance)

        return True

    except sqlite3.Error as error:
        print("Transfer failed:", error)
        return False

#---------------------------------------------

if __name__ == " __main__":
    createDB()