"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    def __init__(self, name, commission_type, contract, salary):
        self.name = name
        self.commission_type = commission_type
        self.contract = contract
        self.salary = salary
        self.hours = 0
        self.comission_contracts = 0
        self.contract_fee = 0
        self.bonus = 0

    def get_pay(self):
        if(self.contract == "monthly"):
            pay = self.salary
        elif(self.contract == "hourly"):
            pay = self.salary * self.hours
        if(self.commission_type):
            if(self.commission_type == "contract"):
                pay += self.commission_contracts * self.contract_fee
            elif(self.commission_type == "bonus"):
                pay += self.bonus
        return pay

    def __str__(self):
        line = self.name + " works on a"
        if(self.contract == "monthly"):
            line += " monthly salary of " + str(self.salary)
        elif(self.contract == "hourly"):
            line += " contract of " + str(self.hours) + " hours at " + str(self.salary) + "/hour"
        if(self.commission_type):
            if(self.commission_type == "contract"):
                line += " and receives a commission for " + str(self.commission_contracts) + "contract(s) at " + str(self.contract_fee) + "/contract"
            elif(self.commission_type == "bonus"):
                line += "and receives a bonus commission of " + str(self.bonus)
        line += ". "
        line += " Their total pay is " + str(self.get_pay())
        return line


# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie', "", "monthly", 4000)

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie', "", "hourly", 25)
charlie.hours = 100

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee', "contract", "monthly", 3000)
renee.commission_contracts = 4
renee.contract_fee = 200

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan', "contract", "hourly", 25)
jan.hours = 150
jan.commission_contracts = 3
jan.contract_fee = 220

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie', "bonus", "monthly", 2000)
robbie.bonus = 1500

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel', "bonus", "hourly", 30)
ariel.hours = 120
ariel.bonus = 600

print(f"billie {str(billie)}")
print(f"charlie {str(charlie)}")
print(f"renee {str(renee)}")
print(f"jan {str(jan)}")
print(f"robbie {str(robbie)}")
print(f"ariel {str(ariel)}")
