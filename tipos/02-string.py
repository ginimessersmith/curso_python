nombre_curso ="ultimate python"
# para un string mas largo
descripcion_curos='''
ultimate python
este curso contempla todos los detalles
del lenguaje python
'''

print(nombre_curso,descripcion_curos)
print('longitud del string nombre_curso: ', len(nombre_curso))
#acceder a un caracter de un string
print('primer caracter',nombre_curso[0])
print('del caracter 2 al 7: ',nombre_curso[2:7])
print('del caracter a partir del 9 al final: ',nombre_curso[9:])
print('del caracter 0 al 9: ',nombre_curso[:9])
print('todo los caracteres (copia) : ',nombre_curso[:])