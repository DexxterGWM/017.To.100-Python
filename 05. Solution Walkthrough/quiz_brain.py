# TODO-1: Asking the questions.

# TODO-2: Checking if the answer was correct.

# TODO-3: Checking if we're the end of the quiz

# Create a class called QuizBrain. Write an __init__ method. Initialise the question_number to 0. Initialise the question_list to an input.
# Retrieve the item at the current question_number from the question_list. Use the input() function to show the user the Question text and ask for the new user's answer.
# Create method called still_has_questions(). Return a boolean depending on the value of question_number. Use the while loop to show the next question until the end.

class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list
    
    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        
        user_answer = input(f' Q.{self.question_number}: {current_question.text} (True/False): ')