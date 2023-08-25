import random
import tkinter as tk
from tkinter import messagebox, filedialog
import tkinter.ttk as ttk

# List of US states and their capitals
states_and_capitals = {
    'West Virginia': 'Charleston',
    'Colorado': 'Denver',
    # Add more states and capitals here
}

# Function to generate wrong answer options
def generate_wrong_answers(correct_answer, all_answers):
    wrong_answers = list(set(all_answers) - set([correct_answer]))
    return random.sample(wrong_answers, 3)

# Function to generate quizzes and answer keys
def generate_quizzes():
    num_quizzes = int(num_quizzes_entry.get())
    num_questions = int(num_questions_entry.get())
    output_folder = output_folder_var.get()

    for quiz_num in range(num_quizzes):
        quiz_filename = f'{output_folder}/capitalsquiz{quiz_num + 1}.txt'
        answer_key_filename = f'{output_folder}/capitalsquiz_answers{quiz_num + 1}.txt'

        with open(quiz_filename, 'w') as quiz_file, open(answer_key_filename, 'w') as answer_key_file:
            quiz_file.write(f"Name:\n\nDate:\n\nPeriod:\n\nState Capitals Quiz (Form {quiz_num + 1})\n\n")

            states = list(states_and_capitals.keys())
            random.shuffle(states)

            for question_num in range(num_questions):
                correct_answer = states_and_capitals[states[question_num]]
                wrong_answers = generate_wrong_answers(correct_answer, list(states_and_capitals.values()))
                all_answers = [correct_answer] + wrong_answers
                random.shuffle(all_answers)

                quiz_file.write(f"{question_num + 1}. What is the capital of {states[question_num]}?\n")
                for i in range(4):
                    quiz_file.write(f"{['A', 'B', 'C', 'D'][i]}. {all_answers[i]}\n")
                quiz_file.write('\n')

                answer_key_file.write(f"{question_num + 1}. {correct_answer}\n")

    messagebox.showinfo("Success", "Quizzes and answer keys generated successfully.")

# Create the main window
root = tk.Tk()
root.title("US State Capitals Quiz Generator")

# Styling using the 'clam' theme
style = ttk.Style()
style.theme_use("clam")

# Labels and entry fields
ttk.Label(root, text="Number of Quizzes:").pack(pady=5)
num_quizzes_entry = ttk.Entry(root)
num_quizzes_entry.pack()

ttk.Label(root, text="Number of Questions per Quiz:").pack(pady=5)
num_questions_entry = ttk.Entry(root)
num_questions_entry.pack()

output_folder_var = tk.StringVar()
output_folder_var.set("output")
ttk.Label(root, text="Output Folder:").pack(pady=5)
output_folder_entry = ttk.Entry(root, textvariable=output_folder_var)
output_folder_entry.pack(side=tk.LEFT)
output_folder_button = ttk.Button(root, text="Browse", command=choose_output_folder)
output_folder_button.pack(side=tk.LEFT, padx=5)

def choose_output_folder():
    folder_selected = filedialog.askdirectory()
    output_folder_var.set(folder_selected)

generate_button = ttk.Button(root, text="Generate Quizzes", command=generate_quizzes)
generate_button.pack(pady=10)

root.mainloop()
