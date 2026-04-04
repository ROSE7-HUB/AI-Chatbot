import os
os.environ["TRANSFORMERS_VERBOSITY"] = "error"
import warnings
warnings.filterwarnings("ignore")
from transformers import pipeline, logging
logging.set_verbosity_error()

chatbot = pipeline(
    "text-generation",
    model="Qwen/Qwen2.5-1.5B-Instruct",
    max_new_tokens=50
)

def get_llm_response(user_input):
    prompt = f"User: {user_input}\nAssistant:"
    response = chatbot(prompt, do_sample=False)
    output = response[0]["generated_text"].split("Assistant:")[-1]
    return output.strip()

if __name__ == "__main__":
    print("Modern AI Chatbot")
    print("Type 'quit' to stop.\n")
    while True:
        user = input("You: ")
        if user.lower() == "quit":
            print("Bot: Goodbye!")
            break
        print("Bot:", get_llm_response(user))
        print()