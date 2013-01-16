import random
 
items = [
        ["an Abyssal Scepter",                2650],
        ["an Aegis of the Legion",            2150],
        ["an Atma's Impaler",                 2300],
        ["a Banner of Command",               2400],
        ["a Banshee's veil",                  2500],
        ["a Bilgewater Cultlass",             1925],
        ["an Executioner's calling",          1900],
        ["a Guardian Angel",                  2600],
        ["a Guinsoo's Rageblade",             2600],
        ["a Hextech Sweeper(dominion/TT)",    1920],
        ["a Kitae's Bloodrazor(dominion/tt)", 2525],
        ["a Last Whisper",                    2135],
        ["a Locket of the Iron Solari",       2000],
        ["a Malady",                          2035],
        ["a Manamune",                        2100],
        ["a Mikael's Crucible",               2200],
        ["a Morellonomicon",                  2200],
        ["a Nashor's tooth",                  2500],
        ["an Odyn's veil(Dominion/TT)",       2610],
        ["an Overlord's bloodmail",           2455],
        ["a Rod of Ages",                     2800],
        ["a Shard of True Ice",               1700],
        ["a Shurelya's Reverie",              2100],
        ["a Spirit Visage",                   2200],
        ["a Spirit of the Ancient Golem",     2400],
        ["a Spirit of the Elder Lizard",      2400],
        ["a Spirit of the Spectral Wraith",   2400],
        ["a Statikk Shiv",                    2500],
        ["a Sunfire Cape",                    2500],
        ["a Sword of the Divine",             2200],
        ["a Brutalizer",                      1337],
        ["a Thornmail",                       2200],
        ["a Tiamat",                          2300],
        ["a Twin Shadows",                    1900],
        ["a Void Staff",                      2295],
        ["a Warmog's Armor",                  2650],
        ["a Wicked Hatchet",                  2840],
        ["a Will of the Ancients",            2500],
        ["a Wit's end",                       2200],
        ["a Zeke's Herald",                   2450]
        ]
 
choices = [ "All Yordle", 
            "All AD Carry",
            "All Mid",
            "All AP Carry",
            "Jungle Fever",
            "All Human",
            "No Humans",
            "No Mana",
            "Alphabet",
            "All Support",
            "Fill Dorians",
            "No Boots",
            "No Consumables",
            "Pick Item",
            "SwapAKill",
            "Keep It Full!",
            "Max Lead",
            "Deadly Aces",
            "Unique Shoes",
            "Follow the Leader",
            "Opposite Day",
            "Low Mobility"]



while(1): 
    result = random.choice(choices)
    print "Rules:",result
    if(result=="Alphabet"):
        print "You must spell something out!"
    elif(result=="Fill Dorians"):
        print "Only boots/dorians items until inventory is full, then may proceed with normal build"
    elif(result=="Pick Item"):
        Item = random.choice(items)        
        print "Everyone MUST build %s by %d minutes."%(Item[0], Item[1]/96+1+1.5+3)
    elif(result=="SwapAKill"):
        print "Every time you get a kill, you you must swap to a new lane (your choice)"
    elif(result=="Keep It Full!"):
        print "Never leave the summoners platform will more empty inventory spaces then when you got there."
    elif(result=="Max Lead"):
        print "You may not push towers while your team is 5 or more kills ahead"
    elif(result=="Deadly Aces"):
        print "If you score an ace, all alive players MUST rush the enemy summoners platform and die there if they reach it."
    elif(result=="Unique Shoes"):
        print "Everyone must have a unique level 2+ set of boots, no duplicates!"
    elif(result=="Follow the Leader"):
        player = [1,2,3,4,5]
        minmark = [10,11,12,13,14,15,16,17,18,19,20]
        print "After the %d minute mark, everyone must follow player number %d" %(random.choice(minmark),random.choice(player))
    elif(result=="Opposite Day"):
        print "Randomly select a champion and build them for the opposite role they usually take"
    elif(result=="Low Mobility"):
        print "No flash, No ghost, No champions with gap closers/escapes"
    elif(result=="Jungle Fever"):
        junglelist = [1,2,3,4,5,6,7,8,9,10]
        jungle = random.choice(junglelist)
        if jungle >=8:
            print "Champions can only leave the jungle while everything in it is dead... in both jungles"
        else:
            print "Champions can only leave your jungle while everything in it is dead"
    raw_input("Press enter to reroll, or CTRL+C to exit\n")
