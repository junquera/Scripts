def exponencial(n):
    if(n <= 1):
        return 1
    else:
        return n * exponencial(n-1)

def binomio(n, k):
    return exponencial(n)/(exponencial(k) * exponencial(n-k))

def piramide(n):
    for i in range(n):
            resul = (n - i - 1) * " "
            for j in range(i+1):
                    resul+=str(binomio(i,j))+" "
            print resul
