class person:
    
    def __init__(self,i,j):
        self.i=i
        self.j=j
        print("Auto calling")
        
    def addition(self):
        output = self.i + self.j
        print("Output sum = ",output)
        
    def substraction(self):
        output = self.i - self.j
        print("Output sub = ",output)
        
    def multiplication(self):
        output = self.i * self.j
        print("output mul= ",output)
        
    def division(self):
        output = self.i/self.j
        print("output div = {:.2f}".format(output))
        
obj = person(4,3)
obj.division()