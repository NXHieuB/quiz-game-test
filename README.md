# quiz-game
Here is a sample Python code for a command-line quiz game that reads questions from a CSV file and presents them to the player one by one:
In this modified code, the load_questions() function reads the questions from the CSV file and returns them as a list of dictionaries. Each dictionary represents a question and contains the question text, a list of options, and the correct answer.

The ask_question() function takes a question as input, presents the question text and options to the player, and asks for their answer. If the player's answer matches the correct answer, it returns True, otherwise False.

The run_quiz() function loads the questions from the CSV file using the load_questions() function, presents each question to the player using the ask_question() function, and updates the player's score based on their answers. At the end of the quiz, the player's final score is displayed.

When you run the Python script, it will load the questions from the quiz_questions.csv file and present them to the player one by one. The player will have to choose an answer from a list of options, and their score will be displayed at the end of the quiz.

The ask_question() function takes an additional argument time_limit, which specifies the number of seconds the player has to answer the question. The function records the start time before presenting the question and options to the player, and then checks the elapsed time after the player has answered. If the elapsed time is greater than the time limit, the function returns False.

The run_quiz() function now takes an additional argument time_limit, which is passed to the ask_question() function for each question. The function records the player's score, stores it in the scores.txt file, and displays a list of high scores. However, the list of high scores is now limited to only the top 10 scores.
