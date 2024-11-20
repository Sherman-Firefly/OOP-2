class IOstring():
    def __init__(self):
        self.strl=""
    
    def get_string(self):
        self.strl=input("Enter a string")

    def print_string(self):
        print("The string is", self.strl.upper())
    
strl=IOstring()
strl.get_string()
strl.print_string()