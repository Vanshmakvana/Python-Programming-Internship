import time

def get_bot_response(user_input):
    """
    Processes the user's input and returns a predefined response
    based on conditional logic (if-elif-else).
    """
    # Clean input: convert to lowercase and remove leading/trailing whitespace
    cleaned_input = user_input.strip().lower()

    # Predefined rules and matching
    if cleaned_input in ["hello", "hi", "hey", "greetings"]:
        return "Hi there! How can I help you today?"
    
    elif cleaned_input in ["how are you", "how are you?", "how is it going"]:
        return "I'm doing great, thanks for asking! How are you?"
    
    elif "name" in cleaned_input:
        return "I am AlphaBot, your friendly Python assistant!"
    
    elif cleaned_input in ["what can you do", "help"]:
        return "I can chat with you! Try saying 'hello', 'how are you', 'name', or 'bye'."
    
    elif cleaned_input in ["bye", "goodbye", "exit", "quit"]:
        return "Goodbye! Have a great day ahead! 👋"
    
    else:
        return "I'm sorry, I didn't quite understand that. Type 'help' to see what I can do!"

def run_chatbot():
    """
    Runs the main interactive loop for the rule-based chatbot.
    """
    print("========================================")
    print("        WELCOME TO ALPHABOT!            ")
    print("========================================")
    print("Chatbot is online! (Type 'bye' or 'exit' to quit)\n")

    while True:
        # Prompt user for input
        user_message = input("You: ")

        # Skip empty inputs
        if not user_message.strip():
            print("Bot: Please type a message!\n")
            continue

        # Get reply from helper function
        bot_reply = get_bot_response(user_message)

        # Print bot response
        print(f"Bot: {bot_reply}\n")

        # Exit loop if user says goodbye
        if user_message.strip().lower() in ["bye", "goodbye", "exit", "quit"]:
            break

if __name__ == "__main__":
    run_chatbot()
