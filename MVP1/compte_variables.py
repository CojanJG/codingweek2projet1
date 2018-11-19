def countVariables(filePath):
    with open (filePath,'r') as file :
        fileList=list(file)
        nombreDeVariables=0
        for i in range (len(fileList)):
            nombreDeVariables=nombreDeVariables+list(fileList[i]).count(' = ')
    return N
    



print(countVariables("EventCandidatA.rb"))