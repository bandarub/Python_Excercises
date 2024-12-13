import csv

def calculate_exercise_points(completed_exercises, total_exercises=40):
    # Sum the exercises if completed_exercises is a list
    if isinstance(completed_exercises, list):
        completed_exercises = sum(completed_exercises)
    
    # Calculate the percentage of exercises completed
    percentage = (completed_exercises / total_exercises) * 100
    
    # Determine the exercise points based on the percentage completed
    if percentage == 0:
        return 0
    elif percentage <= 10:
        return 1
    elif percentage <= 20:
        return 2
    elif percentage <= 30:
        return 3
    elif percentage <= 40:
        return 4
    elif percentage <= 50:
        return 5
    elif percentage <= 60:
        return 6
    elif percentage <= 70:
        return 7
    elif percentage <= 80:
        return 8
    elif percentage <= 90:
        return 9
    else:
        return 10

def calculate_grade(exam_points, exercise_points):
    total_points = exam_points + exercise_points
    if total_points <= 14:
        return 0  # Fail
    elif total_points <= 17:
        return 1
    elif total_points <= 20:
        return 2
    elif total_points <= 23:
        return 3
    elif total_points <= 27:
        return 4
    else:
        return 5

def read_students_data(file_name):
    students = {}
    with open(file_name, newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file, delimiter=';')
        for row in reader:
            students[row['id']] = {'first': row['first'], 'last': row['last']}
    return students

def read_exercise_data(file_name):
    exercises = {}
    with open(file_name, newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file, delimiter=';')
        for row in reader:
            exercises[row['id']] = [int(row[f'e{i}']) for i in range(1, 8)]
    return exercises

def total_exercises(exercise_data):
    totals = {}
    for student_id, exercises in exercise_data.items():
        totals[student_id] = sum(exercises)
    return totals

def read_exam_points(file_name):
    exam_points = {}
    with open(file_name, newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file, delimiter=';')
        for row in reader:
            student_id = row['id']
            points = sum(int(row[f'e{i}']) for i in range(1, 4))  # Adjusted for e1, e2, e3 format
            exam_points[student_id] = points
    return exam_points

# User input for file names
student_info = input("Student information: ")
exercise_data_file = input("Exercises completed: ")
exam_file = input("Exam points: ")

# Read student data and exercises
students = read_students_data(student_info)
exercises = read_exercise_data(exercise_data_file)

# Read exam points data
exam_points = read_exam_points(exam_file)

# Calculate total completed exercises per student
total_completed_exercises = total_exercises(exercises)

# Output grades for each student
for student_id in students:
    if student_id in exercises and student_id in exam_points:
        completed_exercises = total_completed_exercises.get(student_id, 0)
        total_exam_points = exam_points[student_id]
        exercise_points = calculate_exercise_points(completed_exercises)
        grade = calculate_grade(total_exam_points, exercise_points)
        student = students[student_id]
        print(f"{student['first']} {student['last']} {grade}")  # Corrected print statement
