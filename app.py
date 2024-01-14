from string import ascii_letters
from string import ascii_uppercase
from random import choice
from random import randrange
letters = ascii_uppercase + ascii_letters
change_letters =""
user_select_number = int(input("Please enter the length of your password"))
random_number = randrange(len(letters))
if random_number > user_select_number:
    user_select_number = user_select_number + random_number
while len(letters) >= len(change_letters):
    change_letters += choice(letters)
random_password_generator = change_letters[random_number:user_select_number]
print(random_password_generator)