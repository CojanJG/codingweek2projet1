import compte_fonctions
import compte_variables
from nombre_tests_candidat import *
import compte_commentaires

def mvp1(codePath,testPath) :

    nb_variables=compte_variables.countVariables(codePath)
    nb_fonctions=compte_fonctions.compte_fonctions(codePath)
    nb_tests_candidats=nombre_test_candidat(testPath)
    nb_assert_candidat=nombre_assert_candidat(testPath)
    (nombre_commentaires,nombre_commentaires_caracteres)=compte_commentaires.compte_commentaires(codePath)
    dico={"nombre de fonctions":nb_fonctions,"nombre de variables":nb_variables,"nombre de fonctions test":nb_tests_candidats,"nombre de tests":nb_assert_candidat,"nombre de commentaires":nombre_commentaires,"nombre de caractères de commentaires":nombre_commentaires_caracteres}

    return (dico)

#print(mvp1("code_candidat1.txt","code_candidat1_tests.txt"))