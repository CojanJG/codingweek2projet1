from fraude_lignes import *
from comparaison_listes import *
from noms_variables import *
from noms_fonctions import *


def comparaisonDeDeuxCodes(path1,path2):
    
    lignesIdentiques = len(fraude_lignes(path1,path2))
    variablesIdentiques = comparaison(nomsVariables(path1),nomsVariables(path2))
    fonctionsIdentiques = comparaison(noms_fonctions(path1),noms_fonctions(path2))
    
    return([lignesIdentiques,variablesIdentiques,fonctionsIdentiques])

