# Yahtzee

# https://www.reddit.com/r/dailyprogrammer/comments/dv0231/20191111_challenge_381_easy_yahtzee_upper_section/

NO_OF_DICE_SIDES = 6
NUMBER_OF_DICE = 5


def yahtzee_upper(rolls):
	top_score = 0
	scores = []
	
	if(not check_rolls_valid(rolls)):
		return("Invalid rolls given. Finished")

	for i in range(1, NO_OF_DICE_SIDES + 1):
		instances = 0
		if(i in rolls):
			instances = find_instances(i, rolls)
			scores.append(i * instances)
		else:
			scores.append(instances)

	top_score = max(scores)

	return top_score
	

# CALCULATIONS

def find_instances(number, scores):
	# check how many times a value appears in a list
	count = 0 

	for value in scores:
		if(value == number):
			count += 1 

	return count
	
# VALIDATION
def check_rolls_valid(rolls):
	valid = True
	
	if (not correct_number_of_dice_rolls(rolls)):
		valid = False

	for roll in rolls:	
		if((not number_in_range(roll)) or (not number_is_int(roll))):
			valid = False
			
	return valid
	
	
def number_in_range(roll):
	
	if(roll not in range(1, NO_OF_DICE_SIDES + 1)):
		print("Score not within valid range (0-6)")
		return False
	else:
		return True
		
def number_is_int(roll):
	if(type(roll) is not int):
		print("Incorrect Value entered. Score not an int.")
		return False
	else:
		return True
		
def correct_number_of_dice_rolls(rolls):
	no_of_rolls = len(rolls) 
	if(NUMBER_OF_DICE != no_of_rolls):
		print("Incorrect number of values provided")
		return False
	else:
		return True
	
	
# invalid tests
print(yahtzee_upper((1,2,34,4, 5)))

# valid tests
print(yahtzee_upper([2, 3, 5, 5, 6])) # prints 10
print(yahtzee_upper([1, 1, 1, 1, 3])) # prints 4
print(yahtzee_upper([1, 1, 1, 3, 3])) # prints 6
print(yahtzee_upper([1, 2, 3, 4, 5])) # prints 5
print(yahtzee_upper([6, 6, 6, 6, 6])) # prints 30