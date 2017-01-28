import random

def shuffle(deck):
	for i in range(len(deck)):
		new_pos = random.randrange(0, len(deck))
		deck[i], deck[new_pos] = deck[new_pos], deck[i]
	return deck

deck = []
for i in range(52):
	deck.append(i)
print(deck)
print(shuffle(deck))
