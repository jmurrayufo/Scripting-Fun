import os
import re
import shutil
import os.path

TO = []
FROM = []

def lstapp(lst, path):
    for folders in listdir(path):
        if isafolder(folders) == True:
            newpath = pathapp(folders, path)
            if lst == "TO":
                TO.append(newpath)
            if lst == "FROM":
                FROM.append(newpath)

def compfunc (pathA, pathB):
    A = set(listdir(pathA))
    B = set(listdir(pathB))
    C = set()
    if A.intersection(B) > C:
        return True
    else:
        return False

def diffunc(pathA, pathB):
    A = set(pathA)
    B = set(pathB)
    return A - B

def fromiter(FROM, TO):
    if compfunc(FROM, TO) == True:
        copyfunc(FROM, TO)
        lstapp("FROM", FROM)
    else:
        lstapp("FROM", FROM)


def isafolder(qry):
    find = re.search(r"\.\w{2,4}$",qry)
    if os.path.isdir(qry) == True and os.path.islink(qry) == False:
        return True
    else:
        return False

copyticker = 0            
copylist = []

def copyfunc(cpyfrm, cpyto):
    FROMC = listdir(cpyfrm)
    TOC = listdir(cpyto)
    copyticker = 0
    for items in diffunc(FROMC, TOC):
        newcpy = pathapp(items, cpyfrm)
        if isafolder(newcpy) == True:
            newto = pathapp(items, cpyto)
            shutil.copytree(newcpy, newto)
            copyticker += 1
            copylist.append(newcpy)
        else:
            copyticker += 1
            shutil.copy2(newcpy, cpyto)
            copylist.append(newcpy)
        

def pathapp(folder, path):
    return path+"\\"+folder

def wrapup():
    for things in TO:
        lstapp("TO", things)
        for stuff in FROM:
            fromiter(stuff, things)
    if copyticker == 0:
        copyfunc(FROMpath, TOpath)
    print copyticker
    print copylist

def listdir(path):
    return os.listdir(path)

while(1):
    FROMpath = raw_input("place you want to back up FROM?")
    TOpath = raw_input("place you want to back up TO?")

    TO.append(TOpath)
    FROM.append(FROMpath)

    wrapup()
