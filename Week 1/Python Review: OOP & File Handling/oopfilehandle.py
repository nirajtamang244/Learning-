class Student():
    def __init__(self,name,grade,subject):
        self.name=name
        self.grade= grade
        self.subject=subject

    def write(self):
        with open("studentinfo.csv","w") as file:
            file.write(f"name={self.name}\ngrade={self.grade}\nsubject={self.subject}")
    def read(self):
        with open("studentinfo.csv","r") as file:
            print(file.read())

p1=Student("Niraj","A","ComputerScience")

p1.write()
p1.read()

