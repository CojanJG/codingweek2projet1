def nombre_mot_dans_fichier(file_name,mot):             #file_name et mot sont des strings
    with open(file_name,'r') as file:
        n=0
        file_list=list(file):
            for k in file_list:
                k_list=list(k)
                mot_list=list(mot)
                n=n+k_list.count(mot_list)
    return n

def nombre_test_candidat(file_name):
    return nombre_mot_dans_fichier(file_name,'test')

def nombre_assert_candidat(file_name):
    return nombre_mot_dans_fichier(file_name,'assert')
