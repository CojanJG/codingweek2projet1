def compte_fonctions(path):
	i=0
	with open('path','r') as code:
		code2=list(code)
		for k in code2 :
	        	if 'def' in str(k):
				i=i+1
	print (i)
compte_fonctions('code_candidat.txt')
