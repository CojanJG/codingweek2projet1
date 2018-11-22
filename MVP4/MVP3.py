import comparaison_de_deux_codes
import os



def mvp3 (codePath, basePath):
    maxFraude = [0,0,0]
    path=''
    for code in os.listdir(basePath) :
            if sum(comparaison_de_deux_codes.comparaisonDeDeuxCodes(codePath,basePath+"/"+code))> sum(maxFraude) :
                maxFraude = comparaison_de_deux_codes.comparaisonDeDeuxCodes(codePath,basePath+"/"+code)
                path=code
    return(maxFraude,code)

#print (mvp3("code_candidat1.txt",'base_codes_candidats')[1])
