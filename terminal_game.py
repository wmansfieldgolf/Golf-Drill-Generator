import random

class Skill:
	def __init__(self, name, easy_drills_dict, hard_drills_dict):
		self.name = name
		self.easy_drills_dict = easy_drills_dict
		self.hard_drills_dict = hard_drills_dict

	def determine_drill_dict(self, handicap):
		if handicap > 5:
			for key in self.easy_drills_dict:
				print(key)
			random_or_selected(self.easy_drills_dict)
		else:
			for key in self.hard_drills_dict:
				print(key)
			random_or_selected(self.hard_drills_dict)

#Greeting - opening prompts to get info about user
handicap = 0
def greeting():
	print('Welcome to the Golf Drill Generator! Are you ready to get better?\n')
	name = input("Hi! Please enter your name: ")
	print("\nThank you, " + name + "! What is your golf handicap? (If you are a + handicap, please enter it as a negative, i.e. \"-4\"")
	handicap = int(input("\nHandicap: "))
	print("\nOk great. Let's find some drills for you.")
	improvement = input("\nEnter what part of your game you would like to improve the most, putting, short game, or long game: ")
	determine_skill_area(improvement, handicap)

#determines which Skill object to call
def determine_skill_area(improvement, handicap):
	#cleans input string for comparison in following if statement
	if type(improvement) is str:
		improvement_lower = improvement.lower()
		clean_improvement = improvement_lower.strip()

	available_skill_areas = ['putting', 'short game', 'long game']
	if clean_improvement in available_skill_areas:
		print(f'\nOk. Here is a list of {clean_improvement} drills you can do based on your handicap: \n')
		#if necessary, formats string to call Skill object
		if clean_improvement == 'long game' or clean_improvement == 'short game':
			split_improvement = clean_improvement.split()
			formatted_improvement = '_'.join(split_improvement)
			skill_method = eval(formatted_improvement)
			skill_method.determine_drill_dict(handicap)
	else:
		print('\nThat\'s not an option! Please try again. Enter what part of your game you would like to improve the most, putting, short game, or long game:\n')
		determine_skill_area(input('>'), handicap)

def random_or_selected(dict_of_drills):
	print('\nDoes a certain drill look interesting or do you want one randomly selected for you? \nIf there is a drill you are interested in, type the name below.')
	drill_choice = input('\n>')
	lower_drill_choice = drill_choice.lower()
	drill_names = []
	drill_descriptions = []
	#do I need the lists?
	for key, value in dict_of_drills.items():
		drill_names.append(key.lower())
		drill_descriptions.append(value)
	if 'random' in lower_drill_choice:
		rand_num = random.randint(0, len(drill_names)-1)
		print('\nOk here is a random one:\n\n' + drill_names[rand_num].capitalize() + ': ' + drill_descriptions[rand_num])
	elif drill_choice in drill_names:
		print('That\'s a great choice!')
		print('\n' + drill_choice.capitalize() + ': ' + drill_descriptions[drill_names.index(drill_choice)])

easy_putting_drills = {
	'3 foot drill': 'Place 10 tees around the hole at 3 feet, make all 10 putts in a row', 
	'Lag drill': 'From 20 feet, get 3 balls in a row into a 3 foot circle around the hole.',
	'789 drill': 'Place 3 balls at 7, 8 and 9 feet around the hole. Repeat at 2 other holes. Make 3/9 putts.'
}

hard_putting_drills = {

}

easy_short_game_drills = {
	'Chip it close drill': 'Pick 3 spots around the green and drop 3 balls at each spot. Hit all 9 balls to the same flag and try to get 6/9 in a 6 foot circle', 
	'Hole out drill': 'Pick a short, easy chip and hit it until you make 3 shots.',
	'Different club drill': 'Choose a club you don\'t normally chip with and use that around the green. Do you notice an improvement?'
}

hard_short_game_drills = {

}

easy_long_game_drills = {

}

hard_long_game_drills = {

}

putting = Skill('putting', easy_putting_drills, hard_putting_drills)
short_game = Skill('short game', easy_short_game_drills, hard_short_game_drills)
long_game = Skill('long game', easy_long_game_drills, hard_long_game_drills)
greeting()

print('\nThanks for using the Golf Drill Generator. Good Luck!')