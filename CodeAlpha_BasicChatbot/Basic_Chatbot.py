# ==========================================
# CODEALPHA - BASIC CHATBOT
# ==========================================

def chatbot():
    print("=" * 50)
    print("          BASIC CHATBOT")
    print("=" * 50)
    print("Type 'bye' to end the chat.\n")

    while True:
        user = input("You: ").lower()

        if user == "hello":
            print("Bot: Hi!")

        elif user == "hi":
            print("Bot: Hello!")

        elif user == "how are you":
            print("Bot: I'm fine, thanks!")

        elif user == "what is your name":
            print("Bot: I am a Basic Chatbot.")

        elif user == "who made you":
            print("Bot: I was created using Python.")

        elif user == "thank you":
            print("Bot: You're welcome!")

        elif user == "bye":
            print("Bot: Goodbye!")
            break

        else:
            print("Bot: Sorry, I don't understand that.")

chatbot()