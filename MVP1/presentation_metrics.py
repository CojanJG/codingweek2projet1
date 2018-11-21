import compte_fonctions
import compte_variables
from nombre_tests_candidat import *
import compte_commentaires

# resultats_dico:

nb_variables=compte_variables.countVariables("code_candidat1.txt")
nb_fonctions=compte_fonctions.compte_fonctions("code_candidat1.txt")
nb_tests_candidats=nombre_test_candidat("code_candidat1_tests.txt")
nb_assert_candidat=nombre_assert_candidat("code_candidat1_tests.txt")
(nombre_commentaires,nombre_commentaires_caracteres)=compte_commentaires.compte_commentaires("code_candidat1.txt")
dico={"nombre de fonctions":nb_fonctions,"nombre de variables":nb_variables,"nombre de fonctions test":nb_tests_candidats,"nombre de tests":nb_assert_candidat,"nombre de commentaires":nombre_commentaires,"nombre de caractères de commentaires":nombre_commentaires_caracteres}

# print(nombre_test_candidat("code_candidat1.txt"))

print(dico)
