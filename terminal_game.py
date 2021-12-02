import random

#Greeting - opening prompts to get info about user
handicap = 0
def greeting():
	name = input("Hi! Please enter your name: ")
	print("\nThank you, " + name + "! What is your golf handicap? (If you are a + handicap, please enter it as a negative, i.e. \"-4\"")
	handicap = input("\nHandicap: ")
	handicap = int(input("\nHandicap: "))
	print("\nOk that's great. Let's find some drills for you.")
	improvement = input("\nEnter what part of your game you would like to improve the most, putting, short game, or long game: ")
	determine_skill_area(improvement)
	determine_skill_area(improvement, handicap)

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
#Do I need classes? putting, short game and long game are all similar and do similar things... I could use a class here.
def putting(handicap):
	print('')
	dict_of_drills = {}

	if handicap > 5:
		dict_of_drills = {
		'3 foot drill': 'Place 10 tees around the hole at 3 feet, make all 10 putts in a row', 
		'Lag drill': 'From 20 feet, get 3 balls in a row into a 3 foot circle around the hole.',
		'789 drill': 'Place 3 balls at 7, 8 and 9 feet around the hole. Repeat at 2 other holes. Make 3/9 putts.'
		}
		for key in dict_of_drills.keys():
			print(key)
	#else: give harder drills

	random_or_selected(dict_of_drills)

def short_game(handicap):
	dict_of_drills = {}
	if handicap > 5:
		dict_of_drills = {
		'Chip it close drill': 'Pick 3 spots around the green and drop 3 balls at each spot. Hit all 9 balls to the same flag and try to get 6/9 in a 6 foot circle', 
		'Hole out drill': 'Pick a short easy chip and hit it until you make 3 shots.',
		'Different club drill': 'Choose a club you don\'t normally chip with and use that around the green. Do you notice an improvement?'
		}
		for key in dict_of_drills.keys():
			print(key)
	#else:

	random_or_selected(dict_of_drills)

def long_game(handicap):
	pass

def random_or_selected(dict_of_drills):
	print('\nDoes a certain drill look interesting or do you want one randomly selected for you? \nIf there is a drill you are interested in, type the name below.')
	drill_choice = input('\n>')
	lower_drill_choice = drill_choice.lower()
	drill_names = []
	drill_descriptions = []
	#do I need the lists?
	for key, value in dict_of_drills.items():
		drill_names.append(key)
		drill_descriptions.append(value)
	if 'random' in lower_drill_choice:
		rand_num = random.randint(0, len(drill_names)-1)
		print('\nOk here is a random one:\n\n' + drill_names[rand_num] + ': ' + drill_descriptions[rand_num])
	elif drill_choice in drill_names:
		print('That\'s a great choice!')
		print('\n' + drill_choice + ': ' + drill_descriptions[drill_names.index(drill_choice)])

def determine_skill_area(improvement, handicap):
	#cleans input string for comparison in next if statement
	if type(improvement) is str:
		improvement_lower = improvement.lower()
		clean_improvement = improvement_lower.strip()

	available_skill_areas = ['putting', 'short game', 'long game']
	if clean_improvement in available_skill_areas:
		print(f'\nOk. Here is a list of {clean_improvement} drills you can do based on your handicap: \n')
		#need clean improve to have underscore for long game and short game
		if clean_improvement == 'long game' or clean_improvement == 'short game':
			split_improvement = clean_improvement.split()
			formatted_improvement = '_'.join(split_improvement)
			eval(formatted_improvement + '(handicap)')
		else:
			eval(clean_improvement + '(handicap)')
	else:
		print('\nThat\'s not an option! Please try again. Enter what part of your game you would like to improve the most, putting, short game, or long game:\n')
		determine_skill_area(input('>'), handicap)

class Drill:
	def __init__(self, name, skill_area):
		self.name = name
		self.skill_area = skill_area

#lass Putting(Drill):

# Hi Lela, I am going to show you how to save this

greeting()
drill1 = Drill('Putterbreaker', 'Putting')
print('\nThanks for using the Golf Drill Generator. Good Luck!')
# class Drill:
# 	def __init__(self, name, description):
# 		self.name = name
# 		self.description = description

# class Putting(Drill):
# 	def __init__(self, name, description):
# 		super().__init__(name, description)

# drill1 = Drill('Putterbreaker', 'Putting')