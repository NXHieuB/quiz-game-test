import csv

def load_questions(file_path):
    questions = []
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            question = {
                'text': row[0],
                'options': row[1:5],
                'answer': row[5]
            }
            questions.append(question)
    return questions

def ask_question(question):
    print(question['text'])
    for i, option in enumerate(question['options']):
        print(f"{i+1}. {option}")
    answer = input("Your answer (1-4): ")
    print()
    return answer == question['answer']

def run_quiz():
    file_path = 'quiz_questions.csv'
    questions = load_questions(file_path)
    score = 0
    for question in questions:
        if ask_question(question):
            score += 1
    print(f"Your final score is {score}/{len(questions)}.")

    # Storing the score in a file
    with open('scores.txt', 'a') as file:
        file.write(f"{score}\n")

    # Displaying the list of high scores
    print("High scores:")
    with open('scores.txt', 'r') as file:
        scores = [int(line.strip()) for line in file]
        scores.sort(reverse=True)
        for i, score in enumerate(scores):
            print(f"{i+1}. {score}")

if __name__ == "__main__":
    run_quiz()
