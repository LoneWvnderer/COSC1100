#Program Name: Exercise #3
#Author: Rafael Cas
#Date: 2026/10/05
#
#Description: Hotdog Sales Menu 

#Initialize all the variables

traditional = 0
veggie = 0
curry = 0

#Display the menu until user provides correct input

while True:

    print("\nHotdog Sales Menu\n" \
        "1. Traditional\n" \
        "2. Veggie\n" \
        "3. Curry\n" \
        "4. Tally and Exit")

    #If user throws anything that is not a valid number option
    try:
        menu_choice = int(input("\nPlease choose from the available options. "))
    except ValueError:
        print("\nError, invalid input. Letters and special characters are not allowed.")
        continue

    if menu_choice in (1, 2, 3, 4):
        if menu_choice == 1:
            traditional+=1
        elif menu_choice == 2:
            veggie+=1
        elif menu_choice == 3:
            curry+=1
        elif menu_choice == 4:
            #Displays the total number of sales
            total = traditional + veggie + curry

            #Conversions and display output
            print("\n--- Sales Summary ---")
            if total > 0:
                trad_pct = (traditional / total) * 100
                veg_pct = (veggie / total) * 100
                curry_pct = (curry /total) * 100

                print(f"Traditional: {traditional} ({trad_pct:.1f}%)")
                print(f"Veggie: {veggie} ({veg_pct:.1f}%)")
                print(f"Curry: {curry} ({curry_pct:.1f}%)")
                print(f"Total Sold: {total}")
            else:
                #If ALL values entered are 0, this shows as the output
                print("No hot dogs were sold today.")
            break
    else:
        #If user inputs any number that is NOT one of the menu options
        print("\nError, invalid input(s). Please choose from the available menu options.")

#Exits the program
input("\nPress Enter to exit the program.")

    

