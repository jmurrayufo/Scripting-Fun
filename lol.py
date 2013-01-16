import random
 
items = [
        ["Abyssal Scepter",                 2650],
        ["Aegis of the Legion",             2150],
        ["Atma's Impaler",                  2300],
        ["Banner of Command",               2400],
        ["Banshee's veil",                  2500],
        ["Bilgewater Cultlass",             1925],
        ["Executioner's calling",           1900],
        ["Guardian Angel",                  2600],
        ["Guinsoo's Rageblade",             2600],
        ["Hextech Sweeper(dominion/TT)",    1920],
        ["Kitae's Bloodrazor(dominion/tt)", 2525],
        ["Last Whisper",                    2135],
        ["Locket of the Iron Solari",       2000],
        ["Malady",                          2035],
        ["Manamune",                        2100],
        ["Mikael's Crucible",               2200],
        ["Morellonomicon",                  2200],
        ["Nashor's tooth",                  2500],
        ["Odyn's veil(Dominion/TT)",        2610],
        ["Overlord's bloodmail",            2455],
        ["Rod of Ages",                     2800],
        ["Shard of True Ice",               1700],
        ["Shurelya's Reverie",              2100],
        ["Spirit Visage",                   2200],
        ["Spirit of the Ancient Golem",     2400],
        ["Spirit of the Elder Lizard",      2400],
        ["Spirit of the Spectral Wraith",   2400],
        ["Statikk Shiv",                    2500],
        ["Sunfire Cape",                    2500],
        ["Sword of the Divine",             2200],
        ["The brutalizer",                  1337],
        ["Thornmail",                       2200],
        ["Tiamat",                          2300],
        ["Twin Shadows",                    1900],
        ["Void Staff",                      2295],
        ["Warmog's Armor",                  2650],
        ["Wicked Hatchet",                  2840],
        ["Will of the Ancients",            2500],
        ["Wit's end",                       2200],
        ["Zeke's Herald",                   2450]
        ]
 
choices = [ "All Yordle", 
            "All AD Carry",
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
            "Unique Shoes"]
stuff = 1
while(stuff < 5): 
    result = random.choice(choices)
    print "Rules:",result
    if(result=="Alphabet"):
        print "You must spell something out!"
    elif(result=="Fill Dorians"):
        print "Only boots/dorians items until inventory is full, then may proceed with normal build"
    elif(result=="Pick Item"):
        Item = random.choice(items)        
        print "Everyone MUST build a(n) %s by %d minutes."%(Item[0], Item[1]/96+1+1.5+3)
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
    raw_input("you may reroll %s times..." %(5-stuff))
    stuff += 1
    continue
