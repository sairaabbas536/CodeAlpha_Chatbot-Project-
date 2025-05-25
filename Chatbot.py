def chatbot():
    responses = {
        "hello": "Hi!",
        "hi": "Hello!",
        "how are you": "I'm fine, thanks!",
        "bye": "Goodbye!",
        "who are you": "I'm a simple chatbot.",
        "what's your name": "You can call me ChatBot.",
        "thank you": "You're welcome!"
    }

    print("Chatbot: Hello! Type 'bye' to exit.")
    
    while True:
        user_input = input("You: ").lower().strip()
        
        if user_input == "bye":
            print("Chatbot:", responses["bye"])
            break
        
        # Use dictionary to get response
        reply = responses.get(user_input, "Sorry, I didn’t understand that.")
        print("Chatbot:", reply)

# Run the chatbot
chatbot()

