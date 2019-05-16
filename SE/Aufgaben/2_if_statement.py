number=int(input("geben Sie bitte eine Zahl ein: "))

if number>=10:
    print("Die von Ihnen eingegebene Zahl "+str(number)+" ist größer oder gleich 10!")
else:
    print("Die von Ihnen eingegebene Zahl "+str(number)+" ist kleiner als 10!")


number1=int(input("Geben Sie bitte die erste Zahl ein: "))
number2=int(input("Geben Sie bitte die zweite Zahl ein: "))

if number1==number2:
    print("Die Zahlen sind gleich")
elif number1<number2:
    print("Die erste Zahl ist kleiner als die zweite")
else:
    print("Die Zweite Zahl ist größer als die erste!")