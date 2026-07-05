from chatterbot import ChatBot

# Load chatbot
chatbot = ChatBot(
    "CollegeBot",
    storage_adapter="chatterbot.storage.SQLStorageAdapter",
    database_uri="sqlite:///db.sqlite3"
)

print("=" * 50)
print("Simple Q&A Chatbot")
print("Type 'exit' to quit.")
print("=" * 50)

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        print("Bot: Goodbye! Have a nice day.")
        break

    response = chatbot.get_response(user_input)

    print("Bot:", response)