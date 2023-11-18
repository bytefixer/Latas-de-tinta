import time

valor_lata = 50.00
volume_lata = 5
pintura_lata = 3
pi = 3.14

altura = float(input("Determine a altura: "))
raio = float(input("Determine o raio: "))

area_lateral = (2 * pi + altura + raio)
area_base = (pi * raio**2)
area_cilindro = (area_base + area_lateral)
qtd_litros = (area_cilindro / pintura_lata)
qtd_latas = int(qtd_litros / volume_lata)
custo = int(qtd_latas * valor_lata)

print(f"\tA quantidade total será de {qtd_latas} latas de tinta.\n"
      f"\tO custo total será de: R${custo}")

def design():
    print("*---" * 10, end="*\n")

design()
input("Pressione ENTER para encerrar aplicação!")
time.sleep(2)
design()
print("*\tObrigada por utilizar o programa! \t*")
design()
time.sleep(1.5)
print("\n\t\t\t...Finalizando...")


