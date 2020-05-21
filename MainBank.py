import MySQLDBOperations as bank

while True:
    print("""
    Select Operation
    1. Account Open
    2. Deposit
    3. Withdraw
    4. Balance Enquiry
    5. List All Accounts
    6. Exit
    """)
    n=int(input("Enter choice here "))

    if n==1:
        accno=input("Enter account no ")
        cname=input("Enter customer name ")
        bal=int(input("Enter Opening Balance "))
        bank.account_open(accno,cname,bal)
    elif n==2:
        accno=input("Enter account number ")
        details = bank.verifyaccount(accno)
        if details is None:
            print("Invalid account number")
        else:
            amt=int(input("Enter amount to deposit : "))
            bank.deposit(amt,accno)

    elif n==3:
        accno = input("Enter account number ")
        details = bank.verifyaccount(accno)
        if details is None:
            print("Invalid account number")
        else:
            amt = int(input("Enter amount to withdraw : "))
            bank.withdraw(amt, accno)
    elif n==4:
        accno = input("Enter account number ")
        result=bank.verifyaccount(accno)
        if result is None:
            print("Invalid account number")
        else:
            accno,cname,bal=result
            print(f"Customer Name {cname}")
            print(f"Available Balance Rs.{bal}")


    elif n==5:
        data=bank.list_all()
        for account in data:
            print(account)

    elif n==6:
        break
    else:
        print("Invalid choice")