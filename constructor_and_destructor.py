class Employee: 

    # Initializing (Constructor)
    def __init__(self): 
        print("constructor created")
    
    # Deleting (Destructor)
    def __del__(self):
        print("destructor called, employee deleted.")
    
obj = Employee()
del obj
