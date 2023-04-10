import math
GB=float(input("ingrse su almacenamiento del disco en gigabit"))
MG = GB*1024
MD = MG/1.44
print("Numero de Discos necesarios: ", math.ceil(MD))