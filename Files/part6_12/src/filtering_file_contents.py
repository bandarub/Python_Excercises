import os

def filter_solutions():
    # Read the solutions from the 'solutions.csv'
    with open('solutions.csv', 'r') as file:
        lines = file.readlines()

    correct_lines = set()  # Using set to prevent duplicates
    incorrect_lines = set()  # Using set to prevent duplicates

    # Read the existing correct and incorrect solutions if they exist
    if os.path.exists('correct.csv'):
        with open('correct.csv', 'r') as correct_file:
            # Strip newline characters and extra spaces from lines
            correct_lines = set(line.strip() for line in correct_file.readlines())

    if os.path.exists('incorrect.csv'):
        with open('incorrect.csv', 'r') as incorrect_file:
            # Strip newline characters and extra spaces from lines
            incorrect_lines = set(line.strip() for line in incorrect_file.readlines())

    for line in lines:
        # Strip any leading/trailing spaces and split by semicolon
        parts = line.strip().split(';')
        
        if len(parts) != 3:
            continue  # Skip lines that don't have exactly three parts
        
        student_name, problem, result = parts

        try:
            # Try to evaluate the problem (assuming it's a valid Python expression)
            expected_result = eval(problem)
            
            # Compare the expected result to the student's result
            if str(expected_result) == result.strip():  # Strip the result to remove extra spaces
                correct_lines.add(line.strip())  # Add line after stripping extra spaces and newlines
            else:
                incorrect_lines.add(line.strip())  # Add line after stripping extra spaces and newlines
        except Exception as e:
            # In case of an exception (e.g., bad expression), consider the solution incorrect
            print(f"Error evaluating problem: {problem}. Error: {e}")
            incorrect_lines.add(line.strip())  # Add line to incorrect set

    # Write the results back to 'correct.csv' and 'incorrect.csv'
    with open('correct.csv', 'w') as correct_file:
        # Write each line from correct_lines to the file
        for line in sorted(correct_lines):  # Sorting the lines if desired
            correct_file.write(line + "\n")  # Ensure lines end with a newline

    with open('incorrect.csv', 'w') as incorrect_file:
        # Write each line from incorrect_lines to the file
        for line in sorted(incorrect_lines):  # Sorting the lines if desired
            incorrect_file.write(line + "\n")  # Ensure lines end with a newline


if __name__ == "__main__":
    filter_solutions()
