class CoffeMakerMachine:

    menu = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}
    def __init__(self):
        self.money = 0
        self.resources = {
            "water" : 300,
            "milk" : 200,
            "coffee" : 100
        }
        
    def report(self):
        for i, (resource, amount) in enumerate(self.resources.items()):
            if resource == "water" or resource == "milk":
                print(f"{resource}: {amount} ml")
            elif resource == "coffee":
                print(f"{resource} : {amount} gm")    
        print(f"Money: ${self.money}")

    def check_resources(self,coffee_type):
        for i, (items,amount) in enumerate(self.menu[coffee_type]["ingredients"].items()):
            if self.resources[items] < amount:
                print(f"There is shortage!!")
                return False
        return True

    @staticmethod
    def check_cash(coffee_type):
            print(f"Cost of a {coffee_type} is ${CoffeMakerMachine.menu[coffee_type]['cost']}")
            print("insert cash : ")
            total = float(input("How many quarters? : ")) * 0.25
            total += float(input("How many dimes? : ")) * 0.10
            total += float(input("How many nickels? : ")) * 0.05
            total += float(input("How many pennies? : ")) * 0.01
            return total

    def transaction(self,drink, inserted_amount):
        if inserted_amount < CoffeMakerMachine.menu[drink]["cost"]:
            print("amount not sufficient to but the selected drink, your money is refunded")
            return False
        else:
            change = round(inserted_amount - CoffeMakerMachine.menu[drink]["cost"], 1)
            print(f"Here is your change : ${change}")
            self.money += CoffeMakerMachine.menu[drink]['cost']
            return True

    def make_coffee(self,coffee_type):
        for i, (items,amount) in enumerate(CoffeMakerMachine.menu[coffee_type]["ingredients"].items()):
            self.resources[items] -= amount
        print(f"Enjoy your {coffee_type} !!!!")

    def coffee_maker(self):
        while True:
            user_input = input("What would you like to have? (espresso/latte/cappuccino): ")

            if user_input == "report":
                self.report()
                
            elif user_input == "off":
                print("coffee maker machine is shutting off")
                break
            
            elif user_input in self.menu:
                if self.check_resources(user_input):
                    amt_paid = CoffeMakerMachine.check_cash(user_input)
                    if self.transaction(user_input, amt_paid):
                        self.make_coffee(user_input)
            else:
                print(f"Sorry, your choice {user_input} is not in options of drinks we can make")

if __name__ == "__main__":
    coffee_maker = CoffeMakerMachine()
    coffee_maker.coffee_maker()
