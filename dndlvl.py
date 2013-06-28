def XP2Level(xp):
    levelCap = 1000
    level = 1
    while xp >= levelCap and level < 20:
        level += 1
        levelCap += level*1000
    return level

testXPs = [0,1e3,3e3,6e3,
            10e3,15e3,21e3,
            28e3,36e3,45e3,
            55e3,66e3,78e3,
            91e3,105e3,120e3,
            136e3,153e3,171e3,
            190e3]

for i in testXPs:
    print i,XP2Level(i)
