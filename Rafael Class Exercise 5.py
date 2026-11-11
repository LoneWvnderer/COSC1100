'''
Program name: Class Exercise 5
Author: Rafael Cas
Date: 2026-11-06

Description: Midterm Grade Calculator

You have now progressed beyond the midpoint of this course and would like to
write a program to calculate your midterm mark. The description on how your 
midterm mark was calculated is in the course outline. Please refer back to the
course outline for details.

Your program must ask the user for their marks for each assessment, ordered by
type. The assessments include the Pre-Class Activities, Class Exercises, the first
Test. Once the user finishes their entry, calculate and display the user's grade as
a percentage and their percentage for each type of assessment.

Your user may not always enter the correct details when asked. Ensure your
program can identifiy that and guide the user on entering valid data.

Plan to Program!

    With consideration to the Course Outline, given that we need
    the program to work regardless of what the user does, write a
    plan for the program to determine a midterm grade for this course.

'''

print("=== COSC 100 Midterm Grade Calculator ===")

# Collect marks for each category using lists.
categories = ["Pre-Class Activities", "Class Exercises", "Test 1"]
marks, pcts = [], [] # Store the lists for each category.

# Use a single loop to collect all marks for all categories.
for cat in categories:
    print(f"\n--- {cat} ---")
    cat_list = list()

    while True:
        val = input(f"Enter mark (0-100) or 'done': ")

        if val.lower() == 'done':
            break
        try:
            m = float(val)
            if 0 <= m <= 100:
                cat_list.append(m)
            else:
                print("Error! Mark must be between 0 and 100. Please try again.")
        except ValueError:
            print("Error! Invalid input. Please enter a numerical value or 'done'.")

    marks.append(cat_list)
    pcts.append(sum(cat_list) / len(cat_list) if cat_list else 0.0)

# Calculate the weighted overall midterm (10%, 20%, 70%)
overall = (pcts[0] * 10 + pcts[1] * 20 + pcts[2] * 70) / 100

# Display all results. 
print(f"""
=============================
    Midterm Grade Summary
=============================
Pre-Class Activities Average: {pcts[0]:.2f}% (Entries: {len(marks[0])})
Class Exercises Average: {pcts[1]:.2f}% (Entries: {len(marks[1])})
Test 1 Score: {pcts[2]:.2f}% (Entries: {len(marks[2])})
-----------------------------
Overall Midterm Percentage: {overall:.2f}%
============================ 
""")

input("Press Enter to exit the program.")







    
    