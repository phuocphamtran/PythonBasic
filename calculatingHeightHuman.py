
import datetime
def ask_yes_no(promt):
	while True:
		answer = input(promt)
		if answer == "yes":
			return True
		elif answer == "no":
			return False
		else:
			continue

def math_year(year_born):
	now = datetime.datetime.now()
	CURRENT_YEAR = now.year
	return CURRENT_YEAR - year_born

def convert_meter_to_feet(meter):
	METER_TO_FEET = 3.281
	feet = meter * METER_TO_FEET
	feet = round(feet, 1)
	return feet

def print_height_info(height_feet, is_male):
	if is_male == True:
		if height_feet > 6.5:
			print("You are", end=" ")
			for i in range(10):
				print("very", end=" ")
			print("tall as a man")
		elif height_feet > 6.0:
			print("You are tall as a man")
		else:
			print("You are short as a man")
	else:
		if height_feet > 5.7:
			print("You are tall as a girl")
		elif height_feet < 5.0:
			print("You are", end=" ")
			i=0
			while i<10:
				print("very ", end = "")
				i+=1
			print("short as a girl")
		else:
			print("You are short as a girl")	

def print_person_info(firstname, lastname, age, height_feet,is_vietnamese, is_male):
	now = datetime.datetime.now()
	CURRENT_YEAR = now.year
	print("\n---")
	print("Your name is " + firstname + " " + lastname)
	print("{2} is {0} years old in {1}".format(age,CURRENT_YEAR,firstname))
	print("You are " + str(height_feet) + " feet tall")

	if is_vietnamese :
		print("You are from Vietnam")
	else:
		print("You not are from Vietnam")
	print_height_info(height_feet,is_male)

def ask_person_info():
	firstname = input("Your firstname: ")
	lastname = input("Your lastname: ")
	year_born = int(input("When you were born: "))
	height_meter = float(input("Your height (meter): "))
	is_male = ask_yes_no("Are you male (yes/no):")
	is_vietnamese = ask_yes_no("Are you Vietnamese (yes/no):")
	return firstname, lastname, year_born, height_meter, is_male, is_vietnamese

def main():

	firstname, lastname, year_born, height_meter, is_male, is_vietnamese = ask_person_info()
	age = math_year(year_born)
	height_feet = convert_meter_to_feet(height_meter)

	print_person_info(firstname, lastname, age, height_feet,is_vietnamese, is_male)

main()












# print("\n Loop in loop 1:")
# for i in range(0,2):
# 	print(i)
# 	for j in range(3,5):
# 		print(j)

# print("\n Loop in loop 2:")
# for i in range(0,2):
# 	for j in range(3,5):
# 		print(j)
# 	print(i)

# print("\n Loop in loop 3:")
# for i in range(0,2):
# 	for j in range(3,5):
# 		print(j)
# 		print(i)


# baitap for loop
#tuvung module phan du
# s_denominator = 0
# for i in range(100):
# 	if i==1:
# 		continue

# 	if i % 2 == 0:
# 		continue

# 	s_denominator += 1/i
# s = 1 / s_denominator
# s = round(s,2)

# print(s)


# While loop
# i = 0
# while i<5:
# 	print(i)
# 	i += 1


# funtion

# def print_number(max_number):
# 	for i in range(max_number):
# 		print(i)

# print_number(5)

# def add_one(number):
# 	number += 1
# 	return number

# x=2
# new_number = add_one(x)
# print(new_number)

# y=4
# new_number = add_one(y)
# print(new_number)
	

# def main():
# 	student_A_name = "Phuoc"
# 	student_A_math_score = 9
# 	student_A_english_score = 10

# 	student_B_name = "Phuc"
# 	student_B_math_score = 7
# 	student_B_english_score = 5
# 	print_student(student_A_name, student_A_math_score, student_A_english_score)
# 	print_student(student_B_name, student_B_math_score, student_B_english_score)
	

# def print_student(name, math_score, english_score):
# 	print("Student name: " + name)
# 	print("Math" + str(math_score))
# 	print("Enllish" + str(english_score))

# main()
















