

trains_str = ['pink', 'white', 'blue', 'yellow', 'orange', 'black', 'red', 'green', 'loco']

trains = [12.0, 12.0, 12.0, 12.0, 12.0, 12.0, 12.0, 12.0, 14.0]

your_hand = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

#2_hand =

pool = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

trash = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

deck_num = 0.0

def deckcheck(tranes, dek):
	dek = 0.0
	for ele in range(0, len(trains)):
		dek = dek + tranes[ele]
	print(dek)

def prob(tranes):

	deck_num = 0.0
	for ele in range(0, len(tranes)):
		deck_num = deck_num + tranes[ele]
	print('The probability for each train being drawn next is:')
	print('')
	for x in range(0, 9):
		like = tranes[x]/deck_num
		print(trains_str[x])
		print(like)
		print('')



def begin():
	print('')
	print('What is your starting hand?')
	print('')

	for x in range(0, 9):
		print('How many ' + (trains_str[x]) + '?')
		num = raw_input()
		print('')
		trains[x] = trains[x] - int(num)
		your_hand[x] = your_hand[x] + int(num)

	print('')

	print('What is the starting pool?')
	print('')



	for x in range(0, 9):
		print('How many ' + (trains_str[x]) + '?')
		num = raw_input()
		print('')
		trains[x] = trains[x] - int(num)
		pool[x] = pool[x] + int(num)

	prob(trains)


def main():
	print('')
	print('')




#deckcheck(trains, deck_num)
begin()
#prob(trains)


#class player:
	#pass

#player_list = []

#player_list.append(player("joe", 12, 15))
