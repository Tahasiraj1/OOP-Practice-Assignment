class Logger:
    def __init__(self, message):
        self.message = message
        print(f"Constructor: {self.message}")
    
    def __del__(self):
        print(f"Destructor: {self.message}")
    

l = Logger("Hello World!")
del l

    