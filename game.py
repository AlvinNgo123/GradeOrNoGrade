import random

def showAvailableGrades():
	print("Here are the remaining final grades that you could receive: ")
	for grades in originalPapers:
		print(grades, "%")

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

def callTeacher(decr):
	offer = 0
	numLeft = 0
	for score in shufflePapers:
		numLeft += 1
		offer += score
	return int(int(offer / numLeft) - decr)

def checkIfAccept(choice):
	if choice == 'grade':
		return True
	elif (choice == 'no') or (choice == 'no grade'):
		return False

#Welcome Messages 
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
#print(shufflePapers)
#print(originalPapers)

#1) Get user's first selection and remove it from possible papers
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
while (gameIsOver == False) and (len(shufflePapers) > 1):
	showAvailableGrades()
	showAvailableCases()
	print("You will eliminate 2 'papers' at a time")
	choice1 = input("Choose the 1st paper to eliminate: ")
	while (choice1.isnumeric() == False) or (int(choice1) > 11) or (int(choice1) < 1) or (availablePapers[int(choice1)] == False):
		if (choice1.isnumeric() == False) or (int(choice1) > 11) or (int(choice1) < 1):
			choice1 = input("Sorry, that's not a valid response. Please choose another: ")
		else:
			choice1 = input("Sorry, that paper was already eliminated. Please choose another: ")
	choice1 = int(choice1)
	availablePapers[choice1] = False 
	originalPapers.remove(shufflePapers[choice1 - 1])

	print()
	print()
	print("The paper you chose had a grade of " + str(shufflePapers[choice1 - 1]) + "%")
	print()
	print()

	showAvailableGrades()
	showAvailableCases()
	choice2 = input("Choose the 2nd paper to eliminate: ")
	while (choice2.isnumeric() == False) or (int(choice2) > 11) or (int(choice2) < 1) or (availablePapers[int(choice2)] == False):
		if (choice2.isnumeric() == False) or (int(choice2) > 11) or (int(choice2) < 1):
			choice2 = input("Sorry, that's not a valid response. Please choose another: ")
		else:
			choice2 = input("Sorry, that paper was already eliminated. Please choose another: ")
	choice2 = int(choice2)
	availablePapers[choice2] = False 
	originalPapers.remove(shufflePapers[choice2 - 1])

	print()
	print()
	print("The paper you chose had a grade of " + str(shufflePapers[choice2 - 1]) + "%") 
	print()
	print()

	if len(shufflePapers) != 1:
		
		teacherOffer = callTeacher(decr)
		decr = decr - 3.7
		print("Hang On. The teacher wants to offer you " + str(teacherOffer) + "%")
		showAvailableGrades()
		choice3 = input("So.....Grade or No Grade: ")
		if (choice3.lower() == 'grade') or (choice3.lower() == 'no') or (choice3.lower() == 'no grade'):
			gameIsOver = checkIfAccept(choice3.lower())
		else:
			choice3 = input("Sorry, I didn't understand that.....Grade or No Grade: ")


#Two cases
#1) GameIsOver becomes true. This only occurs when user has chosen to accept a grade from the "teacher"  
#2) Length of shufflePapers is 1. This means that only 1 grade is left on the board so the user gets the personal grade that they picked in the beginning. 
if(gameIsOver == True):
	print("Congrats, your final grade is " + str(teacherOffer) + "%") 
else:
	print("It seems you have now reached the last case so go ahead and look at the personal grade you picked in the beginning")
	print("Congrats, your final grade choice was  " + str(personalCase))





