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

# Currently empty class to deal with champions
class Champion():
    Name="BLANK"
    Type="BLANK"
    HP=0
    AD=0
    AP=0
    DIF=0
    Date=""
    IP=0
    RP=0

# Name, Type, HP, Attack, Spells, Difficulty, Date, IP, RP
champions =[
["Ahri"        ,"Mage",     40,  30,  80,  80,  "2011-12-14", 6300, 975],
["Akali"       ,"Assassin", 30,  50,  80,  60,  "2010-05-11", 3150, 790],
["Alistar"     ,"Tank",     90,  60,  50,  80,  "2009-02-21", 1350, 585],
["Amumu"       ,"Tank",     60,  20,  80,  40,  "2009-06-26", 1350, 585],
["Anivia"      ,"Mage",     50,  10,  100, 70,  "2009-07-10", 3150, 790],
["Annie"       ,"Mage",     30,  20,  100, 40,  "2009-02-21", 450,  260],
["Ashe"        ,"Ranged AD",30,  70,  20,  40,  "2009-02-21", 450,  260],
["Blitzcrank"  ,"Fighter",  80,  40,  50,  60,  "2009-09-02", 3150, 790],
["Brand"       ,"Mage",     20,  20,  90,  60,  "2011-04-12", 4800, 880],
["Caitlyn"     ,"Ranged AD",40,  80,  40,  40,  "2011-01-04", 4800, 790],
["Cassiopeia"  ,"Mage",     30,  20,  90,  100, "2010-12-14", 4800, 880],
["ChoGath"     ,"Tank",     40,  30,  80,  70,  "2009-06-26", 1350, 585],
["Corki"       ,"Ranged AD",30,  80,  60,  70,  "2009-09-19", 3150, 790],
["Darius"      ,"Fighter",  50,  90,  20,  30,  "2012-05-23", 6300, 975],
["Diana"       ,"Assassin", 60,  70,  80,  40,  "2012-08-07", 6300, 975],
["Dr. Mundo"   ,"Fighter",  80,  60,  70,  50,  "2009-09-02", 1350, 585],
["Draven"      ,"Ranged AD",40,  90,  20,  60,  "2012-06-06", 6300, 975],
["Elise"       ,"Mage",     50,  60,  70,  80,  "2012-10-26", 6300, 975],
["Evelynn"     ,"Assassin", 20,  40,  70,  80,  "2009-05-01", 1350, 585],
["Ezreal"      ,"Ranged AD",40,  50,  70,  80,  "2010-03-16", 4800, 880],
["Fiddlesticks","Mage",     30,  20,  90,  50,  "2009-02-21", 1350, 585],
["Fiora"       ,"Assassin", 40,  100, 30,  50,  "2012-02-29", 6300, 975],
["Fizz"        ,"Fighter",  40,  30,  70,  60,  "2011-11-15", 6300, 975],
["Galio"       ,"Tank",     70,  30,  60,  40,  "2010-08-10", 4800, 880],
["Gangplank"   ,"Fighter",  60,  70,  40,  50,  "2009-08-19", 3150, 790],
["Garen"       ,"Fighter",  40,  90,  20,  20,  "2010-04-27", 450,  260],
["Gragas"      ,"Fighter",  90,  40,  60,  60,  "2010-02-02", 3150, 790],
["Graves"      ,"Ranged AD",50,  80,  30,  40,  "2011-10-19", 6300, 975],
["Hecarim"     ,"Fighter",  60,  80,  40,  50,  "2012-04-18", 6300, 975],
["Heimerdinger","Mage",     60,  20,  80,  40,  "2009-10-10", 3150, 790],
["Irelia"      ,"Assassin", 40,  70,  50,  50,  "2010-11-16", 4800, 880],
["Janna"       ,"Support",  50,  30,  70,  90,  "2009-09-02", 1350, 585],
["Jarvan IV"   ,"Fighter",  80,  60,  30,  50,  "2011-03-01", 4800, 880],
["Jax"         ,"Assassin", 50,  70,  70,  60,  "2009-02-21", 1350, 585],
["Jayce"       ,"Fighter",  60,  60,  50,  70,  "2012-07-07", 6300, 975],
["Karma"       ,"Support",  70,  10,  80,  80,  "2011-02-01", 3150, 790],
["Karthus"     ,"Mage",     20,  20,  100, 80,  "2009-06-12", 3150, 790],
["Kassadin"    ,"Mage",     50,  30,  80,  80,  "2009-08-07", 3150, 790],
["Katarina"    ,"Assassin", 30,  40,  90,  30,  "2009-09-19", 3150, 790],
["Kayle"       ,"Support",  90,  50,  60,  30,  "2009-02-21", 450,  260],
["Kennen"      ,"Mage",     30,  40,  85,  50,  "2010-04-08", 4800, 880],
["Kha'Zix"     ,"Assassin", 40,  90,  60,  70,  "2012-09-27", 6300, 975],
["Kog'Maw"     ,"Ranged AD",20,  80,  50,  80,  "2010-06-24", 4800, 880],
["LeBlanc"     ,"Mage",     40,  10,  100, 90,  "2010-11-02", 3150, 790],
["Lee Sin"     ,"Assassin", 50,  80,  30,  80,  "2011-04-01", 4800, 880],
["Leona"       ,"Tank",     80,  40,  30,  40,  "2011-07-13", 6300, 975],
["Lulu"        ,"Support",  50,  40,  70,  50,  "2012-03-20", 6300, 975],
["Lux"         ,"Mage",     40,  20,  90,  60,  "2010-10-19", 3150, 790],
["Malphite"    ,"Fighter",  60,  50,  70,  30,  "2009-09-02", 1350, 585],
["Malzahar"    ,"Mage",     20,  20,  90,  60,  "2010-06-01", 4800, 880],
["Maokai"      ,"Tank",     80,  30,  60,  40,  "2011-02-16", 4800, 790],
["Master Yi"   ,"Assassin", 40,  90,  30,  20,  "2009-02-21", 450,  260],
["Miss Fortune","Ranged AD",20,  80,  50,  30,  "2010-09-08", 4800, 880],
["Mordekaiser" ,"Fighter",  60,  60,  60,  30,  "2010-02-24", 3150, 790],
["Morgana"     ,"Support",  60,  10,  80,  70,  "2009-02-21", 1350, 585],
["Nami"        ,"Support",  40,  30,  90,  80,  "2012-12-07", 6300, 975],
["Nasus"       ,"Fighter",  50,  70,  60,  20,  "2009-10-01", 1350, 585],
["Nautilus"    ,"Tank",     60,  40,  80,  50,  "2012-02-14", 6300, 975],
["Nidalee"     ,"Fighter",  40,  50,  70,  80,  "2009-12-17", 3150, 790],
["Nocturne"    ,"Assassin", 50,  90,  20,  50,  "2011-03-15", 4800, 880],
["Nunu"        ,"Fighter",  60,  40,  70,  30,  "2009-02-21", 450,  260],
["Olaf"        ,"Fighter",  50,  90,  30,  40,  "2010-06-09", 3150, 790],
["Orianna"     ,"Mage",     30,  40,  90,  100, "2011-06-01", 4800, 880],
["Pantheon"    ,"Assassin", 30,  90,  30,  30,  "2010-02-02", 3150, 790],
["Poppy"       ,"Fighter",  50,  40,  80,  60,  "2010-01-13", 450,  260],
["Rammus"      ,"Tank",     100, 40,  50,  50,  "2009-07-10", 3150, 790],
["Renekton"    ,"Fighter",  50,  90,  20,  30,  "2011-01-17", 4800, 880],
["Rengar"      ,"Assassin", 40,  70,  20,  50,  "2012-08-21", 6300, 975],
["Riven"       ,"Fighter",  50,  80,  10,  40,  "2011-09-14", 6300, 975],
["Rumble"      ,"Mage",     60,  30,  80,  80,  "2011-04-26", 4800, 880],
["Ryze"        ,"Mage",     20,  20,  100, 30,  "2009-02-21", 450,  260],
["Sejuani"     ,"Tank",     70,  50,  60,  40,  "2012-01-17", 6300, 975],
["Shaco"       ,"Assassin", 40,  80,  60,  90,  "2009-10-10", 3150, 790],
["Shen"        ,"Tank",     90,  30,  30,  30,  "2010-03-24", 3150, 790],
["Shyvana"     ,"Fighter",  60,  70,  50,  40,  "2011-11-01", 6300, 975],
["Singed"      ,"Tank",     60,  50,  70,  50,  "2009-04-18", 1350, 585],
["Sion"        ,"Fighter",  80,  50,  70,  40,  "2009-02-21", 1350, 585],
["Sivir"       ,"Ranged AD",30,  90,  10,  30,  "2009-02-21", 450,  260],
["Skarner"     ,"Fighter",  60,  70,  50,  50,  "2011-08-09", 6300, 975],
["Sona"        ,"Support",  50,  20,  80,  10,  "2010-09-20", 3150, 790],
["Soraka"      ,"Support",  50,  20,  70,  30,  "2009-02-21", 450,  260],
["Swain"       ,"Mage",     60,  20,  90,  50,  "2010-10-05", 4800, 880],
["Syndra"      ,"Mage",     50,  20,  90,  90,  "2012-09-13", 6300, 975],
["Talon"       ,"Assassin", 50,  90,  30,  60,  "2011-08-24", 6300, 975],
["Taric"       ,"Support",  80,  40,  50,  30,  "2009-08-19", 1350, 585],
["Teemo"       ,"Ranged AD",30,  50,  70,  40,  "2009-02-21", 1350, 585],
["Tristana"    ,"Ranged AD",40,  90,  30,  30,  "2009-02-21", 1350, 585],
["Trundle"     ,"Fighter",  60,  70,  20,  50,  "2010-12-01", 4800, 880],
["Tryndamere"  ,"Assassin", 50,  100, 20,  60,  "2009-05-01", 1350, 585],
["Twisted Fate","Ranged AD",20,  60,  60,  90,  "2009-02-21", 1350, 585],
["Twitch"      ,"Ranged AD",20,  90,  30,  80,  "2009-05-01", 3150, 790],
["Udyr"        ,"Fighter",  80,  50,  50,  70,  "2009-12-02", 3150, 790],
["Urgot"       ,"Ranged AD",50,  80,  30,  80,  "2010-08-24", 3150, 790],
["Varus"       ,"Ranged AD",30,  70,  40,  60,  "2012-05-08", 6300, 975],
["Vayne"       ,"Ranged AD",10,  90,  20,  70,  "2011-05-10", 4800, 880],
["Veigar"      ,"Mage",     20,  20,  100, 60,  "2009-07-24", 1350, 585],
["Vi"          ,"Fighter",  50,  80,  30,  50,  "2012-12-19", 6300, 975],
["Viktor"      ,"Mage",     50,  20,  80,  70,  "2011-12-29", 6300, 975],
["Vladimir"    ,"Mage",     60,  20,  80,  20,  "2010-07-27", 4800, 880],
["Volibear"    ,"Fighter",  70,  60,  40,  40,  "2011-11-29", 6300, 975],
["Warwick"     ,"Fighter",  40,  70,  40,  20,  "2009-02-21", 1350, 585],
["Wukong"      ,"Fighter",  50,  80,  20,  30,  "2011-07-26", 6300, 975],
["Xerath"      ,"Mage",     30,  10,  100, 60,  "2011-10-05", 6300, 975],
["Xin Zhao"    ,"Assassin", 60,  80,  30,  30,  "2010-07-13", 3150, 790],
["Yorick"      ,"Fighter",  60,  60,  60,  30,  "2011-06-22", 6300, 975],
["Zed"         ,"Assassin", 40,  80,  10,  80,  "2012-11-13", 6300, 975],
["Ziggs"       ,"Mage",     50,  30,  90,  70,  "2012-02-01", 6300, 975],
["Zilean"      ,"Support",  50,  20,  80,  40,  "2009-04-18", 1350, 585],
["Zyra"        ,"Mage",     30,  40,  80,  70,  "2012-07-24", 6300, 975]
]
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
