class Persona():

    """ Clase responsable de la creacion de una persona en conjunto con sus atributos y comportamientos.
    El constructor de la clase Persona recibe los parametros de 'nombre' y 'apellido'
    : parametro nombre: string
    : parametro apellido: string
    """
    
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

    def getNombre(self):
        """ Metodo que devuelve un string con el nombre de la Persona instanciada
        : return: string
        """
        return self.nombre

    def getApellido(self):
        """ Metodo que devuelve un string con el apellido de la Persona instanciada
        : return: string
        """
        return self.apellido

    def setNacimiento(self, fechaNacimiento):
        """ Metodo que recibe la fecha de Nacimiento de la Persona instanciada
        : parametro fechaNacimiento: datetime
        """
        self.birthDate = fechaNacimiento

    def getNacimiento(self):
        """ Metodo que devuelve un datetime con la fecha de nacimiento que se definio para la Persona instanciada
        : return: int
        """
        return self.birthDate

    #Crear un metodo que devuelva el nombre completo de la persona
