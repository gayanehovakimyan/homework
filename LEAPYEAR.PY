year= int (input ( 'Enter  year: '))
if ( year <0):
	print ( " You can not enter 0 or BC")
if ((year % 400 ==0) or
(year % 4 ==0) and
(year % 100 !=0)):
	print (" Entered year is a leap year ")
else:
	print ("Year in not leap year")
standard = 1600
if ( year < standard):
	print ( (standard - year) // 4)
elif ( year >= standard):
	print ( ( year - standard)//4)


 

