import itertools
import time # testing delays
import re

class players:
	name = "none"
	ADC = 0
	Mid = 0
	Top = 0
	Jungle = 0
	Support = 0

"""
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
"""
def AltOptimalRoles(players):
	assert(len(players)==5)
	maxVal = 0
	maxList = list()
	for i in itertools.permutations(players,5):
		tmpVal = CalculateRolesValue(i)
		if tmpVal >= maxVal:
			# print "\nFound new best!"
			if tmpVal > maxVal:
				maxList = list()
			maxList.append(i)	
			maxVal = tmpVal
			# print "    ADC:",maxList[-1][0].name
			# print "    Mid:",maxList[-1][1].name
			# print "    Top:",maxList[-1][2].name
			# print " Jungle:",maxList[-1][3].name
			# print "Support:",maxList[-1][4].name
			# print "Total Score: %d"%(maxVal)
	return maxList

def CalculateRolesValue(players):
	"""
	Calcuate the value of a given list of players and return that value
	"""
	assert(len(players)==5)
	# lists are in order of ADC, Mid, Top, Jungle, Support
	retVal = 0
	# This set of lines makes it clear that the class Players should really have an array
	#	of numbers, not a set of attributes. It would be less lines to go thorugh given the
	#	simplicity of the data. No worries, not worth fixing now xD
	retVal += players[0].ADC
	retVal += players[1].Mid
	retVal += players[2].Top
	retVal += players[3].Jungle
	retVal += players[4].Support

	return retVal

def ParsePubbyStr(pubStr):
	"""ADC, Mid, Top, Jungle, Support"""
	reStr = "((?:[aA](?:[dD][cC]))"
	reStr += "|(?:[mM](?:id))"
	reStr += "|(?:[tT](?:op))"
	reStr += "|(?:[jJ](?:ungler?))" # Hey look, that R is optional!
	reStr += "|(?:[sS](?:upport))"
	reStr += ")"

	retVal = players()

	pointVal = 100
	# Find a thing
	while(1):
		match	= re.search(reStr,pubStr)	
		if(match):
			print match.group(0)
			# Modify player
			if match.group(0)[0] == "A" or match.group(0)[0] == "a":
				retVal.ADC = pointVal
			elif match.group(0)[0] == "M" or match.group(0)[0] == "m":
				retVal.Mid = pointVal
			elif match.group(0)[0] == "T" or match.group(0)[0] == "t":
				retVal.Top = pointVal 
			elif match.group(0)[0] == "J" or match.group(0)[0] == "j":
				retVal.Jungle = pointVal 
			elif match.group(0)[0] == "S" or match.group(0)[0] == "s":
				retVal.Support = pointVal
			else:
				assert(0),"Invalid string passed matches" 
			pointVal-=20
			# Modify string so we don't match this again
			pubStr = re.sub(match.group(0),"",pubStr)
		else:
			break
	return retVal

#Still need to add a few of the 'usual' players, get relative skill levels for everyone
# Generate a list of players that we normally play with. We don't need to name each object, as the list keeps track of that for us.
regPlayers = list()

# We can reuse tmp every time, and throw it away when done
tmp = players()
tmp.name = "Skyfire156"
tmp.ADC = 60
tmp.Mid = 40
tmp.Top = 40
tmp.Jungle = 40
tmp.Support = 50
regPlayers.append(tmp)

tmp = players()
tmp.name = "Soton"
tmp.ADC = 1
tmp.Mid = 10
tmp.Top = 20
tmp.Jungle = 75
tmp.Support = 90
regPlayers.append(tmp)

tmp = players()
tmp.name = "Mongo988"
tmp.ADC = 30
tmp.Mid = 50
tmp.Top = 50
tmp.Jungle = 10
tmp.Support = 30
regPlayers.append(tmp)

# We are done with this varibale, delete it. We dont NEED to, its small, but its nice to do it anyway
del tmp

"""
# Section commented out to make way for clean code
pub1 = players()
pub1.name = "pubby number 1"
pub2 = players()
pub2.name = "pubby number 2"
pub3 = players()
pub3.name = "pubby number 3"
#makes sure the pubbys get the roles they pick

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
optimalroles(player1, player2, player3, player4, player5)
"""
# Get initial input
print "How many regular players do you have? (The rest are pubbys)"
numRegPlayers = input(">")

# Error check our input
assert(1 < numRegPlayers <= 5),"Players must be from 2-5!!!"
assert(numRegPlayers <= len(regPlayers)),"You don't have that many regulars in the list..."


# Loop until we have enough players (we might need to re-loop a few times for errors)
actualPlayers = list()
while(len(actualPlayers) < numRegPlayers):
	print "\nSelect person to add to the roster"
	# Display the list of players we can pick from
	for p in range(len(regPlayers)):
		print p,":",regPlayers[p].name

	# Get user input
	# We might get junk data, except this and continue
	try:
		index = input(">")
		actualPlayers.append(regPlayers.pop(index))
	except KeyboardInterrupt:
		raise
	except:
		print ">>>You dun goofed, try again!<<<"
		continue # Not needed, here for clarity

# Debug printing, not really needed
for i in actualPlayers:
	print i.name

# We need to fill in the pubby info

while(len(actualPlayers) < 5):
	print "\nWhat is pubby #%d doing?"%(len(actualPlayers)+1)
	print "ADC, Mid, Top, Jungle, Support (Only first letter is needed)"
	role = raw_input(">")

	# General a simple template for that person
	# TODO: This function would be way cooler if the pubby could tell us a few roles, and then we can test them all
	tmp = ParsePubbyStr(role)
	tmp.name = "Pubby%d"%(len(actualPlayers)+1)

	if(tmp.ADC or tmp.Mid or tmp.Top or tmp.Jungle or tmp.Support):
		actualPlayers.append(tmp)
	del tmp

roles = AltOptimalRoles(actualPlayers)
print "Selected %d Role Lists"%(len(roles))

for i in roles:
	print
	print "    ADC:",i[0].name
	print "    Mid:",i[1].name
	print "    Top:",i[2].name
	print " Jungle:",i[3].name
	print "Support:",i[4].name
print "\nTotal Score: %d"%(CalculateRolesValue(i))