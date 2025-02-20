import sys
import os

def check_python_installed(): 
    print("checking if python is installed")
    if sys.version_info.major < 3 or (sys.version_info.major == 3 and sys.version_info.minor < 6):
        print("Python 3.6 or higher is required to run this script.")
        sys.exit(1)
    else:
        print(f"Python {sys.version_info.major}.{sys.version_info.minor} is installed. You're good to go!\n")



def quiz():
    questions = [
        {
            "question": "What is the capital of France?",
            "options": ["A. Paris", "B. London", "C. Berlin", "D. Madrid"],
            "answer": "A"
        },
        {
            "question": "Which Python keyword is used to define a function?",
            "options": ["A. func", "B. define", "C. def", "D. function"],
            "answer": "C"
        },
        {
            "question": "Who directed the movie 'Inception'?",
            "options": ["A. Steven Spielberg", "B. Christopher Nolan", "C. Quentin Tarantino", "D. James Cameron"],
            "answer": "B"
        },
        {
            "question": "What is the output of `print(2 ** 3)` in Python?",
            "options": ["A. 6", "B. 8", "C. 9", "D. 12"],
            "answer": "B"
        },
        {
            "question": "Which of the following is NOT a Python data type?",
            "options": ["A. int", "B. float", "C. string", "D. char"],
            "answer": "D"
        }
    ]

    score = 0
           
    print("Welcome to the Quiz!\n")
    for i, q in enumerate(questions, 1):
        print(f"Question {i}: {q['question']}")
        for option in q['options']:
            print(option)
        user_answer = input("Your answer (A/B/C/D): ").strip().upper()
        if user_answer == q['answer']:
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! The correct answer is {q['answer']}.\n")

    print(f"Quiz ended! Your final score is {score}/{len(questions)}.\n")

def main():
    check_python_installed()
    while True:
        quiz()
        play_again = input("Do you want to play again? (yes/no): ").strip().lower()
        if play_again != "yes":
            print("Thanks for playing! Goodbye!")
            break

if __name__ == "__main__":
    main()
