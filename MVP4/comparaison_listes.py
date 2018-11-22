def comparaison (l1,l2):
	n=0
	for k in range (len(l1)):
		if l1[k] in l2:
			n=n+1
	return n