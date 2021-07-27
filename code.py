import random
import time
progress = "Continue"
random_number = random.randint(1,9)
answer = ""

name = input("Hi question asker, what's your name? ")
time.sleep(1)
while progress == "Continue":
    
    
    if len(name) >= 2:
        print(f"Hi {name}!")
        progress = "Pause"
        time.sleep(2)
    else:
        name = input("Sorry, are you sure that's your name? try again! ")
        time.sleep(2)



progress = True


while progress == True:

    question = input("What question would you like to ask the 8 ball? ")

    
    if len(question) == 0:
        question = input("Sorry, there doesn't seem to be a question here, try again? ")
        time.sleep(2)

        
        
    elif "?" not in question:
        question = input("Sorry, not sure if that's a question, please make sure you put a '?' at the end for the 8-ball to be sure! ")
        time.sleep(2)

    else:
        print(f"You asked, '{question}', let's see what 8-ball says!")
        for i in range(3):
            time.sleep(1)
            print("Asking...")
        
        
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
        
        time.sleep(1)
        print("Magic 8-Ball's answer: "+answer)
        time.sleep(1)
        play_again = input(f"Do you want to play again {name}? Y/N ")
        if play_again.upper() == "Y":
            time.sleep(1)
            print("Great!")
        elif play_again.upper() == "N":
            time.sleep(2)
            print(f"No problem, thanks for playing {name}! Come back again!")
            progress = False
        else:
            play_again = input("Sorry, that answer didn't register, please either type 'Y' or 'N'! ")
        
        

        