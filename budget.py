'''
Class - Category
'''

class Category:
    
    '''
    Class Attributes
    '''
    
    name = ''
    ledger = list()
    
    '''
    Class Constructor
    '''
    
    def __init__(self, name):
        self.name = name
    
    '''
    Class Method - deposit
    '''
    
    def deposit(self, amount, *description):
        
        '''
        Change registration object with variable parameters
        '''
        
        if len(description) > 0:
            self.ledger.append({'amount': amount, 'description': description})
        else:
            self.ledger.append({'amount': amount})
    
    '''
    Class Method - withdraw
    '''
    
    def withdraw(self, amount, *description):
        
        '''
        Check if withdrawal is possible
        '''
        
        if not self.check_funds(amount):
            return False
        else:
            
            '''
            If amount is positive, convert to negative
            '''
            
            if amount > 0:
                amount = amount - amount * 2
            
            '''
            Change registration object with variable parameters
            '''
            
            if len(description) > 0:
                self.ledger.append({'amount': amount, 'description': description})
            else:
                self.ledger.append({'amount': amount})
            
            return True
    
    '''
    Class Method - get_balance
    '''
    
    def get_balance(self):
        
        '''
        Initialize the variables
        '''
        
        total = 0
        padding_length = int((30 - len(self.name)) / 2)
        
        '''
        Title
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
            
            if 'description' in self.ledger[i]:
                temp3 = self.ledger[i]['description'][0][0:23].ljust(23, ' ')
            else:
                temp3 = ' ' * 23
            #temp3 = self.ledger[i]['description']
            #if isinstance(temp3, str): temp3 = temp3[0:23].ljust(23, ' ')
            #if isinstance(temp3, tuple): temp3 = temp3[0][0:23].ljust(23, ' ')
            
            temp4 = self.ledger[i]['amount']
            temp4 = str('{:6.2f}'.format(temp4))
            temp4 = temp4.rjust(7, ' ')
            total += self.ledger[i]['amount']
            
            print(temp3 + temp4)
            
        '''
        Total
        '''
        
        total = str('{:6.2f}'.format(total))
        total = 'Total: ' + total
        print(total)
        
    '''
    Class Method - transfer
    '''
    
    def transfer(self, amount, Instance):
        
        '''
        Check if withdrawal is possible
        '''
        
        if not self.check_funds(amount):
            return False
        else:
            
            '''
            If amount is positive, convert to negative
            '''
            
            if amount > 0:
                amount = amount - amount * 2
            
            '''
            Withdraw executed
            '''
            
            self.ledger.append({'amount': amount, 'description': f'Transfer to {Instance.name}'})
            
            '''
            If amount is negative, convert to positive
            '''
            
            if amount < 0:
                amount = amount + amount * 2
            
            '''
            Destination category deposits
            '''
            
            Instance.deposit(amount, f'Transfer from {self.name}')
            
            '''
            Return value
            '''
            
            return True
    
    '''
    Method - check_funds
    '''
    
    def check_funds(self, amount):
        
        '''
        Totalling the category amount
        '''
        
        total = 0
        for i in range(len(self.ledger)):
            total += self.ledger[i]['amount']
        
        '''
        Check if withdrawal is possible
        '''
        
        if total < amount:
            return False
        else:
            return True

'''
Unknown
'''

def create_spend_chart(categories):
  print(categories)