
def add_student(students: dict, name: str):
    students[name] = []

def print_student(students, name: str):
    if name in students:
        total = len(students[name])
        if total:
            if students[name][0][1] == 0:
                total = total - 1
                print(total)
            print(f"{name}:")
            print(f" {total} completed courses:")
            mar = 0
            for cour in students[name]:
                print(f"  {cour[0]} {cour[1]}")
                mar = mar + cour [1]
            print(f" average grade {mar/total }")
        else:
            print(f"{name}:")
            print(" no completed courses")

    else:
        print(f"{name}: no such person in the database")

def add_course(students: dict, name: str, course: tuple):
    if name in students:
        # Check if the grade is 0; if so, ignore the course
        if course[1] == 0:
            return  # Do nothing if the grade is 0
        
        # Check if the course already exists, and update only if the new grade is higher
        for existing_course in students[name]:
            if existing_course[0] == course[0]:  # Same course
                if existing_course[1] < course[1]:  # Update only if new grade is higher
                    existing_course_index = students[name].index(existing_course)
                    students[name][existing_course_index] = course
                return
        
        # If course doesn't exist or the grade is higher, add the course
        students[name].append(course)

def summary(students: dict):
    # 1. Total number of students
    total_students = len(students)
    
    # 2. Find the student with the most courses
    most_courses_student = None
    max_courses = 0
    for name, courses in students.items():
        if len(courses) > max_courses:
            most_courses_student = name
            max_courses = len(courses)
    
    # 3. Find the student with the best average grade
    best_avg_student = None
    best_avg_grade = 0
    for name, courses in students.items():
        total_grades = sum(course[1] for course in courses)
        avg_grade = total_grades / len(courses) if courses else 0
        if avg_grade > best_avg_grade:
            best_avg_student = name
            best_avg_grade = avg_grade
    
    # Print the summary
    print(f"students {total_students}")
    print(f"most courses completed {max_courses} {most_courses_student}")
    print(f"best average grade {best_avg_grade:.1f} {best_avg_student}")
  

if __name__ == "__main__":
    students = {}
    add_student(students, "Peter")
    add_student(students, "Eliza")
    add_course(students, "Peter", ("Data Structures and Algorithms", 1))
    add_course(students, "Peter", ("Introduction to Programming", 1))
    add_course(students, "Peter", ("Advanced Course in Programming", 1))
    add_course(students, "Eliza", ("Introduction to Programming", 5))
    add_course(students, "Eliza", ("Introduction to Computer Science", 4))
    summary(students)