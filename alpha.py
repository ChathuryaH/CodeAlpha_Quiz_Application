class Question:
    def __init__(self, text, choices, correct_answer):
        self.text = text
        self.choices = choices
        self.correct_answer = correct_answer

    def is_correct(self, answer):
        return answer.lower() == self.correct_answer.lower()

class Quiz:
    def __init__(self):
        self.questions = []
        self.score = 0

    def add_question(self, question):
        self.questions.append(question)

    def start_quiz(self):
        for i, question in enumerate(self.questions, 1):
            print(f"Question {i}: {question.text}")
            for j, choice in enumerate(question.choices, 1):
                print(f"{j}. {choice}")
            
            user_answer = input("Your answer (enter the number): ")
            if question.is_correct(user_answer):
                print("Correct!\n")
                self.score += 1
            else:
                print(f"Wrong! The correct answer was {question.correct_answer}\n")
        
        self.display_score()

    def display_score(self):
        total_questions = len(self.questions)
        print(f"You scored {self.score} out of {total_questions} questions correctly.")

if __name__ == "__main__":
    quiz = Quiz()

    # Example questions
    q1 = Question("What is the capital of France?", ["London", "Berlin", "Paris"], "Paris")
    q2 = Question("Which planet is known as the Red Planet?", ["Earth", "Mars", "Venus"], "Mars")
    q3 = Question("What is 2 + 2?", ["3", "4", "5"], "4")

    quiz.add_question(q1)
    quiz.add_question(q2)
    quiz.add_question(q3)

    print("Welcome to the Quiz!")
    quiz.start_quiz()
