'''
Aahan Mehta, Shreya Roy
SoftDev
K05 -- bitsream
2022-09-29
time spent: 0.7
DISCO:
QCC:
OPS SUMMARY:
    1. Check if dictionary is empty
    2. Pick a random key after making a list of the keys in dictionary
    3. Checks if there aren't any elements in key
    4. Pick random element from dictionary in subsection key, using random.choice()
    5. Returns a list with both krewe member and period
    6. Prints output depending on situation (discovered by checks)
'''
import random

def makeDict(filename):
    dict = {}
    file = open(filename)
    fileStr = file.read()
    file.close()
    fileStr = fileStr.replace("\n","")
    # print(fileStr)
    devoInfoStr = fileStr.split("@@@")
    # print(devoInfoStr)
    for devo in devoInfoStr:
        infos = devo.split("$$$")
        # print(infos)
        key = int(infos[0])
        if key not in dict:
            dict[key] = []
        dict[key].append((infos[1], infos[2]))
    return dict


def getRandKrew(nums):
    if len(nums) == 0:
        return ["empty dict"]
    key = random.choice(list(nums.keys()))
    if len(nums[key]) == 0:
        return ["empty key"]
    return [random.choice(nums[key]), key]

print(getRandKrew(makeDict("krewes.txt")))
