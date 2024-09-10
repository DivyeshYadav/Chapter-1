def display_question(question, options):
  """Displays a question and its multiple-choice options."""
  print(question)
  for i, option in enumerate(options):
    print(f"({i+1}) {option}")

def get_user_answer():
  """Gets the user's answer input and validates it."""
  while True:
    try:
      answer = int(input("Enter your answer number: "))
      if 1 <= answer <= len(options):
        return answer
      else:
        print("Invalid answer. Please enter a number between 1 and", len(options))
    except ValueError:
      print("Invalid input. Please enter a number.")

def check_answer(answer, correct_answer):
  """Checks if the user's answer is correct."""
  if answer == correct_answer:
    print("Correct!")
    return True
  else:
    print("Incorrect.")
    return False

# Quiz questions and answers
questions = [
    "What is the capital of France?",
    "Who painted the Mona Lisa?",
    "What is the highest mountain in the world?"
]

options = [
    ["Berlin", "Paris", "Madrid", "Rome"],
    ["Michelangelo", "Leonardo da Vinci", "Raphael", "Donatello"],
    ["Mount Everest", "K2", "Kangchenjunga", "Lhotse"]
]

correct_answers = [2, 2, 1]  # Index of the correct answer in each options list

# Start the quiz
score = 0
for i, question in enumerate(questions):
  display_question(question, options[i])
  user_answer = get_user_answer()
  if check_answer(user_answer, correct_answers[i]):
    score += 1

# Display final score
print("\nQuiz finished! Your final score is:", score, "out of", len(questions))