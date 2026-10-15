print("================================")
print("       WELCOME TO QUIZMASTER")
print("================================")

name = input("Enter your name: ")

print(f"Hello, {name}!")
print("Let's start the quiz!")

replay=True
questions=[
        {
        "question":"Which language are we using to build this project?",
        "options":["A. Java", "B. Python", "C. C++", "D. JavaScript"],
        "answer":"B"
        },
        {
            "question": "Which data structure follows FIFO?",
            "options": ["A. Stack", "B. Queue", "C. Tree", "D. Graph"],
            "answer": "B"
        },
        {
            "question": "Which keyword defines a function in Python?",
            "options": ["A. func", "B. define", "C. def", "D. function"],
            "answer": "C"
        },
        {
            "question": "Which symbol starts a comment in Python?",
            "options": ["A. //", "B. #", "C. /*", "D. $"],
            "answer": "B"
        },
        {
            "question": "Which data type stores True or False?",
            "options": ["A. int", "B. str", "C. bool", "D. list"],
            "answer": "C"
        }
    ]
while replay:
    score=0
    for i,q in enumerate(questions,start=1):
        print(f"Question {i}:{q['question']}")
        
        for o in q["options"]:
            print(o)
        while True:    
            ans=input("Enter your answer (A/B/C/D): ").strip().upper()
            if(ans in ["A","B","C","D"]):
                break
            else:
                print("Invalid input! Please enter A, B, C, or D.")
        if ans == q["answer"]:
            print("Correct answer!")
            score += 1
        else:
            print(f"Wrong answer! The correct answer is {q['answer']}.")

    total_questions = len(questions)
    percentage = (score / total_questions) * 100

    print("\n==============================")
    print(f"Player: {name}")
    print(f"Final score: {score}/{total_questions}")
    print(f"Percentage: {percentage:.2f}%")

    if percentage >= 80:
        print("Performance: Excellent!")
    elif percentage >= 60:
        print("Performance: Good!")
    elif percentage >= 40:
        print("Performance: Average!")
    else:
        print("Performance: Keep practicing!")

    print("==============================")
    while True:
        reply=input("Do you want to play again? (yes/no):").strip().lower()
        if (reply=='yes' or reply=='no'):
            if reply=="no":
                print("GOODBYE!")
                replay=False
            break
        else:
            print("Invalid input! Please enter yes or no.")    
        
    