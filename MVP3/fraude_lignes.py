def suppression_espace_string(string):
    list=list(string)
    m=0
    while m<len(list) and list[m]==' ':
        list.pop(0)
        #on supprime les espaces
        m+=1
    for m in range(1,len(list)):
        #on repasse à un seul string en concatenant notre liste de string et le mot se retrouve en position 0
        list[0]=list[0]+list[m]
    while len(list)>1:
        list.pop(-1)
    if len(list)>0:
        string=list[0]            #on passe d'une liste de string à un string : ["machin"] -> "machin"
    return string




def fraude_lignes(path1,path2):
    with open(path1,'r') as code1:
        with open(path2,'r') as code2:
            code1_list=list(code1)
            code2_list=list(code2)
            #on supprime d'abord les espaces préliminaires dans les lignes
            for i in range(len(code1_list)):
                code1_list[i]=suppression_espace_string(code1_list[i])
            for i in range(len(code2_list)):
                code2_list[i]=suppression_espace_string(code2_list[i])
            #on crée result qui sera une liste de couple contenant la ligne présente dans les deux dossiers et le nombre de fois qu'on les retrouve
            result=[]
            for i in range(len(code1_list)):
                if code1_list[i] in code2_list and code1_list[i] not in result:
                    #la ligne est dans le 2ème code mais pas déja compté dans result
                    result.append([code1_list[i],1])
                elif code1_list[i] in code2_list :
                    #la ligne est dans code2 et dans result donc on cherche l'endroit dans result et on incrémente
                    k=0
                    while code1_list[i]!=result[k][0] and k<len(result):
                        k+=1
                    result[k][1]+=1
            return result

