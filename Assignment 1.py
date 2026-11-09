'''
Program Name: Assignment #1
Author: Rafael Cas
Date: 2026-10-22

Description: Pizza Pi - Iteration

'''
import math

def main():
    #Set constants
    MIN_DIAMETER = 8.0
    MAX_DIAMETER = 28.0

    #Initialize diameter to a non-zero to start the loop.
    diameter =  -1.0

    #While loop for pizza calculations
    while diameter != 0:
        #For making sure the user inputs are valid.
        user_input = input("Please enter the diameter of your pizza (0 to end the program): ")

        try:
            diameter = float(user_input)
        except ValueError:
            print("\nERROR")
            print("Please enter a valid numeric value. \n")
            continue #Loops back to ask user to put in proper values.

        #Check for the exit condition (the 0).
        if diameter == 0:
            break

        #Validate the range.
        if diameter < MIN_DIAMETER or diameter > MAX_DIAMETER:
            print("\nERROR")
            print(f'The diameter must be in the range of {int(MIN_DIAMETER)}" to {int(MAX_DIAMETER)}".')
            print("Try again.\n")
            continue
            
        print(f'\nPizza Diameter: {diameter}"')

        #Calculate the radius.
        radius = diameter / 2
        total_area = math.pi * (radius ** 2)

        #Pizza slice functions. (IT'S A LOT)
        if 8.0 <= diameter < 12.0:
            #The pizza can be cut into 6 slices.
            slices = 6
            slice_area = total_area / slices
            print(f"Cut in {slices} slices results in an area of {slice_area:.2f}\" per slice.")

        elif 12.0 <= diameter < 14.0:
            #The pizza can be cut into 6 and 8 slices.
            slices = 6
            slice_area = total_area /slices
            print(f"Cut in {slices} slices results in an area of {slice_area:.2f}\" per slice.")

            slices = 8
            slice_area = total_area / slices
            print(f"Cut in {slices} slices results in an area of {slice_area:.2f}\" per slice.")

        elif 14.0 <= diameter < 16.0:
            #The pizza can be cut into 6, 8 and 10 slices.
            slices = 6
            slice_area = total_area /slices
            print(f"Cut in {slices} slices results in an area of {slice_area:.2f}\" per slice.")
            
            slices = 8
            slice_area = total_area / slices
            print(f"Cut in {slices} slices results in an area of {slice_area:.2f}\" per slice.")

            slices = 10 
            slice_area = total_area / slices
            print(f"Cut in {slices} slices results in an area of {slice_area:.2f}\" per slice.")

        elif 16.0 <= diameter < 20:
            #The pizza can be cut into 6, 8, 10 and 12 slices.
            slices = 6
            slice_area = total_area /slices
            print(f"Cut in {slices} slices results in an area of {slice_area:.2f}\" per slice.")
            
            slices = 8
            slice_area = total_area / slices
            print(f"Cut in {slices} slices results in an area of {slice_area:.2f}\" per slice.")

            slices = 10 
            slice_area = total_area / slices
            print(f"Cut in {slices} slices results in an area of {slice_area:.2f}\" per slice.")

            slices = 12 
            slice_area = total_area / slices
            print(f"Cut in {slices} slices results in an area of {slice_area:.2f}\" per slice.")

        elif 20 <= diameter <= 28:
            #The pizza can be cut into 6, 8, 10, 12 and 16 slices.
            slices = 6
            slice_area = total_area /slices
            print(f"Cut in {slices} slices results in an area of {slice_area:.2f}\" per slice.")
                        
            slices = 8
            slice_area = total_area / slices
            print(f"Cut in {slices} slices results in an area of {slice_area:.2f}\" per slice.")
            
            slices = 10 
            slice_area = total_area / slices
            print(f"Cut in {slices} slices results in an area of {slice_area:.2f}\" per slice.")
            
            slices = 12 
            slice_area = total_area / slices
            print(f"Cut in {slices} slices results in an area of {slice_area:.2f}\" per slice.")

            slices = 16 
            slice_area = total_area / slices
            print(f"Cut in {slices} slices results in an area of {slice_area:.2f}\" per slice.")

        print() #For spacing between entries.

#Checks whether the script is being run directly or as a module into another script.
if __name__ == "__main__":
    main()