import os
import re
import shutil

TO = []
FROM = []

def lstapp(lst, path):
    for folders in os.listdir(path):
        if isafolder(folders) == "Yes":
            newpath = pathapp(folders, path)
            if lst == "TO":
                TO.append(newpath)
            if lst == "FROM":
                FROM.append(newpath)

def compfunc (pathA, pathB):
    A = set(os.listdir(pathA))
    B = set(os.listdir(pathB))
    C = set()
    if A.intersection(B) > C:
        return "similar"
    else:
        return "not"

def diffunc(pathA, pathB):
    A = set(os.listdir(pathA))
    B = set(os.listdir(pathB))
    return A - B

def fromiter(FROM, TO):
    if compfunc(FROM, TO) == "similar":
        copyfunc(FROM, TO)
        lstapp("FROM", FROM)
    else:
        lstapp("FROM", FROM)


def isafolder(qry):
    find = re.search(r"\.\w{2,4}$",qry)
    if find == None:
        return "Yes"
    else:
        return "No"

copyticker = 0            
copylist = []
def copyfunc(cpyfrm, cpyto):
    FROM = os.listdir(cpyfrm)
    TO = os.listdir(cpyto)
    for items in diffunc(FROM, TO):
        newcpy = pathapp(items, cpyfrm)
        if isafolder(items) == "Yes":
            shutil.copytree(newcpy, cpyto)
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

while(1):
    FROMpath = raw_input("place you want to back up FROM?")
    TOpath = raw_input("place you want to back up TO?")

    TO.append(TOpath)
    FROM.append(FROMpath)

    wrapup()
    
