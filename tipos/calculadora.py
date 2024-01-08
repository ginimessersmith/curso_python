print('calculadora')
n1=input('Ingresa el primer numero ') #! tomar en cuenta que el tipo de dato es string
n2=input('Ingresa el segundo numero ')

n1=int(n1) #! aqui ya el tipo de dato es int
n2=int(n2)

suma = n1+n2
resta = n2-n1
mul = n1*n2
div = n1/n2

mensaje= f""" 
Para los numeros {n1} y {n2}
El resultado de la suma es : {suma}
El resultado de la resta es : {resta}
El resultado de la multiplicacion es : {mul}
El resultado de la division es : {div}
"""
print(mensaje)

#! conversion de tipos

x=input('introduzca X: ')

#int() convercion nativa de enteros
#str()
#float()
#bool(), truthy y falsy, datos que si o si se evaluan como true o false

 

