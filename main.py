# This entrypoint file to be used in development. Start by reading README.md
import budget
from budget import create_spend_chart
from unittest import main

food = budget.Category("Food")
food.deposit(1000, "initial deposit")
food.withdraw(10.15, "groceries")
food.withdraw(15.89, "restaurant and more food for dessert")
clothing = budget.Category("Clothing")
clothing.deposit(1000, "initial deposit")
food.transfer(50, clothing)
clothing.withdraw(25.55, 'Others')
clothing.withdraw(100, 'Others')
clothing.transfer(250, food)
auto = budget.Category("Auto")
auto.deposit(1000, "initial deposit")
food.transfer(50, auto)
auto.withdraw(15, 'vehicles')
auto.withdraw(45.25, 'airplanes')
auto.withdraw(450, 'Others')
print(food.get_balance())
print(clothing.get_balance())
print(auto.get_balance())

#print(create_spend_chart([food, clothing, auto]))

# Run unit tests automatically
#main(module='test_module', exit=False)