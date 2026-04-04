import re
import random

rules = [
    (r'I need (.*)', [
        "Why do you need {0}?",
        "Would it really help you if you got {0}?",
        "Are you sure you need {0}?"
    ]),
    (r'I feel (.*)', [
        "Why do you feel {0}?",
        "Does feeling {0} happen often?",
        "Tell me more about feeling {0}."
    ]),
    (r'I am (.*)', [
        "Why are you {0}?",
        "How long have you been {0}?",
        "What triggers being {0}?"
    ]),
    (r'\s*My name is (.*)', [
        "Nice name {0}, how can I assist you today?",
        "Nice name {0}, how can I assist you today?",
        "Nice name {0}, how can I assist you today?"
    ]),
    (r'Because (.*)', [
        "Is that the real reason?",
        "What other reasons might there be?",
        "Does that reason explain anything else?"
    ]),
    (r'Hello(.*)', [
        "Hey hey friend!",
        "Hey hey friend!",
        "Hey hey friend!"
    ]),
    (r'My (.*) is (.*)', [
        "Tell me more about your {0}.",
        "How does your {0} being {1} affect you?",
        "Why do you say your {0} is {1}?"
    ]),
    (r'quit', [
        "Goodbye! Take care of yourself.",
        "It was nice talking to you. Bye!"
    ]),
    (r'(.*)', [
        "Tell me more about that.",
        "Can you elaborate on that?",
        "How does that make you feel?",
        "Interesting. Please continue.",
        "What could be the possible solution?"
    ])
]

def get_eliza_response(user_input):
    for pattern, responses in rules:
        match = re.match(pattern, user_input, re.IGNORECASE)
        if match:
            response = random.choice(responses)
            groups = match.groups()
            for i, g in enumerate(groups):
                response = response.replace('{' + str(i) + '}', g)
            return response
    return "Tell me more about that."

if __name__ == "__main__":
    print("ELIZA Chatbot")
    print("Type 'quit' to stop.\n")
    while True:
        user = input("> ")
        if user.lower() == "quit":
            print(random.choice(["Goodbye! Take care of yourself.", "It was nice talking to you. Bye!"]))
            break
        print(get_eliza_response(user))