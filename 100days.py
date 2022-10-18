
# def main():
#     win = GraphWin("TicTacToe")
#     win.setCoords(0.0, 0.0, 3.0, 3.0)
#
#     #horizontal lines
#     Line(Point(0,1), Point(3, 1)).draw(win)
#     Line(Point(0,2), Point(3, 2)) .draw(win)

# vertical lines
# print("Hello world")
# print("high\nhigh\nhigh")
# print("I ve got the love that keeps me waiting")


# print("Hello" + " " + "Ivan")
# Napravis input i ako mu dodas print ispred, sta god da napises posle pitanja na mainu izbacice ti
# print("Hello" + input("What is your name?"))
# print(len(input("What is your name?")))

# name = input("What is your name?")
# print(name)
# name = input("What is your name?")
# length = len(name)
# print(length)
# greeting = "cao"
# print(greeting)
# city = (input("Where did you grow up?\n"))
# print(city)
# animal = (input("What is the name of your first pet?\n"))
# print(animal)
# print("ur band name is " + city + " " + animal)
#
# print("kurac[4]")
#
# number = len(input("What is your name?"))
# new_number = str(number)
# print("Your name has" + " " + new_number + " " + "characters.")

# number = input("Type a two digit number:")
# number_1 = int(number[0])
# number_2 = int(number[1])
# # print(number_1 + number_2)
# height = input("enter your height in m:")
# weight = input("enter your code weight in kg:")
# height_flo = float(height)
# weight_flo = float(weight)
# BMI = weight_flo/(height_flo**2)
# print(int(BMI))

# score = 4/2
# score *= 3
#
# print(score)
#
# print(4//2)
# print(5/2)
#  print(round(5/2))
# #  print(5//2)
# #  print(int(3.67))
# age = input("What is your current age?")
# days = 90*365 - int(age)*365
# weeks = 90*52 - int(age)*52
# months = 90*12 - int(age)*12
# print(f"You have {days} days, {weeks} weeks, and {months} months left.")
# # #print("Welcome to the tip calculator.")
# # total_bill = input("What was the total bill? $")
# percentage = input("What percentage tip would you like to give? 10, 12, or 15?")
# people = input("How many people to split the bill?")
# x = float(total_bill)
# y = float(percentage)
# z = int(people)
# each_person = ((x + (x * (y/100))) / z)
# final_amount = round(each_person,2)
# print(f"${final_amount}")
# # #
# print("Welcome to the rollercoaster!")
# height = int(input("What is your height in cm?"))
# bill = 0
# if height >= 120:
#     print("You can ride the rollercoaster!")
#     age = int(input("What is your age?"))
#     if age < 12:
#      bill = 5
#      print("You have to pay $5.")
#     elif age <= 18:
#      bill = 7
#      print("You have to pay $7")
#     else:
#      bill = 12
#      print("Please pay $12.")

#     photo = (input("Would you like a photo for $3? Yes or No."))
#     if photo == "Yes":
#        bill += 3
#     print(f"Your final bill is {bill}")
# else:
#    print("Sorry, you have to grow taller before you can ride.")
#  number = int(input("Which number do ypu want to check?"))
#  if number%2 == 0:
#      print("Your number is even.")
# else:
#     print("Your number is odd.")
# height = float(input("What is your height in m?"))
# weight = float(input("What is your weight in kg?"))
# #
# BMI = weight/height**2
# print(BMI)
#
# if BMI < 18.5:
#     print("You are underweight.")
# elif BMI < 25:
#     print("You have a normal weight")
# elif BMI < 30:
#     print("You are overweight.")
# elif BMI < 35:
#     print("Debeo si!")
# else:
# #     print("Prase debelo")
#
# year = int(input("Which year do you want to check? "))
#
# if year%400 == 0 and year/400:
#     print("This year is a leap year.")
# elif year%4 == 0 and (not year/100):
#     print("This year is a leap year.")
# else:
#     print("This year is not a leap year.")

# print("Welcome to Python Pizza Deliveries!")
# size = input("What size pizza do you want? S, M, or L ")
# add_pepperoni = input("Do you want pepperoni? Y or N ")
# extra_cheese = input("Do you want extra cheese? Y or N ")
#
# bill = 0
# if size == "S":
#     bill += 15
# elif size == "M":
#     bill += 20
# else:
#     bill += 25
#
# if extra_cheese == "Y":
#     bill += 1
# else:
#     bill += 0
#
# if add_pepperoni == "Y":
#     if size == "S":
#         bill += 2
#     else:
#         bill += 3
#
# print(f"Your final bill is ${bill}")


















#
# print("Welcome to Python Pizza Deliveries!")
# size = input("What size pizza do you want? S, M, or L ")
# add_pepperoni = input("Do you want pepperoni? Y or N ")
# extra_cheese = input("Do you want extra cheese? Y or N ")
#
# bill = 0
#
# if size == "S":
#     bill += 15
# elif size == "M":
#     bill += 20
# else:
#     bill += 25
# if add_pepperoni == "Y":
#     if size == "S":
#         bill += 2
#     else:
#         bill += 3
# if extra_cheese == "Y":
#     bill += 1
#
# print(f"Your final pizza value is ${bill}")

#
# print("Welcome to the Love Calculator!")
# name1 = input("What is your name? \n")
# name2 = input("What is their name? \n")
# lower_case_name = name1.lower()
# lower_case_name2 = name2.lower()
# love = ((lower_case_name.count("l") + lower_case_name.count("o") + lower_case_name.count("v") +lower_case_name.count("e") +lower_case_name2.count("l") + lower_case_name2.count("o") + lower_case_name2.count("v") +lower_case_name2.count("e")) )
# true = ((lower_case_name.count("t") + lower_case_name.count("r") + lower_case_name.count("u") +lower_case_name.count("e") + lower_case_name2.count("t") + lower_case_name2.count("r") + lower_case_name2.count("u") +lower_case_name2.count("e")) )
# score = str(true) + str(love)
#
# score = int(score)
# if score <10 or score>90:
#     print(f'Your score is {score}, you go together like coke and menots.')
# elif score >= 40 and score <= 50:
#     print(f"Your score is {score}, you are alright together.")
# else:
#     print(f"Your score is {score}")
# print("Welcome to Treasure Island.")
# print("Your mission is to find the treasure")
# first_decision = (input("Where do you want to go,'Left' or 'Right'?"))
# if first_decision == "Left":
#     #print(input('You come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across.'))
#     second_decision = (input('You come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across.'))
#     if second_decision == "wait":
#         #print(input("You patient motherfucker, u arrived unharmed to the island. Now there is a house with three doors and by opening two of them u die, u die motherfucker, only 33% to survive.Now choose 'red' 'yellow' or 'blue' "))
#         final_decison = input("You patient motherfucker, u arrived unharmed to the island. Now there is a house with three doors and by opening two of them u die, u die motherfucker, only 33% to survive.Now choose 'red' 'yellow' or 'blue' ")
#
#         if final_decison == "red":
#             print("You found the treasure and you survive.")
#         else:
#             print("Dumb way to die.")
#     else:
#         print("DIe dumb bitch")
#
#
# else:
#     print("You die")

#
# import random
# random_integer = random.randint(1, 10)
# print(random_integer)
#
# random_float = random.random()
# print(random_float*5)

# import random
# random_number = (random.randint(0,1))
# random_number = input(0,1)
# if random_number == 1:
#     print("Heads")
# else:
#     print("Tails")

# import random
#
# toss_coin = random.randint(0, 1)
# if toss_coin == 1:
#     print("Heads")
# else:
#     print("Tails")



# names_string = input("Give me everybody's names, separated by a comma. ")
# names = names_string.split(", ")
#
# num_items = len(names)
# import random
#
# random_name = random.randint(0,len(names)-1)
#
# random_person = names[random_name]
#
# print(f"{random_person} pays the dinner")

#
# row1 = ["⬜️","️⬜️","️⬜️"]
# row2 = ["⬜️","⬜️","️⬜️"]
# row3 = ["⬜️️","⬜️️","⬜️️"]
# map = [row1, row2, row3]
# print(f"{row1}\n{row2}\n{row3}")
# position = input("Where do you want to put the treasure? ")
#
# horizontal = int(position[1])
# vertical = int(position[0])
#
# selected = map[horizontal-1]
# selected[vertical-1] = "X"
# print(f"{row1}\n{row2}\n{row3}")



# fruits = ["Apple", "Peach", "Pear"]
# for fruit in fruits:
#     print(fruit)
#     print(fruit + " pie")

# student_heights = input("Input a list of student heights ").split()
# for n in range(0, len(student_heights)):
#   student_heights[n] = int(student_heights[n])
# denominator = (len(student_heights))
# numerator = (sum(student_heights))
#
# average_height = round(numerator/denominator)
#
# print(f"Average height is {average_height}cm")

#
# student_scores = input("Input a list of student scores ").split()
# for n in range(0, len(student_scores)):
#   student_scores[n] = int(student_scores[n])
# print(student_scores)
# highest_score = 0
# for score in student_scores:
#     if score > highest_score:
#         highest_score = score
# print(f"The highest score in the class is: {highest_score}")
#
# for number in range(1,11,3):
#     print(number)
# total = 0
# for number in range(1, 101):
#     total += number
# print(total)

# total = 0
# for number in range(2,101,2):
#     total += number
# print(total)
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

#
# for number in range(0,101):
#     if number % 3 == 0 and number % 5 == 0:
#         print("FizzBuzz")
#     elif number % 3 == 0:
#         print("Fizz")
#     elif number % 5 == 0:
#         print("Buzz")
#     else:
#         print(number)

# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#
# #


# import random
# letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
# numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
# symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
#
# password = []
#
# print("Welcome to the PyPassword Generator!")
# nr_letters = int(input("How many letters would you like in your password?\n"))
# nr_symbols = int(input(f"How many symbols would you like?\n"))
# nr_numbers = int(input(f"How many numbers would you like?\n"))
# for kurcina in range(1, nr_letters + 1):
#     password += random.choice(letters)
#
#
# for symbol in range(1, nr_symbols+1):
#     random_symbol = random.choice(symbols)
#     password.append(random_symbol)
#
#
# for num in range(1, nr_numbers +1):
#     random_nu = random.choice(numbers)
#     password.append(random_nu)
# print(password)
# random.shuffle(password)
# sifra = ""
# for i in password:
#     sifra += i
#
# print(f'Your password is {sifra}')
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

# list = [1,2,3,4,5,6,7,8]
# import random
#
# def greet(name):
#     random_num = random.choice(list)
#     if random_num > 5:
#         print(f"Hello, how was your day today {name}?")
#     else:
#         print(f"What did you eat today {name}?")
#
# greet("Ivan")

# def greet_with(name, location):
#     print(f'Hello {name}')
#     print(f"What is it like in {location}")
#
# greet_with("Marko", "Florida")



