endyear = int (input("Enter a year"))
standard = 1600
leapyear=[]
for year in range( standard, endyear):
	if ( year % 400 == 0):
		leapyear.append(year)
	elif ( year % 4 ==0 and year % 100 !=0):
		leapyear.append(year)
	else:
		print ( " False")
print (leapyear)
	



