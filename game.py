import random
import time
import pickle
import os.path



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


class GameRules:
	def __init__(self):
		message = """
		 GAME RULES
#########################################

	The game is divided into five steps:
	1. Build Your Character
	2. Choose the Door
	3. Fight with Opponent in the Ring
	4. Advance to the Next Door
	5. Game Terminates
		"""
		print(message)
		self.show(5)

		# Pick a number to show a particular step
		# (or '5' to show all)
		# (or '0' to continue with the game)
        #
		# """
        #
		# x = UserOptionInput(int, message, (0, 1, 2, 3, 4, 5)).get_option()
        #
		# while (x in (1,2,3,4,5)):
		# 	self.show(x)
		# 	x = UserOptionInput(int, message, (0, 1, 2, 3, 4, 5)).get_option()
		# 	print x

	def show(self, input):
		if input == 1:
			self.build()
		elif input == 2:
			self.door()
		elif input == 3:
			self.continues()
		elif input == 4:
			self.over()
		else:
			self.build()
			self.door()
			self.continues()
			self.over()

	def build(self):
		print(
			"""
	Build your character
	********************
	Rules:
	-------
	1. Your character can have few qualities and a power value for each quality.
	2. A quality can have power value as 0,1,2.
	3. Your player can have total power less than or equal to 5.
	4. While building your player, you can customize the powers values for any given quality.

	Assign power value:
	-------------------
	1. You are shown names of all qualities your character can have.
	2. Enter a value for a prompt for each quality your character can have which will be
	   either 0,1 or 2.
	3. Sum of all powers should be equal or less than 5.
	4. If the sun exceeds the total of 5, then you need to re-enter the values.
	5. After building your character you can proceed to play the game.
            """
		)

	def door(self):
		print("""
	Choose a door
	**************
	1. After your character is ready, you need to choose a door to get into the ring.
	2. Behind each door there is a opponent waiting for you to compete.

	In the ring
	*************
	1. Your player competes with a opponent for a given task.
	2. If you win in a particular task, the excess power you have wrt to your opponent gets added to your energy.
	3. If you loose in a particular task, your energy get reduced accordingly.
		""")

	def continues(self):
		print("""
	Advance to the next door (Game continues...)
	*********************************************
	1. You are directed to choose the next door if you have positive energy left after a fight.""")

	def over(self):
		print(
			"""
        Game over
        **********
        1. If your energy become non-positive after a fight, then the game terminates.
        2. Your achievements are shown thereafter.""")


class SaveGame:
	def __init__(self, backUpFile='progress'):
		self.backUpFile = backUpFile
		self.gameData = None
		self.player = None


	def backup_check(self):
		if os.path.isfile(self.backUpFile):
			with open(self.backUpFile) as f:
				d = pickle.load(f)
				f.close()
				if d is not None:
					self.gameData = d
					self.choose_player()
					return
		d = []
		with open(self.backUpFile, 'w') as f:
			pickle.dump(d, f)
			f.close()
		self.choose_player()
		return

	def choose_player(self):
		l = [(k, [s for p, s in enumerate(v) if p == 0][0]) for k, v in enumerate(self.gameData)]
		if l:
			print("Either choose index of player: {}").format([(k + 1, s) for k, s in enumerate(l)])
			print("\n '0' to create a new player")
			input = int(raw_input("Choose a option: {}"))
			if input == 0:
				return False
			else:
				return l[input - 1]
		else:
			return False

	def create_player(self, name, power):
		obj = {str(name): {"played": [], "resume": [],"powers":None}}
		obj["powers"]=power
		self.player = obj
		self.gameData.append(obj)

	def save_game_over(self):
		pop = self.player["resume"].pop()
		self.player["played"].append(pop)

	def new_game(self):
		obj = {"time": int(time.time()), "fights": []}
		self.player["resume"].append(obj)

	def new_fight(self, fTask, fOpponent, fResult, fScore, fInfo):
		obj = [fTask, fOpponent, fResult, fScore, fInfo]
		self.player["resume"]["fights"].append(obj)

	def backup_data(self):
		with open(self.backUpFile, 'w') as f:
			pickle.dump(self.gameData, f)
			f.close()


class Character:
	def __init__(self, name, powers):
		self.name= name
		self.powers= powers

class Player(Character, SaveGame):
	def __init__(self, energy, maxPower):

		# print("You need to build your player.")
		# print("##############################")
		# time.sleep(1)
		# print("  > Scale values[0/1/2] of your player on these qualities: {}").format((', ').join(["\"" + x + "\"" for x in self.show_qualities()]))
		# print("  > You have a total power value of {}, on which you need to scale values of your player.").format(maxPower)
		SaveGame.__init__(self)
		time.sleep(1)
		self.name= self.set_name()
		self.powers= self.set_powers()
		self.energy= energy

		Character.__init__(self, self.name, self.powers)

	time.sleep(1)

	def get_energy(self, input=0):
		# input can be positive or negative
		self.energy= self.energy+input
		return self.energy

	def set_name(self):
		return raw_input("\nEnter name of your player: ")

	def get_name(self):
		return self.name

	def set_powers(self):
		time.sleep(2)
		print("\nAssign power of your player for each quality")
		print("Allowed Values are 0, 1 or 2.")
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

		self.create_player(self.name, self.get_power())
		self.backup_data()
		return powers

	def get_power(self):
		return self.powers

class Stalwart:

	def __init__(self, stalwarts):
		self.stalwarts=stalwarts

	# def add(self, name, power):
	# 	# x= Character.__init__(self,name,power)
	# 	x= (name, power)
	# 	self.stalwarts.append(x)

	def print_obj(self):
		for obj in self.stalwarts:
			print obj

	def print_nStalwart(self):
		print "No of entered stalwarts: {}".format(len(self.stalwarts))

	def get_stalwart_power(self, name):
		return [y[1] for x,y in enumerate(self.stalwarts) if(y[0].lower()==name.lower())][0]

class Task:
	def __init__(self):
		self.taskNumber= 0
		self.task= []

	def set_task(self, taskSet):
		i= random.choice(range(len(taskSet)))
		j= random.choice(range(len(taskSet[i][1])))

		self.task.append( (taskSet[i][0], taskSet[i][1][j]))
		self.taskNumber+=1

	def get_task(self):
		return self.task

class Door:
	def __init__(self):
		self.allOptions= None
		self.option= None

	def set_option(self,choice):
		print(
			"< >< >< >< >< >< < >< >< >< >< >< < >< >< >< >< >< < >< >< >< >< >< "
			"\n< >< >< >< >< >< > Which door you want to enter? < >< >< >< >< >< \n"
		)
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
		print ("You choose DOOR {}".format(self.option_choosen() + 1))

	def option_choosen(self):
		return self.option

	def options_not_chosen(self):
		doorChosen = self.option_choosen()
		doors = self.get_all_options()
		doors.remove(doorChosen)
		return doors

	def get_all_options(self):
		return self.allOptions

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


# CONSTS: QUALITIES, RELATION,TASKS, STALWARTS
class Game(Stalwart, GameRules):
	def __init__(self, qualities, relation, tasks, stalwarts):
		print("Game initializing...")

		self.qualities = qualities
		self.relation = relation
		self.tasks= tasks

		Stalwart.__init__(self, stalwarts)

		time.sleep(2)

		print "Game initilized."
		print ("")

		# GameRules.__init__(self)

	def get_relation_value(self, p1, p2):
		x = p1 - 1
		y = p2 - 1
		return self.relation[x][y]

	def show_qualities(self):
		return self.qualities



class Fight(Task, Opponent, Door):
	def __init__(self, nTasks=3):
		self.nTasks= nTasks # No of options/doors choice given to the user
		Task.__init__(self)
		Opponent.__init__(self)
		Door.__init__(self)

	def initiate(self, tasks, stalwarts):
		for _ in range(self.nTasks):
			self.set_opponent(stalwarts)
			self.set_task(tasks)

		print("Your opponents are ready behind the door. "
			  "\n  ** Choose a door from the given options."
			  "\n  ** And increase your total energy after defeating them.")

		print("\n")

		# User chooses door here
		self.set_option(range(0, self.nTasks))

		return [self.get_task(), self.get_opponent(), self.option_choosen(), self.options_not_chosen()]


	def get_result(self, powerPlayer1, powerPlayer2, tasks, relationMatrix):
		coeff = relationMatrix[tasks]
		score1 = sum([powerPlayer1[x] * coeff[x] for x in range(len(coeff))])
		score2 = sum([powerPlayer2[x] * coeff[x] for x in range(len(coeff))])
		time.sleep(2)
		return score1 - score2



class StartGame(Game, Player, Fight, SaveGame):
	def __init__(self, QUALITIES, RELATION,TASKS, STALWARTS, initialEnergy=5, maxPower=5):

		Game.__init__(self,qualities=QUALITIES, relation=RELATION, tasks=TASKS, stalwarts=STALWARTS)
		print("Let's start ......")
		print ("\n"*2)
		SaveGame.__init__(self)
		self.backup_check()
		self.choose_player()
		print("You need to build your player.")
		print("##############################")
		time.sleep(1)
		print("  > Scale values[0/1/2] of your player on these qualities: {}").format((', ').join(["\"" + x + "\"" for x in self.show_qualities()]))
		print("  > You have a total power value of {}, on which you need to scale values of your player.").format(maxPower)

		Player.__init__(self, energy=initialEnergy, maxPower=maxPower)



		print("\nYou have successfully build your player. Congratulations!!")
		print ("#############################################################")


		Fight.__init__(self)

	def welcome(self):
		print(" " * 20 + "WELCOME TO THE GAME, {} ").format((self.get_name() ).title())

		print ("\n" * 1)


	def one_round_play(self):
		time.sleep(4)
		tasks, opponents, doorChosen, doorsNotChosen= self.initiate(self.tasks, self.stalwarts)

		playerPower = self.get_power()
		opponent = opponents[doorChosen][0]
		opponentPower = opponents[doorChosen][1]
		gameTask = tasks[doorChosen][1]
		gameTaskField = tasks[doorChosen][0] - 1

		print "\n"
		print(
			"" + "*" * 10 + " Your are facing {} on  task: {} " + "*" * 10 + "\n"
		).format(opponent, gameTask)

		time.sleep(2)
		# Doors not choose data
		print(" " * 5 + "Who are the opponent on other not chosen doors?")
		for x in doorsNotChosen:
			print (" " * 7 + " Door: {} || Opponent: {}").format(
				x + 1, opponents[x][0])

		print "\n"

		time.sleep(3)

		result = self.get_result(playerPower, opponentPower, gameTaskField, self.relation)

		if result > 0:
			print(" " * 15 + " You defeated {}. Wow!!".format(opponent))
		elif (result == 0):
			print(" " * 12 + " The game was drawn with {}. So close!!".format(opponent))
		else:
			print(" " * 12 + " You got defeated by {}. Never mind!!".format(opponent))

		time.sleep(2)

		return result


	def play(self):

		self.welcome()

		time.sleep(1)

		playerEnergy= self.get_energy()
		while (playerEnergy > 0):

			result = self.one_round_play()

			playerEnergy = self.get_energy(result)
			print(
				">< >< >< >< >< ><       Your current energy: {}        >< >< >< >< >< "
				"\n>< >< >< >< >< ==================================== < >< >< >< >< >< "
			).format(playerEnergy)

			print "\n"
			if playerEnergy > 0:
				print"\n**************** NEXT DOOR *******************"
			else:
				print" \n Your seems to be exhausted. Play Again " \
					 "\n**************** GAME OVER **********************"


if __name__== "__main__":

######### CONSTANTS #########
	# Qualities on which players compete with each other
	QUALITIES= ('sports', 'politics', 'entrepreneurship','science','entertainment')

	# Inter quality relation matrix
	RELATION=(
		(3,1,1,0,1),
		(1,3,0,1,2),
		(1,0,3,2,1),
		(0,1,2,3,0),
		(1,2,1,0,3))

	# Task list respective of each quality (Keys denotes values from QUALITY constant in order)
	TASKS= (
		(1, ("task11", "task12", "task13", "task14","task15")),
		(2, ("task21", "task22", "task23", "task24","task25")),
		(3, ("task31", "task32", "task33", "task34", "task35")),
		(4, ("task41", "task42", "task43", "task44", "task45")),
		(5, ("task51", "task52", "task53", "task54", "task55")),
	)

	# Legends with their powers in respective field
	STALWARTS=(
		('Virat', (4,0,2,0,1)),
		('Modi', (0,4,1,1,0)),
		('Steve', (0,2,4,2,0)),
		('Enistein',(0,2,1,5,0)),
		('Alpachino', (1,1,2,0,3))
	)


# The game is initialized here
	c = StartGame(QUALITIES, RELATION, TASKS, STALWARTS)
	c.play()



	# data= {1:"harsh"}
	# with open('progress.dat', 'w') as f:
	# 	pickle.dump(data, f)
    #
	# with open('progress.dat') as f:
	# 	data2 = pickle.load(f)
	# 	print data2





	# s=SaveGame()
	# s.check()












