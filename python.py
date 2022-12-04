#This is the welcome screen and level select
print("Welcome to Riddle Me This")
print("The rules are simple you are given a discription and have to spell the word that fits it.")
print("Please select a difficultiy")
print("1 for Easy")
print("2 for Normal")
print("3 for Hard")
leveldifficalty = int(input())
#This is the easy levels
if leveldifficalty == 1:
    print("This celestial object orbits the sun and has a moon but isn't made of gas")
    level1easyuseranswer = input("")
    if level1easyuseranswer == "Earth":
        print("Correct")
    elif level1easyuseranswer == "earth":
        print("Correct")
    elif level1easyuseranswer != "Earth":
        print("Wrong")
    if level1easyuseranswer == "Earth":
        print("Level 1 completed")
    elif level1easyuseranswer == "earth":
        print("Level 1 completed")
    if level1easyuseranswer == "Earth":
        level1easycompletion = "Correct"
    elif level1easyuseranswer == "earth":
        level1easycompletion = "Correct"
    if level1easycompletion == "Correct"
        print("")
#This is the Normal Levels
if leveldifficalty == 2:
    print("This thing lives in the desert it can't move but can hurt")
    level1Normaluseranswer = input("")
    if level1Normaluseranswer == "Cactus":
        print("Correct")
    elif level1Normaluseranswer == "cactus":
        print("Correct")
    elif level1Normaluseranswer != "Cactus":
        print("Wrong")
    print("Level 1 completed")
    if level1Normaluseranswer == "Cactus":
        level1normalcompletion = "Correct"
    elif level1Normaluseranswer == "cactus":
        level1Normalcompletion = "Correct"
#This is the Hard levels
if leveldifficalty == 3:
    print("This invention has been used to capture history")
    level1harduseranswer = input("")
    if level1harduseranswer == "Camera":
        print("Correct")
    elif level1harduseranswer == "camera":
        print("Correct")
    elif level1harduseranswer != "Camera":
        print("Wrong")
    print("Level 1 completed")
    if level1harduseranswer == "Camera":
        level1hardcompletion = "Correct"
    elif level1harduseranswer == "camera":
        level1hardcompletion = "Correct"
#End
