# Write a for loop to iterate over the question_data. Create a Question object from each entry in question_data. Append each Question object to the question_bank.

from question_model import Question
from data import question_data

question_bank = []

for question in question_data:
    question_text = question['text']
    question_answer = question['answer']
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)