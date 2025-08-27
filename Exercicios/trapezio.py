# Faça um programa que, para z trapézios, ler os valores da base maior (B), base menor (b) e altura (h) de um trapézio, calcule e imprima a área do trapézio.
# Depois, informe se a altura é maior, menor ou igual a 20
# A = (B + b) * h  / 2

z = int(input("quantas vezes deseja calcular a area do trapezio: "))
        
for _ in range(z): 

    B = int(input("escreva o valor de B: "))
    b = int(input("escreva o valor de b: "))
    h = int(input("escreva o valor de h: "))
    A = (B + b) * h / 2
    print ( "a area do trapezio e igual a:", A)

    if h > 20: 
        print ("altura maior que 20") 
    if h < 20:      
        print ("altura menor que 20")
    if h == 20:
        print ("altura igual a 20")