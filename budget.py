import math

class Category:
    
    def __init__(self, name):
        self.name = name
        self.ledger = list()

    def __str__(self):
        self.get_balance()
    
    def deposit(self, amount, description = ''):
        self.ledger.append({'amount': amount, 'description': description})
    
    def withdraw(self, amount, description = ''):
        if not self.check_funds(amount):
            return False
        else:
            if amount > 0: amount = amount * -1
            self.ledger.append({'amount': amount, 'description': description})
            return True
    
    def get_balance(self):
        return_str = ''
        padding_length = int((30 - len(self.name)) / 2)
        if len(self.name) % 2 == 0:
            temp1 = '*' * padding_length
            temp2 = '*' * padding_length
            return_str += temp1 + self.name + temp2 + '\n'
        else:
            temp1 = '*' * padding_length
            temp2 = '*' * (padding_length + 1)
            return_str += temp1 + self.name + temp2 + '\n'
        
        total = 0
        for item in self.ledger:
            temp3 = item['description'][0:23].ljust(23, ' ') if item['description'] != '' else ' ' * 23
            temp4 = str('{:6.2f}'.format(item['amount'])).rjust(7, ' ')
            total += item['amount']
            return_str += temp3 + temp4 + '\n'
            
        total_str = str('{:6.2f}'.format(total))
        return_str += 'Total: ' + total_str + '\n'
        return return_str
        
    def transfer(self, amount, Instance):
        if not self.check_funds(amount):
            return False
        else:
            self.withdraw(amount, 'Transfer to ' + Instance.name)
            Instance.deposit(amount, 'Transfer from ' + self.name)
            return True
    
    def check_funds(self, amount):
        total = 0
        for item in self.ledger:
            total += item['amount']
        if total < amount:
            return False
        else:
            return True

def create_spend_chart(categories):
    spent = list()
    total = 0
    if len(categories) <= 4:
        for instance in categories:
            sum = 0
            for item in instance.ledger:
                if item['amount'] < 0: sum += item['amount'] * -1
            spent.append({'name': instance.name, 'spent': sum})
            total += sum
        for item in spent:
            item['percentage'] = math.floor((item['spent'] / total * 100) / 10)
            del item['spent']
        
        # Title
        return_str = ''
        return_str += 'Percentage spent by category' + '\n'
        
        # Y-Axis & chart data
        for val in [100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 0]:
            return_str += str(val).rjust(3, ' ') + '|'
            for item in spent:
                if item['percentage'] * 10 >= val: return_str += ' o '
            return_str += '\n'
        
        # X-Axis
        return_str += ' ' * 4
        for val in range(len(spent)):
            return_str += '---'
        return_str += '-\n'
        
        return return_str