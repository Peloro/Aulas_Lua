# INPUT: função que lê uma entrada do usuário (sempre retorna string)
# INT: converte string para inteiro
loop = int(input("insira um quantos numeros voce quer comparar: "))

# FOR: loop controlado; "ENQUANTO (variavel, ou _ se não for usar essa variavel) ESTIVER DENTRO DO INTERVALO (variavel):"
for _ in range (loop):

    # FLOAT: converte string para número decimal
    num = float(input("insira num: "))
    num1 = float(input( "insira num1: "))

    # IF: estrutura condicional simples; "SE (condição): FAÇA (ação)"
    if (num < num1):
        print (num , "menor que", num1)

    if (num > num1):
        print (num , "maior que" ,num1) 

    if (num == num1) :
        print (num, "é igual" , num1)     

# FOR UTILIZANDO A VARIÁVEL
for i in range (5):
    print ("o valor de i é:", i)










































        

if __name__ == "__main__":
    main()