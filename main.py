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
print(MAGENTA+'Bienvenid@ a mi trivia sobre Python \n'+RESET)
puntaje = random.randint(0,10)
nombre = input(YELLOW+'Ingresa tu nombre: \n'+RESET)
print(nombre, 'Pondremos a prueba tus conocimientos\n')
print(CYAN+'Comenzarás con: ', puntaje, 'puntos'+RESET)
print('\nCada pregunta correcta podrá sumar hasta',GREEN+'10'+RESET,'puntos. \nCada incorrecta restará hasta', RED+'5'+RESET,'puntos! \nY si encuentras la respuesta secreta obtendrás hasta', BLUE+'1000'+RESET,'puntos!!!!!!')

print('\nResponde las siguientes preguntas escribiendo la letra de la alternativa y presionando "Enter" para enviar tu respuesta: \n' )

#Pregunta 1
print('1) ¿Qué es Python?')
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
else: 
  puntaje -= random.randint(0,5)
  print(RED+'\nInconrrecto', nombre+RESET, BLUE+'La respuesta correcta es: Todas las anteriores son correctas'+RESET)
  time.sleep(2)
print(GREEN+'Vamos', nombre, 'hasta ahora tienes', puntaje, 'puntos'+RESET)
time.sleep(3)

#Pregunta 2
print('\n2) ¿Quién creó python?')
print ('a) Guido Van Rossum')
print ('b) Mark Zuckerberg')
print ('c) Brendan Eich')
print ('d) James Gosling')

respuesta_2 = input(YELLOW+"\nTu respuesta a la pregunta 2 es: "+RESET)

while respuesta_2 not in ('a', 'b', 'c', 'd', 'x'):
  respuesta_2 = input('debes responder a,b,c o d. Ingresa nuevamente tu respuesta: ')
  
if respuesta_2 == 'x':
  puntaje += 1000
  print('\nEste es el mensaje secreto: "No como cerdo"')
elif respuesta_2 == 'b':
  puntaje -= random.randint(0,5)
  print(RED+'\nInconrrecto', nombre+RESET, BLUE+'La respuesta correcta es: Guido Van Rossum'+RESET)
elif respuesta_2 == 'c':
   puntaje -= random.randint(0,5)     
   print(RED+'\nInconrrecto', nombre+RESET, BLUE+'La respuesta correcta es: Guido Van Rossum'+RESET)
elif respuesta_2 == 'd':
   puntaje -= random.randint(0,5)   
   print(RED+'\nInconrrecto', nombre+RESET, BLUE+'La respuesta correcta es: Guido Van Rossum'+RESET)
else:
  puntaje += random.randint(0,10)
  print(GREEN+'Muy bien', nombre, '!'+RESET)
time.sleep(2)
print(GREEN+'Vamos', nombre, 'hasta ahora tienes', puntaje, 'puntos'+RESET)
time.sleep(3)

#Pregunta 3
print('\n3) ¿Dónde se utiliza Python?')
print ('a) Data analytics, Big data, Machine learning, Desarrollo web.')
print ('b) Data mining, Data science, Juegos y gráficos 3D.')
print ('c) Inteligencia artificial, Blockchain')
print ('d) Todas las anteriores.\n')

respuesta_3 = input(YELLOW+"\nTu respuesta a la pregunta 3 es: "+RESET)
while respuesta_3 not in ('a', 'b', 'c', 'd'):
  respuesta_3 = input('debes responder a,b,c o d. Ingresa nuevamente tu respuesta: ')
if respuesta_3 == 'a':
   puntaje = puntaje - 5     
   print(RED+'\nInconrrecto', nombre+RESET, BLUE+'La respuesta correcta es: Todas las anteriores son correctas'+RESET)
elif respuesta_3 == 'b':
  puntaje = puntaje * 5
  print(RED+'\nInconrrecto', nombre+RESET, BLUE+'La respuesta correcta es: Todas las anteriores son correctas'+RESET)
elif respuesta_3 == 'c':
 puntaje = puntaje / 5        
 print(RED+'\nInconrrecto', nombre+RESET, BLUE+'La respuesta correcta es: Todas las anteriores son correctas'+RESET)
else: 
  puntaje += random.randint(0,5)
  print(GREEN+'Muy bien\n', nombre, '!'+RESET)
time.sleep(1)
print(GREEN+'Gracias', nombre, 'por jugar mi trivia, alcanzaste', puntaje, 'puntos'+RESET)