#Banking problem :

#Cash withdrawal ===> message

#deposit ===> message

#Solution : 3 methods :

#1. Account() :fname,lname,min=total_balance
#2. Deposit() === Your account has been credited wtih cash
#3. Withdraw() - Your account has been debitted with cash
class Banking:
    bank_name='Sbi'

    def account(self,acc_no,fname,lname,min_bal):
        self.acc_no=acc_no
        self.fname=fname
        self.lname=lname
        self.min_bal=min_bal

    def deposit(self,amount):
        self.amount=amount
        print("Your",Banking.bank_name,"account has been creditted with:",self.amount)
        print("Your total balance is: ",self.amount+self.min_bal)
    def withdraw(self,amount2):
        self.amount2=amount2
        if self.amount2 >= self.min_bal:
            print("Your account has got debitted with : ", self.amount2)
            print("Your total balance is: ",self.amount2+self.min_bal )
        else:
            print("Insufficient funds")


person=Banking()
person.account('1234','nihal','h',5000)
choice=int(input("Enter your choice:\n1.Deposit\n2.Withdrawal\n"))
print()
person.withdraw(6000)




























































