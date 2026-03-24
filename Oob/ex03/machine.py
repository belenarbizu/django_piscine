from beverages import *
import random


class CoffeeMachine:
    def __init__(self):
        self.count = 0


    def repair(self):
        self.count = 0


    def serve(self, beverage):
        if self.count > 9:
            raise self.BrokenMachineException()        

        self.count += 1
        
        if random.randint(0, 4) == 0:
            return self.EmptyCup()

        return beverage()


    class EmptyCup(HotBeverage):
        def __init__(self, price=0.90, name="empty cup"):
            super().__init__(price, name)


        def description(self):
            return "An empty cup?! Gimme my money back!"


    class BrokenMachineException(Exception):
        def __init__(self):
            super().__init__("This coffee machine has to be repaired.")


if __name__ == "__main__":
    machine = CoffeeMachine()
    beverages = [HotBeverage, Coffee, Tea, Chocolate, Cappuccino]
    for i in range(11):
        try:
            print(machine.serve(beverages[random.randint(0, 4)]))
        except Exception as e:
            print(e)
            machine.repair()
    for i in range(11):
        try:
            print(machine.serve(beverages[random.randint(0, 4)]))
        except Exception as e:
            print(e)