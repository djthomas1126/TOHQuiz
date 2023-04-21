import os
arr = []
def stripNewLine():
    current_directory = os.path.dirname(__file__)
    print(current_directory)
    current_directory += "\Transcripts\ALyingWitchAndAWarden.txt"
    print(current_directory)
    file = open(current_directory, encoding="utf8")
    lines = file.readlines()
    
    

    for x in lines:
        y = x.strip("\n")
        if y != "": 
            arr.append(y)
        # if lines[x] != "\n":
        #     print(lines[x])
arr2 = []
def stripBrackets():
    
    row = 0
    for x in arr:
        arr2.append("")
        i = 0
        while i < len(x):
            if (x[i] == "["):
                while True:
                    i+=1
                    if x[i] == "]":
                        i+=1
                        break
            if i < len(x):
                arr2[row] += x[i]
               
            i += 1

        row+=1 
    #print(arr2)   


stripNewLine()
stripBrackets()

arr3 = []
for x in arr2:
    if x != "":
        arr3.append(x)

#print(arr3)
print(os.path.dirname(__file__))
f = open(os.path.dirname(__file__) + "\\new\\test.txt", "w")
for x in arr3:
    f.write(x.strip() + "\n")