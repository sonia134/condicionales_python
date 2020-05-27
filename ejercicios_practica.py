#!/usr/bin/env python
'''
Condicionales [Python]
Ejercicios de práctica
---------------------------
Autor: Inove Coding School
Version: 1.1
 
Descripcion:
Programa creado para que practiquen los conocimietos adquiridos durante la semana
'''

__author__ = "Inove Coding School"
__email__ = "alumnos@inove.com.ar"
__version__ = "1.1"

def ej1():
    # Ejercicios de práctica con números

    '''
    Realice un programa que solicite por consola 2 números
    Calcule la diferencia entre ellos e informe por pantalla
    si el resultado es positivo, negativo o cero.
        
    '''
    print('Ingrese 1º numero:')
    num_1= int(input())
    print('Ingrese 2º numero:')
    num_2= int(input())
    
    resta= num_1 - num_2

    if resta > 0:
      print('El resultado es:', resta, 'un numero positivo')
    elif (resta < 0):
      print('El resultado es:', resta, 'un numero negativo')
    else:
      print('El Resultado es igual a 0')

def ej2():
    # Ejercicios de práctica con números

   '''
   Realice un programa que solicite el ingreso de tres números
   enteros, y luego en cada caso informe si el número es par
   o impar.
   Para cada caso imprimir el resultado en pantalla.
    
   '''
    
    
    num_1 = int(input('Ingrese el primer número:\n')) 
    num_2 = int(input('Ingrese el segundo número:\n'))
    num_3 = int(input('Ingrese el tercer número:\n'))

  
    if (num_1 / 2) = 0:
      print('El numero entero es par')
    else:
      print('El numero entero es impar')
    if (num_2 / 2) = 0:
      print('El numero entero es par')
    else:
      print('El numero entero es impar')
    if (num_3 / 2) = 0:
      print('El numero entero es par')
    else:
      print('El numero es impar')
  

def ej3():
    # Ejercicios de práctica con números

    '''
    Realice una calculadora, se ingresará por línea de comando dos números
    Luego se ingresará como tercera entrada al programa el símbolo de la operación
    que se desea ejecutar
    - Suma (+)
    - Resta (-)
    - Multiplicación (*)
    - División (/)
    - Exponente/Potencia (**)

    Se debe efectuar el cálculo correcto según la operación ingresada por consola
    Imprimir en pantalla la operación realizada y el resultado
    

    '''

    num_2 = int(input('Ingrese el primer número:\n'))

    num_3 = int(input('Ingrese el segundo número:\n'))

    print('ingrese el simbolo segun la operacion que desea ejecutar')

    simb = str(input())

    if (simb =="+"):
        suma = num_2 + num_3
        print('Usted eligio el signo +, el resultado es:', suma)
    if (simb =="-"):
        resta = num_2 - num_3
        print('Usted eligio el signo -, el resultado es:', resta)
    if (simb =="*"):
        mult = num_2 * num_3
        print('Usted eligio el signo *, el resultado es:', mult)
    if (simb =="/"):
        div= num_2 / num_3
        print('Usted eligio el signo /, el resultado es:', div)
    else:
      print('Signo no corresponde')

def ej4():

    # Ejercicios de práctica con cadenas
    
    '''
    Realice un programa que solicite por consola 3 palabras cualesquiera
    Luego el programa debe consultar al usuario como quiere ordenar las palabras
    1 - Ordenar por orden alfabético (usando el operador ">")
    2 - Ordenar por cantidad de letras (longitud de la palabra)

    Si se ingresa "1" por consola se deben ordenar las 3 palabras por orden alfabético
    e imprimir en pantalla de la mayor a la menor

    Si se ingresa "2" por consola se deben ordenar las 3 palabras por cantidad de letras
    e imprimir en pantalla de la mayor a la menor

   '''
  
  
  
    texto_1 = str(input('Ingrese la primera palabra:\n'))

    texto_2 = str(input('Ingrese la segunda palabra:\n'))

    texto_3 = str(input('Ingrese la tercer palabra:\n'))

    
    print('Ingrese A, si necesita ordenar alfabeticamente\nIngrese L, si necesita ordenar por longitud')
    aux= str(input())
    
    
    

    if (aux=="A"):
      if (texto_1 < texto_2):
       if(texto_2 < texto_3):
         print(texto_1, texto_2,texto_3)
      if (texto_2 > texto_1):
        if(texto_1 > texto_3):
         print(texto_3,texto_2,texto_1)
      if(texto_1 > texto_2):
        if(texto_2 > texto_3):
         print(texto_2,texto_1,texto_3)
      if(texto_3 > texto_2):
        if(texto_3 < texto_1):
         print(texto_2,texto_3,texto_1)
      if(texto_2 > texto_3):
        if(texto_3 > texto_1):
         print(texto_1,texto_3,texto_2)
      if(texto_1 > texto_2):
        if(texto_1 < texto_3):
          print(texto_2,texto_1,texto_3)
    elif (aux=="L"):
      if(len(texto_1) < len(texto_2)): 
        if(len(texto_2) < len(texto_3)):
         print(texto_1, texto_2, texto_3)
      if(len(texto_1) < len(texto_2)):
        if(len(texto_2) > len(texto_3)):
         print(texto_3,texto_1, texto_2)
      if(len(texto_1)) > len(texto_2):
        if(len(texto_2) > len(texto_3)):
         print(texto_3, texto_2, texto_1)
      if(len(texto_1)) > len(texto_2) and (len(texto_1) < len(texto_3)):
        if(len(texto_2) < len(texto_3)):
         print(texto_2, texto_1, texto_3)
      if(len(texto_1) > len(texto_2)) and (len(texto_1) > len(texto_3)):
        if(len(texto_2) < len(texto_3)):
          print(texto_2,texto_3,texto_1)
    else:
      print('ingreso erroneo')
      


def ej5():
     
     # Ejercicios de práctica con números
       
      '''
      Realice un programa que solicite ingresar tres valores de temperatura
      De las temperaturas ingresadas por consola determinar:
      1 - ¿Cuáles de ellas es la máxima temperatura ingresada?
      2 - ¿Cuáles de ellas es la mínima temperatura ingresada?
      3 - ¿Cuál es el promedio de las temperaturas ingresadas?

      En cada caso imprimir en pantalla el resultado  

      '''
      tem_1 = int(input('Ingrese la primer temperatura:\n'))

      tem_2 = int(input('Ingrese la segunda temperatura:\n'))

      tem_3 = int(input('Ingrese la tercer temperatura:\n'))

      if(tem_1 < tem_2) and (tem_1 < tem_3) and (tem_2 < tem_3): # 50 60 80 
        min=tem_1
        max=tem_3
        print('la temperatura minima ingresada es:',min) 
        print('la temperatura maxima ingresada es:',max)
      
      if(tem_1 > tem_2) and (tem_2 < tem_3) and (tem_1 > tem_3 ): #100 15 60
        min=tem_2
        max=tem_1
        print('la temperatura minima ingresada es:',min) 
        print('la temperatura maxima ingresada es:',max)
      
      if(tem_1 > tem_3) and (tem_2 > tem_3) and (tem_2 > tem_1): # 10 100 8
        min=tem_3
        max=tem_2
        print('la temperatura minima ingresada es:',min) 
        print('la temperatura maxima ingresada es:',max) 

      if(tem_1 > tem_2) and (tem_2 > tem_3) and (tem_1 > tem_3): # 80 60 55
        min=tem_3
        max=tem_1
        print('la temperatura minima ingresada es:',min) 
        print('la temperatura maxima ingresada es:',max) 
      
      if(tem_1 < tem_2) and (tem_2 > tem_3) and (tem_1 < tem_3): # 60 105 85
        min=tem_1
        max=tem_2
        print('la temperatura minima ingresada es:',min) 
        print('la temperatura maxima ingresada es:',max) 
      
     
   

      prom_temp= (tem_1 + tem_2 + tem_3) / 3
      print('El promedio de las temperaturas ingresadas son:', prom_temp)




if __name__ == '__main__':
    print("Ejercicios de práctica")
    #ej1()
    ej2()
    #ej3()
    #ej4()
    #ej5()
