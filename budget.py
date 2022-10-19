'''
Class - Category
'''

class Category:
    
    '''
    Class Constructor
    '''
    
    def __init__(self, name):
        self.name = name
        self.ledger = list()
    
    '''
    Class Method - deposit
    '''
    
    def deposit(self, amount, *description):
        
        '''
        Change object with variable parameters
        '''
        
        if len(description) > 0:
            if isinstance(description, tuple):
                self.ledger.append({'amount': amount, 'description': description[0]})
            elif isinstance(description, str):
                self.ledger.append({'amount': amount, 'description': description})
        else:
            self.ledger.append({'amount': amount, 'description': ''})
    
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
            #print(self.ledger[i])
            if isinstance(self.ledger[i]['description'], tuple):
                temp3 = self.ledger[i]['description'][0][0:23].ljust(23, ' ')
            elif isinstance(self.ledger[i]['description'], str):
                temp3 = self.ledger[i]['description'][0:23].ljust(23, ' ')
            elif 'description' in self.ledger[i]:
                temp3 = ' ' * 23
            
            temp4 = self.ledger[i]['amount']
            temp4 = str('{:6.2f}'.format(temp4))
            temp4 = temp4.rjust(7, ' ')
            total += self.ledger[i]['amount']
            
            print(temp3 + temp4)
            
        '''
        Total
        '''
        
        total_str = str('{:6.2f}'.format(total))
        print('Total: ' + total_str)
        
        '''
        Return value
        '''
        
        return total
        
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
            Withdraw executed
            '''
            
            self.withdraw(amount, 'Transfer to ' + Instance.name)
            
            '''
            Destination category deposits
            '''
            
            Instance.deposit(amount, 'Transfer from ' + self.name)
            
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