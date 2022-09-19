import random
import time
BLACK = '\033[30m'
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
WHITE = '\033[37m'
RESET = '\033[39m'
#TRIVIA 
#Bienvenida
print(MAGENTA+'Bienvenid@ a mi trivia sobre Python \n'+RESET)
nombre = input(YELLOW+'Ingresa tu nombre: \n'+RESET).upper()
#Preparación
time.sleep(1)
print('\nPondremos a prueba tus conocimientos\n¿',CYAN+f'{nombre}'+RESET,'estás preparada?')
#Indicaciones
time.sleep(1)
print('\nCada pregunta correcta podrá sumar hasta',GREEN+'10'+RESET,'puntos. \nCada incorrecta restará hasta', RED+'5'+RESET,'puntos! \nY si encuentras la respuesta secreta obtendrás hasta', BLUE+'1000'+RESET,'puntos!!!!!!')
time.sleep(1)
puntaje=random.randint(0,11)  
print(CYAN+'\nComenzarás con: ', puntaje, 'puntos'+RESET)
time.sleep(1)
print('\nResponde las siguientes preguntas escribiendo la letra de la alternativa y presionando "Enter" para enviar tu respuesta: \n' ) 
  
#Pregunta 1
time.sleep(1)
print(BLUE+'1) ¿Qué es Python?'+RESET)
print ('a) Es un lenguaje de programación de alto nivel.')
print ('b) Lenguaje multiplataforma.')
print ('c) De código abierto.')
print ('d) Todas las anteriores.')
  
respuesta_1 = input(YELLOW+"\nTu respuesta a la pregunta 1 es: "+RESET)  
while respuesta_1 not in ('a', 'b', 'c', 'd'):
    respuesta_1 = input('debes responder a,b,c o d. Ingresa nuevamente tu respuesta: ')
    
if respuesta_1 == 'd':
  puntaje += random.randint(0,10)
  print(GREEN+'\n Muy Bien', nombre+RESET)
  time.sleep(1)
else: 
    puntaje -= random.randint(0,5)
    print(RED+'\nInconrrecto,'+RESET, CYAN+f'{nombre}!'+RESET, BLUE+'La respuesta correcta es:'+RESET,YELLOW+'Todas las anteriores'+RESET)
    time.sleep(2)
print(GREEN+'Vamos', nombre, 'hasta ahora tienes', puntaje, 'puntos'+RESET)
time.sleep(1)
  
  #Pregunta 2
print(BLUE+'\n2) ¿Quién creó python?'+RESET)
print ('a) Guido Van Rossum')
print ('b) Mark Zuckerberg')
print ('c) Brendan Eich')
print ('d) James Gosling')
  
respuesta_2 = input(YELLOW+"\nTu respuesta a la pregunta 2 es: "+RESET)
  
while respuesta_2 not in ('a', 'b', 'c', 'd', 'x'):
    respuesta_2 = input('debes responder a,b,c o d. Ingresa nuevamente tu respuesta: ')
    
if respuesta_2 == 'x':
    puntaje += 1000
    print('\nEste es el mensaje secreto:',CYAN+'"Soy alérgica al plátano"'+RESET)
    time.sleep(1)
elif respuesta_2 == 'b':
    puntaje -= random.randint(0,5)
    print(RED+'\nInconrrecto,'+RESET, CYAN+f'{nombre}!'+RESET, BLUE+'La respuesta correcta es:'+RESET,YELLOW+'Guido Van Rossum'+RESET)
    time.sleep(1)
elif respuesta_2 == 'c':
     puntaje -= random.randint(0,5)     
     print(RED+'\nInconrrecto,'+RESET, CYAN+f'{nombre}!'+RESET, BLUE+'La respuesta correcta es:'+RESET,YELLOW+'Guido Van Rossum'+RESET)
     time.sleep(1)
elif respuesta_2 == 'd':
     puntaje -= random.randint(0,5)   
     print(RED+'\nInconrrecto,'+RESET, CYAN+f'{nombre}!'+RESET, BLUE+'La respuesta correcta es:'+RESET,YELLOW+'Guido Van Rossum'+RESET)
     time.sleep(1)
else:
    puntaje += random.randint(0,10)
    print(GREEN+'\nMuy bien', nombre, '!'+RESET)
    time.sleep(1)
print(GREEN+'Vamos', nombre, 'hasta ahora tienes', puntaje, 'puntos'+RESET)
time.sleep(2)
  
  #Pregunta 3
print(BLUE+'\n3) ¿Dónde se utiliza Python?'+RESET)
print ('a) Data analytics, Big data, Machine learning, Desarrollo web.')
print ('b) Data mining, Data science, Juegos y gráficos 3D.')
print ('c) Inteligencia artificial, Blockchain')
print ('d) Todas las anteriores.\n')
  
respuesta_3 = input(YELLOW+"\nTu respuesta a la pregunta 3 es: "+RESET)
while respuesta_3 not in ('a', 'b', 'c', 'd'):
    respuesta_3 = input('debes responder a,b,c o d. Ingresa nuevamente tu respuesta: ')
if respuesta_3 == 'a':
     puntaje = puntaje - 5     
     print(RED+'\nInconrrecto,'+RESET, CYAN+f'{nombre}!'+RESET, BLUE+'La respuesta correcta es:'+RESET,YELLOW+'Todas las anteriores'+RESET)
     time.sleep(1)
elif respuesta_3 == 'b':
    puntaje = puntaje * 5
    print(RED+'\nInconrrecto,'+RESET, CYAN+f'{nombre}!'+RESET, BLUE+'La respuesta correcta es:'+RESET,YELLOW+'Todas las anteriores'+RESET)
    time.sleep(1)
elif respuesta_3 == 'c':
   puntaje = puntaje / 5        
   print(RED+'\nInconrrecto,'+RESET, CYAN+f'{nombre}!'+RESET, BLUE+'La respuesta correcta es:'+RESET,YELLOW+'Todas las anteriores'+RESET)
   time.sleep(1)
else: 
    puntaje += random.randint(0,5)
    print(GREEN+'\nMuy bien', nombre, '!'+RESET)
time.sleep(2)
#Despedida
print(MAGENTA+'\nGracias', nombre, 'por jugar mi trivia, alcanzaste', BLUE+f'{puntaje}'+RESET,MAGENTA+'puntos'+RESET)
