from datetime import datetime
import random

user_name = ""
tasks = []
chat_history = []

jokes = [
    "Why do programmers prefer Python? Because it has fewer bugs!",
    "Why was the computer cold? It left its Windows open!",
    "Debugging is like being a detective in a crime movie where you are also the murderer."
]

quotes = [
    "Success is the sum of small efforts repeated daily.",
    "Discipline beats motivation.",
    "Your future is created by what you do today."
]

facts = [
    "Python was created by Guido van Rossum in 1991.",
    "The first computer bug was an actual moth.",
    "Python is one of the most popular programming languages."
]


def save_note():
    note = input("Enter Note: ")

    with open("notes.txt", "a", encoding="utf-8") as file:
        file.write(note + "\n")

    print("Bot: Note saved successfully!")


def add_task():
    task = input("Enter Task: ")
    tasks.append(task)
    print("Bot: Task added successfully!")


def show_tasks():
    if not tasks:
        print("Bot: No tasks available.")
        return

    print("\n===== TO-DO LIST =====")

    for index, task in enumerate(tasks, start=1):
        print(f"{index}. {task}")


def show_help():

    print("\n" + "=" * 70)
    print("                    ALPHABOT COMMAND CENTER")
    print("=" * 70)

    print("\n👤 USER COMMANDS")
    print("-" * 70)
    print(" hello          : Greet the chatbot")
    print(" my name        : Tell the bot your name")
    print(" who am i       : Display your saved name")
    print(" your name      : Know the bot's name")
    print(" how are you    : Ask how the bot is doing")

    print("\n DATE & TIME")
    print("-" * 70)
    print(" date           : Show current date")
    print(" time           : Show current time")

    print("\n UTILITIES")
    print("-" * 70)
    print(" calculator     : Perform calculations")
    print(" add note       : Save a note to notes.txt")
    print(" add task       : Add a task to your To-Do list")
    print(" show tasks     : View all tasks")

    print("\n FUN COMMANDS")
    print("-" * 70)
    print(" joke           : Hear a random joke")
    print(" motivate me    : Get a motivational quote")
    print(" fact           : Learn a random fact")

    print("\n SYSTEM")
    print("-" * 70)
    print(" history        : View chat history")
    print(" help           : Show command menu")
    print(" bye            : Exit the chatbot")

    print("\n" + "=" * 70)
    print("Tip: Commands are not case-sensitive.")
    print("=" * 70 + "\n")


print("=" * 70)
print("        CODEALPHA SMART PERSONAL ASSISTANT CHATBOT")
print("=" * 70)

print("Hello! I am Monday! ")
print("Type 'help' to view commands.\n")

while True:

    user_input = input("You: ").strip().lower()

    chat_history.append("User: " + user_input)

    if user_input in ["hello", "hi", "hey"]:

        response = "Hello! Nice to meet you."

    elif user_input == "how are you":

        response = "I'm doing great. Thanks for asking."

    elif user_input == "my name":

        user_name = input("Bot: What is your name? ")
        response = f"Welcome {user_name}!"

    elif user_input == "who am i":

        if user_name:
            response = f"You are {user_name}."
        else:
            response = "I don't know your name yet."

    elif user_input == "your name":

        response = "My name is Monday."

    elif user_input == "date":

        response = datetime.now().strftime(
            "Today's date is %d-%m-%Y"
        )

    elif user_input == "time":

        response = datetime.now().strftime(
            "Current time is %I:%M:%S %p"
        )

    elif user_input == "calculator":

        try:

            num1 = float(input("First Number: "))
            op = input("Operator (+ - * /): ")
            num2 = float(input("Second Number: "))

            if op == "+":
                response = f"Result = {num1 + num2}"

            elif op == "-":
                response = f"Result = {num1 - num2}"

            elif op == "*":
                response = f"Result = {num1 * num2}"

            elif op == "/":
                response = (
                    "Cannot divide by zero"
                    if num2 == 0
                    else f"Result = {num1 / num2}"
                )

            else:
                response = "Invalid Operator"

        except ValueError:
            response = "Invalid Number"

    elif user_input == "joke":

        response = random.choice(jokes)

    elif user_input == "motivate me":

        response = random.choice(quotes)

    elif user_input == "fact":

        response = random.choice(facts)

    elif user_input == "add note":

        save_note()
        continue

    elif user_input == "add task":

        add_task()
        continue

    elif user_input == "show tasks":

        show_tasks()
        continue

    elif user_input == "history":

        print("\n===== CHAT HISTORY =====")

        for chat in chat_history:
            print(chat)

        continue

    elif user_input == "help":

        show_help()
        continue

    elif user_input in ["bye", "exit", "quit"]:

        print("Bot: Goodbye! Have a wonderful day.")
        break

    else:

        response = (
            "Sorry, I don't understand that command. "
            "Type 'help' to see available commands."
        )

    chat_history.append("Bot: " + response)
    print("Bot:", response)