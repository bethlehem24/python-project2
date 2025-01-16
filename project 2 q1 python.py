#1) Create a simple Python program application that does the following:


print("Hello User!")

# Ask for the user's name?

name = input("what is your name?")

 # Then responds "Hello <user's name>"

print("Hello," + name)

#Ask for the user's year of birth

year_of_birth = int(input("when were you born?"))

#Get the current year

from datetime import datetime

current_year = datetime.now().year

#calculate the user's age
age=current_year-year_of_birth

#print out the user's age
print(F"{name},you are {age} years old.")

 # Then ask: "Do you know how to drive?"

knows_driving = input("Do you know how to drive? (Yes/No)").strip().lower()

# Then ask: "How old were you when you got your driving license" if the user replied "Yes" to the above question

if knows_driving == "yes":

 # Ask when they got their driving license

    driving_age = int(input("How old were you when you got your driving license? "))
    license_year = year_of_birth + driving_age
    years_driving = current_year - license_year

 # Output the license year and years of driving

    print(f"You got your driving license in {license_year} and you have been driving for {years_driving} years.")


    # Then outputs: "You are <age> years old now but you still can't drive. You were supposed to get your license in <year>,<x> years ago at the age of 30 at the latest" If the user replied "No" and is over the age of 30
else:
    if age > 30:
        license_deadline_year = year_of_birth + 30
        years_overdue  = current_year - license_deadline_year
        print(f"You are {age} years old now but you still can't drive. You were supposed to get your license in {license_deadline_year} , {years_overdue}  years ago at the age of 30 at the latest" )


    # Then outputs: "You are <age> years old now and you should work on getting your driving license before you turn 30. You have <x> years to go until the year <year>" If the user replied "No" and is under the age of 30

    else:
        years_until_30 = 30 - age
        expected_license_year = current_year +  years_until_30 
        print(f"You are {age} years old now and you should work on getting your driving license before you turn 30. You have {years_until_30} years to go until the year {expected_license_year}.")

 