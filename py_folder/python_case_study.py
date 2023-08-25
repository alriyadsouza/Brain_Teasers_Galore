import random
import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk

# List of US states and their capitals
states_and_capitals = {
    'Alabama': 'Montgomery',
    'Alaska': 'Juneau',
    'Arizona': 'Phoenix',
    'Arkansas': 'Little Rock',
    'California': 'Sacramento',
    'Colorado': 'Denver',
    'Connecticut': 'Hartford',
    'Delaware': 'Dover',
    'Florida': 'Tallahassee',
    'Georgia': 'Atlanta',
    'Hawaii': 'Honolulu',
    'Idaho': 'Boise',
    'Illinois': 'Springfield',
    'Indiana': 'Indianapolis',
    'Iowa': 'Des Moines',
    'Kansas': 'Topeka',
    'Kentucky': 'Frankfort',
    'Louisiana': 'Baton Rouge',
    'Maine': 'Augusta',
    'Maryland': 'Annapolis',
    'Massachusetts': 'Boston',
    'Michigan': 'Lansing',
    'Minnesota': 'St. Paul',
    'Mississippi': 'Jackson',
    'Missouri': 'Jefferson City',
    'Montana': 'Helena',
    'Nebraska': 'Lincoln',
    'Nevada': 'Carson City',
    'New Hampshire': 'Concord',
    'New Jersey': 'Trenton',
    'New Mexico': 'Santa Fe',
    'New York': 'Albany',
    'North Carolina': 'Raleigh',
    'North Dakota': 'Bismarck',
    'Ohio': 'Columbus',
    'Oklahoma': 'Oklahoma City',
    'Oregon': 'Salem',
    'Pennsylvania': 'Harrisburg',
    'Rhode Island': 'Providence',
    'South Carolina': 'Columbia',
    'South Dakota': 'Pierre',
    'Tennessee': 'Nashville',
    'Texas': 'Austin',
    'Utah': 'Salt Lake City',
    'Vermont': 'Montpelier',
    'Virginia': 'Richmond',
    'Washington': 'Olympia',
    'West Virginia': 'Charleston',
    'Wisconsin': 'Madison',
    'Wyoming': 'Cheyenne'
}



# Function to generate wrong answer options
def generate_wrong_answers(correct_answer, all_answers):
    wrong_answers = list(set(all_answers) - set([correct_answer]))
    return random.sample(wrong_answers, 3)

# Function to generate quizzes and answer keys
def generate_quizzes():
    num_quizzes = int(num_quizzes_entry.get())
    num_questions = 50  # Fixed to 50 questions per quiz
    output_folder = output_folder_var.get()

    for quiz_num in range(num_quizzes):
        quiz_filename = f'C:/Users/User/Desktop/py_folder/output/capitalsquiz{quiz_num + 1}.txt'
        answer_key_filename = f'C:/Users/User/Desktop/py_folder/output/capitalsquiz_answers{quiz_num + 1}.txt'

        with open(quiz_filename, 'w') as quiz_file, open(answer_key_filename, 'w') as answer_key_file:
            quiz_file.write(f"Name:\n\nDate:\n\nPeriod:\n\nState Capitals Quiz (Form {quiz_num + 1})\n\n")

            states = list(states_and_capitals.keys()) * (num_questions // len(states_and_capitals))
            random.shuffle(states)

            for question_num in range(num_questions):
                state = states[question_num]
                correct_answer = states_and_capitals[state]
                wrong_answers = generate_wrong_answers(correct_answer, list(states_and_capitals.values()))
                all_answers = [correct_answer] + wrong_answers
                random.shuffle(all_answers)

                quiz_file.write(f"{question_num + 1}. What is the capital of {state}?\n")
                for i, answer in enumerate(all_answers):
                    quiz_file.write(f"{chr(ord('A') + i)}. {answer}\n")
                quiz_file.write('\n')

                answer_key_file.write(f"{question_num + 1}. {correct_answer}\n")

    messagebox.showinfo("Success", "Quizzes and answer keys generated successfully.")


# Create the main window
root = tk.Tk()
root.title("US State Capitals Quiz Generator")

# Set the background color to white
root.configure(bg="antiquewhite")

# Custom font
custom_font = ("Helvetica", 14)
heading_font = ("Helvetica", 24, "bold")
label_font = ("Helvetica", 14)

# Create a function to add a horizontal line for visual separation
def add_horizontal_line():
    tk.Label(root, bg="antiquewhite", height=1).pack(fill="x", pady=5)

# Heading
add_horizontal_line()
heading_label = tk.Label(root, text="QUIZ GENERATOR", font=heading_font, bg="antiquewhite")
heading_label.pack(pady=5)

# Load the GIF image
image_path = "C:/Users/User/Desktop/py_folder/quiz_time.png"
image = Image.open(image_path)
image = image.resize((300, 200))  # Resize the image if needed
photo = ImageTk.PhotoImage(image)

# Create a label to display the image
image_label = tk.Label(root, image=photo, bg="antiquewhite")
image_label.image = photo  # Keep a reference to the photo to prevent it from being garbage collected
image_label.pack(pady=5)

# Label and entry fields
tk.Label(root, text="Number of Quizzes:", font=custom_font, bg="antiquewhite").pack(pady=(50, 0))
num_quizzes_entry = tk.Entry(root, font=custom_font)
num_quizzes_entry.pack()
add_horizontal_line()

tk.Label(root, text="Number of Questions per Quiz:", font=custom_font, bg="antiquewhite").pack()
num_questions_entry = tk.Entry(root, font=custom_font)
num_questions_entry.pack()
add_horizontal_line()

output_folder_var = tk.StringVar()
output_folder_var.set("output")
output_folder_label = tk.Label(root, text="Output Folder:", font=custom_font, bg="antiquewhite")
output_folder_label.pack()
output_folder_entry = tk.Entry(root, textvariable=output_folder_var, font=custom_font)
output_folder_entry.pack()
add_horizontal_line()

def choose_output_folder():
    folder_selected = filedialog.askdirectory()
    output_folder_var.set(folder_selected)

output_folder_button = tk.Button(root, text="Browse", font=custom_font, bg="lightcoral", command=choose_output_folder)
output_folder_button.pack(pady=(5, 20))
add_horizontal_line()

generate_button = tk.Button(root, text="Generate Quizzes", font=custom_font, bg="lightcoral", command=generate_quizzes)
generate_button.pack()

# Exit full-screen mode on Escape key press
def exit_fullscreen(event):
    root.attributes("-fullscreen", False)

root.bind("<Escape>", exit_fullscreen)

# Set full-screen mode
root.attributes('-fullscreen', True)

root.mainloop()
