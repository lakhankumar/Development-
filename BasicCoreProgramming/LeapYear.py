def CheckLeap(year):  
  if((year % 400 == 0) or  
     (year % 100 != 0) and  
     (year % 4 == 0)):   
    print( year, " is a leap Year")
  else:  
    print (year, " is not a leap Year")  
  
year = int(input("Enter the year: "))  
if year>999:
    CheckLeap(year)
else:
    print("Invalid year")