import tkinter as tk
from tkinter import ttk
import time
import openpyxl
import random

def main():
    root = tk.Tk()
    root.title("Quiz Game")

    style = ttk.Style()
    style.configure('Background.TFrame', background='#f0f0f0')  # Set background color for frames
    style.configure('TButton', foreground='#ffffff', background='#4CAF50')  # Set button colors
    style.map('TButton', background=[('active', '#45a049')])

    def start_quiz():
        name = name_entry.get()
        roll_number = roll_number_entry.get()
        difficulty = difficulty_var.get()
        start_quiz_window(name, roll_number, difficulty)

    main_frame = ttk.Frame(root, style='Background.TFrame')
    main_frame.pack(expand=True, fill='both')

    welcome_label = ttk.Label(main_frame, text="Welcome to the Quiz Game!", font=('Arial', 24))
    welcome_label.pack(pady=20)

    name_label = ttk.Label(main_frame, text="Name:")
    name_label.pack()
    name_entry = ttk.Entry(main_frame)
    name_entry.pack()

    roll_number_label = ttk.Label(main_frame, text="Roll Number:")
    roll_number_label.pack()
    roll_number_entry = ttk.Entry(main_frame)
    roll_number_entry.pack()

    difficulty_label = ttk.Label(main_frame, text="Select Difficulty:")
    difficulty_label.pack()

    difficulty_var = tk.IntVar()
    easy_button = ttk.Radiobutton(main_frame, text="Easy 😀", variable=difficulty_var, value=1)
    easy_button.pack(anchor='w')

    medium_button = ttk.Radiobutton(main_frame, text="Medium 🙂", variable=difficulty_var, value=2)
    medium_button.pack(anchor='w')

    hard_button = ttk.Radiobutton(main_frame, text="Hard 😎", variable=difficulty_var, value=3)
    hard_button.pack(anchor='w')

    start_button = ttk.Button(main_frame, text="Start Quiz", command=start_quiz)
    start_button.pack(pady=20)

    def start_quiz_window(name, roll_number, difficulty):
        quiz_window = tk.Toplevel(root)
        quiz_window.title("Quiz Game")

        questions = get_questions(difficulty)

        score = {"value": 0}
        correct_answers = []

        def ask_question():
            nonlocal score
            if questions:
                question = questions.pop(0)
                correct_answers.append((question["question"], question["options"][question["correct_answer"]]))
                question_label = tk.Label(quiz_window, text=question["question"], font=("Arial", 16), background='#f0f0f0')
                question_label.pack(pady=10)

                shuffled_options = random.sample(question["options"], len(question["options"]))
                for i, option in enumerate(shuffled_options):
                    answer_button = ttk.Button(quiz_window, text=f"{i+1}. {option}", command=lambda i=i: handle_answer(i, question), style='Quiz.TButton')
                    answer_button.pack(side="top", pady=5)

                start_time = time.time()

                def handle_answer(answer_index, question):
                    nonlocal score
                    elapsed_time = time.time() - start_time
                    if elapsed_time <= 10 or difficulty < 3:  # Allow only 10 seconds for hard questions
                        if shuffled_options[answer_index] == question["options"][question["correct_answer"]]:
                            score["value"] += 1
                        for widget in quiz_window.winfo_children():
                            widget.destroy()
                        ask_question()
                    else:
                        for widget in quiz_window.winfo_children():
                            widget.destroy()
                        ask_question()

                timer_label = tk.Label(quiz_window, text="", font=("Arial", 14), background='#f0f0f0')
                timer_label.pack(pady=10)
                update_timer(timer_label, start_time)

                if len(correct_answers) > 1:
                    previous_button = ttk.Button(quiz_window, text="Previous", command=previous_question, style='Quiz.TButton')
                    previous_button.pack(side="top", pady=5)

            else:
                display_score(name, roll_number, score["value"], correct_answers)

        def previous_question():
            correct_answers.pop()
            score["value"] -= 1
            for widget in quiz_window.winfo_children():
                widget.destroy()
            ask_question()

        ask_question()

    root.mainloop()

def get_questions(difficulty):
    easy_questions = [
        {"question": "What is the capital of France?",
         "options": ["London", "Berlin", "Paris", "Rome"],
         "correct_answer": 2},
        {"question": "In which year did the first iPhone launch?",
         "options": ["2004", "2007", "2010", "2013"],
         "correct_answer": 1},
        {"question": "What is the capital of Japan?",
         "options": ["Beijing", "Tokyo", "Seoul", "Bangkok"],
         "correct_answer": 1},
        {"question": "Who wrote 'Romeo and Juliet'?",
         "options": ["William Shakespeare", "Jane Austen", "Charles Dickens", "Mark Twain"],
         "correct_answer": 0},
        {"question": "What is the largest mammal?",
         "options": ["Elephant", "Whale", "Giraffe", "Kangaroo"],
         "correct_answer": 1},
        {"question": "Which planet is known as the Red Planet?",
         "options": ["Venus", "Jupiter", "Mars", "Saturn"],
         "correct_answer": 2},
        {"question": "What is the chemical symbol for water?",
         "options": ["Wa", "Wo", "H2O", "O2"],
         "correct_answer": 2},
        {"question": "Who discovered penicillin?",
         "options": ["Alexander Fleming", "Marie Curie", "Louis Pasteur", "Isaac Newton"],
         "correct_answer": 0},
        {"question": "What is the currency of Germany?",
         "options": ["Euro", "Dollar", "Pound", "Yen"],
         "correct_answer": 0},
        {"question": "What is the tallest mountain in the world?",
         "options": ["Mount Kilimanjaro", "Mount Everest", "Mount Fuji", "Mount McKinley"],
         "correct_answer": 1}
    ]

    medium_questions = [
        {"question": "What is the square root of 25?",
         "options": ["2", "5", "10", "None of these"],
         "correct_answer": 0},
        {"question": "The largest country in the world by land area is:",
         "options": ["Russia", "Canada", "China", "United States"],
         "correct_answer": 0},
        {"question": "Who painted the Mona Lisa?",
         "options": ["Vincent van Gogh", "Leonardo da Vinci", "Pablo Picasso", "Michelangelo"],
         "correct_answer": 1},
        {"question": "Which gas do plants absorb during photosynthesis?",
         "options": ["Oxygen", "Carbon Dioxide", "Nitrogen", "Hydrogen"],
         "correct_answer": 1},
        {"question": "What is the currency of France?",
         "options": ["Euro", "Pound", "Dollar", "Yen"],
         "correct_answer": 0},
        {"question": "What is the capital of Australia?",
         "options": ["Melbourne", "Sydney", "Canberra", "Brisbane"],
         "correct_answer": 2},
        {"question": "Who invented the telephone?",
         "options": ["Thomas Edison", "Alexander Graham Bell", "Guglielmo Marconi", "Nikola Tesla"],
         "correct_answer": 1},
        {"question": "What is the chemical symbol for gold?",
         "options": ["Au", "Ag", "Fe", "Hg"],
         "correct_answer": 0},
        {"question": "Which planet is known as the Blue Planet?",
         "options": ["Earth", "Neptune", "Uranus", "Pluto"],
         "correct_answer": 0},
        {"question": "Who wrote 'To Kill a Mockingbird'?",
         "options": ["Harper Lee", "Ernest Hemingway", "F. Scott Fitzgerald", "John Steinbeck"],
         "correct_answer": 0}
    ]

    hard_questions = [
        {"question": "What is the first element in the periodic table?",
         "options": ["Hydrogen", "Helium", "Lithium", "Beryllium"],
         "correct_answer": 0},
        {"question": "What is the capital of Nepal?",
         "options": ["Kathmandu", "Delhi", "Islamabad", "Dhaka"],
         "correct_answer": 0},
        {"question": "Who is the author of 'The Great Gatsby'?",
         "options": ["F. Scott Fitzgerald", "Ernest Hemingway", "John Steinbeck", "Harper Lee"],
         "correct_answer": 0},
        {"question": "Which is the largest ocean on Earth?",
         "options": ["Atlantic Ocean", "Indian Ocean", "Arctic Ocean", "Pacific Ocean"],
         "correct_answer": 3},
        {"question": "Who discovered the theory of relativity?",
         "options": ["Isaac Newton", "Albert Einstein", "Galileo Galilei", "Stephen Hawking"],
         "correct_answer": 1},
        {"question": "Which country is known as the Land of the Rising Sun?",
         "options": ["China", "Japan", "South Korea", "Thailand"],
         "correct_answer": 1},
        {"question": "What is the chemical formula for table salt?",
         "options": ["NaCl", "H2O", "C6H12O6", "CO2"],
         "correct_answer": 0},
        {"question": "Who painted the famous artwork 'The Starry Night'?",
         "options": ["Vincent van Gogh", "Leonardo da Vinci", "Pablo Picasso", "Michelangelo"],
         "correct_answer": 0},
        {"question": "What is the largest desert in the world?",
         "options": ["Sahara Desert", "Arabian Desert", "Gobi Desert", "Antarctica Desert"],
         "correct_answer": 0},
        {"question": "What is the speed of light in a vacuum?",
         "options": ["299,792,458 meters per second", "300,000,000 meters per second", "100,000,000 meters per second", "500,000,000 meters per second"],
         "correct_answer": 0}
    ]

    if difficulty == 1:
        if len(easy_questions) >= 10:
            return random.sample(easy_questions, 10)  # Select 10 random easy questions
        else:
            return easy_questions
    elif difficulty == 2:
        if len(medium_questions) >= 10:
            return random.sample(medium_questions, 10)  # Select 10 random medium questions
        else:
            return medium_questions
    elif difficulty == 3:
        if len(hard_questions) >= 10:
            return random.sample(hard_questions, 10)  # Select 10 random hard questions
        else:
            return hard_questions

def update_timer(label, start_time):
    elapsed_time = int(time.time() - start_time)
    remaining_time = max(0, 10 - elapsed_time)
    label.config(text=f"Time left: {remaining_time} seconds", background='#f0f0f0')
    if remaining_time > 0:
        label.after(1000, update_timer, label, start_time)

def display_score(name, roll_number, score, correct_answers):
    score_window = tk.Toplevel()
    score_window.title("Quiz Score")

    score_frame = ttk.Frame(score_window, padding=20, style='Background.TFrame')
    score_frame.pack()

    score_label = ttk.Label(score_frame, text=f"🎉 Congratulations {name} ({roll_number})! 🎉\nYour final score is: {score}/10", font=("Arial", 16))
    score_label.pack(pady=10)

    compliment_label = ttk.Label(score_frame, text=compliment(score, name), font=("Arial", 12))
    compliment_label.pack(pady=10)

    for question, answer in correct_answers:
        answer_label = ttk.Label(score_frame, text=f"{question}: {answer}", font=("Arial", 12))
        answer_label.pack()

    score_window.mainloop()

def compliment(score, name):  # Updated compliment function
    if score >= 8:
        return 'That was GREAT!! ' + name
    elif score > 5:
        return 'NOT BAD!! ' + name
    elif score > 3:
        return 'Ohh NO,That was not Good!! ' + name
    elif score <= 3:
        return 'Ohh NO, You need Serious Focus ' + name


if __name__ == "__main__":
    main()
