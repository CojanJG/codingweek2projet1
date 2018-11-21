def compte_fonctions(path):
	i=0
	l=[]
	with open(path,'r') as code:
		code2=list(code)
		for k in code2 :
			a=0
			b=0
			if 'def' in k:
				i=i+1
				k_list=list(k)
				def_list=list('def')
				a=k_list.index('f')
				if '(' in k:
					b=k_list.index('(')
					l.append(k[a+1:b])
				else:
					l.append(k[a+1:])
	print (i,l)
compte_fonctions('code_candidat1.txt')
