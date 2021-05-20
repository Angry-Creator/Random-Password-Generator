import random

def simple_password_generator():
			while True:
				password_length = str(input("Length of Password : "))
				if password_length.lower() == "back":
					break
				elif password_length.isdecimal() == True or password_length != "back":
						if password_length != "back" and password_length.isdecimal() == False:
							password_length = 0
						password = []
						for i in range(int(password_length)):
							if random.choice([1,2]) == 1:
								password.append(random.choice(alphabets))
							else:
								password.append(random.choice(numbers))
						random.shuffle(password)
						print("\n" + "\033[32m" + "Generated Password:  " +"".join(password) + "\n" + "\033[39m")

def complex_password_generator():
		while True:
			number_length = str(input("Length of Password Numbers : "))
			if number_length.lower() == "back":
				break
			elif number_length.isdecimal() == True or number_length != "back":
				if number_length != "back" and number_length.isdecimal() == False:
					number_length = 0
				alphabet_length = str(input("Length of Password Alphabet: "))
				if alphabet_length.lower() == "back":
					break
				elif alphabet_length.isdecimal() == True or alphabet_length != "back":
					if alphabet_length != "back" and alphabet_length.isdecimal() == False:
						alphabet_length = 0
					special_key_length = str(input("Length of Password Special Keys: "))
					if special_key_length.lower() == "back":
						break
					elif special_key_length.isdecimal() == True or special_key_length != "back":
						if special_key_length != "back" and special_key_length.isdecimal() == False :
							special_key_length = 0
						#Password Total Lenght for future use
						password_length = int(number_length)+int(alphabet_length) + int(special_key_length)
						password = []
						for i in range(int(number_length)):
							if int(number_length) > 0:
								password.append(random.choice(numbers))
						for i in range(int(alphabet_length)):
							if int(alphabet_length) > 0:
								password.append(random.choice(alphabets))
						for i in range(int(special_key_length)):
							if int(special_key_length) > 0:
								password.append(random.choice(special_keys))
						random.shuffle(password)
						print("\n" + "\033[32m" + "Generated Password: " +"".join(password) + "\n" + "\033[39m")
			

alphabets = "a b c d e f g h i j k l m n o p q r s t u v w x y z".split(" ")
numbers = "1 2 3 4 5 6 7 8 9 0".split(" ")
special_keys = ["@", "#", "$"]
print("**CREATED BY Angry-Creator**")
while True:
	try:
		option = int(input("\n=== Main Menu ===\n\n1. Simple Random Password Generator(password length is 8)\n2. Complex Random Password Generator\n>> "))
		print("\nType back to go the Main Menu\n")
		if option == 1:
			simple_password_generator()		
		elif option == 2:
			complex_password_generator()
		elif option > 2:
			print("\033[32m" + "More Options Coming Soon" +  "\033[39m")
							
	except ValueError:
		print("\nInvalid input\n")
	
	except:
		print("\nAn error occoured\n")
		break



#Your not allowed to copy this my code
