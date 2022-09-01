import aritmetico
import saida

def entrada_dados():
    i=0
    lista_entrada=[]
    while i<2:
        numero=float(input("\nDigite um elemento da sua lista: "))
        lista_entrada.append(numero)
        i+=1
    print(saida.impressora(aritmetico.adicao(lista_entrada[0], lista_entrada[1]), lista_entrada[0], lista_entrada[1]))

entrada_dados()