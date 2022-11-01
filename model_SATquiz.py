import random

SAT_data = []
SAT_questions = [
    {"question":"After having his tonsels removed, the child was listless for a few days.", "correct_answer":"Spelling", "incorrect_answers":["Capitalization","Grammar","Punctuation"]},
    {"question":"In the complex number system, which of the following is equal to (14 − 2i)(7 + 12i)?","correct_answer":"122 + 154i","incorrect_answers":["74","122","74 + 154i"]},
    {"question":"The intricacy of the mathematical equation, drove the student trying to solve it crazy.","correct_answer":"Punctuation","incorrect_answers":["Spelling","Capitalization","Grammar"]},
    {"question":"The graph of y = (2x − 4)(x − 4) is a parabola in the xy-plane. In which of the following equivalent equations do the x- and y-coordinates of the vertex of the parabola appear as constants or coefficients?","correct_answer":"y=2(x-3)² - 2","incorrect_answers":["y = 2x² - 12x + 16"," y = 2x(x − 6) + 16","y = (x − 2)(2x − 8)"]},
    {"question":"If y = x³ + 2x + 5 and z = x² + 7x + 1, what is 2y + z in terms of x?","correct_answer":"2x³ + x² + 11x + 11","incorrect_answers":["3x³ + 11x + 11","2x³ + x² + 9x + 6","2x³ + 2x² + 18x + 12"]},
    {"question":"The hybrid tomatoes is immune to most common diseases.","correct_answer":"Grammar","incorrect_answers":["Spelling","Capitalization","Punctuation"]},
    {"question":"At a primate reserve, the mean age of all the male primates is 15 years, and the mean age of all female primates is 19 years. Which of the following must be true about the mean age m of the combined group of male and female primates at the primate reserve?","correct_answer":"15 < m < 19","incorrect_answers":["m = 17","m > 17","m < 17"]},
    {"question":"Nurses plays a vital role in the healthcare profession.","correct_answer":"Grammar","incorrect_answers":["Spelling","Capitalization","Punctuation"]},
    {"question":"If y = kx + 2k, where k is a constant, and if y = -14 when x = 5, what is the value of x when y = -24?","correct_answer":"10","incorrect_answers":["-10","-24","-2"]},
    {"question":"The bachalor never married. Most people thought it was because of misogyny.","correct_answer":"Spelling","incorrect_answers":["Punctuation","Capitalization","Grammar"]}]


def initSAT():
    # setup jokes into a dictionary with id, joke, haha, boohoo
    item_id = 0
    for item in SAT_questions:
        SAT_data.append({"id": item_id, "results": item})
        item_id += 1
        
# Return all jokes from jokes_data
def getSAT():
    return(SAT_data)

# Joke getter
def getSATq(id):
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