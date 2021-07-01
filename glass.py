# Write a Python class that defines a water glass
# When you make an instance of WaterGlass you input how full the glass is
# You can refill the glass. If you refill a full glass let the user know the glass has overflowed.
# You can take a sip of the water
# You can pour out the glass
# tTe glass can tell you how full it is
# Write some Driver code that makes a new water glass and utilizes all the methods.

# Solution in Python # 

class WaterGlass():
    def __init__(self, fullness):
        self.fullness = fullness
    def refill(self):
        if self.fullness >= 90:
            print("Your glass has overflowed! Oh no!")
            self.fullness = 100
        else:
            self.fullness = 100
        return self.fullness
    def pour(self):
        self.fullness = 0
        print("Your glass is now empty")
        return self.fullness
    def sip(self):
        if self.fullness == 0:
            print("There's no water left!")
        else:
            self.fullness = self.fullness - 10
        return self.fullness
    def full(self):
        print(f"Your glass is {self.fullness}% full")
    
def main():
    while True:
        ask = input("What do you want to do? Sip / pour / refill / check fullness / quit ")
        if ask.lower() == "sip":
            glass.sip()
        elif ask.lower() == "pour":
            glass.pour()
        elif ask.lower() == "refill":
            glass.refill()
        elif ask.lower() == "check fullness":
            glass.full()
        elif ask.lower() == "quit":
            break
        else:
            print("Enter a valid selection")
    
glass = WaterGlass(60)
main()

