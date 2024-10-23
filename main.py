# Ethan Lawrence
# oct 23 2024
# Fortune Teller

import random
# import sys
import time

# Input
# Fortunes
fortunes = []
fortunes.append("You are a winner!")
fortunes.append('A secret admirer will soon send you a sign of affection!')
fortunes.append('The one you love is much closer than you think!')
fortunes.append('Good things will happen to you by the end of the day today!')
fortunes.append('Fame and fortune will be yours if you take the time to learn Python!')
fortunes.append("I'm just a computer program, and have no magical powers!")

# colors
magic_colors = []
magic_colors.append('blue')
magic_colors.append('red')
magic_colors.append('green')
magic_colors.append('yellow')

username = input('Please enter your first name:   ')

# Start
print(f'Welcome to my Python Fortune Teller program, {username}!')

question = input('Do you want me to tell you your fortune? [y/n]:   ').lower()
if question in ['y', 'yes']:
    time.sleep(1)
    color = input('Okay! To get your fortune, please input a magic color: [blue/red/green/yellow]:   ').lower()
    time.sleep(1)
    print('Getting your fortune...')
    time.sleep(2)
    print(f'Here is your fortune, {username}:')
    time.sleep(1)
    if color in magic_colors:
        print(fortunes[random.randint(0, len(fortunes) - 1)])
    else:
        print("Please choose a magic color of either 'blue', 'red', 'green', or 'yellow'.")
        time.sleep(1)
        print("Once you have input a magic color, I will reveal your fortune!")

print(f'Thank you for playing my Fortune Teller game today, {username}!')
print('Goodbye!')
