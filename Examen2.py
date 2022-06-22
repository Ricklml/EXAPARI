print("El valor de A es de 270, El valor de B es de 340, El valor de C es de 390 ")
print("Solo se aceptan monedas $10, $50, $100")
print("Escoge una letra")
letra=input()
if letra == 'A' or letra == 'a':
    j=True
    while j:
        print("Deposite su dinero")
        d=int(input())
        resta=270-d
        print(resta)
        if resta>270:
            print("Ingrese mas monedas")
            d=int(input())
            resta=270-d
            if resta==270:
                n=False   
if letra == 'B' or letra == 'b':
    print("Deposite su dinero")
    d=int(input())
if letra == 'C' or letra == 'c':
    print("Deposite su dinero")
    d=int(input())