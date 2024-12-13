class Flyable:
    def fly(self):
        print("i can fly")
class Swimmable:
    def swim(self):
        print("i can swim")
class Duck(Flyable,Swimmable):
    pass
a=Duck()
a.fly()
a.swim()
    


        