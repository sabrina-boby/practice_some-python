

class Triangle:
    height=""
    base=""

    def set_value(self,height,base):
        self.height=height
        self.base=base

    def display(self):
        result=(0.5*self.base*self.height)
        print(result)
        # print(f"height : {self.height},base : {self.base} ,  result = {0.5*self.height*self.base}")




tin=Triangle()
tin.set_value(20,10)
tin.display()
