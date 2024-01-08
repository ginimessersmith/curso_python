animal=" chanchito feliz "
#mayusculas:
print(animal.upper())
#minuscula
print(animal.lower())
# capitalizado
print(animal.capitalize())
# titulo
print(animal.title())
# remover los espacios en blanco de los extremos
print(animal.strip())
# unir en una sola instruccion dos o mas funciones:
print(animal.strip().capitalize())
# remover los espacios en blanco de los extremos
print(animal.strip())
# remover los espacios en la izquierda
print(animal.lstrip())
# remover los espacios en la derecha
print(animal.rstrip())
# buscar string dentro de la variable, retorna su posicion, si no -1
print(animal.find("fe"))
# reemplazar caracteres, primer argumento es buscar el string a reemplazar, segundo argumente es el valor a reemplazar
print(animal.replace("fe","fer"))
# verificar si un string se encuentra en la variable:
print("nch" in animal)
# verificar si un string no se encuentra en la variable:
print("nch" not in animal)