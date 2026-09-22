def start_chat():
    print("=========================================")
    print("(     Welcome to my CodeAlpha Bot!      )")
    print("=========================================")
    print("Quick tip: Type 'bye' or 'exit' whenever you want to quit.\n")
    print("Bot: Hey! I'm your AI chat assistant for this project. What's on your mind?")   
    while True:
        msg = input("\nYou: ").strip().lower()        
        if msg == 'bye' or msg == 'goodbye' or msg == 'exit' or msg == 'quit':
            print("Bot: See ya! Good luck with the rest of the internship tasks!")
            break
        elif 'hello' in msg or 'hi' in msg or 'hey' in msg:
            print("Bot: Hello! Hope your day is going great so far.")
        elif 'how are you' in msg or 'how is it going' in msg or "how's it going" in msg:
            print("Bot: I'm doing good, thanks! Just sitting here running inside your terminal.")
        elif 'your name' in msg or 'who are you' in msg:
            print("Bot: I'm just a simple rule-based chatbot built for my CodeAlpha programming task.")
        elif 'help' in msg or 'what can you do' in msg:
            print("Bot: I can chat about basic things! Try saying: 'hi', 'how are you', 'what is your name', or 'bye'.")
        else:
            print("Bot: Sorry, I didn't quite catch that. Could you try rephrasing, or type 'help'?")

if __name__ == "__main__":
    start_chat()
