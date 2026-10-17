class employee:
    def  __init__(self):
        print("employee created")

    def __del__(self):
        print("Destructor called")

def Create_obj():
    print("making object.......")
    obj=employee()
    print("function end........")
    return obj
print("Calling create_obj() function..........")
obj=Create_obj()
print("program end ......")