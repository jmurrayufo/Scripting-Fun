import itertools

class players:
	name = "none"
	ADC = 0
	Mid = 0
	Top = 0
	Jungle = 0
	Support = 0
#Still need to add a few of the 'usual' players, get relative skill levels for everyone
Skyfire156 = players()
Skyfire156.name = "Skyfire156"
Skyfire156.ADC = 60
Skyfire156.Mid = 40
Skyfire156.Top = 40
Skyfire156.Jungle = 40
Skyfire156.Support = 50

Soton = players()
Soton.name = "Soton"
Soton.ADC = 20
Soton.Mid = 20
Soton.Top = 20
Soton.Jungle = 60
Soton.Support = 70

Mongo988 = players()
Mongo988.name = "Mongo988"
Mongo988.ADC = 30
Mongo988.Mid = 50
Mongo988.Top = 50
Mongo988.Jungle = 10
Mongo988.Support = 30

pub1 = players()
pub1.name = "pubby number 1"
pub2 = players()
pub2.name = "pubby number 2"
pub3 = players()
pub3.name = "pubby number 3"
#makes sure the pubbys get the roles they pick
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
			pub3.ADC = 101
		if pubrolex == "Mid":
			pub3.Mid = 101
		if pubrolex == "Top":
			pub3.Top = 101
		if pubrolex == "Jungle":
			pub3.Jungle = 101
		if pubrolex == "Support":
			pub3.Support = 101
# determines number of players vs pubbys
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
	pubrole1 = raw_input("Role of pubby number 1? (ADC, Mid, Top, Jungle, Support )") 
	pubbyroles(pub1, pubrole1)
if numpub >= 2:
	player4 = pub2
	pubrole2 = raw_input("Role of pubby number 2? (ADC, Mid, Top, Jungle, Support)")
	pubbyroles(pub2, pubrole2)
if numpub == 3:
	player3 = pub3
	pubrole3 = raw_input("Role of pubby number 3? (ADC, Mid, Top, Jungle, Support)")
	pubbyroles(pub3, pubrole3)
	
def rolepermute():
	for role in itertools.permutations('abcde',5):
		yield role
# does math		
def optimalroles (player1, player2, player3, player4, player5):
	p1 = 0
	p2 = 0
	p3 = 0
	p4 = 0
	p5 = 0
	score = p1+p2+p3+p4+p5
	#takes the permutations and assigns them- position is player number, letter is role
	for role1 in rolepermute():
		if role1[0] == 'a':
			p1 = player1.ADC
		if role1[0] == 'b':
			p1 = player1.Mid
		if role1[0] == 'c':
			p1 = player1.Top
		if role1[0]== 'd':
			p1 = player1.Jungle
		if role1[0] == 'e':
			p1 = player1.Support
		if role1[1] == 'a':
			p2 = player2.ADC
		if role1[1] == 'b':
			p2 = player2.Mid
		if role1[1] == 'c':
			p2 = player2.Top
		if role1[1]== 'd':
			p2 = player2.Jungle
		if role1[1] == 'e':
			p2 = player2.Support
		if role1[2] == 'a':
			p3 = player3.ADC
		if role1[2] == 'b':
			p3 = player3.Mid
		if role1[2] == 'c':
			p3 = player3.Top
		if role1[2]== 'd':
			p3 = player3.Jungle
		if role1[2] == 'e':
			p3 = player3.Support
		if role1[3] == 'a':
			p4 = player4.ADC
		if role1[3] == 'b':
			p4 = player4.Mid
		if role1[3] == 'c':
			p4 = player4.Top
		if role1[3]== 'd':
			p4 = player4.Jungle
		if role1[3] == 'e':
			p4 = player4.Support
		if role1[4] == 'a':
			p5 = player5.ADC
		if role1[4] == 'b':
			p5 = player5.Mid
		if role1[4] == 'c':
			p5 = player5.Top
		if role1[4]== 'd':
			p5 = player5.Jungle
		if role1[4] == 'e':
			p5 = player5.Support
#'saves' a score and compares it to the next iteration
		score1 = p1+p2+p3+p4+p5
		if score1 > score:
			score = score1
			order = [role1]
#'unpacks' the permutation saved as best
		stuffit = order[0]
	if stuffit[0] == "a":
		r1 = "ADC"
	if stuffit[0] == "b":
		r1 = "Mid"
	if stuffit[0] == "c":
		r1 = "Top"
	if stuffit[0] == "d":
		r1 = "Jungle"
	if stuffit[0] == "e":
		r1 = "Support"
	if stuffit[1] == "a":
		r2 = "ADC"
	if stuffit[1] == "b":
		r2 = "Mid"
	if stuffit[1] == "c":
		r2 = "Top"
	if stuffit[1] == "d":
		r2 = "Jungle"
	if stuffit[1] == "e":
		r2 = "Support"
	if stuffit[2] == "a":
		r3 = "ADC"
	if stuffit[2] == "b":
		r3 = "Mid"
	if stuffit[2] == "c":
		r3 = "Top"
	if stuffit[2] == "d":
		r3 = "Jungle"
	if stuffit[2] == "e":
		r3 = "Support"
	if stuffit[3] == "a":
		r4 = "ADC"
	if stuffit[3] == "b":
		r4 = "Mid"
	if stuffit[3] == "c":
		r4 = "Top"
	if stuffit[3] == "d":
		r4 = "Jungle"
	if stuffit[3] == "e":
		r4 = "Support"
	if stuffit[4] == "a":
		r5 = "ADC"
	if stuffit[4] == "b":
		r5 = "Mid"
	if stuffit[4] == "c":
		r5 = "Top"
	if stuffit[4] == "d":
		r5 = "Jungle"
	if stuffit[4] == "e":
		r5 = "Support"
	print player1.name+" is "+r1
	print player2.name+" is "+r2
	print player3.name+" is "+r3
	print player4.name+" is "+r4
	print player5.name+" is "+r5

optimalroles(player1, player2, player3, player4, player5)
