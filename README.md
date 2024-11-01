1.- Prepara un ejemplo donde expliques cómo hacer en Python 3 lo siguiente:

NOTA: Se puede preguntar a la IA o internet, pero yo iré revisando que entiendan lo que están haciendo, sólo esta tarea 1.

Clonar una lista. ¿Cuál es la diferencia en Python entre “shallow copy” y “deep copy”? Añadir un elemento a una lista. Quitar un elemento de una lista. Crear una nueva lista con los 4 últimos elementos de una lista. Convertir las palabras de una cadena (separadas por espacios) en una lista. Comentarios de una línea. Comentarios multilínea.

2.- En Python 3 los tipos simples pasan por valor y los compuestos por referencia. Crea un ejemplo con 3 funciones que:

Reciban 2 números y devuelvan la suma. Reciban una lista y modifiquen esa misma lista (referencia) duplicando los valores de todos los elementos. No debe devolver nada. Reciban una lista y devuelvan una copia de esa misma lista (referencia) duplicando los valores de todos los elementos. La lista original no debe modificarse.

3.- A partir de un contexto donde queremos almacenar un usuario y su contraseña, haz un ejemplo que explique cómo se haría:

Usando una lista. Usando un diccionario. Al llenarse, las contraseñas deben pasarse a un formato Hash (por ejemplo, SHA-512). El ejemplo debe llenar la lista con 5 usuarios/contraseña y hacer dos consultas.

4.- Explica con ejemplos cómo funcionan los operadores “is”, “not”, “in” en Python 3.

5.- Tarea:

Pon un ejemplo de cómo pasar varios parámetros desde la consola a un programa Python 3. Pon un ejemplo de cómo hacer “sobrecarga de funciones” (funciones que pueden recibir varios números de parámetros), incluyendo el caso en que el número de parámetros no esté definido.

6.- Tarea:

Crea una lista en la cual cada elemento de esa lista sea una lista con dos valores: tamaño y peso. Utilizando Key functions, haz que esta lista se ordene por mayor altura y, en caso de igualdad, por menor peso. Explica en comentarios qué es realmente la “key function”. Pista: en la ayuda se menciona: “El valor del parámetro key debe ser una función (u otro callable) que tome un solo argumento y devuelva una clave para usar con fines de ordenación. Esta técnica es rápida porque la función key se llama exactamente una vez por cada registro de entrada.”

7.- Tarea:

Define la clase Car en Python 3. La clase tendrá como atributos “matrícula” (numérica) y “color”. Crea un método imprimir y, además, dos métodos adicionales que elijas. En segundo lugar, haz que el programa pida un número “n” por teclado y se creen “n” instancias de la clase, donde cada instancia: Cada “matrícula” tendrá un número consecutivo desde 1 hasta “n”. El “color” será para cada instancia un color aleatorio obtenido de esta lista: ["red", "white", "black", "pink", "blue"]. Finalmente, el programa deberá imprimir los valores de las 10 primeras instancias. En caso de que “n” sea menor que 10, solo se imprimirán “n” instancias.

8.- Tarea:

Explica y pon un ejemplo sencillo de una función lambda en Python 3. Después, pon un ejemplo que utilice las funciones de Python: Usando “map()” (y “list()” e “int()” como apoyo para convertir a lista y a números enteros), lee desde teclado una cadena de texto formada por números separados por espacios y transfórmala en una lista formada por números enteros. Usando “filter()”, elimina de la cadena anterior los números menores que 10. Con la cadena resultante y usando “reduce()”, devuelve la multiplicación de los elementos de la lista.

9.- Crea un programa Python 3 que organice los archivos de la carpeta actual. Para cada extensión de archivo, el programa moverá todos los archivos con esa extensión a una carpeta con el mismo nombre que la extensión. Por ejemplo, una lista con extensiones [“png”, “mp4”, “doc”] moverá los archivos ".png" a una carpeta "png", los ".mp4" a una carpeta "mp4", y los ".doc" a una carpeta "doc", si no corresponde la extensión ignorar el archivo. Para distribuir el programa, empaquétalo con PyInstaller.

Manejando ficheros: https://unipython.com/operaciones-con-archivos-y-carpetas-en-python/ Manejandro PyInstaller: https://www.devdungeon.com/content/pyinstaller-tutorial

10.- Diseña la clase Escuela para hacer un programa en Python 3 que permita la gestión completa de varias escuelas. Cada escuela se instanciará a partir de la clase Escuela, que contendrá la información de la escuela (nombre, localidad, responsable...), así como la información de los diferentes profesores y grupos de alumnos, utilizando las siguientes clases auxiliares:

Clase Escuela: Deberá tener métodos para añadir/eliminar alumnos y profesores. Clase Profesor: Contendrá la información de los profesores (nombre, tipo de profesor: ciencias, letras o mixto). Clase Alumno: Contendrá la información de los alumnos (nombre, curso, profesor responsable). Las clases deben estar en ficheros independientes. Ejemplo: Python Importar clase desde otro archivo Cada clase deberá tener sus métodos CRUD: Crear (constructor) Leer (Getters y toString) Actualizar (Setters) Eliminar (Si fuera necesario, en este caso eliminar de una lista) No habrá ningún alumno que asista a dos escuelas diferentes, ni ningún profesor que trabaje en varias escuelas. Las clases deben estar definidas en un archivo separado del programa. Asegúrate de que las relaciones entre las clases están bien representadas y de que hay métodos para gestionar correctamente todos los elementos (inserción, modificación, eliminación, visualización, etc.).

11.- SQLAlchemy es una biblioteca de Python que incluye un ORM (Object Relational Mapping). (NOTA: De esto aprenderán más concretamente en Acceso a Datos) Basándote en el diseño de clases de la pregunta anterior, haz un nuevo programa que añada persistencia a las clases, manteniendo sus relaciones, utilizando el ORM de Python incluido en SQLAlchemy con el driver de SQLite.

Haz un código de ejemplo que permita probar la persistencia de los objetos de la clase Alumno. SQLAlchemy. Tutorial de Python SQLAlchemy. Relaciones de tablas en SQLAlchemy. Una buena estrategia para probar la persistencia es hacer un código/funciones que creen/modifiquen/eliminen algunos objetos, cerrar el programa, comentar esos fragmentos y comprobar que, a pesar de no ejecutarse los cambios, estos están reflejados en la persistencia y en el programa. Para instalar SQLAlchemy, puedes ayudarte con pip3 install SQLAlchemy.
