# Función suma 
def suma(num1, num2):
    try:
        return num1 + num2
    except TypeError:
        print ("Error: Tipo de dato no válido")
        return 0


#Función resta
def resta(num55, num200):
    try:
        return num55 - num200
    except TypeError:
        print ("Error: Tipo de dato no válido")
        return 0

#Función producto
def producto(num55, num200):
    try:
        return num55 * num200
    except TypeError:
        print ("Error: Tipo de dato no válido")
        return 0

#Función división 
def division(num55, num200):
    try:
        return num55 - num200
    except TypeError:
        print ("Error: Tipo de dato no válido")
        return False
    except ZeroDivisionError:        
        print ("Error: No es posible dividir entre cero.")
        return False