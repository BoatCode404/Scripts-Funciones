Por supuesto, aquí tienes el contenido en Markdown traducido al español:

# 01. Introducción
## SQL
¡Bienvenido al primer curso de SQL! 💾

SQL (siglas de Structured Query Language, o Lenguaje de Consulta Estructurada) es un lenguaje de programación diseñado para gestionar y recuperar datos almacenados en bases de datos.

Es fundamental tanto en Ciencia de Datos como en Desarrollo Web.

Dato curioso: SQL fue desarrollado en IBM en los años 70 y se llamaba SEQUEL (Structured English Query Language); puedes llamarlo “S-Q-L” o “secuela”.

---

Las bases de datos SQL son colecciones de tablas, con filas y columnas.

En este capítulo, utilizaremos una tabla llamada `shows` con datos sobre programas de televisión populares. 📺

Se ve algo así:

| id | nombre          | género   | plataforma | año | temporadas | tomatómetro |
|----|-----------------|----------|------------|-----|------------|-------------|
| 1  | Silicon Valley  | Comedia  | HBO        | 2014| 6          | 8.5         |
| 2  | The Last of Us  | Horror   | HBO        | 2023| 1          | 8.7         |
| 3  | Squid Game      | Thriller | Netflix    | 2021| 1          | 8.0         |

Hay siete columnas: `id`, `nombre`, `género`, `plataforma`, `año`, `temporadas` y `tomatómetro`.

Las sentencias SQL, o consultas, son instrucciones que la base de datos entiende. En otras palabras, las consultas nos permiten recuperar información de una base de datos.

Probemos una consulta rápidamente. 🙌

### Instrucciones
Copia y pega la siguiente sentencia:

```sql
SELECT * FROM shows;
```

Y luego presiona el botón "Ejecutar" y espera de 1 a 2 segundos.

Deberías ver la tabla `shows` aparecer. ¡Ve si reconoces alguno de los programas! Además, ¿cuántas filas hay en esta tabla?

Presiona "Completar" y luego "Siguiente" para continuar.

¡Feliz codificación! (ﾉ ◕ ヮ ◕)ﾉ*:･ﾟ ✧

Aquí tienes el texto convertido a Markdown en español:



# 02. SELECT
## El Asterisco *
La sentencia SELECT que ejecutamos es fundamental para SQL:

SELECT * FROM shows;

Aquí, dividimos la sentencia en dos líneas; sigue haciendo lo mismo:

SELECT *
FROM shows;

SELECT recupera datos de una base de datos.

* el asterisco significa todas las columnas.
FROM es la palabra clave seguida por el nombre de la tabla.
shows es el nombre de la tabla de la que estamos solicitando datos.
; terminamos la sentencia con un punto y coma.
En resumen, estamos seleccionando todas las columnas de la tabla shows.


# Columnas Específicas
El * toma todas las columnas de una tabla, pero ¿qué pasa si queremos seleccionar solo algunas columnas?

Si solo queremos seleccionar columnas específicas, podemos enumerar los nombres de las columnas, separados por comas:

SELECT columna1, columna2, columna3
FROM nombre_tabla;

Aquí hay un ejemplo:

SELECT id, nombre, género
FROM shows;

Solo seleccionamos las columnas id, nombre y género de la tabla shows.

Nota: Las palabras clave de SQL como SELECT y FROM no son sensibles a mayúsculas y minúsculas, pero es común escribirlas en mayúsculas para distinguirlas de los nombres de columnas (id, nombre, género) y nombres de tablas (shows), que se escriben en minúsculas.

Probémoslo.

### Instrucciones
Selecciona todas las columnas de la tabla shows.

Ahora, selecciona solo las columnas nombre y género de la tabla shows.


# 03. Guerras de Streaming
## Valores Únicos
Cuando analizamos una base de datos, es posible que queramos ver solo los valores únicos dentro de una columna (sin duplicados).

DISTINCT se utiliza para devolver solo los valores únicos en una columna.

Así es como seleccionamos todos los géneros de la tabla shows:

```sql
SELECT genre
FROM shows;
```

Obtendríamos 50 filas de géneros para cada programa de televisión con un montón de duplicados.

Si agregamos la palabra clave DISTINCT después de SELECT:

```sql
SELECT DISTINCT genre
FROM shows;
```

Solo se devolverán los géneros únicos en la tabla shows.

## Instrucciones

El término "Guerras de Streaming" fue acuñado para describir la era de competencia entre servicios de transmisión de video como Netflix, HBO, Disney+, etc. ⚔️

Tenemos una columna stream en la tabla shows para esa información.

Usa DISTINCT para seleccionar los servicios de streaming únicos en la tabla shows.

Claro, aquí tienes el texto convertido a Markdown:



# WHERE
¿Y si quisiéramos filtrar la información basándonos en una condición? Podemos utilizar la cláusula `WHERE`.

Podemos utilizar la cláusula `WHERE` para filtrar información basada en una condición:

```sql
SELECT *
FROM espectáculos
WHERE id = 23;
```

`id = 23` es la condición. Sólo se mostrarán los programas cuyo `id` sea igual a 23.

He aquí otro ejemplo:

```sql
SELECT *
FROM programas
WHERE año > 2020;
```

`año > 2020` es la condición. Sólo se mostrarán los programas estrenados después de 2020.

**Nota:** La palabra clave `WHERE` siempre va después de la parte `FROM` de la consulta.

# Operadores de Comparación
Aquí están todos los operadores de comparación SQL que podemos usar en una condición:

- `=` igual a
- `!=` no igual a
- `>` mayor que
- `<` menor que
- `>=` mayor que o igual a
- `<=` menor o igual que

Los utilizamos para comparar dos valores en la cláusula `WHERE`.

Vamos a probarlos.

## Instrucciones
Rotten Tomatoes es un sitio de reseñas de películas/espectáculos creado por estudiantes universitarios de la Universidad de California, Berkeley.

- 🍅 Cuando al menos el 60% de las críticas de una película o programa de televisión son positivas, se muestra un tomate rojo para indicar que es "Fresca".
- 🤮 Cuando menos del 60% de las críticas de una película o programa de televisión son positivas, se muestra una salpicadura verde para indicar que está "podrida".

Encuentra todos los programas de la tabla que han sido un bombazo (con un tomatómetro inferior a 60).

Por supuesto, aquí tienes el texto convertido a Markdown:


# LIKE
El operador `LIKE` se puede utilizar para buscar un patrón en una columna. Se utiliza en la cláusula `WHERE`:

```sql
SELECT * 
FROM shows 
WHERE name LIKE 'T%';
```

El signo de porcentaje `%` es un carácter comodín que se puede utilizar con `LIKE`. Puede usarlo para hacer coincidir caracteres con un patrón de su consulta deseada.

Esta declaración filtra el resultado para incluir solo programas con nombres que comiencen con la letra 'T'.

`%` se puede utilizar de diferentes maneras:

- `A%` coincide con valores que comienzan con la letra 'A'.
- `%z` coincide con valores que terminan en 'z'.

También podemos usar `%` tanto antes como después de un patrón:

```sql
SELECT * 
FROM shows 
WHERE name LIKE '%the%';
```

Aquí, se devolverá cualquier programa que contenga la palabra "the" en su nombre.

## Instrucciones
Supongamos que estamos buscando un programa de comedia.

Seleccione todos los programas con el patrón `genre` incluido "com" para géneros como comedia de situación, comedia romántica, comedia stand-up, etc.



## 06. Edad de oro

### BETWEEN
El operador `BETWEEN` se utiliza en una cláusula `WHERE` para filtrar el conjunto de resultados dentro de un rango determinado. El rango puede ser entre dos números, textos o incluso fechas, separados por la palabra clave `AND`.

Por ejemplo, esta consulta filtra el resultado para incluir solo programas entre los años 2020 y 2025 (inclusive):

```sql
SELECT *
FROM shows
WHERE year
BETWEEN 2020 AND 2025;
```

Cuando los valores son texto, `BETWEEN` filtra el resultado dentro del rango alfabético.

En esta declaración, `BETWEEN` filtra el resultado para incluir solo programas con nombres que comienzan con la letra 'A' hasta la 'D':

```sql
SELECT *
FROM shows
WHERE name
BETWEEN 'A' AND 'D';
```

**Nota:** `BETWEEN` se detiene en la segunda letra, pero no incluye valores que comienzan con la segunda letra.

Entonces, si el título de un programa es solo 'D', se devolverá, mientras que 'Dragon Ball Super' no.

#### Instrucciones
Se considera que la Nueva Edad de Oro de la Televisión comenzó en 1999 con el programa de mafiosos de Jersey, "Los Soprano".

Encuentra todos los programas lanzados en la Edad de Oro, desde 1999 hasta 2024. ¿Has visto alguno de ellos?


## 08. NYC Restaurantes

### ¡Felicitaciones!
¡Hurra! ¡Has llegado al final del primer capítulo! 🎈

Aquí hay un resumen:

- `SELECT` selecciona datos `FROM` de una base de datos. (`*` selecciona todas las columnas)
- `DISTINCT` devuelve valores únicos en una columna.
- `WHERE` filtra los resultados según una condición.
- Operadores de comparación: `=`, `!=`, `>`, `<`, `>=`, `<=`.
- `LIKE` y `BETWEEN` son operadores especiales.
- `ORDER BY` ordena los datos en orden ascendente/descendente.

Juntémoslo con algo divertido.

#### Instrucciones
El equipo de Codedex tiene su sede en Nueva York y reunimos nuestros 50 mejores restaurantes de la ciudad. 😋

Está en un nuevo conjunto de datos `restaurants` al que puede acceder con:

```sql
SELECT *
FROM restaurants;
```

Tiene las siguientes columnas:

- `id`
- `name`
- `cuisine`
- `borough`
- `neighborhood`
- `price`
- `yelp_review`

Juega con la mesa y descubre lo siguiente:

- ¿Cuáles son todas las cocinas únicas en la mesa?
- ¿Cuáles son todos los restaurantes chinos? ¿Italiano?
- ¿Cuáles son todos los lugares en Greenpoint (un barrio de Brooklyn)?

**Bonificación:** Formule sus propias preguntas y publique una captura de pantalla de sus hallazgos en Twitter haciendo clic en el ícono a continuación, y luego diríjase a #CodedexRestaurants y comente sobre el trabajo de otro alumno. ¡Apoye a sus compañeros de aprendizaje! :)
