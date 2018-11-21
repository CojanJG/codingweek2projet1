def countVariables(filePath):
    with open (filePath,'r') as file :
        fileList=list(file)
        nombreDeVariables=0
        for ligne in fileList:
            if len(ligne)>=2:
                for k in range(1,len(ligne)):
                    if ligne[k]=='=' and ligne[k+1]!='=' and (ligne[k-1] not in ['=','!','+','>','<']):
                        nombreDeVariables+=1
    return nombreDeVariables
    
# print(countVariables("test.txt"))


# print(countVariables("EventCandidatA.rb"))
