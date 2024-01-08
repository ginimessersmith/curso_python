import math

numero = 2  # numero entero
decimal = 2.3  # decimal
imaginario = 2j  # 2i

#!operaciones

print(1+3)
print(1-3)
print(2*3)
print(2/3) #dividir con decimal
print(2//3) #dividir solo con parte entera
print(2%3) #modulo o residuo
print(2**3) #potencia de un numero

#*sumar la misma variable
#numero=numero+2
numero+=2
print("el valor de la var numero es: ",numero)

#!   MODULO MATH
#! Un modulo es como otro archivo ya creado con funciones escritas en python, se importa
print("MODULO MATH: ")
print(round(1.5)) #* muestra el valor mas cercano, 1.3 = 1, 1.5 = 2
print(abs(-77)) #* retorna el valor absoluto del parametro 
print(math.ceil(1.9))#* retorna el valor superior mas cercano
print(math.floor(1.9))#* retorna el valor inferior mas cercano
print(math.isnan(22)) #* retorna true si el valor del parametro no es un numero
print(math.pow(10,3))#* retorna la potencia de un numero, primer argumento es la base, segundo argumento es el exponente
print(math.sqrt(10))#* retorna la raiz cuadrada