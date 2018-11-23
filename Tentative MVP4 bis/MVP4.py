from test.test1 import mvp1

#from test import *

resultat = open("resultat.txt", "w")


#On utilise notre mvp1 pour un premier resultat sous forme de dictionnaire 


print(mvp1("code_candidat1.txt","code_candidat1_tests.txt"))

#Idem avec MVP2
"""
import MVP2

resultat.write("\n\n Résultat de la deuxième analyse (MVP2)\n")
resultat.write(str(MVP2.mvp2("code_candidat1.txt")))

#Test de fraude avec MVP3

import MVP3

fraude=MVP3.mvp3("code_candidat1.txt",'base_codes_candidats')

resultat.write("\n\n Résultat du test de fraude (MVP3)\n\n Le code le plus proche du fichier inspecté est "+fraude[1]+'\n')
resultat.write("Ces codes ont : \n")
resultat.write(str(fraude[0][0])+ ' Lignes identiques\n')
resultat.write(str(fraude[0][1])+' Variables de même nom\n')
resultat.write(str(fraude[0][2])+" Fonctions de même nom")

"""