class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print(f"my name is {self.name} and my age is {self.age}")
person_1=person("javhara",19)
print(person_1.name)
print(person_1.age)
person_1.display()
