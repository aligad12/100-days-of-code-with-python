class Animal:
    def __init__(self):
        self.num_eyes = 2
    
    def breathe(self):
        print("inhale","exhale")


class Fish(Animal):
    def __init__(self):
        super().__init__() #this part of the codes allow the child class to initialize everything in the parent class after it inherits it
        #using the parent class's constructor

    def swim(self):
        print("moving in water.")

    def breathe(self):
        super().breathe() #like this you get hold of the parent class and you can pull the method in it so your method does the same as it and then you can modify it
        print("doing this under water.")


nemo = Fish()
nemo.swim()
nemo.breathe()
cow = Animal()
cow.breathe()