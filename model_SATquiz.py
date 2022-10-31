import random

SAT_data = []
SAT_questions = {
    "response_code":0,
    "results":[{"question":"The average number of students per classroom, y, at Central High School can be estimated using the equation y = 0.8636x + 27.227, where x represents the number of years since 2004 and x ≤ 10. Which of the following statements is the best interpretation of the number 0.8636 in the context of this problem?", "correct_answer":"The estimated yearly increase in the average number of students per classroom", "incorrect_answers":["The estimated average number of students per classroom in 2004","The estimated average number of students per classroom in 2014","The estimated yearly decrease in the average number of students per classroom"]},
    {"question":"In the complex number system, which of the following is equal to (14 − 2i)(7 + 12i)?","correct_answer":"122 + 154i","incorrect_answers":["74","122","74 + 154i"]},
    {"question":"The recommended daily calcium intake for a 20-year-old person is 1,000 milligrams (mg). One cup of milk contains 299 mg of calcium and one cup of juice contains 261 mg of calcium. Which of the following inequalities represents the possible number of cups of milk, m, and cups of juice, j, a 20-year-old person could drink in a day to meet or exceed the recommended daily calcium intake from these drinks alone?","correct_answer":"299m + 261j ≥ 1,000","incorrect_answers":["299m + 261j > 1,000","299/m + 261/j ≥ 1,000","299/m + 261/j > 1,000"]},
    {"question":"The graph of y = (2x − 4)(x − 4) is a parabola in the xy-plane. In which of the following equivalent equations do the x- and y-coordinates of the vertex of the parabola appear as constants or coefficients?","correct_answer":"y=2(x-3)² - 2","incorrect_answers":["y = 2x² - 12x + 16"," y = 2x(x − 6) + 16","y = (x − 2)(2x − 8)"]},
    {"question":"If y = x³ + 2x + 5 and z = x² + 7x + 1, what is 2y + z in terms of x?","correct_answer":"2x³ + x² + 11x + 11","incorrect_answers":["3x³ + 11x + 11","2x³ + x² + 9x + 6","2x³ + 2x² + 18x + 12"]},
    {"question":"A company’s manager estimated that the cost C, in dollars, of producing n items is C = 7n + 350. The company sells each item for $12. The company makes a profit when the total income from selling a quantity of items is greater than the total cost of producing that quantity of items. Which of the following inequalities gives all possible values of n for which the manager estimates that the company will make a profit?","correct_answer":"n > 70","incorrect_answers":[" n < 70","n < 84","n > 84"]},
    {"question":"At a primate reserve, the mean age of all the male primates is 15 years, and the mean age of all female primates is 19 years. Which of the following must be true about the mean age m of the combined group of male and female primates at the primate reserve?","correct_answer":"15 < m < 19","incorrect_answers":["m = 17","m > 17","m < 17"]},
    {"question":"A researcher wanted to know if there is an association between exercise and sleep for the population of 16-year-olds in the United States. She obtained survey responses from a random sample of 2,000 United States 16-year-olds and found convincing evidence of a positive association between exercise and sleep. Which of the following conclusions is well supported by the data?","correct_answer":"There is a positive association between exercise and sleep for 16-year-olds in the United States.","incorrect_answers":["There is a positive association between exercise and sleep for 16-year-olds in the world.","Using exercise and sleep as defined by the study, an increase in sleep is caused by an increase of exercise for 16-year-olds in the United States.","Using exercise and sleep as defined by the study, an increase in sleep is caused by an increase of exercise for 16-year-olds in the world."]},
    {"question":"A biology class at Central High School predicted that a local population of animals will double in size every 12 years. The population at the beginning of 2014 was estimated to be 50 animals. If P represents the population n years after 2014, then which of the following equations represents the class’s model of the population over time?","correct_answer":"P = 50(2)^n/12","incorrect_answers":["P = 12 + 50n","P = 50 + 12n","P = 50(2)^(12n)"]},
    {"question":"What country hosted the 2014 Winter Olympics?","correct_answer":"Russia","incorrect_answers":["Canada","United States","Germany"]}]
}

def initSAT():
    # setup jokes into a dictionary with id, joke, haha, boohoo
    item_id = 0
    for item in SAT_questions:
        SAT_data.append({"id": item_id, "question": item})
        item_id += 1
    # prime some haha responses
    for i in range(10):
        id = getRandomQuestion()['id']
    # prime some haha responses
    for i in range(5):
        id = getRandomQuestion()['id']
        
# Return all jokes from jokes_data
def getSAT():
    return(SAT_data)

# Joke getter
def getSAT(id):
    return(SAT_data[id])

# Return random joke from jokes_data
def getRandomQuestion():
    return(random.choice(SAT_data))

# Pretty Print joke
def printQuestion(question):
    print(question['id'], question['question'], "\n")

# Number of jokes
def countQuestion():
    return len(SAT_data)

# Test Joke Model
if __name__ == "__main__": 
    initSAT()  # initialize jokes

    # Random joke
    print("Random joke")
    printQuestion(getRandomQuestion())
    
    # Count of Jokes
    print("Jokes Count: " + str(countQuestion()))