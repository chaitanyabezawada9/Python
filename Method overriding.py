class Customer:
    def __init__(self, name):
        self.name = name

    def get_discount(self, total_amount):
        discount = total_amount * 0.05  # Assuming regular customers get 5%
        print(self.name, "gets a discount of", discount)

class Premium_customer(Customer):  # Use correct base class name
    def get_discount(self, total_amount):
        discount = total_amount * 0.10  # Premium customers get 10%
        print(self.name, "gets a discount of", discount)

# Creating instances with correct class names
regular_customer = Customer("Chinnu")
premium_customer = Premium_customer("Amul")

# Calling methods
regular_customer.get_discount(2000)
premium_customer.get_discount(2000)

#Output:
#       Chinnu gets a discount of 100.0
#       Amul gets a discount of 200.0
