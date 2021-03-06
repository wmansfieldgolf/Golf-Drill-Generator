import random

class Skill:
	def __init__(self, name, easy_drills_dict, hard_drills_dict):
		self.name = name
		self.easy_drills_dict = easy_drills_dict
		self.hard_drills_dict = hard_drills_dict

	def determine_drill(self, handicap):
		if handicap > 5:
			for key in self.easy_drills_dict:
				print(key)
			random_or_selected(self.easy_drills_dict)
		else:
			for key in self.hard_drills_dict:
				print(key)
			random_or_selected(self.hard_drills_dict)

# dictionaries of drills passed into instances of class Skill
easy_putting_drills = {
	'3 foot drill': 'Place 10 tees around the hole at 3 feet, make all 10 putts in a row', 
	'Lag drill': 'From 20 feet, get 3 balls in a row into a 3 foot circle around the hole.',
	'789 drill': 'Place 3 balls at 7, 8 and 9 feet around the hole. Repeat at 2 other holes. Make 3/9 putts.'
}

hard_putting_drills = {
	'345 drill': 'Create 6 branches around the hole with putts at 3, 4, and 5 feet. To complete a branch, make the 3, 4, and 5 foot putts in a row. How many putts do you miss while completing all 6 branches?',
	'789 drill': 'Place 3 balls at 7, 8 and 9 feet around the hole. Repeat at 2 other holes. Make 5/9 putts.', 
	'Putter breaker': 'Start with a 4 foot putt. If you miss, go back by 3 feet and make that putt (7ft), etc. If you miss again, continue going back another 3 feet. The max distance from the hole you can get is 13 feet. If you make the longer putt, move back up 3 feet. Once you make it back to the 4 foot putt, make it to move to a different hole. Repeat 18 times. How many putts does it take to complete 18 holes?'
}

easy_short_game_drills = {
	'Chip it close drill': 'Pick 3 spots around the green and drop 3 balls at each spot. Hit all 9 balls to the same flag and try to get 6/9 in a 7 foot circle', 
	'Hole out drill': 'Pick a short, easy chip and hit it until you make 3 shots.',
	'Different club drill': 'Choose a club you don\'t normally chip with and use that around the green. Do you notice an improvement?'
}

hard_short_game_drills = {
	'Up and down game': 'Pick 9 shots around the green to hit to one flag. Hit the shot, then putt it out. Goal is 6/9 up and downs.',
	'Chip it close drill': 'Pick 3 spots around the green and drop 3 balls at each spot. Hit all 9 balls to the same flag and try to get 6/9 in a 4 foot circle.',
	'Landing spot game': 'Pick a relatively easy chip and pick where you want the ball to land on the green. Place a ball on the tee at that spot and hit the chip until you knock the ball off the tee.'
}

easy_long_game_drills = {
	'Start line game': 'Place an alignment stick in the ground about 10 feet in front of you on the line between your ball and target. Hit 5 shots starting left of the stick, and 5 shots starting right, alternating each shot.',
	'Fairway game': 'Choose two different targets down range that are the \"edge\" of the fairway. Hit 4/7 balls in the fairway.'
	}

hard_long_game_drills = {
	'Hit the fairway game': 'Pick two targets on the range to be the edges of your fairway. Hit 7 drives in a row into the fairway. If you miss, make a 5 foot putt to continue where you left off. If you miss, start the drill over.',
	'10 minute game': 'Make a pile of 10 balls. Choose different targets to represent the edges of your \"fairways\" so you have three \"fairways\" to rotate between each shot. Using the balls from the pile, hit a driver into whatever fairway you pick, changing each shot. If you miss, add a ball to the pile. After 10 minutes, how many balls do you have left?'
}

#Greeting - opening prompts to get info about user
def greeting():
	print('\nWelcome to the Golf Drill Generator! Are you ready to get better?\n')
	name = input("Please enter your name: ")
	print(f'\nThank you, {name.strip().title()}! What is your golf handicap to the nearest whole number? (If you are a + handicap, please enter it as a negative, i.e. \"-4\"')

	#ensures handicap is an int
	handicap = input('\nHandicap: ')
	while not isinstance(handicap, int):
		try:
			handicap = int(handicap)
		except ValueError:
			print('\nLet\'s try that again. You can enter a whole number between -10 and 36.')
			handicap = input('\nHandicap: ')

	print('\nOk great. Let\'s find some drills for you.')
	
	improvement = input('\nEnter what part of your game you would like to improve the most. You can choose putting, short game, or long game: ')
	determine_skill_area(improvement, handicap)

#determines which Skill instance to call
def determine_skill_area(improvement, handicap):

	#instantiates different skill areas
	putting = Skill('putting', easy_putting_drills, hard_putting_drills)
	short_game = Skill('short game', easy_short_game_drills, hard_short_game_drills)
	long_game = Skill('long game', easy_long_game_drills, hard_long_game_drills)

	#cleans input string for comparison in following if statement
	improvement_lower = improvement.lower()
	clean_improvement = improvement_lower.strip()

	available_skill_areas = ['putting', 'short game', 'long game']
	if clean_improvement in available_skill_areas:
		print(f'\nOk. Here is a list of {clean_improvement} drills you can do based on your handicap: \n')
		
		if clean_improvement == 'long game':
			long_game.determine_drill(handicap)
		elif clean_improvement == 'short game':
			short_game.determine_drill(handicap)
		else:
			putting.determine_drill(handicap)

	else:
		print('\nThat\'s not an option! Please try again. Enter what part of your game you would like to improve the most, putting, short game, or long game:\n')
		determine_skill_area(input('>'), handicap)

#gets user input on what drill they would like to do and prints the description
def random_or_selected(dict_of_drills):
	print('\nDoes a certain drill look interesting or do you want one randomly selected for you? \nIf there is a drill you are interested in, type the name below.')
	drill_choice = input('\n>')
	lower_drill_choice = drill_choice.lower()

	drill_names = []
	drill_descriptions = []

	for key, value in dict_of_drills.items():
		drill_names.append(key.lower())
		drill_descriptions.append(value)

	while True:
		if 'random' in lower_drill_choice:
			rand_num = random.randint(0, len(drill_names)-1)
			print('\nOk here is a random one:\n\n' + drill_names[rand_num].capitalize() + ': ' + drill_descriptions[rand_num])
			break
		elif lower_drill_choice in drill_names:
			print('\nThat\'s a great choice!')
			print('\n' + lower_drill_choice.capitalize() + ': ' + drill_descriptions[drill_names.index(lower_drill_choice)])
			break
		else:
			print('\nHmm. I don\'t seem to have that drill. Try selecting one from the list or typing \"random\".')
			lower_drill_choice = input('>').lower()
			continue
###

#runs the entire program
greeting()

#end of program
print('\nThanks for using the Golf Drill Generator. Happy practicing!\n')

###