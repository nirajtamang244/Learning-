#Create a Person class with name and age attributes and a method to return 
# "Hello, I am [name] and I am [age] years old!".

class person():
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print(f"Hello, I am {self.name} and I am {self.age} years old")
#Create two objects of the Person class and print their details.
p1= person("niraj",21)
p2= person ("alisha",21)

p1.display()
p2.display()