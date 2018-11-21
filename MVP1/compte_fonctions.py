def compte_fonctions(path):
    i=0
    with open(path,'r') as code:
        code2=list(code)
        for k in code2 :
            if 'def' in k:
                i=i+1
    return(i)

# compte_fonctions('code_candidat.txt')


### compte le nombre de lignes où on trouve au moins un "def", mais a priori ce ne devrait pas être gênant.
