from datetime import date , datetime
class Utils():

    
    def stringToUpperCase(self, string):
        """ Metodo que recibe un string y devuelve en modo UPERCASE el string recibido
        : parametro string: string
        : return: string
        """
        return str.upper(string)

    def getFecha(self, year, month, day):
        """ Metodo que recibe por parametros el año, mes y dia en formato int y devuelve en modo datetime la fecha recibida 
        : parametro year: int
        : parametro month: int
        : parametro day: int
        : return: datetime
        """
        return date(year,month,day)

    ##Crear un metodo que recibiendo la fecha de nacimiento de una persona, devuelva la edad que tiene
    # Tips: date y datetime permiten acceder a valores como Year, Month y Day para hacer el calculo
    #       Con el metodo datetime.now() pueden obtener la fecha de hoy en formato datime
    