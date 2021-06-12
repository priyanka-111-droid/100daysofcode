# Quiz project

Fork or download project from [here](https://replit.com/@appbrewery/quiz-game-start)

Question asked to user,they reply True or False and then update their scores.

## Part 1:Creating question class

Task:In question_model.py,create Question class with `__init__()`method and two attributes:text and answer 

## Part 2:Create List(question bank) of Question objects

Task1:in main.py, from question_model import Question and from data import question_data

Task2:create question bank with list of question objects each initialized with question and answer.

## Part 3:The QuizBrain and next_question() method

Task1:create class QuizBrain.Write __init__() method.Set question_number to 0,question_list to an input.

Task2:create function next_question() that for displaying current question number and current question text to user.

Task3:in main.py,from quiz_brain import QuizBrain.

## Part 4:How to continue showing new questions?

Task1:In quiz_brain.py,create function still_has_questions() that will return True if current question number is less than number of questions in question list.

Task2:In main.py,run while loop with condition that if still_has_questions() is True,move to next question.

## Part 5:Check answer,keep score.

Task1:in quiz_brain.py,set variable score to 0

Task2:In quizbrain.py,create function check_answer() to see if user's answer matches correct answer,if yes,then increase score.Print correct answer and score after each question.

Task3:In main,py,after finishing all questions,print final score of user.