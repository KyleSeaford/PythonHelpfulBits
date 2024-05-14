# Description: This file contains functions that prompt the user for input.

def questionString(question, defaultAnswer):
    answer = input(f"{question} [{defaultAnswer}]")
    if answer == "":
        answer = defaultAnswer
    return answer    

def questionInt(question, defaultAnswer):
    answer = questionString(question, defaultAnswer)
    answer = answer.strip()
    if answer.isdigit() == False:
        raise Exception("Invalid input, Please enter an integer")
    return int(answer)

def questionIntWithRange(question, defaultAnswer, minValue, maxValue):
    answer = questionInt(question, defaultAnswer)
    if answer > maxValue:
        raise Exception(f"Invalid input, Please enter an integer less than {maxValue}")    
    if answer <= minValue:
        raise Exception(f"Invalid input, Please enter an integer greater than {minValue}")   
    return answer

def questionChoices(question, defaultAnswer, choices):
    answer = questionString(question, defaultAnswer)
    answer = answer.lower().strip()
    if answer not in choices:
        raise Exception(f"Invalid input, Please enter one of the following: {choices}")
    return answer

def questionChoicesLoop(question, defaultAnswer, choices):
    while True:
        try:
            answer = questionChoices(question, defaultAnswer, choices)
            return answer
        except Exception as e:
            print(e)

def questionStringLoop(question, defaultAnswer):
    while True:
        try:
            answer = questionString(question, defaultAnswer)
            return answer
        except Exception as e:
            print(e)

def questionIntLoop(question, defaultAnswer):
    while True:
        try:
            answer = questionInt(question, defaultAnswer)
            return answer
        except Exception as e:
            print(e)

def questionIntWithRangeLoop(question, defaultAnswer, minValue, maxValue):
    while True:
        try:
            answer = questionIntWithRange(question, defaultAnswer, minValue, maxValue)
            return answer
        except Exception as e:
            print(e)

def questionStringBlank(question, defaultAnswer):
    answer = input(f"{question} {defaultAnswer}")
    if answer == "":
        answer = defaultAnswer
    return answer

