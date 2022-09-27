number=float(input())
if number>75:
    if number<=100:
        print("Intervalo (75,100]")
    else:
        print("Fora de intervalo")
elif number>50:
    if number<=75:
        print("Intervalo (50,75]")
    else:
        print("Fora de intervalo")
elif number>25:
    if number<=50:
        print("Intervalo (25,50]")
    else:
        print("Fora de intervalo")
elif number>=0:
    if number<=25:
        print("Intervalo [0,25]")
    else:
        print("Fora de intervalo")   
else:
    print("Fora de intervalo")
