import os, sys, random, time
from ast import Str
from os import system, name

# Variables
game_name = "Win a Tenner"
game_score = 0
count = 0
cont_name = ""

# ascii art
ascii_intro = '''
 __    __  ____  ____        ____      ______    ___  ____   ____     ___  ____  
|  |__|  ||    ||    \      /    |    |      |  /  _]|    \ |    \   /  _]|    \ 
|  |  |  | |  | |  _  |    |  o  |    |      | /  [_ |  _  ||  _  | /  [_ |  D  )
|  |  |  | |  | |  |  |    |     |    |_|  |_||    _]|  |  ||  |  ||    _]|    / 
|  `  '  | |  | |  |  |    |  _  |      |  |  |   [_ |  |  ||  |  ||   [_ |    \ 
 \      /  |  | |  |  |    |  |  |      |  |  |     ||  |  ||  |  ||     ||  .  \\
  \_/\_/  |____||__|__|    |__|__|      |__|  |_____||__|__||__|__||_____||__|\_|'''

ascii_hl = '''
 __ __  ____   ____  __ __    ___  ____        ___   ____       _       ___   __    __    ___  ____   __ 
|  |  ||    | /    ||  |  |  /  _]|    \      /   \ |    \     | |     /   \ |  |__|  |  /  _]|    \ |  |
|  |  | |  | |   __||  |  | /  [_ |  D  )    |     ||  D  )    | |    |     ||  |  |  | /  [_ |  D  )|  |
|  _  | |  | |  |  ||  _  ||    _]|    /     |  O  ||    /     | |___ |  O  ||  |  |  ||    _]|    / |__|
|  |  | |  | |  |_ ||  |  ||   [_ |    \     |     ||    \     |     ||     ||  `  '  ||   [_ |    \  __ 
|  |  | |  | |     ||  |  ||     ||  .  \    |     ||  .  \    |     ||     | \      / |     ||  .  \|  |
|__|__||____||___,_||__|__||_____||__|\_|     \___/ |__|\_|    |_____| \___/   \_/\_/  |_____||__|\_||__'''

def clear():
    """Clear screen function"""
    if name == 'nt':
        _ = system ('cls')
    else:
        _ = system ('clear')
    time.sleep(1)

def print_delay(sec, phrase, cleared):
    """Delays print of each text line. Use first parameter to determine length of time""" 
    print(phrase)
    time.sleep(sec)
    if cleared:
        clear()

#####################################################################################################################################
####################################### Gameshow Introduction ########################################################################
#####################################################################################################################################

def introduction():

    global cont_name
    print_delay (4, ascii_intro, True)
    print_delay (4,'Welcommmme to another exciting episode of Win A Tenner!!!', True)
    print_delay (4,'Today, one lucky contestant will have the chance to play for... £10!', True)
    print_delay (4,'Hi there contestant. Introduce yourself for the benefit of the audience and the viewers at home.', True)
    cont_name = input (f'Please enter your name:\n')
    cont_name = cont_name.title()
    clear()
    print_delay (4,f'{cont_name}, we\'ve got FOUR amazing games for you to play today.', True)
    print_delay (4,'You\'ll score points in each game depending on how well you perform.', True)
    print_delay (4,'The more points you get, the better the prize you\'ll receive at the end.', True)
    print_delay (4, 'The first round today will be...', True)
    print_delay (4, 'The Higher Lower game!!!!', True)
    round1_intro()

#####################################################################################################################################
####################################### Round 1 introduction ########################################################################
#####################################################################################################################################

def round1_intro():
    """ This function introduces the contestant to the rules of the first round."""
    global ascii_hl
    global cont_name
    print_delay (3,f'{ascii_hl}', True)
    print_delay (4,f'{cont_name}, I hope you\'re ready to test those brain cells.', True)
    print_delay (4,'Here\'s how to play Higher or Lower.', True)
    print_delay (4,'In this round you\'ll be shown two face down cards.', True)
    print_delay (4,'In a minute, the value of the first card will be revealed and it\'s up to you to guess if the following card\'s value will be higher or lower than it.', True)
    print_delay (4,'If you guess correctly, you\'ll score a point.', True)
    print_delay (4,'If you guess incorrectly, you\'ll get nothing.', True)
    print_delay (4,'You\'ll then be presented with two further cards and do it all again until you\'ve been through three rounds.', True)
    print_delay (4,'At the end of the game, your points will be totalled up and will carry into the next round.\n', True)
    time.sleep (2)
    clear()

def round1_ready():
    """ This function prompts the player to proceed when they\'re ready."""

    ready_up = input (f'Are you ready {cont_name}?\n\nYES = Y\nNO = N\n\n')
    ready_up = ready_up.upper()

    if ready_up == 'Y':
        clear()
        print_delay (2, 'ROUND 1', False)
        print_delay (2,'The value of the very first card is...\n', False)
    else:
        clear()
        print_delay(3,f'That\'s not the answer we all wanted to hear! The clock\'s ticking {cont_name}. Let me know when you want to start...\n', True)
        time.sleep(1)
        clear()
        round1_ready()

def round1_summary():
    """Summarizes player score and offers a witty comment based on their performance"""
    if game_score <=1:
        print_delay (4,f'So {cont_name}, you scored {game_score} points during this game. Let\'s be honest, my cat could do better! There\'s all to play for in the next round... Rock Paper Scissors', True)
    if game_score ==2:
        print_delay (4,f'So {cont_name}, you scored {game_score} points during this game. That\'s a good start but there\'s still loads more points to earn in the next round... Rock Paper Scissors', True)
    if game_score ==3:
        print_delay (4,f'So {cont_name}, you scored {game_score} points during this game. What a great start! You\'ve definitely got the X-factor. There\'s still all to play for in the next round... Rock Paper Scissors', True)
    time.sleep(4)
    clear()

#####################################################################################################################################
################################### Round 1 game starts here ########################################################################
#####################################################################################################################################
def round1_game():
    """Randomly generates two card values and prompts user to guess if the second value is higher/lower than the first value."""
    
    # Global and local variables
    suits = ['Diamonds', 'Spades', 'Clubs', 'Hearts']
    faces = ['Jack', 'Queen', 'King', 'Ace']

    global game_score
    global count

    current_card1 = random.choice(suits)
    current_card2 = random.choice(suits)
    cnum1 = random.choice(range(2,15))
    cnum2 = random.choice(range(2,15))
    guess = ""
    answer = ""

    # Troubleshooting code to avoid duplicate values between cnum1 and cnum2        
    while cnum1 == cnum2:
        cnum2 = random.choice(range(2,15))

    # Comparison between the two cnum values to see which value is higher/lower and assign an answer
    if cnum1 < cnum2:
        answer = 'H'
    elif cnum1 > cnum2:
        answer = 'L'

    # Change cnum1 value to a face card if greater than 10 
    for face in faces:
        if cnum1 > 10:
            face_num = cnum1 -11
            face = faces[face_num]
            cnum1 = face
            break

    # Reveals value of first card and prompts higher/lower guess from player. Also checks if the very first card is being shown or a later one
    if count <1: 
        print_delay (2,f'{cnum1} of {current_card1}!\n', False)
    else:
        print_delay (2, f'ROUND {count+1}', False)
        print_delay (2, f'The value of the next card is {cnum1} of {current_card1}!\n', False)
    guess = input ('Do you think the value of the next card is higher or lower?\n\nHIGHER = H\nLOWER = L\n \n')
    guess = guess.upper()
    if guess != 'H' and guess !='L':
        print_delay (2,f'Hey {cont_name}, try entering \'H\' or \'L\' as your answer.', False)
        guess = input ('Do you think the value of the next card is higher or lower?\n\nHIGHER = H\nLOWER = L\n \n')
        guess = guess.upper()


    # Change cnum2 value to a face card if greater than 10 
    for face in faces:
        if cnum2 > 10:
            face_num = cnum2 -11
            face = faces[face_num]
            cnum2 = face
            break

    print_delay (2,f'The next card\'s value is {cnum2} of {current_card2}', True)

    # Answer confirmation
    if guess == answer:
        game_score += 1
        print_delay (2,'You guessed correctly! You\'re score is...', False)
        print_delay (2,f'\n{game_score}', True)
        clear()
    else:
        print_delay (2,'Unlucky. You guessed incorrectly. You\'re score is...', False)
        print_delay (2,f'\n{game_score}', True)
        clear()
    count +=1


# Check to see how many times the game has been payed. If more than 3, proceed to summary
    if count >2:
        round1_summary
    else:
        round1_game()
    clear()

introduction()
round1_ready()
round1_game()
round1_summary()








