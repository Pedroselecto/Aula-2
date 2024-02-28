#Obs: Shit + alt + seta para baixo. Copia a linha para baixo.

"""

Operadores
    - Aritméticos
    - Atribuição
    - Comparação (ou relacionais)
    - Lógicos (ou booleanos)

"""

x = 10
y = 5.0

print(x + y)  # soma
print(x - y)  # subtração
print(x * y)  # multiplicação
print(x / y)  # divisão
print(x // y) # divisão inteira (pega o quociente da divisão e arredonda para baixo, para pegar um número inteiro. Por exemplo, 7//3 seria 2)
print(x % y)  # módulo
print(x ** y) # potência

# Quando um dos operandos for uma str (string):

print("-" * 30)
print("-" + "+")

print(round(x + y, 1))

# Operadores de atribuição

x = 2
x += 1
x -= 4
x *= 6
x/= 2
x //= 4
x **= 2
x %= 5
print(x)

# Operadores de comparação

print("-" * 30)
print(x < y)  # menor que
print(x > y)  # maior que
print(x >= y) # maior ou igual a
print(x <= y) # menor ou igual a
print(x == y) # igual a
print(x != y) # diferente de

z = "abc"
w = "Abc"

print("-" * 30)
print(z > w)
print(z < w)
print(z > w)
print (z >= w)
print(z <= w)
print(z == w)
print(z != w)


# Operadores lógicos

a = True
b = False

print(a and b) # E
print(a or b)  # OU
print (not a)  # NÃO

# Type casting
#idade = int(input("informe sua idade: "))
#print("sua idade é" + str(idade))
print(bool(""))
print(bool(0))
print(bool(0.0))
print(bool("10"))
print(bool(12.5))
print(bool(1))

print("10" or 75)
print(True or 0)
print(False or "abc")
print("" or 10.5)

texto = "abc"
print(0 and int(texto))
print(10 and "")
print(10 and "abc")

# Pythonico
#nome = input("informe o seu nome: ") or "Valor inválido"

#print (nome)

"""

Precedência dos operadores

()
**
* / // %
+ -
< <= > >= == !=
not
and
or
"""
print("-" * 30)
print(4 > 2 * 3 ** 2 - 7 and 4 * 6 - 7 // 2 or not 10 + 2 <= 5)

print(4 > 2 * 3 ** 2 - (7 and 4) * (6 - 7) // 2 or (not 10 + 2) <= 5)


ap1 = float(input("Coloque sua nota AP1: "))
ap2 = float(input("Coloque sua nota AP2: "))
ac = float(input("Coloque sua nota AC: "))

media = (ap1 + ap2) * 0.4 + ac * 0.2
print(media)
