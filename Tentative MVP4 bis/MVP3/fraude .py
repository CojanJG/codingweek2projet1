import os
i=0

for doc in os.listdir('base_codes_candidats') :
    print(doc)
print(i)

def fraude (codePath, basePath):
     maxFraude = [0,0,0]
    for code in os.listdir(basePath) :
        if sum(comparaisonDeDeuxCodes(codePath,code))>maxFraude :
            maxFraude = comparaisonDeDeuxCodes(codePath,code)
    return(maxFraude)
