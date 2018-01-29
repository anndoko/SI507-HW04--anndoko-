# Create a function that asks users “What is your question?” (or something similar) and saves the response.
def prompt():
    user_question = input("Please enter your question or enter 'quit' to end the program.\n")
    return user_question

user_input = ""
while user_input != "quit":
    user_input = prompt()

    # checks if user input is a question (i.e., ends in a ‘?’) and, if not, prints “I’m sorry, I can only answer questions.”
    if user_input[-1] != "?":
        print("I’m sorry, I can only answer questions.")
