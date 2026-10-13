import math

# Program Name: Exercise #2
# Author: Rafael Cas
# Date: 2026/09/25
#
# Description: Duck Reservoir Coverage Calculator

print ('Rubber Duck Reservoir Coverage Calculator \n' 
'-----------------------------------------') 

#Define constants

PI = math.pi

#Get user input 

reservoir_length= float(input ("Enter reservoir length (m): "))
reservoir_width = float(input ("Enter reservoir width (m): "))
duck_diameter = float(input ("Enter rubber duck diameter (m): "))

#Total area of reservoir

reservoir_area = reservoir_length * reservoir_width
duck_area = pow((duck_diameter / 2), 2) * PI
ducks_needed = reservoir_area / duck_area

#Output of the functions

print('\n--- Coverage Results ---')
print(f"Reservoir Area: {reservoir_area: .2f} square meters.")
print(f"Area per duck: {duck_area: .4f} square meters.")
print(f'{int(ducks_needed)} ducks are needed to fill the reservoir.')

#Prompt user to close program when finished using.

input('\nPress Enter to exit the program.')





