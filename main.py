# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

class CustomerType:
    def __init__(self, bags: list, population: int, name:str):
        self.bags = bags
        self.bag_people = {}
        self.name = name

        for bag in bags:
            self.bag_people[bag] = 0

        self.population = population

    def pick_bag(self, bag):
        bag.pick()
        self.population -= 1
        self.bag_people[bag] += 1

    def unpick_bag(self, bag):
        bag.unpick()
        self.population += 1
        self.bag_people[bag] -= 1

    def print_assignments(self):
        print(f" For customer type: {self.name}")
        for bag in self.bag_people:
            print(f"We have assigned {self.bag_people[bag]} people in {bag.name}")


class Bag:
    def __init__(self, lollies: list, name:str):
        self.lollies = lollies
        self.name = name

    def pick(self):
        for lolly in self.lollies:
            lolly.quantity -= 1

    def check_if_empty(self):
        for lolly in self.lollies:
            if lolly.quantity < 1:
                return True
            else:
                return False

    def unpick(self):
        for lolly in self.lollies:
            lolly.quantity += 1


class Lolly:
    def __init__(self, quantity: int):
        self.quantity = quantity


def MBR(CustomerTypes) -> CustomerType:
    if len(CustomerTypes) == 0:
        return False
    min_customer_type = CustomerTypes[0]

    for CustomerType in CustomerTypes:
        if len(CustomerType.bags) < len(min_customer_type.bags):
            min_customer_type = CustomerType

    return min_customer_type


apple = Lolly(10)
strawberry = Lolly(7)

justApple = Bag([apple],"just apple")
appleStraw = Bag([apple, strawberry], "apple and strawberry")

CustomerType1 = CustomerType([justApple, appleStraw], 5, "Strawberry and apple or plain apple.")
CustomerType2 = CustomerType([appleStraw], 5, "Strawberry and apple only.")

completely_all_customers = [CustomerType1,CustomerType2]
allCustomers = [CustomerType1, CustomerType2]


def bag_assigner(all_customers):
    min_customer_type = MBR(all_customers)
    if not min_customer_type:
        print("Solution:")
        for CustomerType in completely_all_customers:
            CustomerType.print_assignments()
        print("End solution")
        return

    if min_customer_type.population == 0:
        all_customers.remove(min_customer_type)
        bag_assigner(all_customers)
        all_customers.append(min_customer_type)
        return

    for bag in min_customer_type.bags:
        if not bag.check_if_empty():
            min_customer_type.pick_bag(bag)
            bag_assigner(all_customers)
            min_customer_type.unpick_bag(bag)
    return


bag_assigner(allCustomers)
