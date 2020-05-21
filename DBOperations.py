import sqlite3

def init():
    db=sqlite3.connect("bank.db")
    c=db.cursor()
    c.execute("""
    CREATE TABLE IF NOT EXISTS account(
        accno INTEGER PRIMARY KEY,
        cname VARCHAR(30),
        bal numeric(12,2)
    )
    """)
    db.close()

def account_open(accno,cname,bal):
    db=sqlite3.connect("bank.db")
    c=db.cursor()
    c.execute(f"INSERT INTO account VALUES({accno},'{cname}',{bal})")
    db.commit()
    db.close()
    print("Account Opened Successfully...!!")

def verifyaccount(accno):
    db = sqlite3.connect("bank.db")
    c = db.cursor()
    c.execute(f"select * from account where accno={accno}")
    result=c.fetchone()
    db.close()
    return result

def deposit(amt,accno):
    db=sqlite3.connect("bank.db")
    c=db.cursor()
    c.execute(f"update account set bal=bal+{amt} where accno={accno}")
    db.commit()
    db.close()
    print("Amount Deposited..!!")

def withdraw(amt,accno):
    db = sqlite3.connect("bank.db")
    c = db.cursor()
    c.execute(f"update account set bal=bal-{amt} where accno={accno}")
    db.commit()
    db.close()
    print("Amount Withdrawn successfully..!!")


def list_all():
    db = sqlite3.connect("bank.db")
    c = db.cursor()
    c.execute("SELECT * FROM account")
    data=c.fetchall()
    db.close()
    return data

if __name__=="__main__":
    init()