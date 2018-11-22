def nomsVariables(filePath):
    #renvoie la liste des noms des varibles utilisées
    with open (filePath,'r') as file :
        fileList=list(file)
        noms=[]
        for i in range (len(fileList)):
            if " = " in fileList[i]:
                caracteres = list(fileList[i])
                k=caracteres.index("=")
                l=k-2
                while fileList[i][l]!=' ':
                    l=l-1
                noms.append(fileList[i][l+1:k-1])
    return (noms)



import enchant
def testNoms (noms):
    #renvoi un duet avec le nombre de variables bien nommées et le nombre de variables mal nommées
    d = enchant.Dict("en_US")
    bonnesVariables = 0
    mauvaisesVariables = 0
    for i in range (len(noms)):
        if d.check(noms[i]) :
            bonnesVariables=bonnesVariables + 1
        else :
            mauvaisesVariables=mauvaisesVariables + 1
    return([bonnesVariables, mauvaisesVariables])
    
#print(testNoms(nomsVariables('EventCandidatA.rb')))
#print(nomsVariables('EventCandidatA.rb'))

