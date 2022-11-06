import random
import time
from typing import Tuple


def get_user_name(progress: bool) -> str:
    username = input("Hi questioner, what's your name? ")
    time.sleep(1)
    while progress:
        if len(username) >= 2:
            print(f"Hi {username}!")
            progress = False
            time.sleep(2)
        else:
            username = input("Sorry, are you sure that's your name? try again! ")
            time.sleep(2)
    return username


def get_eight_ball_answer(random_number: int) -> str:
    if random_number == 1:
        answer = "Yes - definitely."
    elif random_number == 2:
        answer = "It is decidedly so."
    elif random_number == 3:
        answer = "Without a doubt."
    elif random_number == 4:
        answer = 'Reply hazy, try again.'
    elif random_number == 5:
        answer = 'Ask again later'
    elif random_number == 6:
        answer = 'Better not tell you now'
    elif random_number == 7:
        answer = 'My sources say no.'
    elif random_number == 8:
        answer = "Outlook not so good."
    elif random_number == 9:
        answer = "Very doubtful"
    else:
        answer = 'Error'
    return answer


def ask_to_play_again(play_again: str, username: str, progress: bool) -> bool:
    if play_again.upper() == "Y":
        time.sleep(1)
        print("Great!")
    elif play_again.upper() == "N":
        time.sleep(2)
        print(f"No problem, thanks for playing {username}! Come back again!")
        progress = False
    else:
        play_again = input("Sorry, that answer didn't register, please either type 'Y' or 'N'! ")
    return progress


def run_magic_eight_ball(question: str, username: str, progress: bool) -> Tuple[str, bool]:
    print(f"You asked, '{question}', let's see what Magic 8-ball says!")
    random_number = random.randint(1, 9)
    for _ in range(3):
        time.sleep(1)
        print("Asking...")
    answer = get_eight_ball_answer(random_number)
    time.sleep(1)
    print("Magic 8-Ball's answer: " + answer)
    time.sleep(1)
    play_again = input(f"Do you want to play again {username}? Y/N ")
    progress = ask_to_play_again(play_again, username, progress)
    return play_again, progress


def execute_eight_ball_program(progress: bool, username: str):
    while progress:
        question = input("What question would you like to ask the 8 ball? ")

        if len(question) == 0:
            question = input("Sorry, there doesn't seem to be a question here, try again? ")
            time.sleep(2)
        elif "?" not in question:
            question = input(
                "Sorry, not sure if that's a question, please make sure you put a '?' at the end for the 8-ball to be "
                "sure! ")
            time.sleep(2)
        else:
            play_again, progress = run_magic_eight_ball(question, username, progress)
