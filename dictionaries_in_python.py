'''
myDict = {
    "Fast": "In a Quick manner",
    "Harsh": "A Coder",
    "Marks" : [1, 2, 3, 4],
    "anotherdict": {'harsh': 'uwu'}
}

print(myDict["Fast"])
print(myDict["Harsh"])
print(myDict["Marks"])
print(myDict['anotherdict'])
print(myDict['anotherdict']['harsh'])
'''


myDict = {
    "fast": "In a Quick manner",
    "harsh": "A Coder",
    "marks" : [1, 2, 3, 4],
    "anotherdict": {'harsh': 'uwu'},
    1:2
}


#Dictionary Methods
print(list(myDict.keys()))
print(myDict.values())
print(myDict.items())
print(myDict)
updateDict = {
    "Aayush" : "Friend",
    2:3,
     "harsh": "A typer",
}
myDict.update(updateDict)
print(myDict)

print(myDict.get("harsh2")) #it just prints none since the harsh2 is not present in the dictionary 
#print(myDict["harsh2"]) #it throws error since it is not present in the dictionary

