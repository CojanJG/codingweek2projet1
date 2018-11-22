import doublon
import noms_variables
import noms_fonctions
import longueur_lignes

def mvp2 (codePath):
    dico={}
    dico['Nombre de lignes de plus de 80 caractères']=longueur_lignes.testLignes(codePath,80)
    dico['Nombre de variables bien nommés']=noms_variables.testNoms(codePath)[0]
    dico['Nombre de variables mal nommés']=noms_variables.testNoms(codePath)[1]
    dico['Nombre de fonctions bien nommés']=noms_fonctions.noms_fonctions(codePath)[0]
    dico['Nombre de fonctions mal nommés']=noms_fonctions.noms_fonctions(codePath)[1]
    dico['Nombre de lignes en double']=len(doublon.doublon(codePath))
    return(dico)

#print(mvp2("code_candidat1.txt"))
