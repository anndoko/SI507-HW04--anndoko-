import random

# Create a function that asks users “What is your question?” (or something similar) and saves the response.
def prompt():
    user_question = input("Please enter your question or enter 'quit' to end the program.\n")
    return user_question

# Create a list of 20 answers
magic_ans = [
"It is certain",
"It is decidedly so",
"Without a doubt",
"Yes definitely",
"You may rely on it",
"As I see it, yes",
"Most likely",
"Outlook good",
"Yes",
"Signs point to yes",
"Reply hazy try again",
"Ask again later",
"Better not tell you now",
"Cannot predict now",
"Concentrate and ask again",
"Don't count on it",
"My reply is no",
"My sources say no",
"Outlook not so good",
"Very doubtful",
]

user_input = ""
while user_input != "quit":
    user_input = prompt()
    answer = random.choice(magic_ans)
    print(answer)
