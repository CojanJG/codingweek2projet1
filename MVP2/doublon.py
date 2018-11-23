def suppression_espace_string(string):
    liste=list(string)
    m=0

    while liste[0]==" ":
        liste.pop(0)

#    while m<len(liste) and liste[m]==' ':                   #attention ici m augmente mais on supprime tooujours l'élément 0!!
#        liste.pop(0)
#        #on supprime les espaces en début de ligne
#        m+=1

    for m in range(1,len(liste)):
        #on repasse à un seul string en concatenant notre liste de string et le mot se retrouve en position 0
        liste[0]=liste[0]+liste[m]
    while len(liste)>1:
        liste.pop(-1)
    if len(liste)>0:
        string=liste[0]                                     #on passe d'une liste de string à un string : ["machin"] -> "machin"
    return string

def doublon(path):
    #trouve les lignes de code en double
    #argument = chemin du fichier à analyser
    with open(path,'r') as code:
        code_list=list(code)
        result=[]
        for i in range (len(code_list)):
            #suppression des espaces initiaux
            code_list[i]=suppression_espace_string(code_list[i])
            if code_list[i] in code_list[i+1:]:               #on retrouve cette ligne dans les lignes qui suivent
                #on vérifie si cette ligne n'a pas déjà été compté comme redondante
                j=-1
                for k in range(len(result)):
                    if code_list[i]==result[k][0]:          #on regarde si la ligne est déjà comptée comme doublon
                        j=k
                if j!=-1:
                    result[j][1]+=1                         #on ajoute un au nombre d'occurences de la ligne considérée
                else:
                    result.append([code_list[i],2])         #sinon on ajoute la ligne à la liste doublons
        return result


# print(suppression_espace_string("   bonjour merci aurevoir  "))
# print("abcd")
# print(" abcd")

print(doublon("test_mvp2.txt"))
