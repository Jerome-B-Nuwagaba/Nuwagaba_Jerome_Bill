# Super class
class Person:
    def __init__(self, id, name, gender, age):
        self.id = id
        self.name = name
        self.gender = gender
        self.age = age
        

    def display_info(self):
        print(f'ID: {self.id}, Name: {self.name}, Gender: {self.gender}, Age: {self.age}')


# Subclass: Student
class Student(Person):
    def __init__(self, id, name, gender, age, course):
        super().__init__(id, name, gender, age)
        self.course = course

    def display_info(self):
        super().display_info()
        print(f'Student Course: {self.course}')


# Subclass: Lecturer
class Lecturer(Person):
    def __init__(self, id, name, gender, age, course):
        super().__init__(id, name, gender, age)
        self.course = course

    def display_info(self):
        super().display_info()
        print(f'Lecturer Teaches: {self.course}')


# Subclass: Staff
class Staff(Person):
    def __init__(self, id, name, gender, age, role):
        super().__init__(id, name, gender, age)
        self.role = role

    def display_info(self):
        super().display_info()
        print(f'Staff Role: {self.role}')


# Create instances of each class
student1 = Student('S1001', 'Mark Johns', 'Male', 20, 'Computer Science')
lecturer1 = Lecturer('L2001', 'Dr. Robert', 'Male', 45, 'Law')
staff1 = Staff('F3001', 'Ms. Anne', 'Female', 38, 'Librarian')

# Display the information
print('\nStudent Information;')
student1.display_info()

print('\nLecturer Information;')
lecturer1.display_info()

print('\nStaff Information;')
staff1.display_info()