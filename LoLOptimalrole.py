import itertools
import time # testing delays
import re
import random # Has some handy funcitons

class players:
	name = "none"
	ADC = 0
	Mid = 0
	Top = 0
	Jungle = 0
	Support = 0


def AltOptimalRoles(players,tolerance=0):
	"""
		Permute though all the possiable positions the 5 players have. 
	"""
	assert(len(players)==5)
	maxVal = 0
	maxList = list()
	for i in itertools.permutations(players,5):
		tmpVal = CalculateRolesValue(i)
		if tmpVal + tolerance >= maxVal:
			# print "\nFound new best!"
			if tmpVal > maxVal:
				maxVal = tmpVal
			maxList.append(i)	

			# Purge the list of anything that fails tolerances. Note that we only do this 
			# 	if we add something new to the list! 
			for index in reversed(range(len(maxList))):
				if CalculateRolesValue(maxList[index]) + tolerance < maxVal:
					maxList.pop(index) #Remove that index
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
	"""
		Take a string, and parse it into a players() object for the permutations
	"""
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

roles = AltOptimalRoles(actualPlayers,50)
print "\nSelected %d Role Lists"%(len(roles))

# # Debug
# for i in roles:
# 	print
# 	print "    ADC:",i[0].name
# 	print "    Mid:",i[1].name
# 	print "    Top:",i[2].name
# 	print " Jungle:",i[3].name
# 	print "Support:",i[4].name
# 	print "        Score: %d"%(CalculateRolesValue(i))

final = random.choice(roles)
print
print "    ADC:",final[0].name
print "    Mid:",final[1].name
print "    Top:",final[2].name
print " Jungle:",final[3].name
print "Support:",final[4].name
print " (Score: %d)"%(CalculateRolesValue(final))
