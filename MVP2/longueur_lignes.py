def testLignes(filePath,N):
    #renvoi le nombre de lignes de plus de N caractère (On prend N=80 de manière générale)
    nombreDeLignes = 0
    with open (filePath,'r') as file :
        fileList=list(file)
        for i in range (len(fileList)):
            if len(fileList[i]) > N :
                nombreDeLignes=nombreDeLignes+1
    return(nombreDeLignes)

print(testLignes('EventCandidatA.rb',80))