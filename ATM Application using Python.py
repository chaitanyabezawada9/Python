class Bank:
    balance = 10000

    def login(self, pin):
        if pin == 9999:
            return True
        else:
            return False

    def credit(self, amount):
        self.balance += amount

    def debit(self, amount):
        self.balance -= amount

    def display(self):
        print("Current Balance is:", self.balance)


obj = Bank()
flag = False

for i in range(1, 4):
    if obj.login(int(input('Enter PIN Code: '))):
        flag = True
        break
    else:
        print("Invalid PIN, try again.")

if flag:
    while True:
        o = input("""
                     Press c for credit
                     Press d for debit
                     Press b for balance
                     Press e for exit""")
        if o.lower() == 'c':
            obj.credit(int(input('Enter the Amount: ')))
            print('After credit, total Amount is:')
            obj.display()

        elif o.lower() == 'd':
            amount = int(input('Enter the Amount: '))
            if amount < obj.balance:
                obj.debit(amount)
                print('After debit, total Amount is:')
                obj.display()
            else:
                print('Insufficient Balance')
                obj.display()

        elif o.lower() == 'b':
            print('Total Balance is:')
            obj.display()

        elif o.lower() == 'e':
            exit(0)
else:
    print("Your PIN Code attempts have been finished.")

