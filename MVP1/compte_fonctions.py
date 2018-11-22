import enchant
def compte_fonctions(path):
	d = enchant.Dict('en_US')
	i=0
	l=[]
	n=0
	m=0
	with open(path,'r') as code:
		code2=list(code)
		for k in code2 :
			a=0
			b=0
			if 'def' in k:
				#on compte le nombre de fonctions que comprend le code
				i=i+1
				k_list=list(k)
				def_list=list('def')
				a=k_list.index('f')
				#on crée la liste des noms des fonctions
				if '(' in k:
					b=k_list.index('(')
					l.append(k[a+2:b])
				else:
					l.append(k[a+2:])
	for j in range(len(l)):
		#les noms dans la liste sont nettoyés de la ponctuation autorisée et de commandes  
		l[j]=l[j].replace('self.','')
		l[j]=l[j].replace('\n','')
		l[j]=l[j].split('_')
		Flag=True
		#on teste les mots composants les noms des fonctions pour vérifier qu'ils sont anglais
		for u in l[j]:
			if not d.check(u):
				#not an English Word
				Flag=False
		if Flag==False:
			#on compte le nombre de fonctions avec des noms comprenant autres choses que des mots anglais et des underscores
			n=n+1
		else:
			m=m+1
	return [i,l,n,m]

print('nombre de fonctions:', compte_fonctions('code_candidat1.txt')[0])
print('nom des fonctions:', compte_fonctions('code_candidat1.txt')[1])
print('nombre de fonctions mal nommées:', compte_fonctions('code_candidat1.txt')[2])
print('nombre de fonctions bien nommées:', compte_fonctions('code_candidat1.txt')[3])
