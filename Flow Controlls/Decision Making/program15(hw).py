#Calculate your age from the following data : Age=?

#current_year :
#current_month :
#current_date :
#birth_year :
#birth_month :
#birth_date :


#Solution :
#Age = current_year - birth_year

#Current data:#2023 year
#10 month
#3 date

#Birth data : #2022
#10
#4
#age=2023-2022 = 0

current_year=int(input("Enter the current year:" ))
current_month=int(input("Enter the current month:" ))
current_date=int(input("Enter the current date:" ))
birth_year=int(input("Enter the birth year:"))
birth_month=int(input("Enter the birth month:"))
birth_date=int(input("Enter the birth date:"))
age=current_year-birth_year

if(current_month<birth_month):
    print(age-1)
elif(current_month>=birth_month):
    if(current_date>=birth_date):
        print(age)
