def chatbot():
    print("Chatbot: Hi! I'm a simple chatbot. Type 'bye' to exit.")

    while True:
        user_input = input("You: ").lower()

        if user_input in ["hi", "hello", "hey"]:
            print("Chatbot: Hello! How can I help you today?")
        elif "how are you" in user_input:
            print("Chatbot: I'm just a bunch of code, but I'm doing great! How about you?")
        elif "your name" in user_input:
            print("Chatbot: I'm ChatBot 1.0!")
        elif "help" in user_input:
            print("Chatbot: Sure, I'm here to help. What do you need assistance with?")
        elif "bye" in user_input:
            print("Chatbot: Goodbye! Have a nice day.")
            break
        else:
            print("Chatbot: I'm not sure how to respond to that. Can you rephrase?")
chatbot()
