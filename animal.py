class Animal:
    def speak(self):
        print("animal is speaking")
class Dog(Animal):
    def speak(self):
        print("woof!")
dog=Dog()
dog.speak()

