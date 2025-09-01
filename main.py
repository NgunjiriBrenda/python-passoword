#password
import random
print('Your password: ')

chars = 'abcdefghijklmnopqrstuvwxz1234567890!@#$%^&*()?'

password = ' '
for x in range(16):
    password += random.choice(chars)

print(password)


#random.int()
import random
print(dir(random))



#random.shuffle()
import random
cards = ["Ace", "King", "10", "Queen", "9"]
print("Original Decks:" "cards")

random.shuffle(cards)
print("Shuffled Decks:", cards)


