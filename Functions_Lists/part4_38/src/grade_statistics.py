def calculate_exercise_points(exercises_completed):
    if exercises_completed >= 100:
        return 10
    return exercises_completed // 10

def determine_grade(total_points):
    if total_points < 15:
        return 0  # fail
    elif 15 <= total_points <= 17:
        return 1
    elif 18 <= total_points <= 20:
        return 2
    elif 21 <= total_points <= 23:
        return 3
    elif 24 <= total_points <= 27:
        return 4
    elif 28 <= total_points <= 30:
        return 5
    
results = []

while True:
    line = input("Exam points and exercises completed: ")
    if line.strip() == "":
        break
    exam_points, exercises_completed = map(int, line.split())
    results.append((exam_points, exercises_completed))

total_points = []
grades_count = [0] * 6
passed_count = 0

for exam_points, exercises_completed in results:
    exercise_points = calculate_exercise_points(exercises_completed)
    total = exam_points + exercise_points
        
    if exam_points < 10:
        grade = 0
    else:
        grade = determine_grade(total)
        
    total_points.append(total)
    grades_count[grade] += 1
        
    if grade > 0:
        passed_count += 1
    
points_average = sum(total_points) / len(total_points)
pass_percentage = (passed_count / len(total_points)) * 100 if total_points else 0

print("Statistics:")
print(f"Points average: {points_average:.1f}")
print(f"Pass percentage: {pass_percentage:.1f}")
print("Grade distribution:")
    
for grade in range(5, -1, -1):
    print(f"  {grade}: {'*' * grades_count[grade]}")