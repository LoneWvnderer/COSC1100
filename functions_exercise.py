'''

Program Name: Class Exercise 6
Author: Rafael Cas
Date: 2026-11-09

Description: Functions

For some analysis of lists of grades, we need three functions in a file called
function_exercise.py. The file and the functions must be named exactly as shown 
for this to work correctly. The three functions are as follows:

-is_list_numeric(list_to_check): returns True if all of the list's 
elements are numeric, returns False otherwise.

-cap_list(list_to_cap, minimum=0, maximum=100): brings all elements lower than
minimum equal to minimum, and all elements greater than maximum equal to maximum.
Return the resulting capped list.

-drop_highest_and_lowest(list_to_drop): drops the highest and lowest valued 
elements in a list. Return the shrunken list, or an empty list if there are 
fewer than 3 elements.

'''

# Sam's ver. of Function 1

def is_list_numeric(list_to_check):

    # Checks if the values are a integer or float.
    for value in list_to_check:
        if type(value) != int and type(value) != float:
            return False

    return True

# Function 2

def cap_list(list_to_cap, minimum = 0, maximum = 100):
    result = []

    # Checks if the values entered meet the parameters, then appends the values to the parameters set.
    for value in list_to_cap:
        if value < minimum:
            result.append(minimum)
        elif value > maximum:
            result.append(maximum)
        else:
            result.append(value)

    return result

# Function 3

def drop_highest_and_lowest(list_to_drop):

    for value in list_to_drop:
        # If there are fewer than 3 elements.
        if len(list_to_drop) < 3:
            return []

        # Create a copy of the list to avoid combining lists.
        new_list = list_to_drop.copy()

        # Remove highest and lowest values.
        new_list.remove(max(new_list))
        new_list.remove(min(new_list))

    return new_list

# === Desk Checks ===

# Desk Check 1

print("\n--- Desk Check 1 ---")

numbers = [10, 20, 30, 40]
mixed = [10, "Hello", 30]

print("All numeric: ", is_list_numeric(numbers))
print("Mixed values: ", is_list_numeric(mixed))

# Desk Check 2

print("\n--- Desk Check 2 ---")

scores = [-10, 25, 75, 120]

print("Capped scores: ", cap_list(scores))

# Desk Check 3

print("\n--- Desk Check 3 ---")

grades = [65, 80, 90, 70, 100]

print("Remaining grades: ", drop_highest_and_lowest(grades))

# Wait for user input before closing
input("\nPress Enter to exit the program.")

