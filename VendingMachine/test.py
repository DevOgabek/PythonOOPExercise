from beverage import Beverage
from vending_machine import VendingMachine

coca_cola = Beverage("Coca Cola", 3200)
suv = Beverage("Suv", 1000)
pepsi = Beverage("Pepsi", 2500)

# Creating vending machine object
vending_machine = VendingMachine()

# Adding beverages to the vending machine
vending_machine.addBeverage(coca_cola)
vending_machine.addBeverage(suv)
vending_machine.addBeverage(pepsi)

# Recharging cards
vending_machine.rechargeCard(12, 12000)
vending_machine.rechargeCard(21, 5600)
vending_machine.rechargeCard(99, 15800)

# Refilling columns
vending_machine.refillColumn(1, "Coca Cola", 1)
vending_machine.refillColumn(2, "Suv", 10)
vending_machine.refillColumn(3, "Pepsi", 15)
vending_machine.refillColumn(4, "Suv", 20)

# Selling a beverage
result = vending_machine.sell("Coca Cola", 12)
print("Sold from column number:", result)
print("Remaining credit on card 12:", vending_machine.getCredit(12))
print("Remaining quantity of Coca Cola in the machine:", vending_machine.availableCans("Coca Cola"))