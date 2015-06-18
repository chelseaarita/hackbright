def convert_to_seconds(hours, minutes, seconds):
	total = 60*minutes + 3600*hours + seconds
	return total

print convert_to_seconds(1, 2, 45)

def convert_to_seconds(hours,minutes,seconds):
	total = 60*minutes + 3600*hours + seconds
	return total 
print convert_to_seconds(0,0,60)

def convert_to_seconds(hours, minutes, seconds):
	total = 60*minutes + 3600*hours + seconds
	return total
print convert_to_seconds (1, 1, 1)

def convert_to_seconds(hours, minutes, seconds):
	total = 60*minutes + 3600*hours + seconds
	return total

print convert_to_seconds(1, 2, 45)

def convert_to_hours(seconds):
	hours = seconds/3600
	minutes = (seconds-3600*hours)/60
	seconds = (seconds-3600*hours)-(minutes*60)
	return (hours, minutes, seconds)
convert_to_hours(3670)

def print_time(tuple):
	print "hours:%i, minutes: %i, seconds: %i" % tuple
print_time(convert_to_hours(3500))

def convert_to_inches(feet, inches):
	total = (feet*12) + inches
	print total
convert_to_inches(2,12)

def convert_to_feet(inches):
	feet = inches/12
	inches = inches - (feet*12)
	return (feet, inches)
print convert_to_feet (38)

def print_feet(convert_to_feet):
	print "Feet: %i, Inches: %i" % convert_to_feet
print_feet (convert_to_feet(38))

print range (0,11,2)

def recursively_count(num):
	num+=2
	print "num plus 2 is ", num
	while num<11:
			print "num is ", num
			recursively_count(num)
recursively_count(0)

def crazy_count_for():
		for i in range(11):
			print i
		for i in range(20,101,10):
			print i
crazy_count_for()

def unique_letters(full_name):
	#"RACHEL"
	#first thing is to make this a list, using split
	#full_name=full_name.split(""
	list(full_name)
	count=0
	unique=0
	#[R,A,C,H,E,L]
	for i in range(0,len(full_name)):
		for j in range(0, len(full_name)):
			if full_name[i]==full_name:
				count+=1
		if count==1
			unique+=1
		count=0
	return unique
	#iterate through each letter, and then evaluate it
	#equals anything else in the list
	#starting at R go through the list,if we see an R, increment our count by 1
	print unique_letters("Rachel")
	#if it equals, count +=1
	#unique will be +1 when count is 1

num = 50
if(num>50):
	print "too high"
elif(num==50):
	print "just right"
else:
	print "too low"


object = "blue"
if (object !=str):
	print "type of object is", type(object)
	print "object to a string is", str(object)
if (object==str):
	print "it is a string"
