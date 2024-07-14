import copy
l=[]
acc_no=1
class bank:
    def __init__(self):
        global acc_no
        print("Please Enter the account details")
        print("Enter The Account Holder Name:")
        name=input()
        print("Enter The Accunt Type:")
        typ=input()
        print("Enter The Amount For Initial deposit")
        amt=int(input())
        self.ac_name=name
        self.ac_type=typ
        self.ac_amt=amt
        self.acc_no=acc_no
        acc_no+=1
        print("Account Sucessfully created")
    def display(self):
        print("The Account Details")
        print("Account Number:",self.acc_no)
        print("Account Name:",self.ac_name)
        print("Account Type:",self.ac_type)
        print("Account Balance:",self.ac_amt)
    def deposit(self):
        print("Enter the Amount to Deposit:")
        n=int(input())
        if(n<0):
            print("Enter the valid number")
        else:
            self.ac_amt+=n
    def withdraw(self):
        print("Enter the amount to Withdraw")
        m=int(input())
        if(self.ac_amt>=m):
            self.ac_amt-=m
            print("Amount Successfully Debited")
        else:
            print("Insufficient Balance")
print("0- For create the Accoount")
print("1- For display the account detail")
print("2- For deposit amount")
print("3- For withdraw the money")
print("4- exit")
while(True):
    print("Enter the choice:")
    c=int(input())
    if(c==4):
        break
    if(c==0):
        x=bank()
        l.append(x)
    else:
        id=int(input("Enter Your Account number:"))
        for i in l:
            if(i.acc_no==id):
                if(c==1):
                    i.display()
                elif(c==2):
                    i.deposit()
                elif(c==3):
                    i.withdraw()
                break
        else:
            print("Account no  not found--")
        


