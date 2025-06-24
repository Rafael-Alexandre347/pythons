while True:

    print("___________________________________________________________________")
    print("|_________________________________________________________________|")
    print("|____________Bem-Vindo(a) ao Conversor de Temperatura!____________|")
    print("|_________________________________________________________________|")
    print("|_________________________________________________________________|\n")

    print("1 - Célsius para Kelvin \n2 - Célsius para Fahrenheit")
    print("3 - Fahrenheit para Célsius \n4 - Fahrenheit para Kelvin")
    print("5 - Kelvin para Célsius \n6 - Kelvin para Fahrenheit\n")

    while True:
        try:
            decisao = int(input("Qual função você deseja? "))
            if (decisao >= 1 and decisao <= 6):
                break
            else:
                print("Essa função não está disponível. Por favor, escolha uma opção válida.")
        except ValueError:
            print("Entrada Inválida. Digite um número válido.")

    decisaoInt = int(decisao)

    def solicitar_temperatura(origem):
        return float(input(f"Informe a temperatura em {origem}: "))

    def celsius_para_kelvin(c):
        return c + 273.15

    def celsius_para_fahrenheit(c):
        return (c * 1.8) + 32

    def fahrenheit_para_celcsius(f):
        return (f - 32) / 1.8

    def fahrenheit_para_kelvin(f):
        return ((f - 32) / 1.8 ) + 273.15

    def kelvin_para_celsius(k):
        return k - 273.15

    def kelvin_para_fahrenheit(k):
        return (k - 273.15) * 1.8 + 32

    if(decisaoInt == 1):
        tempEmC = solicitar_temperatura("Célsius")
        tempRes = celsius_para_kelvin(tempEmC)
        print(f"O resultado da conversão de Célsius para Kelvin é de {tempRes}ºK")

    elif(decisaoInt == 2):
        tempEmC = solicitar_temperatura("Célsius")
        tempRes = celsius_para_fahrenheit(tempEmC)
        print(f"O resultado da conversão de Célsius para Fahrenheit é de {tempRes}ºF")

    elif(decisaoInt == 3):
        tempEmF = solicitar_temperatura("Fahrenheit")
        tempRes = fahrenheit_para_celcsius(tempEmF)
        print(f"O resultado da conversão de Fahrenheit para Célsius é de {tempRes}ºC")

    elif(decisaoInt == 4):
        tempEmF = solicitar_temperatura("Fahrenheit")
        tempRes = fahrenheit_para_kelvin(tempEmF)
        print(f"O resultado da conversão de Fahrenheit para Kelvin é de {tempRes}ºK")

    elif(decisaoInt == 5):
        tempEmK = solicitar_temperatura("Kelvin")
        tempRes = kelvin_para_celsius(tempEmK)
        print(f"O resultado da conversão de Kelvin para Célsius é de {tempRes}ºC")

    elif(decisaoInt == 6):
        tempEmK = solicitar_temperatura("Kelvin")
        tempRes = kelvin_para_fahrenheit(tempEmK)
        print(f"O resultado da conversão de Kelvin para Fahrenheit é de {tempRes}ºF")

    print(f"Temperatura convertida: {tempRes:.2f}º")

    input("")

    continuar = input("Deseja realizar outra conversão? ")
    if (continuar.lower() != "sim"):
        print("Muito obrigado por usar o conversor de temperaturas!")
        break