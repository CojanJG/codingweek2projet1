def suppression_espace_string(string):
    liste=list(string)
    m=0
    while m<len(liste) and liste[m]==' ':
        liste.pop(0)
        #on supprime les espaces
        m+=1
    for m in range(1,len(liste)):
        #on repasse à un seul string en concatenant notre liste de string et le mot se retrouve en position 0
        liste[0]=liste[0]+liste[m]
    while len(liste)>1:
        liste.pop(-1)
    if len(liste)>0:
        string=liste[0]            #on passe d'une liste de string à un string : ["machin"] -> "machin"
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
            if code_list[i] in code_list[i:]:    #on retrouve cette ligne dans les lignes qui suivent
                #on vérifie si cette ligne n'a pas déjà été compté comme redondante
                j=-1
                for k in range(len(result)):
                    if code_list[i]==result[k][0]:
                        j=k
                if j!=-1:
                    result[j][1]+=1
                else:
                    result.append([code_list[i],2])
        return result


