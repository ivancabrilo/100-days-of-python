'''TIP CALCULATOR'''

print("Welcome to the tip calculator.")
total_bill = input("What was the total bill? $")
percentage = input("What percentage tip would you like to give? 10, 12, or 15?")
people = input("How many people to split the bill?")
x = float(total_bill)
y = float(percentage)
z = int(people)
each_person = ((x + (x * (y/100))) / z)
final_amount = round(each_person,2)
print(f"${final_amount}")





'''ROLLERCOASTER PRICE GENERATOR'''

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm?"))
bill = 0
if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age?"))
    if age < 12:
     bill = 5
     print("You have to pay $5.")
    elif age <= 18:
     bill = 7
     print("You have to pay $7")
    else:
     bill = 12
     print("Please pay $12.")
    photo = (input("Would you like a photo for $3? Yes or No."))
    if photo == "Yes":
       bill += 3
    print(f"Your final bill is {bill}")
else:
   print("Sorry, you have to grow taller before you can ride.")

  
  


''' LEAP YEAR CALCULATOR '''

year = int(input("Which year do you want to check? "))

if year%400 == 0 and year/400:
    print("This year is a leap year.")
elif year%4 == 0 and (not year/100):
    print("This year is a leap year.")
else:
    print("This year is not a leap year.")

  

  
  
''' PIZZA BILL CALCULATOR ''' 

print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")

bill = 0
if size == "S":
    bill += 15
elif size == "M":
    bill += 20
else:
    bill += 25

if extra_cheese == "Y":
    bill += 1
else:
    bill += 0

if add_pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3

print(f"Your final bill is ${bill}")





''' LOVE MATHCING CALCULATOR '''

print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
lower_case_name = name1.lower()
lower_case_name2 = name2.lower()
love = ((lower_case_name.count("l") + lower_case_name.count("o") + lower_case_name.count("v") +lower_case_name.count("e") +lower_case_name2.count("l") + lower_case_name2.count("o") + lower_case_name2.count("v") +lower_case_name2.count("e")) )
true = ((lower_case_name.count("t") + lower_case_name.count("r") + lower_case_name.count("u") +lower_case_name.count("e") + lower_case_name2.count("t") + lower_case_name2.count("r") + lower_case_name2.count("u") +lower_case_name2.count("e")) )
score = str(true) + str(love)

score = int(score)
if score <10 or score>90:
    print(f'Your score is {score}, you go together like coke and menots.')
elif score >= 40 and score <= 50:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}")
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure")
first_decision = (input("Where do you want to go,'Left' or 'Right'?"))
if first_decision == "Left":
    second_decision = (input('You come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across.'))
    if second_decision == "wait":
        final_decison = input("You were patient, you arrived unharmed to the island. Now there is a house with three doors and you have 33.33% to survive. Now choose 'red' 'yellow' or 'blue' ")
        if final_decison == "red":
            print("You found the treasure and you survive.")
        else:
            print("Dumb way to die.")
    else:
        print("You die")


else:
    print("You die")


  
  
  
''' HEAD OR TAILS'''

import random
random_integer = random.randint(1, 10)
print(random_integer)

random_float = random.random() 
print(random_float*5)

import random
random_number = (random.randint(0,1))
random_number = input(0,1)
if random_number == 1:
    print("Heads")
else:
    print("Tails")

import random

toss_coin = random.randint(0, 1)
if toss_coin == 1:
    print("Heads")
else:
    print("Tails")


  
  
  
''' WHO PAYS THE BILL GENERATOR?'''

names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
num_items = len(names)

import random

random_name = random.randint(0,len(names)-1)
random_person = names[random_name]
print(f"{random_person} pays the dinner")





''' HIT THE BOX'''

row1 = ["⬜️","️⬜️","️⬜️"]
row2 = ["⬜️","⬜️","️⬜️"]
row3 = ["⬜️️","⬜️️","⬜️️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")

horizontal = int(position[1])
vertical = int(position[0])

selected = map[horizontal-1]
selected[vertical-1] = "X"
print(f"{row1}\n{row2}\n{row3}")





'''AVERAGE HEIGHT CALCULATOR'''

student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
  
denominator = (len(student_heights))
numerator = (sum(student_heights))
average_height = round(numerator/denominator)
print(f"Average height is {average_height}cm")





''' BEST STUDENT CALCULATOR'''
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
highest_score = 0
for score in student_scores:
    if score > highest_score:
        highest_score = score
print(f"The highest score in the class is: {highest_score}")





''' RANDOM PASSWORD GENERATOR '''

import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

password = []

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
for kurcina in range(1, nr_letters + 1):
    password += random.choice(letters)


for symbol in range(1, nr_symbols+1):
    random_symbol = random.choice(symbols)
    password.append(random_symbol)


for num in range(1, nr_numbers +1):
    random_nu = random.choice(numbers)
    password.append(random_nu)
print(password)
random.shuffle(password)
sifra = ""
for i in password:
    sifra += i

print(f'Your password is {sifra}')





''' HANGMAN GAME '''

logo = '''
 _
| |
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |
                   |___/    '''
print(logo)
import random
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

end_of_game = False

word_list = ['chemistry', 'monster', 'magnesium','abruptly',
'absurd',
'abyss',
'affix',
'askew',
'avenue',
'awkward',
'axiom',
'azure',
'bagpipes',
'bandwagon',
'banjo',
'bayou',
'beekeeper',
'bikini',
'blitz',
'blizzard',
'boggle',
'bookworm',
'boxcar',
'boxful',
'buckaroo',
'buffalo',
'buffoon',
'buxom',
'buzzard',
'buzzing',
'buzzwords',
'caliph',
'cobweb',
'cockiness',
'croquet',
'crypt',
'curacao',
'cycle',
'daiquiri',
'dirndl',
'disavow',
'dizzying',
'duplex',
'dwarves',
'embezzle',
'equip',
'espionage',
'euouae',
'exodus',
'faking',
'fishhook',
'fixable',
'fjord',
'flapjack',
'flopping',
'fluffiness',
'flyby',
'foxglove',
'frazzled',
'frizzled',
'fuchsia',
'funny',
'gabby',
'galaxy',
'galvanize',
'gazebo',
'giaour',
'gizmo',
'glowworm',
'glyph',
'gnarly',
'gnostic',
'gossip',
'grogginess',
'haiku',
'haphazard',
'hyphen',
'iatrogenic',
'icebox',
'injury',
'ivory',
'ivy',
'jackpot',
'jaundice',
'jawbreaker',
'jaywalk',
'jazziest',
'jazzy',
'jelly',
'jigsaw',
'jinx',
'jiujitsu',
'jockey',
'jogging',
'joking',
'jovial',
'joyful',
'juicy',
'jukebox',
'jumbo',
'kayak',
'kazoo',
'keyhole',
'khaki',
'kilobyte',
'kiosk',
'kitsch',
'kiwifruit',
'klutz',
'knapsack',
'larynx',
'lengths',
'lucky',
'luxury',
'lymph',
'marquis',
'matrix',
'megahertz',
'microwave',
'mnemonic',
'mystify',
'naphtha',
'nightclub',
'nowadays',
'numbskull',
'nymph',
'onyx',
'ovary',
'oxidize',
'oxygen',
'pajama',
'peekaboo',
'phlegm',
'pixel',
'pizazz',
'pneumonia',
'polka',
'pshaw',
'psyche',
'puppy',
'puzzling',
'quartz',
'queue',
'quips',
'quixotic',
'quiz',
'quizzes',
'quorum',
'razzmatazz',
'rhubarb',
'rhythm',
'rickshaw',
'schnapps',
'scratch',
'shiv',
'snazzy',
'sphinx',
'spritz',
'squawk',
'staff',
'strength',
'strengths',
'stretch',
'stronghold',
'stymied',
'subway',
'swivel',
'syndrome',
'thriftless',
'thumbscrew',
'topaz',
'transcript',
'transgress',
'transplant',
'triphthong',
'twelfth',
'twelfths',
'unknown',
'unworthy',
'unzip',
'uptown',
'vaporize',
'vixen',
'vodka',
'voodoo',
'vortex',
'voyeurism',
'walkway',
'waltz',
'wave',
'wavy',
'waxy',
'wellspring',
'wheezy',
'whiskey',
'whizzing',
'whomever',
'wimpy',
'witchcraft',
'wizard',
'woozy',
'wristwatch',
'wyvern',
'xylophone',
'yachtsman',
'yippee',
'yoked',
'youthful',
'yummy',
'zephyr',
'zigzag',
'zigzagging',
'zilch',
'zipper',
'zodiac',
'zombie',
]

chosen_word = random.choice(word_list)
guesses = []
lives = 7
display = []
for letter in chosen_word:
    display += "_"
while not end_of_game:
    guess = input("Guess a letter:").lower()

    if guess in display:
        print(f'You have already guessed letter {guess}.')

    for position in range(len(chosen_word)):
        letter = chosen_word[position]

        if letter == guess:
            display[position] = letter

    if guess not in display:
        print(f"The letter {guess} is not in the word")
        lives -= 1
        if guess in guesses:
            print(f"You have already guessed letter {guess}")
            lives += 1

        for g in chosen_word:
            guesses += guess


        if lives == 6:
            print(stages[6])
        elif lives == 5:
            print(stages[5])
        elif lives == 4:
            print(stages[4])
        elif lives == 3:
            print(stages[3])
        elif lives == 2:
            print(stages[2])
        elif lives == 1:
            print(stages[1])
        elif lives == 0:
            end_of_game = True
            print(stages[0])
            print("You lost")
            print(f'The word was {chosen_word}')

    print(display)
    if "_" not in display:
        end_of_the_game = True
        print("You won")
 
 
 
 
 
 ''' PAINT AMOUNT CALCULATOR'''
 
test_h = int(input("Height of wall:"))
test_w = int(input("Width of wall:"))
coverage = 5
import math
def paint_calc(height, width, cover):
    area = height * width
    num_of_cans = math.ceil(area/cover)
    print(f'You will need {num_of_cans} cans of paint')

paint_calc(height = test_h, width = test_w, cover = coverage)
n = int(input("Check this number"))





''' PRIME NUMBER CHECKER '''

n = int(input("Check this number"))

def prime_checker(number):
    if number % 1 == 0:
        if number % 3 == 0 or number % 2 == 0:
            if number != 3 and number != 2:
                print("It's not a prime number.")
            else:
                print("It's a prime number")

        else:
            print("It's a prime number")


prime_checker(number = n)





''' CAESAR CIPHER '''

logo = """
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88
            88             88
           ""             88
                          88
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8
8b         88 88       d8 88       88 8PP""""""" 88
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88
              88
              88
"""
print(logo)
end_of_cipher = False
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def caesar(t, sh, richtung):
    list = ""

    if sh > 25:
        sh = sh%26
    if richtung == "decode":
        sh *= -1
    for letter in t:
        if letter in alphabet:
            x = alphabet.index(letter)
            new_postion = x + sh
            list += alphabet[new_postion]
        else:
            list += letter

    print(f'The {direction}d text is {list}')



caesar(t = text , sh = shift, richtung = direction)


while not end_of_cipher:
    play_again = input("Do you want to restart cipher program?\n").lower()
    if play_again == "yes":
        alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                    'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
                    'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        caesar(t = text , sh = shift, richtung = direction)
    elif play_again == "no":
        end_of_cipher = True
      
      
      
 
 
''' NUMBER OF DAYS IN A MONTH OF A CERATIN YEAR '''

def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return(True)
            else:
                return(False)
        else:
            return(True)
    else:
        return(False)


def days_in_month(year, month):
    month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if (is_leap(year)) == True:
        month_days[2]=29
        return(month_days[month])
    else:
        return(month_days[month])

year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)




''' SILENT AUCTION '''

 from replit import clear

bidding_ended = False
bid = {}


def bidding(all_bidders):
    highest_bid = 0
    winner = ""
    for bidder in all_bidders:
        bid_amount = all_bidders[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a highest bid of ${highest_bid}\n")


while not bidding_ended:
    name = input("What is your name?\n")
    price = int(input("What is your bid?\n$"))
    bid[name] = price
    more_players = input('Are there any other bidders? Type "yes" or "no".\n')
    if more_players == "yes":
        clear()
    else:
        bidding(bid)
        bidding_ended = True


bidding_ended = False
bid={}

def bidding(all_bidders):
  highest_bid = 0
  winner = ""
  for bidder in all_bidders:
    bid_amount= all_bidders[bidder]
    if bid_amount > highest_bid:
      highest_bid = bid_amount
      winner = bidder
  print(f"The winner is {winner} with a highest bid of ${highest_bid}\n")


while not bidding_ended:
  name = input("What is your name?\n")
  price = int(input("What is your bid?\n$"))
  bid[name]=price
  more_players = input('Are there any other bidders? Type "yes" or "no".\n')
  if more_players == "yes":
    clear()
  else:
    bidding(bid)
    bidding_ended = True

    
    
    
    
''' BLACK JACK '''
    
logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""

print(logo)
import random
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
my_cards = []
dealers_cards = []
def another_card():
    random_card = random.choice(cards)
    return random_card

for me in range(2):
    my_cards.append(another_card())

for dilera in range(1):
    dealers_cards.append(another_card())

def my_sum():
    total = sum(my_cards)
    return total

def deal_sum():
    total_deal = sum(dealers_cards)
    return total_deal

def score_track():
    print(f'Your cards: {my_cards}, current score: {my_sum()} ')
    print(f"Dealers cards are {dealers_cards}, current score: {deal_sum()} ")


def defeat():
    if deal_sum() > my_sum() and deal_sum() <= 21:
        print(f'Your cards: {my_cards}, current score: {my_sum()} ')
        print(f"Dealers cards are {dealers_cards}, current score: {deal_sum()} ")
        print("You lost")


def draw():
    if deal_sum() == my_sum():
        print(f'Your cards: {my_cards}, and score: {my_sum()} ')
        print(f"Dealers cards are {dealers_cards}, and score: {deal_sum()} ")
        print("It'a draw")


def win():
    if deal_sum() < my_sum():
        print(f'Your cards: {my_cards}, and score: {my_sum()} ')
        print(f"Dealers cards are {dealers_cards}, and score: {deal_sum()} ")
        print("You won")


score_track()
game_on = True
while game_on:
    if my_sum() < 21:
        over21 = False

        while not over21:
            next_card = input("Type 'y' to get another card, type 'n' to pass: ").lower()

            if next_card == "y":
                my_cards.append(another_card())
                score_track()

                if 11 in my_cards and my_sum > 21:
                    my_cards.remove(11)
                    my_cards.append(1)

                elif my_sum() > 21:
                    over21 = True
                    print("lost")

            elif next_card == "n":
                over21 = True
                score_track()

                if deal_sum() < 17:

                    under17 = True
                    while under17:
                        dealers_cards.append(another_card())
                        deal_sum()

                        if deal_sum() >= 17:
                            if 11 in dealers_cards and deal_sum() > 21:
                                dealers_cards.remove(11)
                                dealers_cards.append(1)
                            elif deal_sum() >21:
                                print("won")

                            under17 = False


                game_on = False


draw()
win()
defeat()





   
 
 
 
       
       
 



