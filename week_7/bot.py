
import random

random_responses = ["That's quite interesting, please elaborate.",
                    "I understand. Please continue.",
                    "Could you provide more context for that statement?",
                    "The weather has been unusual lately, don't you think?",
                    "Let's discuss something else.",
                    "Did you watch the game last night?"]

print("Greetings! I am Marvin, a simple robot.")
print("Feel free to end our conversation at any time by typing 'bye'")
print("After each response, press 'enter'")
print("How are you doing today?")

while True:
    user = input("> ")
    if user.lower() == 'bye':
        break
    else:
        response = random.choice(random_responses)
        print(response)

print("It was a pleasure conversing with you. Goodbye!")