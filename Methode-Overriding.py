class Phone :
    def __init__(self):
        print("I am phone class")

class Realme(Phone) :
    def __init__(self):
        super().__init__()
        print("Now,I am realme class")
        

r = Realme()


