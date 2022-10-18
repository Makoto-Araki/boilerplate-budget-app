'''
Class - Category
'''

class Category:
    
    '''
    Attributes
    '''
    
    name = ''
    ledger = list()
    
    '''
    Constructor
    '''
    
    def __init__(self, name):
        self.name = name
    
    '''
    Method - deposit
    '''
    
    def deposit(self, amount, description):
        self.ledger.append({'amount': amount, 'description': description})
    
    '''
    Method - withdraw
    '''
    
    def withdraw(self, amount, *description):
        if self.ledger[0]['amount'] >= amount:
            if amount > 0:
                amount = amount - amount * 2
            if len(description) > 0:
                self.ledger.append({'amount': amount, 'description': description})
            else:
                self.ledger.append({'amount': amount, 'description': ''})
            return True
        else:
            return False
    
    '''
    Method - get_balance
    '''
    
    def get_balance(self):
        
        '''
        Calculate the number of title padding
        '''
        
        padding_length = int((30 - len(self.name)) / 2)
        
        '''
        Assembling the title string
        '''
        
        if len(self.name) % 2 == 0:
            temp1 = '*' * padding_length
            temp2 = '*' * padding_length
            title = temp1 + self.name + temp2
        else:
            temp1 = '*' * padding_length
            temp2 = '*' * (padding_length + 1)
            title = temp1 + self.name + temp2
        
        '''
        Iterate over a list in an object
        '''
        
        for i in range(len(self.ledger)):
            description = self.ledger[i]['description']
            amount = self.ledger[i]['amount']
            print(description[0:24])
    
    '''
    Method - transfer
    '''
    
    def transfer(self, amount, instance):
        print('Hello World')
    
    '''
    Method - check_funds
    '''
    
    def check_funds(self, amount):
        print('Hello World')

'''
Unknown
'''

def create_spend_chart(categories):
  print(categories)