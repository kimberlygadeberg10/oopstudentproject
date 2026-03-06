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