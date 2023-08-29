frase = "Hello World!!"
print(frase)
print(len(frase))
print(frase[0])
print(frase[1])
a = "Hello"
b = "World!"
c = " "
d = "!"
print(a + c + b)
print(a + " " + b)
print(a + " " + b + "!")

print(frase[0:5])
print(frase[ :5])
print(frase[6:12])
print(frase[6:])

#frase[0] = "h"

frase_lista = list(frase)
print(frase_lista)
frase_lista[5] = ","
print(frase_lista)

frase_inteira = " ".join(frase_lista)
print(frase_inteira)

print(frase.startswith("Hello"))
print(frase.endswith("World"))
print("Hello" in frase)

print(frase.count("a"))
print(frase.count("o"))

print(frase.find("Hello"))
print(frase.find("o"))
print(frase.find("e"))
print(frase.find("Olá"))
print(frase.find("a"))

print(frase.split())
print(frase.replace("World" , "mundo"))
print(frase)


