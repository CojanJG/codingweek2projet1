def doublon(path):
    #trouve les lignes de code en double
    #argument = chemin du fichier à analyser
    with open(path,'r') as code:
        code_list=list(code)
        result=[]
        for i in range (len(code_list)):
            print(result)
            if code_list[i] in code_list[i:]:    #on retrouve cette ligne dans les lignes qui suivent
                #on vérifie si cette ligne n'a pas déjà été compté comme redondante
                j=-1
                for k in range(len(result)):
                    if code_list[i]==result[k][0]:
                        j=k
                if j!=-1:
                    result[j][1]+=1
                else:
                    result.append([code_list[i],1])
        return result,len(result)

print (doublon("test.txt"))
