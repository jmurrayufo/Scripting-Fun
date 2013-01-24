class players:
	ADC = 0
	Mid = 0
	Top = 0
	Jungle = 0
	Support = 0

Skyfire156 = players()
Skyfire156.ADC = 60
Skyfire156.Mid = 40
Skyfire156.Top = 40
Skyfire156.Jungle = 40
Skyfire156.Support = 50

Soton = players()
Soton.ADC = 20
Soton.Mid = 20
Soton.Top = 20
Soton.Jungle = 60
Soton.Support = 70

Mongo988 = players()
Mongo988.ADC = 30
Mongo988.Mid = 50
Mongo988.Top = 50
Mongo988.Jungle = 10
Mongo988.Support = 30

pub1 = players()
pub2 = players()
pub3 = players()

def pubbyroles(pub, pubrolex):
	if pub == pub1:
		if pubrolex == "ADC":
			pub1.ADC = 101
		if pubrolex == "Mid":
			pub1.Mid = 101
		if pubrolex == "Top":
			pub1.Top = 101
		if pubrolex == "Jungle":
			pub1.Jungle = 101
		if pubrolex == "Support":
			pub1.Support = 101
	if pub == pub2:
		if pubrolex == "ADC":
			pub2.ADC = 101
		if pubrolex == "Mid":
			pub2.Mid = 101
		if pubrolex == "Top":
			pub2.Top = 101
		if pubrolex == "Jungle":
			pub2.Jungle = 101
		if pubrolex == "Support":
			pub2.Support = 101	
	if pub == pub3:
		if pubrolex == "ADC":
			pub1.ADC = 101
		if pubrolex == "Mid":
			pub1.Mid = 101
		if pubrolex == "Top":
			pub1.Top = 101
		if pubrolex == "Jungle":
			pub1.Jungle = 101
		if pubrolex == "Support":
			pub1.Support = 101

number1 = input("How many players?")
if number1 == 1:
	print "Figure it out yourself, ya lazy bastard!"
if number1 >= 2:
	player1 = input("Summoner name of player 1?")
	player2 = input("Summoner name of player 2?")
if number1 >= 3:
	player3 = input("Summoner name of player 3?")
if number1 >= 4:
	player4 = input("Summoner name of player 4?")
if number1 == 5:
	player5 = input("Summoner name of player 5?")
numpub = 5-number1
if numpub >= 1:
	player5 = pub1
	pubrole1 = raw_input("Role of pubby number 1? '('ADC, Mid, Top, Jungle, Support ')'") 
	pubbyroles(pub1, pubrole1)
if numpub >= 2:
	player4 = pub2
	pubrole2 = raw_input("Role of pubby number 2? '('ADC, Mid, Top, Jungle, Support ')'")
	pubbyroles(pub2, pubrole2)
if numpub == 3:
	player3 = pub3
	pubrole3 = raw_input("Role of pubby number 3? '('ADC, Mid, Top, Jungle, Support ')'")
	pubbyroles(pub3, pubrole3)
#def optimalroles (player1, player2, player3, player4, player5)
	
