class Budget:

    def __init__(self,category, amount):
        self.category = category
        self.amount = amount
        
    #methods
    def deposit(self):
            deposit = float(input('Enter deposit amount: '))
            self.amount += deposit
            return f'Depost Successfull'
            

    def withdrawal(self):
        withdraw = float(input('Enter amount to withdraw:'))
        if self.amount >= withdraw:
            self.amount -= withdraw
            return f'Withdraw is successfull'
        else:
            print('Insufficient balance')
            return f'Choose a different amount'


    def transfer(self):
        transfer = float(input('Enter amount to transfer '))
        if self.amount >= transfer:
            self.amount -= transfer
            return f'Your transfer is  successfull'
        else:
            print('Insufficient balance ')
            return f'Choose a different amount'

    
    def  check_balance(self):
        return f'\n Your curent balance is {self.amount}'
              

# creating objects of class
category = Budget('Food', 2000)
category_1 = Budget('clothing', 5000)
category_2 = Budget('Entertainment', 7000) 

# Calling methods with class objects
print('****** Food Category ******')
print(category.deposit())
print(category.withdrawal())
print(category.transfer())
print(category.check_balance())


print('****** Clothing Category ******')
print(category_1.deposit())
print(category_1.withdrawal())
print(category_1.transfer())
print(category_1.check_balance())


print('****** Entertainment Category ******')
print(category_2.deposit())
print(category_2.withdrawal())
print(category_2.transfer())
print(category_2.check_balance())