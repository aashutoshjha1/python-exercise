class Animal:
    def __init__(self, name):
        self.name = name
        print(f"Animal __init__ called for {self.name}")

    def speak(self):
        print(f"{self.name} makes a sound.")

class Dog(Animal):  # Dog inherits from Animal
    def __init__(self, name, breed):
        super().__init__(name)  # Calls Animal's __init__
        self.breed = breed
        print(f"Dog __init__ called for breed {self.breed}")

    def speak(self):
        super().speak()  # Optional: calls the parent's speak()
        #print(f"{self.name} barks.")


a = Dog("dog", "local")
a.speak()

