import os

def readFile(fileName):

    directory = os.path.dirname(__file__)
    directory += "\\OldTranscripts\\" + fileName + ".txt"

    file = open(directory, encoding="utf-8")
    lines = file.readlines()

    return lines

def stripNewLine(lines):
    updatedLines = []
    for line in lines:
        line = line.strip("\n")
        if line != "": 
            updatedLines.append(line)
    return updatedLines

def stripBrackets(lines):
    updatedLines = []
    for line in lines:
        updatedLine = ""
        isBracket = False
        for char in line:
            if char == "[":
                isBracket = True
            elif char == "]":
                isBracket = False
            else:
                if isBracket == False:
                    updatedLine += char
        if updatedLine != "":
            updatedLines.append(updatedLine)
    return updatedLines

def stripDoubleSpaces(lines):
    updatedLines = []
    for line in lines:
        updatedLine = line[0]
        for i in range(1, len(line)):
                if not (line[i] == line[i-1] and line[i] == " "):
                    updatedLine += line[i]
        updatedLines.append(updatedLine)
    return updatedLines

def writeFile(fileName, lines):
    file = open(os.path.dirname(__file__) + "\\Transcripts\\" + fileName + ".txt", "w")
    for line in lines:
        file.write(line + "\n")
   
episodeNames = ["AdventuresInTheElements", "AgonyOfAWitch", "ALyingWitchAndAWarden", "AnySportInAStorm", "CloudsOnTheHorizon", "Covention", "EchoesOfThePast", "EclipseLake", "EdasRequiem", "EdgeOfTheWorld", "ElsewhereAndElsewhen", "EnchantingGromFright", "EscapeOfThePalisman", "EscapingExpulsion", "FolliesAtTheCovenDayParade", "ForTheFuture", "HollowMind", "HootysMovingHassle", "HuntingPalismen", "IWasATeenageAbomination", "KeepingUpAFearAnces", "KingsTide", "KnockKnockKnockinOnHootysDoor", "LabyrinthRunners", "LostInLanguage", "OnceUponASwap", "OTitanWhereArtThou", "ReachingOut", "ReallySmallProblems", "SenseAndInsensitivity", "SeparateTides", "SomethingVenturedSomeoneFramed", "ThanksToThem", "TheFirstDay", "TheIntruder", "ThemsTheBreaksKid", "ThroughTheLookingGlassRuins", "UnderstandingWillow", "WatchingAndDreaming", "WingItLikeWitches", "WitchesBeforeWizards", "YesterdaysLie", "YoungBloodOldSouls"]
for episode in episodeNames:
    lines = readFile(episode)
    lines = stripNewLine(lines)
    lines = stripBrackets(lines)
    lines = stripDoubleSpaces(lines)
    writeFile(episode, lines)