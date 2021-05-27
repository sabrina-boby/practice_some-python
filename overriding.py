
class Phone:
    # def __init__(self):
    #   print("I am from phone class")
    def name(self):
        print("my name is boby")
    


class samsung(Phone):
    def __init__(self):
        super().name()
        print("i am from samsung class")


s=samsung() 
