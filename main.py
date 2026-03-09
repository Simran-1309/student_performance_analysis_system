import math

# -----------------------------
# Student Class
# -----------------------------
class Student:
    def __init__(self, student_id, name, branch, marks):
        self.student_id = student_id
        self.name = name
        self.branch = branch
        self.marks = marks

    def calculate_total(self):
        return sum(self.marks)

    def calculate_average(self):
        return self.calculate_total() / len(self.marks)

    def calculate_grade(self):
        avg = self.calculate_average()

        if avg >= 90:
            return "A"
        elif avg >= 80:
            return "B"
        elif avg >= 70:
            return "C"
        elif avg >= 60:
            return "D"
        else:
            return "F"

    def display(self):
        print("ID:", self.student_id)
        print("Name:", self.name)
        print("Branch:", self.branch)
        print("Marks:", self.marks)
        print("Total:", self.calculate_total())
        print("Average:", round(self.calculate_average(), 2))
        print("Grade:", self.calculate_grade())
        print("-------------------------")


# -----------------------------
# Student Management Functions
# -----------------------------
students = []


def add_student():
    student_id = input("Enter Student ID: ")
    name = input("Enter Name: ")
    branch = input("Enter Branch: ")

    marks = []
    subjects = ["Mathematics", "Physics", "Programming", "Electronics", "Signal Processing"]

    for sub in subjects:
        m = int(input(f"Enter marks for {sub}: "))
        marks.append(m)

    student = Student(student_id, name, branch, marks)
    students.append(student)

    print("Student added successfully!")


def display_students():
    if not students:
        print("No student records found.")
        return

    for s in students:
        s.display()


def search_student():
    sid = input("Enter Student ID to search: ")

    for s in students:
        if s.student_id == sid:
            s.display()
            return

    print("Student not found.")


def find_topper():
    if not students:
        print("No records available.")
        return

    topper = max(students, key=lambda s: s.calculate_total())

    print("Class Topper:")
    topper.display()


def subject_highest():
    if not students:
        print("No records available.")
        return

    subjects = ["Math", "Physics", "Programming", "Electronics", "Signal Processing"]

    for i in range(5):
        highest = max(students, key=lambda s: s.marks[i])
        print(f"Highest in {subjects[i]}: {highest.name} ({highest.marks[i]})")


def class_average():
    if not students:
        print("No records available.")
        return

    total = sum(s.calculate_average() for s in students)
    avg = total / len(students)

    print("Class Average Marks:", round(avg, 2))


# -----------------------------
# File Handling
# -----------------------------
def save_data():
    with open("students.txt", "w") as f:
        for s in students:
            data = [s.student_id, s.name, s.branch] + list(map(str, s.marks))
            line = ",".join(data)
            f.write(line + "\n")

    print("Data saved successfully.")


def load_data():
    try:
        with open("students.txt", "r") as f:
            for line in f:
                data = line.strip().split(",")

                student_id = data[0]
                name = data[1]
                branch = data[2]
                marks = list(map(int, data[3:]))

                students.append(Student(student_id, name, branch, marks))

        print("Data loaded successfully.")

    except FileNotFoundError:
        print("No saved data found.")


# -----------------------------
# Statistical Analysis
# -----------------------------
def subject_average():
    if not students:
        print("No records available.")
        return

    subjects = ["Math", "Physics", "Programming", "Electronics", "Signal Processing"]

    for i in range(5):
        avg = sum(s.marks[i] for s in students) / len(students)
        print(f"Average marks in {subjects[i]}: {round(avg,2)}")


def standard_deviation():
    if not students:
        print("No records available.")
        return

    all_marks = []

    for s in students:
        all_marks.extend(s.marks)

    mean = sum(all_marks) / len(all_marks)

    variance = sum((x - mean) ** 2 for x in all_marks) / len(all_marks)

    std = math.sqrt(variance)

    print("Standard Deviation:", round(std, 2))


def grade_distribution():
    grades = {"A":0, "B":0, "C":0, "D":0, "F":0}

    for s in students:
        g = s.calculate_grade()
        grades[g] += 1

    print("Grade Distribution:")
    for g in grades:
        print(g, ":", grades[g])


# -----------------------------
# Menu Driven Interface
# -----------------------------
def menu():
    while True:
        print("\n--- Student Performance Analysis System ---")
        print("1. Add Student")
        print("2. Display Students")
        print("3. Search Student by ID")
        print("4. Find Class Topper")
        print("5. Subject Highest Marks")
        print("6. Class Average")
        print("7. Subject Average")
        print("8. Standard Deviation")
        print("9. Grade Distribution")
        print("10. Save Data")
        print("11. Load Data")
        print("12. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            display_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            find_topper()
        elif choice == "5":
            subject_highest()
        elif choice == "6":
            class_average()
        elif choice == "7":
            subject_average()
        elif choice == "8":
            standard_deviation()
        elif choice == "9":
            grade_distribution()
        elif choice == "10":
            save_data()
        elif choice == "11":
            load_data()
        elif choice == "12":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Try again.")


# Run program
menu()