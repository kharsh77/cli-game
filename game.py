import random
import time

class Character:
	def __init__(self, name, powers):
		self.name= name
		self.powers= powers

class Player(Character):
	def __init__(self, energy):
		self.name= self.set_name()
		self.powers= self.set_powers()
		self.energy= energy
		Character.__init__(self,self.name, self.powers)


	def get_energy(self, input=0):
		# input can be positive or negative
		self.energy= self.energy+input
		return self.energy

	def set_name(self):
		return raw_input("\nEnter name of your player: ")

	def get_name(self):
		return self.name

	def set_powers(self):
		print("\n Assign power of your player for each quality")
		print(" Allowed Values are 0, 1 or 2.")
		powers=[]
		sumFlag= False
		while(not sumFlag):
			for x,y in enumerate(QUALITIES):
				flag= False
				userInput=1
				while(not flag):
					try:
						userInput = raw_input("   assign for \"{}\": ".format(y))
						if int(userInput) in [0, 1, 2]:
							powers.append(int(userInput))
							flag = True
						else:
							print("     Invalid input. Please try again!!")

					except ValueError:
						if type(userInput)==str :
							print('     Only integers\'r allowed. Try again!!')
						else:
							userInput=1
							flag=True

			print("\n\n  Your entered values are:")
			for x in range(len(QUALITIES)):
				print("   {} : {}".format(QUALITIES[x], powers[x]))
			if(sum(powers)>5):
				print("     ...total power summed {}, which exceeded the limit. Please enter again.").format(sum(powers))
				powers = []
			else: sumFlag= True
		return powers

	def get_power(self):
		return self.powers

class RuleSetup:
	def __init__(self, qualities, relation):
		"""Welcome to the Game		
		"""
		self.qualities= qualities
		self.relation= relation

	def get_relation_value(self, p1, p2):
		x= p1-1
		y=p2-1
		return self.relation[x][y]

	def show_qualities(self):
		return self.qualities

class Stalwart():

	def __init__(self):
		self.stalwarts=[]

	def add(self, name, power):
		# x= Character.__init__(self,name,power)
		x= (name, power)
		self.stalwarts.append(x)

	def print_obj(self):
		for obj in self.stalwarts:
			print obj

	def print_nStalwart(self):
		print "No of entered stalwarts: {}".format(len(self.stalwarts))

	def get_power(self, name):
		return [y[1] for x,y in enumerate(self.stalwarts) if(y[0].lower()==name.lower())][0]

class UserOptionInput:

	def __init__(self, type, message, option=()):
		self.userInput= self.validate(type,message, option)

	def validate(self, type, message, option):
		userInput=None
		try:
			userInput= int(raw_input(message))
			if option:
				userInput= userInput
				if userInput in option:
					return userInput
				else:
					print("Error: You choose {}. Expected input are {}").format(str(userInput), option)
					return False

		except ValueError:
			if type(userInput) is not type:
				print("Error: The typed input is not a {}").format(type)
				return False
		return type(userInput)

	def get_option(self):
		return self.userInput

class Door:
	def __init__(self):
		print(
			"< >< >< >< >< >< < >< >< >< >< >< < >< >< >< >< >< < >< >< >< >< >< "
			"\n< >< >< >< >< >< > Which door you want to enter? < >< >< >< >< >< \n"
		)
		self.allOptions= None
		self.option= None

	def set_option(self,choice):
		flag= False
		option= None
		while(not flag):
			# Increased options value, so that user needs to fill only whole numbers.
			option= UserOptionInput(int, "Enter a value [options: {}]: ".format(
				", ".join([str(x+1) for x in choice])), [x+1 for x in choice]).get_option()
			option= option-1
			if option in choice: flag= True
			else: print("          Incorrect input. Try again.")
		self.allOptions= choice
		self.option= option

	def option_choosen(self):
		return self.option

	def get_all_options(self):
		return self.allOptions

class Task:
	def __init__(self):
		self.taskNumber= 0
		self.task= []

	def set_task(self, taskSet):
		i= random.choice(range(len(taskSet)))
		j= random.choice(range(len(taskSet[i][1])))
		# self.taskField.add(taskSet[i][0])
		self.task.append( (taskSet[i][0], taskSet[i][1][j]))
		self.taskNumber+=1

	def get_task(self):
		return self.task

class Opponent:
	def __init__(self):
		self.opponentNumber=0
		self.opponents=[]

	def set_opponent(self, stalwarts):
		i= random.choice(range(len(stalwarts)))
		self.opponents.append(stalwarts[i])
		self.opponentNumber+=1

	def get_opponent(self):
		return self.opponents

if __name__== "__main__":
	# what are differnt powers
	# how power are related to esch other
	QUALITIES= ('sports', 'politics', 'entrepreneurship','science','entertainment')
	# INTER_POWER_COEFFICIENTS=[0,1,2,3]
	RELATION=(
		(3,1,1,0,1),
		(1,3,0,1,2),
		(1,0,3,2,1),
		(0,1,2,3,0),
		(1,2,1,0,3))

	TASKS= (
		(1, ("task11", "task12", "task13", "task14","task15")),
		(2, ("task21", "task22", "task23", "task24","task25")),
		(3, ("task31", "task32", "task33", "task34", "task35")),
		(4, ("task41", "task42", "task43", "task44", "task45")),
		(5, ("task51", "task52", "task53", "task54", "task55")),
	)


	# Add stalwarts
	STALWARTS=(
		('Virat', (4,0,2,0,1)),
		('Modi', (0,4,1,1,0)),
		('Steve', (0,2,4,2,0)),
		('Enistein',(0,2,1,5,0)),
		('Alpachino', (1,1,2,0,3))
	)

	########## GAME RULES
	#################################
	# print(
	# """
	# Build your character
	# ********************
	# Rules:
	# 1. Your character can have five qualities and a power for each quality.
	# 2. A quality can have power value as 0,1,2.
	# 3. By default your character has power of "1" for each quality.
	# 4. You can customize the powers of your character for a given quality to either 0,1 or 2 but the
	#    sum of total powers should be 5.
    #
	# Acions:
	# 1. You are shown names of all qualities your character can have.
	# 2. Enter a value for a prompt for each quality your character can have which will be
	#    either 0,1 or 2.
	# 3. Sum of all powers should be equal or less than 5.
	# 4. It the sun exceeds the total of 5, then you need to enter again.
	# 5. After building your character you can proceed to choose the door.
    #
    #
    # Choose a door
    # *************
    # 1. After your character is ready, you need to choose a door to get into the ring.
    #
    # In the ring
    # *************
    # 1. You character competes with a opponent for a given task.
    # 2. If you win in a particular task, you get excess power wrt to your opponent added to you energy.
    # 3. If you loose in a particular task, your energy get reduced accordingly.
    # 4. Next, you are directed to choose the next door.
    # 5. If your energy become non-positive then the game terminates. Your achievements are
     #    shown thereafter.
	# """)

    ########## INITIALIZING
	################################

	print("Game initializing...")
	# print("\n"*2)

	iRuleSetup = RuleSetup(QUALITIES, RELATION)

	iStalwart = Stalwart()
	[iStalwart.add(x[0], x[1]) for x in STALWARTS]

	# time.sleep(3)
	print "Game initilized."
	print ("")

	print("Let's start ......")
	print ("")
	print("You need to build your player.")
	print("##############################")

	print("  > Scale values[0/1/2] of your player on these qualities: {}").format(
		(', ').join(["\""+x+"\"" for x in iRuleSetup.show_qualities()])
	)

	print("  > You have a total power vakue of {}, on which you need to scale values of your player.").format(len(QUALITIES))

	INITIAL_ENERGY= 5
	print("  > Initially your player has energy value of {}").format(INITIAL_ENERGY)

	# Build your player
	iPlayer= Player(INITIAL_ENERGY)

	print("\nYou have successfully build your player. Congratulations!!")
	print ("#############################################################")


	# game
	# player has positive energy
	# sets tasks and opponent
	# player choose a door
	# player plays a game with an opponent
	# player energy get revised

	print(" "*20+"WELCOME TO THE GAME, {} ").format((iPlayer.get_name()).title())

	print ("\n" * 1)


	def get_result(player1, player2, task, relationMatrix):
		coeff= relationMatrix[task]
		score1= sum([player1[x]* coeff[x] for x in range(len(coeff))])
		score2 = sum([player2[x] * coeff[x] for x in range(len(coeff))])
		time.sleep(2)
		return score1-score2


	def fight(nTasks, TASKS, iStalwart, iPlayer):
		# nTasks= nDoors = nOpponent

		t=Task()
		o=Opponent()
		for x in range(nTasks):
			t.set_task(TASKS)
			o.set_opponent(iStalwart.stalwarts)

		tasks= t.get_task()
		opponents= o.get_opponent()

		print("Your opponents are ready behind the door. "
			  "\n  ** Choose a door from the given options."
			  "\n  ** And increase your total energy after defeating them.")

		print("\n")

		door= Door()
		door.set_option(range(0,nTasks))
		doorChosen= door.option_choosen()
		doorAllChoice= door.get_all_options()
		doorAllChoice.remove(doorChosen)
		print ("You choose DOOR {}".format(doorChosen+1))

		playerPower= iPlayer.get_power()
		opponent= opponents[doorChosen][0]
		opponentPower= opponents[doorChosen][1]
		gameTask= tasks[doorChosen][1]
		gameTaskField = tasks[doorChosen][0]-1

		print "\n"
		print(
			"  "+"*"*10+" Your are facing {} on  task: {} "+"*"*10+"\n"
		).format(opponent, gameTask)

		#Doors not choose data
		print( " " * 5 + "Who are the opponent on other not chosen doors?")
		for x in doorAllChoice:
			# print ("Door: {} || Task: {} || Opponent: {}").format(x + 1, tasks[x], opponents[x])
			print (" "*7+" Door: {} || Opponent: {} || task: {}").format(
				x+1, opponents[x][0], tasks[x][1])

		print "\n"

		result= get_result(playerPower, opponentPower, gameTaskField, RELATION)

		if result > 0:
			print(" "*15+" You defeated {}. Wow!!".format(opponent))
		elif(result == 0):
			print(" "*12+" The game was drawn with {}. So close!!".format(opponent))
		else:
			print(" "*12+" You got defeated by {}. Never mind!!".format(opponent))

		# newEnergy= iPlayer.get_energy(input= result)


		time.sleep(2)

		return result


	def game():

		playerEnergy= iPlayer.get_energy()
		playerPower= iPlayer.get_power()

		while (playerEnergy > 0):
			print "PLAYER CURRENT ENERGY:", iPlayer.get_energy()
			result= fight(3, TASKS, iStalwart, iPlayer)

			playerEnergy= iPlayer.get_energy(result)
			print(
				">< >< >< >< >< >< >< >< Your current energy: {} >< >< >< >< >< >< >< "
				"\n>< >< >< >< >< >< >< >< >< >< >< >< < >< >< >< >< >< < >< >< >< >< >< "
			).format(playerEnergy)

			print "\n"
			if playerEnergy>0:
				print"\n**************** NEXT DOOR *******************"
			else:
				print" \n**************** GAME OVER **********************"

	game()

























