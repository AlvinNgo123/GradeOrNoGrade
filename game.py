import random

#Welcome Messages 
welcomeMsg = "Welcome to 'Grade or No Grade'!"
directionMsg = "Your objective is to get the highest grade possible by eliminating lower grades and teacher negotiations."
firstCase = "There are 11 graded 'papers'. Let's start off by picking your personal paper"
print(welcomeMsg)
print(directionMsg)
print(firstCase)

#A+, A, A-, B+, B, B-, C+, C, C-, D, F in percent form
#Store all different grades in 2 arrays (1st kept in order, 2nd to be shuffled ) and their availabilities in a dictionary
originalPapers = [100, 95, 90, 88, 85, 80, 78, 75, 70, 60, 50]
shufflePapers = [100, 95, 90, 88, 85, 80, 78, 75, 70, 60, 50]
availablePapers = {1: True, 2: True, 3: True, 4: True, 5: True, 6: True, 7: True, 8: True, 9: True, 10: True, 11: True}


## Shuffles array 'a' in place with Fisher-Yates algorithm.
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

shuffle(shufflePapers)
print(shufflePapers)
print(originalPapers)

#1) Get user's first selection and remove it from possible papers
firstSelection = int(input("Choose your personal paper #(1-11): "))
#print(firstSelection) 
availablePapers[firstSelection] = False
personalCase = shufflePapers[firstSelection - 1]
originalPapers.remove(personalCase)
#print(originalPapers)


#2) Loop the program where it eliminates 2 grades at a time and then checks with "teacher"

#If offer is accepted, game is over. Otherwise, continue the game
def callTeacher():
	offer = 0
	numLeft = 0
	for score in shufflePapers:
		numLeft += 1
		offer += score
	return (int(offer / numLeft))

def checkIfAccept(choice):
	if (choice == 'Grade') or (choice =='grade'):
		return True
	else:
		return False


gameIsOver = False
while (gameIsOver == False):
	choice1 = int(input("Choose the next paper to eliminate: "))
	while availablePapers[choice1] == False:
		choice1 = int(input("Sorry, that paper was already eliminated. Please choose another: "))
	availablePapers[choice1] = False 
	originalPapers.remove(shufflePapers[choice1 - 1])

	choice2 = int(input("Choose the next paper to eliminate: "))
	while availablePapers[choice2] == False:
		choice2 = int(input("Sorry, that paper was already eliminated. Please choose another: "))
	availablePapers[choice2] = False 
	originalPapers.remove(shufflePapers[choice2 - 1])

	teacherOffer = callTeacher()
	print("Hang On. The teacher wants to offer you " + str(teacherOffer))
	choice3 = input("So.....Grade or No Grade: ")
	while (choice3 != 'grade') or (choice3 != 'Grade') or (choice3 != 'no grade') or (choice3 != 'No Grade') or (choice3 != 'No grade'):
		choice3 = input("Sorry I didn't understand that.....Grade or No Grade: ")
	gameIsOver = checkIfAccept(choice3)

print("Congrats, you won " + str(teacherOffer)) 
#If it reaches the last one, it opens the personal one and thats the final grade





