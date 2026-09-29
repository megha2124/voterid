#Python program to check age for voter eligibility
from datetime import datetime
birth_year = int(input("Enter your birth year : "))

current_year = datetime.now().year

age = current_year - birth_year

print("Your age is : ", age)

if age >= 18 :
    print("Eligible to vote")
    # Eligible for voting

else : 
    print("Not eligible to vote")
    #Not eligible for voting

    