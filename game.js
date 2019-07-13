const welcomeMsg = "Welcome to 'Grade or No Grade'!"
const directionMsg = "Your objective is to finish the game with the highest grade possible by eliminating the lower grades and negotiating with the teacher."
const firstCase = "Let's start off by picking your personal 'paper'"

console.log(welcomeMsg)
console.log(directionMsg)
console.log(firstCase)

//A+, A, A-, B+, B, B-, C+, C, C-, D, F
//Store different cases in an array
let originalPapers = ["A+", "A", "A-", "B+", "B", "B-", "C+", "C", "C-", "D", "F"]

/**
 * Shuffles array 'a' in place with Fisher-Yates algorithm.
 * Code from https://stackoverflow.com/questions/6274339/how-can-i-shuffle-an-array
 */
function shuffle(a) {
    var j, x, i;
    for (i = a.length - 1; i > 0; i--) {
        j = Math.floor(Math.random() * (i + 1));
        x = a[i];
        a[i] = a[j];
        a[j] = x;
    }
    return a; 
} 

papers = shuffle(originalPapers)
console.log(papers) 

//Get user's personal first grade
let firstPaper = window.prompt("Please pick a 'paper' # from 0 to 9")







