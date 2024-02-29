#author: Jay Sanders
#class: CS 325
#due: 2024-03-01

class Order_Info:
    def __init__(self, name, email, address, items):
        self.nameVal = name
        self.emailVal = email
        self.addressVal = address
        self.itemsVal = items
    @property
    def name(self):
        return self.nameVal
    @name.setter
    def name(self, newName):
        self.nameVal = newName
    @property
    def email(self):
        return self.emailVal
    @email.setter
    def email(self, newEmail):
        self.emailVal = newEmail
    @property
    def address(self):
        return self.addressVal
    @address.setter
    def address(self, newAddress):
        self.addressVal = newAddress
    @property
    def items(self):
        return self.itemsVal
    @items.setter
    def items(self, newItems):
        self.itemsVal = newItems
class Cost_Calculator:
    def __init__(self, taxRate, discount, items):
        self.taxVal = taxRate
        self.discVal = discount
    def total(self, order):
        total = sum(item[1] for item in order)
        return (total * (1 - self.discVal)) * self.taxVal
class Order_Validate:
    def __init__(self, customerInfo : Order_Info, inventory):
        self.items = customerInfo.items
        self.isValid = True
        self.inventoryVal = inventory
    def validate(self):
        #checking if inventory is there to fulfil order
        return self.isValid

class Confirmation:
    def __init__(self, customerInfo : Order_Info):
        self.email = customerInfo.emailVal
        self.items = customerInfo.itemsVal
        self.name = customerInfo.nameVal
    def sendEmail(self, cost):
        print(f"To: {self.email}\n\nDear {self.name},\n\n Your order of {self.items} totaling {cost} has been shipped")#this would be implented with the smtblib library
class Inventory:
    def __init__(self, customerInfo : Order_Info, inventory):
        self.items = customerInfo.items
        self.inventoryVal = inventory
    def updateInventory(self):
        for item in self.items:
            print("updating inventory")

def main():
    items = ["shirt", "shirt", "pants"]
    person1 = Order_Info("John Jones", "johnpjones@gmail.com", "123 main st townville, IL", items)
    inventory = [("shirt", 5), ("pants", 10)]
    cost = Cost_Calculator(0.10, 0.05, items)
    validate = Order_Validate(person1, inventory)
    if validate.validate():
        confirm = Confirmation(person1)
        confirm.sendEmail(cost)
        invUpdate = Inventory(person1, inventory)
        invUpdate.updateInventory()
        print("Order confirmation sent")
    else:
        print("Order confirmation not sent")

if __name__ == "__main__":
    main()