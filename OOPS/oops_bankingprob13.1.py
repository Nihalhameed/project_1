class Banking:
    bank_name='Sbi'
    acc_no=123456

    def account(self,fname,lname):
        self.fname=fname
        self.lname=lname
        self.min_bal=5000
        self.total_bal=self.min_bal #setting this variable without mentioning it in arguments since min_bal has a value
    def deposit(self,amount):
        self.amount=amount
        self.total_bal+=self.amount
        print("Your", Banking.bank_name, "account has been creditted with:", self.amount,"Your total balance is",self.total_bal)
    def withdraw(self,cash):
        self.cash=cash
        if self.cash > self.total_bal:
            print("Insufficient balance")
        else:
            self.total_bal-=self.cash
            print("Your", Banking.bank_name, "account has been debitted with:",self.cash,"Your total balance is",self.total_bal)
person=Banking()
person.account('varun','k')
person.deposit(15000)
person.withdraw(5000)
