def main():

    loop =  int(input( "insira um quantos numeros voce quer comparar: "))

    for _ in range (loop):

        num = float(input("insira num: "))
        num1 = float(input( "insira num1: "))

        if (num < num1):
            print (num , "menor que", num1)

        if (num > num1):
            print (num , "maior que" ,num1) 
        
     

        if (num == num1) :
            print ( num, "é igual" , num1)     











































        

if __name__ == "__main__":
    main()