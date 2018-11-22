def comparaisonDeDeuxCodes(path1,path2):
    
    lignesIdentiques = len(fraude_lignes(path1,path2))
    variablesIdentiques = comparaison_listes(nomsVariables(path1),nomsVariables(path2))
    fonctionsIdentiques = comparaison_listes(nomsFonctions(path1),nomsFonctions(path2))
    
    return([lignesIdentiques,variablesIdentiques,fonctionsIdentiques])


