from VideoJuegos import VideoJueegos


class CRUD_VideoJuegos:

    def __init__(self):
        self.juegos = []
        self.contador=  0



    #METODO PARA CREAR JUEGOS
    def crear(self,nombre,genero,precio,foto,passw):

        for juego in self.juegos:

            if juego.nombre == nombre:
                print('el nombre de usuario ya esata en uso')
                return False

        nuevo =  VideoJueegos(self.contador, nombre,genero,precio,foto,passw )        
        self.juegos.append(nuevo)  
        self.contador += 1    
        return True


    def listar(self):

        print ('id:\tNombre:\t\tNombre de usuario:')

        for juego in self.juegos:

            print(str(juego.id) + '\t' + juego.genero +'\t\t' + juego.nombre)



var_crud = CRUD_VideoJuegos();

var_crud.crear('fifa 20','Deportes','Q100.00','https://media.vandal.net/m/86853/fifa-21-202092911423764_1.jpg','pass123')
var_crud.crear('fifa 21','Deportes','Q100.00','https://media.vandal.net/m/86853/fifa-21-202092911423764_1.jpg','pass123')

var_crud.listar()
