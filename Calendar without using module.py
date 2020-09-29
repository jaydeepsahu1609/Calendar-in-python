#Takes Month as Input
i= False
while(not i):
	month= int(input("Enter month (1-12) : "))
	if(month>12 or month<1):
		print("Invalid value. Enter again")
	else:
		i=True
	#Takes Year as Input
i=False
while (not i):
	year = int(input("Enter year (yyyy) : "))
	if(year<1800 or year> 2099):
		print("Year must be in between 1800 - 2099. Enter again")
	else: 
		i=True
#-------------------------------------------------------------

#Dictionary for Months with corresponding number
month_dictionary= {1: "January", 2:"February", 3:"March",4:"April", 5:"May", 6:"June", 7:"July", 8:"August", 9:"September", 10:"October", 11:"November", 12:"December"}

#List for days of Week
week_list = ['S', 'M', 'T','W', 'Th', 'F', 'Sa']

#Number of days in the Month to be printed
days_count = {1:31, 2:28 if(not(year%4 or year%400)) else 29, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}

#-------------------------------------------------------------
#Calculation For Finding the Day on the First date of month
century_digits = int(year/100)
year_digits = int(year%(century_digits*10))

value = year_digits + year_digits//4

if century_digits == 18:
    value += 2
elif century_digits == 19:
    value += 0
elif century_digits == 20:
    value += 6

if month == 1 and year_digits% 4 != 0: 
    value += 0
elif month == 1 and year_digits% 4 == 0: 
    value += -1
elif month == 2 and year_digits% 4 != 0:
    value += 3
elif month == 2 and year_digits% 4 == 0: 
    value += 2
elif month == 3:
    value += 3
elif month == 4:
    value += 6
elif month == 5:
    value += 1
elif month == 6:
    value += 4
elif month == 7:
    value += 6
elif month == 8:
    value += 2
elif month == 9:
    value += 5
elif month == 10:
    value += 0
elif month == 11:
    value += 3
elif month == 12:
    value += 5

value = (value + 1) % 7 #value = first day of month, can be found via month_dictionary
#-------------------------------------------------------------

#For printing dates
def date_print():
		#Week days printing
		for i in week_list:
			print(i, end='\t')
		print(' ')
		temp = 0
		
		#Vacant Spaces for first week, if needed
		for i in range(0, value):
			print("\t", end='')
			temp += 1
			
		#Prints date	
		for i in range(1,days_count[month]+1):
			temp += 1
			if (temp==7):
				print(i)
				temp=0
			else:
			#New line after a complete week	
				print(i, end='\t')
		print(" ")

#-------------------------------------------------------------

#Lines for Decoration
def  line():
		print("___________________________________________________")

#-------------------------------------------------------------
#CALENDAR DISPLAY
line()
print("\t\t",month_dictionary[month], year)
line()
date_print()
line()

#------------------END OF PROJECT-----------------------