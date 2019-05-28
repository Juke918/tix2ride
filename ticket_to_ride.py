pink = 12.0
white = 12.0
blue = 12.0
yellow = 12.0
orange = 12.0
black = 12.0
red = 12.0
green = 12.0
loco = 14.0
deck = pink + white + blue + yellow + orange + black + red + green + loco

#create a function that each time that it is called, it spits out the probability of getting a pink card from the deck

def prob():
	plike = 100 * (pink / deck) #the probability of picking a pink card in %
	print (plike)
	wlike = 100 * (white / deck) #the prob of picking a white card in %
	print(wlike)
	blike = 100 * (blue / deck) #the prob of picking a blue card in %
	print (blike)
	ylike = 100 * (yellow / deck) #the prob of picking a yellow card in %
	print (ylike)
	olike = 100 * (orange / deck) #the prob of picking a orange card in %
	print (olike)
	blacklike = 100 * (black / deck) #the prob of picking a black card in %
	print ((str(blacklike) + '%'))
	rlike = 100 * (red / deck) #the prob of picking a red card in %
	print ((str(rlike)) + '%')
	glike = 100 * (green / deck) #the prob of picking a green card in %
	print ((str(glike)) + '%')
	lolike = 100 * (loco / deck) #the prob of picking a locomotive card in %
	print((str(lolike)) + '%')

prob()