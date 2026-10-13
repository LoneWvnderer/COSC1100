# Program Name: Exercise #3
# Author: Rafael Cas
# Date: 2026/09/28
#
# Description: Student GPA Display

print('COSC1100 Student Information Entry \n'
      '----------------------------------')

#Get user inputs

#(FOR SELF) Comment these out if you want to use the while loop
student_number = (input("Please enter your student number: "))
gpa = (input("Please enter your GPA: "))

#Conditional statements and output display

#(FOR SELF) Uncomment and indent everything under if you want the program to keep prompting the user instead of exiting the program
#while True:
    #student_number = (input("Please enter your student number: "))
    #gpa = (input("Please enter your GPA: "))

if(student_number.isnumeric() and len(student_number) == 9 and
        gpa.replace('.', '', 1).isnumeric() and (float(gpa) >= 0 and float(gpa) <= 4)):
        print(f"Your student number: {student_number}")
        print(f"Your GPA: {float(gpa):.1f}")
        #break #Exit the loop when the input is invalid
    
else:
    print('\nInvalid input(s), please try again.')

input('\nPress Enter to exit the program.')







