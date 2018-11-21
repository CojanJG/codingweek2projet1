
def compte_commentaires(path):
    with open(path,'r') as code:
        code_list=list(code)
        for i in range(len(code_list)):
            code_list[i]=list(code_list[i])
        number_commentaires=0
        number_commentaires_caracteres=0
        for ligne in code_list:
            for k in range(len(ligne)):
                if ligne[k]=="#":
                    number_commentaires+=1
                    number_commentaires_caracteres=number_commentaires_caracteres+len(ligne)-k
        return number_commentaires,number_commentaires_caracteres

# print(compte_commentaires("Code_candidat1.txt"))
