def one_piece_quiz():
    """Simple One Piece trivia game"""
    
    questions = {
        "What is Luffy's dream?": "king of the pirates",
        "What is the name of Luffy's ship?": "thousand sunny",
        "How many crew members does Luffy have?": "10",
    }
    
    score = 0
    print("=== One Piece Trivia Quiz ===\n")
    
    for question, answer in questions.items():
        user_answer = input(f"{question} ").lower().strip()
        
        if user_answer == answer:
            print("✓ Correct!\n")
            score += 1
        else:
            print(f"✗ Wrong! Answer: {answer}\n")
    
    print(f"Final Score: {score}/{len(questions)}")

if __name__ == "__main__":
    one_piece_quiz()