# Step 1: Define the Student class
class Student:
    def __init__(self, name, email, grades=None):
        """
        Initializes a new Student object.
        :param name: str - student's name
        :param email: str - student's email
        :param grades: list of int - initial grades
        """
        self.name = name
        self.email = email
        # If no grades provided, initialize an empty list
        self.grades = grades if grades is not None else []

    def add_grade(self, grade):
        """Adds a new grade to the student's grades list."""
        self.grades.append(grade)

    def average_grade(self):
        """Returns the average of all grades, or 0 if no grades."""
        if not self.grades:
            return 0
        return sum(self.grades) / len(self.grades)

    def display_info(self):
        """Prints the student's name, email, and grades."""
        print(f"Name: {self.name}")
        print(f"Email: {self.email}")
        print(f"Grades: {self.grades}")

    def grades_tuple(self):
        """Returns the grades as a tuple (immutable)."""
        return tuple(self.grades)
    
    # Step 2: Create student objects
student1 = Student("Alice Johnson", "alice@example.com", [88, 92])
student2 = Student("Bob Smith", "bob@example.com", [75, 85])
student3 = Student("Charlie Brown", "charlie@example.com", [90, 95])

# Add 2 new grades to each student
student1.add_grade(94)
student1.add_grade(87)

student2.add_grade(82)
student2.add_grade(78)

student3.add_grade(88)
student3.add_grade(91)

# Display information and average grade for each student
students = [student1, student2, student3]
for student in students:
    student.display_info()
    print(f"Average Grade: {student.average_grade():.2f}\n")
    
    # Step 3: Dictionary mapping student emails to Student objects
student_dict = {
    student1.email: student1,
    student2.email: student2,
    student3.email: student3
}

def get_student_by_email(email):
    """
    Safely retrieve a student from the dictionary using their email.
    Uses .get() so the program doesn't crash if the email doesn't exist.
    """
    student = student_dict.get(email)

    if student:
        print(f"\nStudent found for email: {email}")
        student.display_info()
    else:
        print(f"\nNo student found with email: {email}")

    return student

# Create a set of all unique grades across all students
unique_grades = set()

for student in students:
    unique_grades.update(student.grades)

print("\nUnique grades across all students:")
print(unique_grades)

# Test retrieving a student
get_student_by_email("alice@example.com")

