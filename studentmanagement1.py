class Student:
    def _init_(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

class StudentManagementSystem:
    def _init_(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def remove_student(self, name):
        for student in self.students:
            if student.name == name:
                self.students.remove(student)
                return True
        return False

    def search_student(self, name):
        for student in self.students:
            if student.name == name:
                return student
        return None

    def update_student_grade(self, name, grade):
        for student in self.students:
            if student.name == name:
                student.grade = grade
                return True
        return False

# main program loop
sms = StudentManagementSystem()
while True:
    print("\n")
    print("Student Management System")
    print("-------------------------")
    print("1. Add Student")
    print("2. Remove Student")
    print("3. Search Student")
    print("4. Update Student Grade")
    print("5. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        name = input("Enter student name: ")
        age = int(input("Enter student age: "))
        grade = int(input("Enter student grade: "))
        student = Student(name, age, grade)
        sms.add_student(student)
        print("Student added successfully!")
    elif choice == 2:
        name = input("Enter student name: ")
        if sms.remove_student(name):
            print("Student removed successfully!")
        else:
            print("Student not found!")
    elif choice == 3:
        name = input("Enter student name: ")
        student = sms.search_student(name)
        if student:
            print("Student found:")
            print("Name:", student.name)
            print("Age:", student.age)
            print("Grade:", student.grade)
        else:
            print("Student not found!")
    elif choice == 4:
        name = input("Enter student name: ")
        grade = int(input("Enter new grade: "))
        if sms.update_student_grade(name, grade):
            print("Student grade updated successfully!")
        else:
            print("Student not found!")
    elif choice == 5:
        break
    else:
        print("Invalid choice!")