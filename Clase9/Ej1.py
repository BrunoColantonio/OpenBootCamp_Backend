paises = input("Ingrese paises, separandolos por ',': ")
lista_paises = paises.split(",")
set_paises = set(lista_paises)

print(sorted(set_paises))
