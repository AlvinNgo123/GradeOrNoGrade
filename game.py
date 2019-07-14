import random


welcomeMsg = "Welcome to 'Grade or No Grade'!"
directionMsg = "Your objective is to get the highest grade possible by eliminating lower grades and teacher negotiations."
firstCase = "There are 11 graded 'papers'. Let's start off by picking your personal paper"

print(welcomeMsg)
print(directionMsg)
print(firstCase)

#A+, A, A-, B+, B, B-, C+, C, C-, D, F
#Store different cases in an array
originalPapers = ["A+", "A", "A-", "B+", "B", "B-", "C+", "C", "C-", "D", "F"]


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

papers = shuffle(originalPapers)
print(papers) 