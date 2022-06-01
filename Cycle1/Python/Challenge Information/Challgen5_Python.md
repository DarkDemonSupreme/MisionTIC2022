Te contrataron como ingeniero de software junior para desarrollar una aplicación, para la empresa ServiPaquetes, que ayude con la gestión de los paquetes. 

Específicamente para calcular el costo de los envíos de los paquetes. Para ello, tú decides que harás la aplicación de forma progresiva, semana tras semana.
 Es decir, el software que empieces a plantear desde esta semana, igual será útil en la última semana.
  La empresa te indica que es fundamental que sigas el orden en el que ellos te indican los datos, puesto que el sistema de ellos los arroja en un orden específico.

Esta semana la empresa te comunica que terminaron la fase de pruebas de su nuevo sistema.
 Este nuevo y mejorado sistema ahora genera un archivo json que contiene algunos datos de la empresa y, lo más importante, los datos de los paquetes.
  Ellos te piden que, por favor, adaptes tu programa para que pueda leer el archivo generado por su sistema. Aquí te presentan una imagen de la estructura de datos generada:

También, te proporcionaron el archivo generado por el sistema, puedes descargarlo haciendo clic aquí.

Tu tarea esta semana es adaptar la función costoTotal de tal forma que el primer parámetro que esta solicita (numeroPaquetes), en lugar de recibir un número, reciba una lista con la información de los paquetes. Esto implica que el ciclo que usas dentro de la función debe adaptarse también, además de que ya no será necesario tomar los datos de los paquetes por entrada estándar, ya que estos datos vienen en formato de diccionario dentro de la lista de paquetes.

Lee detenidamente el planteamiento del reto, cuando se te indique que hay que seguir un orden, es necesario que así sea. Sigue atentamente los pasos de la solución del reto si tienes dificultades al resolverlo. Planteamiento del reto Con respecto a la situación planteada, tendrás que tomar el código de la semana pasada y adaptar la función costoTotal. Para esto, reemplaza el parámetro numeroPaquetes por otro que tenga más sentido, por ejemplo, listaPaquetes. Luego, haz que el ciclo dentro de la función itere sobre la lista, tomando cada elemento de esta. Los elementos dentro de la lista son diccionarios cuyas llaves son: ALTO, ANCHO y PROFUNDO, esto significa que ya NO se deberán tomar los datos como entrada estándar, en su lugar, se usan los datos que vienen en cada diccionario que representa cada paquete.

IMPORTANTE: Cuando vayas a entregar el reto, quítale todos los textos decorativos o informativos para el usuario. Solo debes dejar el código funcional. Es decir, si imprimes cosas tipo “Ingrese …”, “El valor es …”, deberás de quitarlo. Solo imprime lo que te indica el planteamiento del problema y en el orden en que se solicita.

Acciones de aprendizaje

1. Identifica las variables que se quieren definir.
2. Recordar de qué manera se pueden recolectar datos por entrada estándar para definir variables.
3. Recordar el uso de estructuras iterativas.
4. Recordar el uso de funciones.
5. Recordar el concepto de estructura de datos.
6. Recordar el uso de diccionarios.

Solución del reto

1. Toma el código de la semana pasada.
2. Cambia el nombre del parámetro numeroPaquetes por listaPaquetes, de la función costoTotal, es decir, la función debería ser costoTotal(listaPaquetes, descuento).
3. Adapta el ciclo que usas dentro de la función, de tal forma que itere el parámetro listaPaquetes. Te recomendamos que uses un ciclo for.
a. Cada elemento dentro de la lista es un diccionario que tiene como llaves ALTO, ANCHO y PROFUNDO, usa esas llaves para tomar el dato respectivo al alto, ancho y profundo.
b. Envía los datos tomados a la función calcularCosto.
c. El código restante es similar al del reto de la semana pasada.

Nota: Aquí se plantea lo estrictamente necesario que se debe de hacer para solucionar el reto en CodeRunner, sin embargo, te recomendamos que uses código adicional, impresiones de pantalla y demás elementos necesarios para resolverlo en tu computador. A la hora de entregar el código, solo pega las dos funciones, sin ninguna impresión de pantalla.