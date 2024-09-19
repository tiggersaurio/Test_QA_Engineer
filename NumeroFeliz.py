def suma_cuadrados_digitos(n):
    return sum(int(digit)**2 for digit in str(n))

def es_numero_feliz(n):
    vistos = set()
    while n != 1 and n not in vistos:
        vistos.add(n)
        n = suma_cuadrados_digitos(n)
    return n == 1


numero = int(input("Ingrese un número para verificar si es feliz: "))
if es_numero_feliz(numero):
    print(f"{numero} es un número feliz")
else:
    print(f"{numero} no es un número feliz")
