def tam(n):
	i = 0
	while(n>0):
		n=n/10
		i+=1
	return i

def posicion(n, a):
	for i in range(n):
		a=a/10
	b = a/10
	a= a - 10*b
	return a

print "Numeros narcisistas"
for i in range(10**7):
	t = tam(i)
	resultado = posicion(0,i)**t
	for j in range(t-1):
		resultado += posicion(j+1,i)**t
	if resultado == i:
		print i