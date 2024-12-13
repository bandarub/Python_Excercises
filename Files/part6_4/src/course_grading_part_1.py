import csv

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


student_info = input("Student information: ")
exercise_data = input("Exercises completed: ")

students = read_students_data(student_info)
exercises = read_exercise_data(exercise_data)

total = total_exercises(exercises)

for student_id, total in total.items():
  student = students.get(student_id)
  if student:
    print(f"{student['first']} {student['last']} {total}")