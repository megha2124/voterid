from datetime import datetime
birth_year = int(input("Enter your birth year : "))

current_year = datetime.now().year

age = current_year - birth_year

print("Your age is : ", age)

if age >= 18 :
    print("Eligible to vote")

else : 
    print("Not eligible to vote")

    