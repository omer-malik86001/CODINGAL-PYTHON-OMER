class myclass:
    __privatevar=10

    def __privMeth(self):
        print("I am inside privMeth")
    def hello(self):
        print("The value of private variable is", myclass.__privatevar)
obj=myclass()
obj.hello()
obj.__privMeth()


