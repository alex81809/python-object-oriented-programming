class Student: 
    def __init__(self, name, age): 
        self.name = name
        self.age = age

student1 = Student("Messi", 37)
student2 = Student("Ronaldo", 41)

print("the name of the first student: ", student1.name)
print("the age of the first student: ", student1.age)

print(" ")

print("the name of the second student: ", student2.name)
print("the age of the second student: ", student2.age)
