#Produces drills to do for golf practice

import random

#Greeting - opening prompts to get info about user
handicap = 0
def greeting():
	name = input("Hi! Please enter your name: ")
	print("\nThank you, " + name + "! What is your golf handicap? (If you are a + handicap, please enter it as a negative, i.e. \"-4\"")
	handicap = input("\nHandicap: ")
	print("\nOk that's great. Let's find some drills for you.")
	improvement = input("\nEnter what part of your game you would like to improve the most, putting, short game, or long game: ")
	determine_skill_area(improvement)

def determine_skill_area(improvement):
	if type(improvement) is str:
		improvement_lower = improvement.lower()
	if improvement_lower == 'putting':
		print('\nOk. Here is a list of putting drills you can do: ')
		#call here
	elif improvement_lower == 'short game':
		print('\nOk. Here is a list of short game drills you can do: ')
		#call here
	elif improvement_lower == 'long game':
		print('\nOk. Here is a list of driving range drills you can do: \n')
		#call here
	else:
		print('\nPlease enter one of the following options: putting, short game, long game.')
		determine_skill_area(input('>'))






class Drill:
	def __init__(self, name, skill_area):
		self.name = name
		self.skill_area = skill_area

class Putting(Drill):
	
greeting()
drill1 = Drill('Putterbreaker', 'Putting')
