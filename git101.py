from persona import Persona
from utils import Utils

# Lista de participantes de la escuela
participantes = []

# Primera persona instanciada
persona1 = Persona("Nombre", "Apellido")
persona1.setNacimiento(Utils().getFecha(2000,1,21))  

# Se agrega la persona instanciada a la lista de perticipantes
participantes.append(persona1)

# Instancien y agregen las personas a la lista. La idea del ejercicio es que cada quien haga su propia instancia 
# de Persona con sus datos.

print("Hola Escuelita")
#for participante in participantes:
    #mostrar el nombre completo en mayuscula del participante
    #mostrar la edad calculada de la persona