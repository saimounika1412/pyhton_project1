import random

class SimpleChatbot:
    def _init_(self):
        self.greetings = [
            "Hello!",
            "Hi there!",
            "How are you doing?",
            "Nice to see you!"
        ]
        self.responses = {
            "how are you": ["I'm doing well, thank you.", "I'm great, thanks for asking."],
            "what's your name": ["I'm a simple chatbot.", "You can call me Chatbot."],
            "bye": ["Goodbye!", "See you later!", "Take care!"]
        }

    def get_response(self, user_input):
        user_input = user_input.lower()
        for key in self.responses:
            if key in user_input:
                return random.choice(self.responses[key])
        return "I'm not sure I understand."

    def start_chat(self):
        print(random.choice(self.greetings))
        while True:
            user_input = input("You: ")
            if user_input.lower() == "bye":
                print(self.get_response(user_input))
                break
            else:
                print("Chatbot:", self.get_response(user_input))

if _name_ == "_main_":
    chatbot = SimpleChatbot()
    chatbot.start_chat()
