idade: int
salario: float
nome: str
sexo: str

idade = 32
salario = 4560.9
nome = "Maria Silva"
sexo = "F"

print(f" A funcionaria {nome}, sexo {sexo}, ganha {salario} e tem idade {idade} anos")
print (" A funcionaria {:s} , sexo {:s} , ganha {:.2f} e tem idade {:d} anos " .format (nome,sexo,salario,idade))