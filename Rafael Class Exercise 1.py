# Program Name: Exercise #1
# Author: Rafael Cas
# Date: September 18, 2026
#
# Description: Ice Cream Usage

# ----- CONSTANTS -----
SCOOP_VOLUME_ML = 120.0 # milliliters per scoop
KIDDIE_SCOOPS = 0.5
SMALL_SCOOPS = 1.0
MEDIUM_SCOOPS = 2.0
LARGE_SCOOPS = 3.0

# ----- INPUT -----
print("Ice Cream Shop Weekly Usage Calculator")
print("--------------------------------------")
kiddie_count = int(input("How many *kiddie* cones were sold this week? "))
small_count = int(input("How many *small* cones were sold this week? "))
medium_count = int(input("How many *medium* cones were sold this week? "))
large_count = int(input("How many *large* cones were sold this week? "))

# ----- PROCESSING -----
# Calculate total scoops for each cone size
kiddie_scoops_total = kiddie_count * KIDDIE_SCOOPS
small_scoops_total = small_count * SMALL_SCOOPS
medium_scoops_total = medium_count * MEDIUM_SCOOPS
large_scoops_total = large_count * LARGE_SCOOPS

# Total scoops used in the week
total_scoops = (kiddie_scoops_total + small_scoops_total + medium_scoops_total + large_scoops_total)

# Convert scoops to milliliters and liters
total_ml = total_scoops * SCOOP_VOLUME_ML
total_liters = total_ml / 1000.0

# ----- OUTPUT -----
print("\n--- Weekly Ice Cream Usage ---")
print(f"Total scoops used: {total_scoops:.1f} scoops")
print(f"Total volume used: {total_ml:.0f} mL")
print(f"                   or {total_liters:.2f} L")
print("\nUse this amount to help plan your next week's stock order.")

input("\nPress Enter to exit the program.")


