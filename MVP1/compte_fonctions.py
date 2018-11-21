def compte_fonctions(path):
	from nltk.corpus import wordnet
	i=0
	l=[]
	n=0
	m=0
	a=0
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
					l.append(k[a+2:b])
				else:
					l.append(k[a+2:])
	for j in range(len(l)):
		l[j]=l[j].replace('self.','')
		l[j]=l[j].replace('\n','')
		l[j]=l[j].split('_')
		print(l[j])
		Flag=True
		for u in l[j]:
			if not wordnet.synsets(u):
				#English Word
				Flag=False
				a=a+1
		if Flag==False:
			n=n+1
		else:
			m=m+1
	print (a)
	print ('nombre de fonctions:',i)
	print (l)
	print ('nombre de fonctions mal nommées:',n)
	print ('nombre de fonctions bien nommées:',m)
compte_fonctions('code_candidat1.txt')
