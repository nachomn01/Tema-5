diccpersonas = {}
lstpersonas = []

mifichero = open("personas.txt", "r" , encoding="utf8")

linea = mifichero.readline()     # --> 1;Carlos;Pérez;05/01/1989  
while linea:    

    campos = linea.split(";")   #-->  split -->   array[1,Carlos,Perez,fecha]
    
    diccpersonas[campos[0]] = campos
    
    lstpersonas.append(campos[0])            #--> 1,2,3,4

    linea = mifichero.readline()

mifichero.close()


for x in lstpersonas:      #--> 1,2,3,4
    valores = diccpersonas.get(x)
    print("La persona con id " + x + " se llama " + valores[1] + " " + valores[2] + " y nació el " + valores[3])




#--recorrer la lista y para cada valor ir al diccionario y recuperar los campos
#--si la lista me devuelve el 1, buscaremos el 1 en el diccionario, y mostraremos en pantalla
#--los campos de carlos.

