class area:
    def __init__(self,length,width):
        self.length=length
        self.width=width
    def display(self):
         return print(self.length*self.width)
a=area(5,10)
b=area(20,30)
c=area(30,20)
a.display()
b.display()
c.display()

    