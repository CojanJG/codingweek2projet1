import compte_fonctions.py
import compte_variables.py
import nombre_tests_candidat.py
import compte_commentaires.py

def resultats_dico():
    (nombre_commentaires,nombre_commentaires_caracteres)=compte_commentaires("code_candidat1.txt")
    dico={"nombre de commentaires":nombre_commentaires,"nombre de caractères de commentaires":nombre_commentaires_caracteres}

