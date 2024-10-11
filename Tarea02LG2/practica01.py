class Libro:
    def __init__(self, titulo, autor, isbn):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn

    def __str__(self):
        return f"{self.titulo} por {self.autor} (ISBN: {self.isbn})"

class Estudiante:
    def __init__(self, nombre, numero_estudiante):
        self.nombre = nombre
        self.numero_estudiante = numero_estudiante

    def __str__(self):
        return f"{self.nombre} (Número de estudiante: {self.numero_estudiante})"

class Biblioteca:
    def __init__(self):
        self.libros = []      
        self.estudiantes = [] 
    
    def agregarLibro(self, libro):
        if isinstance(libro, Libro):  
            self.libros.append(libro)
            print(f"Libro '{libro.titulo}' agregado a la biblioteca.")
        else:
            print("Error: Solo se pueden agregar objetos de tipo Libro.")

    def eliminarLibro(self, isbn):
        for libro in self.libros:
            if libro.isbn == isbn:
                self.libros.remove(libro)
                print(f"Libro '{libro.titulo}' eliminado de la biblioteca.")
                return
        print("Error: No se encontró un libro con ese ISBN.")

    def listarLibros(self):
        if not self.libros:
            print("No hay libros disponibles en la biblioteca.")
            return
        print("Libros disponibles en la biblioteca:")
        for libro in self.libros:
            print(libro)

    
    def agregarEstudiante(self, estudiante):
        if isinstance(estudiante, Estudiante): 
            self.estudiantes.append(estudiante)
            print(f"Estudiante '{estudiante.nombre}' agregado a la biblioteca.")
        else:
            print("Error: Solo se pueden agregar objetos de tipo Estudiante.")

    def eliminarEstudiante(self, numero_estudiante):
        for estudiante in self.estudiantes:
            if estudiante.numero_estudiante == numero_estudiante:
                self.estudiantes.remove(estudiante)
                print(f"Estudiante '{estudiante.nombre}' eliminado de la biblioteca.")
                return
        print("Error: No se encontró un estudiante con ese número.")

    def listarEstudiantes(self):
        if not self.estudiantes:
            print("No hay estudiantes registrados en la biblioteca.")
            return
        print("Estudiantes registrados en la biblioteca:")
        for estudiante in self.estudiantes:
            print(estudiante)

#Uso
if __name__ == "__main__":
    
    libro1 = Libro("Cien años de soledad", "Gabriel García Márquez", "978-3-16-148410-0")
    libro2 = Libro("Don Quijote de la Mancha", "Miguel de Cervantes", "978-3-16-148410-1")

    estudiante1 = Estudiante("Juan Pérez", "12345")
    estudiante2 = Estudiante("María López", "67890")

    biblioteca = Biblioteca()

    biblioteca.agregarLibro(libro1)
    biblioteca.agregarLibro(libro2)

    biblioteca.listarLibros()

    biblioteca.agregarEstudiante(estudiante1)
    biblioteca.agregarEstudiante(estudiante2)

    biblioteca.listarEstudiantes()

    biblioteca.eliminarLibro("978-3-16-148410-0")
    biblioteca.eliminarEstudiante("12345")

    biblioteca.listarLibros()
    biblioteca.listarEstudiantes()