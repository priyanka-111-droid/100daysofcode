from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank=[]
for x in question_data:
    text_for_each_question=x["text"]
    answer_for_each_question=x["answer"]

    new_question=Question(text_for_each_question,answer_for_each_question)

    question_bank.append(new_question)


quiz=QuizBrain(question_bank)


while quiz.still_has_questions()==True:
    quiz.next_question()

print("You have completed the quiz!!")
print(f"Final score is:{quiz.score}/{quiz.question_number}")
