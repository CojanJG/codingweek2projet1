def compte_com(path):
    with open(path,'r') as code:
        code_list=list(code)
        for i in range(len(code_list)):
            code_list[i]=list(code_list[i])
        number_com=0
        number_com_carac=0
        for ligne in code_list:
            for k in range(len(ligne)):
                if ligne[k]=="#":
                    number_com+=1
                    number_com_carac=number_com_carac+len(ligne)-k
        return number_com,number_com_carac

print(compte_com("EventCandidat.rb.txt"))
