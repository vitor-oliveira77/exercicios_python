import math
base = float(input("base do retangulo: "))
altura = float(input("altura do retangulo: "))

area = base * altura
perimetro = 2 * (base + altura)
diagonal = math.sqrt(base*base + altura ** 2)

print(f" AREA = {area:.4f}")
print(f"Perimetro = {perimetro:.4f}")
print(f"Diagonal = {diagonal:.4f}")