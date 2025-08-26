# CAlCULAR A ÁREA DO TRAPÉZIO
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