def km_a_metro(kilometros):
    return kilometros * 1000

def metro_a_pie(metros):
    return metros * 3.28084

def pulgadas_a_yarda(pulgadas):
    return pulgadas / 36

def millas_a_centimetros(millas):
    return millas * 160934.4

def milimetros_a_decimetros(milimetros):
    return milimetros / 100

# Ejemplos de uso:
kilometros = 5
metros = 1000
pulgadas = 72
millas = 2
milimetros = 250

print(f"{kilometros} km son {km_a_metro(kilometros)} metros")
print(f"{metros} metros son {metro_a_pie(metros)} pies")
print(f"{pulgadas} pulgadas son {pulgadas_a_yarda(pulgadas)} yardas")
print(f"{millas} millas son {millas_a_centimetros(millas)} centímetros")
print(f"{milimetros} milímetros son {milimetros_a_decimetros(milimetros)} decímetros")
