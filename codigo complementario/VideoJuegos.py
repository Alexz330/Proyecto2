class VideoJueegos:

    def __init__(self,id,nombre,genero,precio,foto,passw):

        self.id = id
        self.nombre = nombre
        self.genero = genero 
        self.precio = precio
        self.foro = foto
        self.passw = passw

    def imprimir_tipo(self):
        print(self.nombre + ' es un juego:' + self.genero)    

    def autentificar(self,nombre,passw):

        if self.nombre == nombre and  self.passw == passw:
            print ('LA autentificacion es correcta')
            return True
        print('la autentificaion es incorecta')
        return False    

fifa =  VideoJueegos(1, 'fifa 20','Deportes','Q100.00','https://media.vandal.net/m/86853/fifa-21-202092911423764_1.jpg','pass123' )
fifa.imprimir_tipo();

fifa.autentificar('fifa 20','pass1232')