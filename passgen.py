
# AUTHOR = Adarsh Gupta(Adarshaddee)
# AIM = Create RANDOM Passwords
# VERSION = 1.0 

# NOTE: THIS TOOL IS ONLY FOR EDUCATIONAL PURPOSE


import os
import random
import string
from termcolor import colored

# to clear the screen
os.system("clear")

# input
input(colored("Press ENTET key to continue.............", "red"))

# to clear the screen
os.system("clear")

print("\n")

# user options

print(colored(" [ 1 ] Easy", "yellow"))
print(colored(" [ 2 ] Medium", "yellow"))
print(colored(" [ 3 ] Hard", "yellow"))
print(colored(" [ 9 ] Exit\n", "yellow"))


#user input
user_ch = int(input(colored("Enter your choice:\nAD4rSH_> ", "cyan")))




# if user's choice is 2, then
if user_ch == 1:
	
	#charcters
	char = []
	char.extend(list(string.ascii_letters))
	
	random.shuffle(char)
	
	# password length
	plen = int(input(colored("\nEnter your password length: \nAD4rSH_> ", "blue")))
	
	# logic
	passwrd = "".join(char[0:plen])
	
	# printing password
	print("Your password is: ", "".join(passwrd))
	
	# to save the password
	sav = input(colored("\nDo you want to save your password (y/n) : \nAD4rSH_> ", "magenta"))
	
	
	# if user don't save the password
	if sav == "n" or sav == "N":
		print(colored("\nBye - Bye\n\n", "red"))
	
	# if user save password	
	elif sav == "y" or sav == "Y":
		
		# asking for password name
		name = input(colored("\nName your password: \nAD4rSH_> ","red"))
		
		# to save the password
		dict = {name:passwrd}
		
		# file handling
		f = open("easy.txt", "a")
		f.write(str(dict))
		f.write("\n")
		f.close
		
		# sucessful message
		print(colored("\nSucessfully added.....................\n\n", "blue"))

	# else statement
	else:
		print(colored("\nPlease enter a valid value!!!\n\n", "red"))




# if user's choice is 3, then
elif user_ch == 2:
	
	#charcters
	char = []
	char.extend(list(string.ascii_letters))
	char.extend(list(string.digits))
	
	random.shuffle(char)
	
	# password length
	plen = int(input(colored("\nEnter your password length: \nAD4rSH_> ", "blue")))
	
	# logic
	passwrd = "".join(char[0:plen])
	
	# printing password
	print("Your password is: ", "".join(passwrd))
	
	# to save the password
	sav = input(colored("\nDo you want to save your password (y/n) : \nAD4rSH_> ", "magenta"))
	
	
	# if user don't save the password
	if sav == "n" or sav == "N":
		print(colored("\nBye - Bye\n\n", "red"))
	
	# if user save password	
	elif sav == "y" or sav == "Y":
		
		# asking for password name
		name = input(colored("\nName your password: \nAD4rSH_> ","red"))
		
		# to save the password
		dict = {name:passwrd}
		
		# file handling
		f = open("medium.txt", "a")
		f.write(str(dict))
		f.write("\n")
		f.close
		
		# sucessful message
		print(colored("\nSucessfully added.....................\n\n", "blue"))

	# else statement
	else:
		print(colored("\nPlease enter a valid value!!!\n\n", "red"))




# if user's choice is 5, then
elif user_ch == 3:
	
	#charcters
	char = []
	char.extend(list(string.ascii_letters))
	char.extend(list(string.digits))
	char.extend(list(string.hexdigits))
	char.extend(list(string.punctuation))
	
	
	random.shuffle(char)
	
	# password length
	plen = int(input(colored("\nEnter your password length: \nAD4rSH_> ", "blue")))
	
	# logic
	passwrd = "".join(char[0:plen])
	
	# printing password
	print("Your password is: ", "".join(passwrd))
	
	# to save the password
	sav = input(colored("\nDo you want to save your password (y/n) : \nAD4rSH_> ", "magenta"))
	
	
	# if user don't save the password
	if sav == "n" or sav == "N":
		print(colored("\nBye - Bye\n\n", "red"))
	
	# if user save password	
	elif sav == "y" or sav == "Y":
		
		# asking for password name
		name = input(colored("\nName your password: \nAD4rSH_> ","red"))
		
		# to save the password
		dict = {name:passwrd}
		
		# file handling
		f = open("hard.txt", "a")
		f.write(str(dict))
		f.write("\n")
		f.close
		
		# sucessful message
		print(colored("\nSucessfully added.....................\n\n", "blue"))

	# else statement
	else:
		print(colored("\nPlease enter a valid value!!!\n\n", "red"))




elif user_ch == 9:
	print(colored("\nSee you again!!!\n", "red"))		
						
else:
	print(colored("Please enter a valid value", "red"))
