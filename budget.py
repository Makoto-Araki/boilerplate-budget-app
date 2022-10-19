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
        Initialize the variable
        '''
        
        total = 0
        
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
        else:
            temp1 = '*' * padding_length
            temp2 = '*' * (padding_length + 1)
        
        print(temp1 + self.name + temp2)
        
        '''
        Iterate over a list in an object
        '''
        
        for i in range(len(self.ledger)):
            
            '''
            Description + Amount
            '''
            
            temp3 = self.ledger[i]['description']
            if isinstance(temp3, str): temp3 = temp3[0:23].ljust(23, ' ')
            if isinstance(temp3, tuple): temp3 = temp3[0][0:23].ljust(23, ' ')
            
            temp4 = self.ledger[i]['amount']
            temp4 = str('{:6.2f}'.format(temp4))
            temp4 = temp4.rjust(7, ' ')
            
            print(temp3 + temp4)
            
            '''
            Calculate Total
            '''
            
            total += self.ledger[i]['amount']
            
        '''
        Display Total
        '''
        
        total = str('{:6.2f}'.format(total))
        total = 'Total: ' + total
        print(total)
        
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