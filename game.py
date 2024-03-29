import random

# Shows the player what grades they could still possibly win (show them everytime before they make a choice)
def showAvailableGrades():
	print("Here are the remaining final grades that you could receive: ")
	for grades in originalPapers:
		print(grades, "%")

# Shows the player what 'papers' they could still select from to eliminate
def showAvailableCases():
	print("Here are the available 'papers' to choose from: ")
	for paper, availability in availablePapers.items():
		if availability == True:
			print(paper)

## Shuffles array 'ar' in place with Fisher-Yates algorithm.
## Code from http://code.activestate.com/recipes/360461-fisher-yates-shuffle/
def shuffle(ar):
    a=len(ar)
    b=a-1
    for d in range(b,0,-1):
      e=random.randint(0,d)
      if e == d:
            continue
      ar[d],ar[e]=ar[e],ar[d]
    return ar

# Basic algorithm that generates the 'teacher's offer for the player based on my number of 'papers' left and decr value
# that gets smaller with each passing round
def callTeacher(decr):
	offer = 0
	numLeft = 0
	for score in shufflePapers:
		numLeft += 1
		offer += score
	return int(int(offer / numLeft) - decr)

# A check function to see whether or not the player accepts the offer from the teacher
def checkIfAccept(choice):
	if choice == 'grade':
		return True
	elif (choice == 'no') or (choice == 'no grade'):
		return False

# A check function that gets the users choice and makes sure that it is a valid choice before carrying out the removal process
def getUsersChoice(choice):
	while (choice.isnumeric() == False) or (int(choice) > 11) or (int(choice) < 1) or (availablePapers[int(choice)] == False):
		if (choice.isnumeric() == False) or (int(choice) > 11) or (int(choice) < 1):
			choice = input("Sorry, that's not a valid response. Please choose another: ")
		elif (availablePapers[int(choice)] == False):
			choice = input("Sorry, that paper was already eliminated. Please choose another: ")
	choice = int(choice)
	availablePapers[choice] = False 
	originalPapers.remove(shufflePapers[choice - 1])
	 
# A print function that just outputs to the terminal what the grade of the paper that the player chose was.
def printUsersChoice(choice):
	print()
	print() 
	print("The paper you chose had a grade of " + str(shufflePapers[int(choice) - 1]) + "%")
	print()
	print()

	
#Welcome(Intro) Messages 
welcomeMsg = "Welcome to 'Grade or No Grade'!"
directionMsg = "Your objective is to get the highest grade possible by eliminating lower grades and negotiating with your 'teacher'."
firstCase = "There are 11 graded 'papers'. Let's start off by picking your personal paper."
print(welcomeMsg)
print(directionMsg)
print(firstCase)

#A+, A, A-, B+, B, B-, C+, C, C-, D, F in percent form
#Store all different grades in 2 lists (1st kept in order, 2nd to be shuffled ) and their availabilities in a dictionary
originalPapers = [100, 95, 90, 88, 85, 80, 78, 75, 70, 60, 50]
shufflePapers = [100, 95, 90, 88, 85, 80, 78, 75, 70, 60, 50]
availablePapers = {1: True, 2: True, 3: True, 4: True, 5: True, 6: True, 7: True, 8: True, 9: True, 10: True, 11: True}

shuffle(shufflePapers)

#1) Get user's first selection as their personal 'paper' and remove it from possible papers
firstSelection = input("Choose your personal paper #(1-11): ")
while (firstSelection.isnumeric() == False) or (int(firstSelection) < 1) or (int(firstSelection) > 11):
	firstSelection = input("Sorry, that's not valid response. Please choose your personal paper between 1 and 11: ")
firstSelection = int(firstSelection)
availablePapers[firstSelection] = False
personalCase = shufflePapers[firstSelection - 1]


#2) Loop the program where it eliminates 2 grades at a time and then checks with "teacher"
#If offer is accepted, game is over. Otherwise, continue the game
gameIsOver = False
decr = 10
roundCount = 1
while (gameIsOver == False) and (len(originalPapers) != 2): 
	showAvailableGrades()
	showAvailableCases()
	if (roundCount == 1) and (len(originalPapers) == 3):
		print("You are down to the last 2 'papers'. You will only pick one this round before you look at your personal paper.")
		userChoice = input("Which paper do you choose: ")
	elif roundCount == 1:
		print("You will eliminate 2 'papers' at a time")
		userChoice = input("Choose the 1st paper to eliminate: ")
		roundCount = 2
	elif roundCount == 2:
		userChoice = input("Choose the 2nd paper to eliminate: ")
		roundCount = 1 
	getUsersChoice(userChoice)
	printUsersChoice(userChoice)
	

	if (len(originalPapers) != 2) and (roundCount == 1):
		teacherOffer = callTeacher(decr)
		decr = decr - 3.7
		print("Hang On. The teacher wants to offer you " + str(teacherOffer) + "%")
		showAvailableGrades()
		choice = input("So.....Grade or No Grade: ")
		if (choice.lower() == 'grade') or (choice.lower() == 'no') or (choice.lower() == 'no grade'):
			gameIsOver = checkIfAccept(choice.lower())
		else:
			choice = input("Sorry, I didn't understand that.....Grade or No Grade: ")


#Two cases
#1) GameIsOver becomes true. This only occurs when user has chosen to accept a grade from the "teacher"  
#2) Length of originalPapers is 2. This means that only 1 grade is left on the board so the user gets the personal grade that they picked in the beginning. 
if(gameIsOver == True):
	print("Congrats, your final grade is " + str(teacherOffer) + "%") 
else:
	print("It seems you have now reached the last case so go ahead and look at the personal grade you picked in the beginning")
	print("Congrats, your personal grade was " + str(personalCase) + "%")





