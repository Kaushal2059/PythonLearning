
# Understanding *args i.e passing unlimited number of arguments in the function
def add(*args):
    sum = 0
    for n in args:
        sum += n
    print (sum)
    
add(1,2,3,4,5)

# Understanding **kwargs i.e passing unlimited number of arguments in the function

def calculate(n, **kwargs):
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)

calculate(2, add = 1, multiply = 2)

class Car():
    def __init__(self,**kwargs):
        # self.make = kwargs["make"]
        #self.model = kwargs["model"]
        self.make = kwargs.get("make") #get will simply return none instead of throwing error if the attribute is left
        self.model = kwargs.get("model")

car = Car(make = "nissan")
print(car.make)