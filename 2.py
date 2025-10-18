import random

def load_questions(filename):
    questions = []
    with open(filename,'r') as f:
        for line in f:
            if ',' in line:
                question,answer = line.strip().split(',',1)
                questions.append((question,answer))
    return questions

def quiz_game():
    questions = load_questions('questions.txt')
    random.shuffle(questions)
    score = 0
    asked = 0
    
    print('Welcome to the Flashcard Quiz')
    print("Type 'quit' to stop playing\n")
    
    for i ,(question,answer) in enumerate(questions,1):
        user_answer = input(f"{i}.{question}").strip()
        
        
        if user_answer.lower() == 'quit':
            break
        
        asked += 1
        
        if user_answer.lower() == answer.lower().strip():
            print("correct answer!\n")
            score += 1
        else:
            print(f"wrong answer! The correct answer was : {answer}\n")
            
    print(f" Quiz finished! Your final score was {score} out of {asked}")
    

if __name__ == "__main__":
    quiz_game()
        