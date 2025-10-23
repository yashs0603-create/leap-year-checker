#leap year program
year=int(input("Enter the year\n"))
if year%4!=0:
    print("Given year is not a leap year")
elif year%400!=0:
    print("Given year is not a leap year")
elif year % 100 == 0:
    print("Given year is not a leap year")
else:
    print("Given year is a leap year")

year=int(input("Enter the year:\n"))
if year%4==0:
    if year%100==0:
        if year%400==0:
            print("Leap year")
        else:
            print("Not leap year")
    else:
        print("Leap year")
else:
    print("Not a leap year")
