from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

# Create chatbot
chatbot = ChatBot(
    "CollegeBot",
    storage_adapter="chatterbot.storage.SQLStorageAdapter",
    database_uri="sqlite:///db.sqlite3"
)

# Create trainer
trainer = ChatterBotCorpusTrainer(chatbot)

# Train with English corpus
trainer.train("chatterbot.corpus.english")

print("\nTraining completed successfully!")