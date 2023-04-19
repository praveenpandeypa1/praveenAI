
import random

# define possible user inputs and corresponding bot responses
responses = {
    "hi": ["Hello!", "Hi there!", "Hey!"],
    "how are you": ["I'm doing well, thank you.", "I'm fine, thanks for asking.", "I'm good, and you?"],
    "what are you doing": ["Just chatting with you!", "Nothing much, what about you?", "Just hanging out."],
    "bye": ["Goodbye!", "Bye-bye!", "See you later!"],
}

# define function to generate bot response
def respond(input_text):
    input_text = input_text.lower()
    for key in responses:
        if input_text in key:
            return random.choice(responses[key])
    return "I'm sorry, I don't understand what you're saying."

# greet user and start conversation
print("Hello! I'm a chatbot. What's your name?")
name = input()
print(f"Nice to meet you, {name}! How can I help you today?")

# start loop to receive user input and generate bot response
while True:
    user_input = input().strip()
    if user_input == "exit":
        print("Goodbye!")
        break
    response = respond(user_input)
    print(response)
