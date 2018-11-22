def nombre_mot_dans_fichier(file_name,mot):             #file_name et mot sont des strings
    with open(file_name,'r') as file:
        n=0
        file_list=list(file)
        for k in file_list:                             #k est le string correspondant à une ligne
            if mot in k:
                n=n+1
    return n

#ajoute un si le mot est dans la ligne, mais un aussi si le mot y est deux fois...

def nombre_test_candidat(file_name):
    return nombre_mot_dans_fichier(file_name,'test')

def nombre_assert_candidat(file_name):
    return nombre_mot_dans_fichier(file_name,'assert')

## def liste_mots(phrase):                                 #phrase est un string qu'on veut décomposer
##     k=0
##     liste_mots=[]
##     liste_lettres=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
##     while k<len(phrase):
##         if phrase[k] in liste_lettres:
##             mot=phrase[k]
##             k=k+1
##             while (phrase[k] in liste_lettres):
##                 mot=mot+phrase[k]
##                 if k<len(phrase):
##                     k=k+1
##                 else:
##                     liste_mots=liste_mots+[mot]
##                     return liste_mots
##             liste_mots=liste_mots+[mot]
##         else:
##             k=k+1
##     return liste_mots
    


# print(nombre_test_candidat("code_candidat1.txt"))
# print(nombre_test_candidat("code_candidat1_tests.txt"))
# print(liste_mots("test de la fonction liste de mots"))
