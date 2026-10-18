class dad:
    def __init__(self,eyes,aggresive):
        self.eyes=eyes
        self.aggresive=aggresive
    def display (self):
        print(self.eyes,self.aggresive) 
class child(dad):
    def __init__(self,age,name,eyes,aggresive):
        self.age=age
        self.name=name
        dad.__init__(self,eyes,aggresive)
obj=child(12,"omer","dark brown","no")
obj.display()



