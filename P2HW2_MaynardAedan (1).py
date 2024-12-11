# Aedan Maynard
# 10/13/24
# P2HW2
# Understanding Lists

# Step 1: Initialize an empty list
grades = []

# Step 2: Prompt the user to enter grades for each module
grades.append(float(input("Enter grade for Module 1: ")))
grades.append(float(input("Enter grade for Module 2: ")))
grades.append(float(input("Enter grade for Module 3: ")))
grades.append(float(input("Enter grade for Module 4: ")))
grades.append(float(input("Enter grade for Module 5: ")))
grades.append(float(input("Enter grade for Module 6: ")))

# Step 4: Calculate the lowest grade
lowest_grade = min(grades)

# Step 5: Calculate the highest grade
highest_grade = max(grades)

# Step 6: Calculate the sum of grades
sum_of_grades = sum(grades)

# Step 7: Calculate the average of grades
average_grade = sum_of_grades / len(grades)

# Step 8: Display results
print(f"\nLowest Grade:        {lowest_grade}")
print(f"Highest Grade:       {highest_grade}")
print(f"Sum of Grades:       {sum_of_grades}")
print(f"Average of Grades:   {average_grade:.2f}")
