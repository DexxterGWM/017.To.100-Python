# TODO-1: Asking the questions.

# TODO-2: Checking if the answer was correct.

# TODO-3: Checking if we're the end of the quiz

# Create a class called QuizBrain. Write an __init__ method. Initialise the question_number to 0. Initialise the question_list to an input.
# Retrieve the item at the current question_number from the question_list. Use the input() function to show the user the Question text and ask for the new user's answer.

class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
    
    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        input(f' Q.{self.question_number}: {current_question.text} (True/False): ')