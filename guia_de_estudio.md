# Guía de estudio local

Las páginas indicadas son posiciones físicas del PDF, comenzando en 1.

Los extractos son la fuente principal. Las explicaciones del modelo local son borradores que requieren comprobación.


## Normalización


### Resumen · extractos del PDF


Normalización

Entrenamiento de redes neuronales

Fuente: 15.1.0 Normalización.pptx.pdf, p. 1.


### Conceptos clave · extractos del PDF


Normalización

Fuente: 15.1.0 Normalización.pptx.pdf, p. 1.


## Normalizar


### Resumen · extractos del PDF


• La normalización es una técnica de
 preparación de datos.

Fuente: 15.1.0 Normalización.pptx.pdf, p. 2.


• La normalización es un proceso que permite
 transformar las variables de un rango de
 valores a una escala numérica común.Normalizar
 • Es decir que al normalizar se ajustan los
 valores de entrada (algunas veces dedatos
 salida) para que estén dentro de un rango
 mas pequeño y consistente:

Fuente: 15.1.0 Normalización.pptx.pdf, p. 2.


• Valores entre 0 y 1 o bien entre -1 y 1.

Fuente: 15.1.0 Normalización.pptx.pdf, p. 2.


Ejemplo:
 • Sin normalizar: 0, 10, 20, 30, 40
 • Normalizados [0-1]: 0.0, 0.25, 0.50, 0.75, 1.0

Fuente: 15.1.0 Normalización.pptx.pdf, p. 2.


### Conceptos clave · extractos del PDF


Normalizar

Fuente: 15.1.0 Normalización.pptx.pdf, p. 2.


### Definiciones · extractos del PDF


• La normalización es una técnica de
 preparación de datos.

Fuente: 15.1.0 Normalización.pptx.pdf, p. 2.


• La normalización es un proceso que permite
 transformar las variables de un rango de
 valores a una escala numérica común.Normalizar
 • Es decir que al normalizar se ajustan los
 valores de entrada (algunas veces dedatos
 salida) para que estén dentro de un rango
 mas pequeño y consistente:

Fuente: 15.1.0 Normalización.pptx.pdf, p. 2.


### Ejemplos · extractos del PDF


Ejemplo:
 • Sin normalizar: 0, 10, 20, 30, 40
 • Normalizados [0-1]: 0.0, 0.25, 0.50, 0.75, 1.0

Fuente: 15.1.0 Normalización.pptx.pdf, p. 2.


## Porque es necesario normalizar?


### Resumen · extractos del PDF


• Desea implementar un programa que prediga el precio de un
 vehículo usados utilizando dos datos de entrada:
 • Antigüedad: de 0 a 20 años.

Fuente: 15.1.0 Normalización.pptx.pdf, p. 3.


• Precio original: de 10,000 a 100,000 USD.

Fuente: 15.1.0 Normalización.pptx.pdf, p. 3.


• Cuando la red neuronal analiza estos datos, el número "100,000"
 es 5,000 veces más grande que "20".

Fuente: 15.1.0 Normalización.pptx.pdf, p. 3.


La red neuronal pensará
 matemáticamente que el precio es muchísimo más importante que
 la antigüedad, simplemente porque el número es mayor.

Fuente: 15.1.0 Normalización.pptx.pdf, p. 3.


• La normalización pone a ambos en el mismo nivel de importancia.

Fuente: 15.1.0 Normalización.pptx.pdf, p. 3.


### Conceptos clave · extractos del PDF


Porque es necesario normalizar?

Fuente: 15.1.0 Normalización.pptx.pdf, p. 3.


### Definiciones · extractos del PDF


• Cuando la red neuronal analiza estos datos, el número "100,000"
 es 5,000 veces más grande que "20".

Fuente: 15.1.0 Normalización.pptx.pdf, p. 3.


La red neuronal pensará
 matemáticamente que el precio es muchísimo más importante que
 la antigüedad, simplemente porque el número es mayor.

Fuente: 15.1.0 Normalización.pptx.pdf, p. 3.


### Fórmulas o comandos · extractos del PDF


La red neuronal pensará
 matemáticamente que el precio es muchísimo más importante que
 la antigüedad, simplemente porque el número es mayor.

Fuente: 15.1.0 Normalización.pptx.pdf, p. 3.


• La normalización pone a ambos en el mismo nivel de importancia.

Fuente: 15.1.0 Normalización.pptx.pdf, p. 3.


### Comprender y practicar · extractos del PDF


• Desea implementar un programa que prediga el precio de un
 vehículo usados utilizando dos datos de entrada:
 • Antigüedad: de 0 a 20 años.

Fuente: 15.1.0 Normalización.pptx.pdf, p. 3.


## Beneﬁcios de normalizar en ML


### Resumen · extractos del PDF


• Velocidad de Entrenamiento
 • Reducción en la perdida
 • Facilidad en la convergencia del modelo
 • Estabilidad Numérica, previniendo errores tipo Nan (not a
 number) o inf (∞) o el colapso del modelo
 • Justicia entre Variables al asegurar que todas las variables
 contribuyan al entrenamiento equitativamente

Fuente: 15.1.0 Normalización.pptx.pdf, p. 4.


### Conceptos clave · extractos del PDF


Beneﬁcios de normalizar en ML

Fuente: 15.1.0 Normalización.pptx.pdf, p. 4.


## Métodos


### Resumen · extractos del PDF


Cuándo
Método Fórmula Resultado
 usarlo
 Cuando
 conoce los
Escalado Datos entre 0
 límites (ej.

Fuente: 15.1.0 Normalización.pptx.pdf, p. 5.


MétodosMin-Max y 1
 píxeles de mas imagen).

Fuente: 15.1.0 Normalización.pptx.pdf, p. 5.


Cuando los comunes
 Media = 0, datos tienen
Estandarización Desv.

Fuente: 15.1.0 Normalización.pptx.pdf, p. 5.


### Conceptos clave · extractos del PDF


Métodos

Fuente: 15.1.0 Normalización.pptx.pdf, p. 5.


### Fórmulas o comandos · extractos del PDF


Cuando los comunes
 Media = 0, datos tienen
Estandarización Desv.

Fuente: 15.1.0 Normalización.pptx.pdf, p. 5.


### Memorizar · extractos del PDF


Cuándo
Método Fórmula Resultado
 usarlo
 Cuando
 conoce los
Escalado Datos entre 0
 límites (ej.

Fuente: 15.1.0 Normalización.pptx.pdf, p. 5.


## Codigo en Pythom


### Resumen · extractos del PDF


#No normaliza pero prepara la herramienta
 scaler_X = MinMaxScaler()
 scaler_y = MinMaxScaler()

Fuente: 15.1.0 Normalización.pptx.pdf, p. 6.


#Normaliza: encuentra los maximos y minimos, posterirmente aplica la
 formula de escalado en normalizacion
 X_scaled = scaler_X.fit_transform(X)
 y_scaled = scaler_y.fit_transform(y)

Fuente: 15.1.0 Normalización.pptx.pdf, p. 6.


#Desnormalizar
 y_scaled = scaler_y.inverse_transform(y)

Fuente: 15.1.0 Normalización.pptx.pdf, p. 6.


### Conceptos clave · extractos del PDF


Codigo en Pythom

Fuente: 15.1.0 Normalización.pptx.pdf, p. 6.


### Fórmulas o comandos · extractos del PDF


#No normaliza pero prepara la herramienta
 scaler_X = MinMaxScaler()
 scaler_y = MinMaxScaler()

Fuente: 15.1.0 Normalización.pptx.pdf, p. 6.


#Normaliza: encuentra los maximos y minimos, posterirmente aplica la
 formula de escalado en normalizacion
 X_scaled = scaler_X.fit_transform(X)
 y_scaled = scaler_y.fit_transform(y)

Fuente: 15.1.0 Normalización.pptx.pdf, p. 6.


#Desnormalizar
 y_scaled = scaler_y.inverse_transform(y)

Fuente: 15.1.0 Normalización.pptx.pdf, p. 6.


## Demostración


### Resumen · extractos del PDF


Demostración

Fuente: 15.1.0 Normalización.pptx.pdf, p. 7.


### Conceptos clave · extractos del PDF


Demostración

Fuente: 15.1.0 Normalización.pptx.pdf, p. 7.


Demostración

Fuente: 20.2 Redes neuronales convolucionales.pptx.pdf, p. 18.


## Conclusión


### Resumen · extractos del PDF


Normalizar:
 • No cambia la información esencial de los datos.

Fuente: 15.1.0 Normalización.pptx.pdf, p. 8.


• Facilita que la red encuentre una solución óptima.

Fuente: 15.1.0 Normalización.pptx.pdf, p. 8.


### Conceptos clave · extractos del PDF


Conclusión

Fuente: 15.1.0 Normalización.pptx.pdf, p. 8.


## Ejercicio


### Resumen · extractos del PDF


Predicción de precios de casas
 En este ejercicio intentará construir una red neuronal que prediga el precio de una casa de
 acuerdo con una fórmula simple.

Fuente: 15.1.0 Normalización.pptx.pdf, p. 9.


Si el precio de la casa fuera tan fácil como que una casa cuesta 50000 + 50000 por habitación,
 de modo que una casa de 1 habitación cuesta 100000, una casa de 2 habitaciones cuesta
 150000, etc.

Fuente: 15.1.0 Normalización.pptx.pdf, p. 9.


¿Cómo crearía una red neuronal que aprenda esta relación para predecir que una casa de 7
 habitaciones cuesta cerca de 400000, etc.?

Fuente: 15.1.0 Normalización.pptx.pdf, p. 9.


Una planta industrial desea predecir el Produccion (X)
 Dia Consumo (Y) [kWh]
 [Toneladas] consumo de energía diaria en
 Kilovatios-hora (kWh) en función de la 1 10 1,200

Fuente: 15.1.0 Normalización.pptx.pdf, p. 10.


2 20 1,850 producción diaria en toneladas procesadas.

Fuente: 15.1.0 Normalización.pptx.pdf, p. 10.


3 30 2,400
 Los datos recolectados durante 12 días de 4 40 3,100

Fuente: 15.1.0 Normalización.pptx.pdf, p. 10.


5 50 3,750 operación son los siguientes:
 6 60 4,300

Fuente: 15.1.0 Normalización.pptx.pdf, p. 10.


### Conceptos clave · extractos del PDF


Ejercicio

Fuente: 15.1.0 Normalización.pptx.pdf, p. 9.


Ejercicio

Fuente: 15.1.0 Normalización.pptx.pdf, p. 10.


Ejercicio

Fuente: 16.1 Implementando una Red Neuronal y codificacion one-hot.pptx.pdf, p. 15.


Ejercicio

Fuente: 20.2 Redes neuronales convolucionales.pptx.pdf, p. 19.


### Definiciones · extractos del PDF


5 50 3,750 operación son los siguientes:
 6 60 4,300

Fuente: 15.1.0 Normalización.pptx.pdf, p. 10.


### Ejemplos · extractos del PDF


Predicción de precios de casas
 En este ejercicio intentará construir una red neuronal que prediga el precio de una casa de
 acuerdo con una fórmula simple.

Fuente: 15.1.0 Normalización.pptx.pdf, p. 9.


• Horas de sueño, Minutos de ejercicio diario, Tazas de café consumidas

Fuente: 16.1 Implementando una Red Neuronal y codificacion one-hot.pptx.pdf, p. 15.


• Solicitar horas de sueño, minutos de ejercicio y tazas de café, y predecir el nivel de estrés.

Fuente: 16.1 Implementando una Red Neuronal y codificacion one-hot.pptx.pdf, p. 15.


• Realizar el siguiente ejercicio para comprender cómo el número de
 filtros y el tipo de pooling (Max o Average) afectan: la capacidad de
 extracción de características, la complejidad del modelo, y la
 precisión en clasificación de imágenes.

Fuente: 20.2 Redes neuronales convolucionales.pptx.pdf, p. 19.


• Realizar x ejercicios con:
 • Maxpooling y pocos filtros: 16/32
 • Maxpooling con mas filtros: 64
 • MaxPolling con muchos filtros: 128
 • Averagepooling y pocos filtros: 16/32
 • Averagepooling con mas filtros: 48/64
 • Averagepooling y con muchos filtros: 128
• Registre los valores de perdida, preciscion, tiempo de entrenamiento.

Fuente: 20.2 Redes neuronales convolucionales.pptx.pdf, p. 19.


### Memorizar · extractos del PDF


Predicción de precios de casas
 En este ejercicio intentará construir una red neuronal que prediga el precio de una casa de
 acuerdo con una fórmula simple.

Fuente: 15.1.0 Normalización.pptx.pdf, p. 9.


## Ejercicios


### Resumen · extractos del PDF


Ejercicio 1: predecir el puntaje de un examen según horas de estudio y
 asistencia a clases (Sí / No).

Fuente: 15.1.0 Normalización.pptx.pdf, p. 11.


Horas de estudio Asistencia Puntaje

Fuente: 15.1.0 Normalización.pptx.pdf, p. 11.


Ejercicio 2: predecir la temperatura final del café después de 10 minutos según
Ejercicios la temperatura inicial (°C) y el tipo de taza (Plástico, Cerámica, Vidrio).

Fuente: 15.1.0 Normalización.pptx.pdf, p. 11.


Temp inicial Tipo de taza Temp después de 10 min (centígrados)

Fuente: 15.1.0 Normalización.pptx.pdf, p. 11.


Obtener: Aplicar one-hot encoding a la columna alfa-numerica, Normalizar
 entradas y salida, crear un programa interactivo que pregunte la temperatura
 inicial y tipo de taza y prediga la temperatura final.

Fuente: 15.1.0 Normalización.pptx.pdf, p. 11.


### Conceptos clave · extractos del PDF


Ejercicios

Fuente: 15.1.0 Normalización.pptx.pdf, p. 11.


### Procedimientos · extractos del PDF


Ejercicio 2: predecir la temperatura final del café después de 10 minutos según
Ejercicios la temperatura inicial (°C) y el tipo de taza (Plástico, Cerámica, Vidrio).

Fuente: 15.1.0 Normalización.pptx.pdf, p. 11.


Temp inicial Tipo de taza Temp después de 10 min (centígrados)

Fuente: 15.1.0 Normalización.pptx.pdf, p. 11.


### Ejemplos · extractos del PDF


Ejercicio 1: predecir el puntaje de un examen según horas de estudio y
 asistencia a clases (Sí / No).

Fuente: 15.1.0 Normalización.pptx.pdf, p. 11.


Ejercicio 2: predecir la temperatura final del café después de 10 minutos según
Ejercicios la temperatura inicial (°C) y el tipo de taza (Plástico, Cerámica, Vidrio).

Fuente: 15.1.0 Normalización.pptx.pdf, p. 11.


### Comprender y practicar · extractos del PDF


Obtener: Aplicar one-hot encoding a la columna alfa-numerica, Normalizar
 entradas y salida, crear un programa interactivo que pregunte la temperatura
 inicial y tipo de taza y prediga la temperatura final.

Fuente: 15.1.0 Normalización.pptx.pdf, p. 11.


## Red Neuronal


### Resumen · extractos del PDF


Red Neuronal

 Red Neuronal y codificacion

Fuente: 16.1 Implementando una Red Neuronal y codificacion one-hot.pptx.pdf, p. 1.


Red Neuronal

Fuente: 16.1 Implementando una Red Neuronal y codificacion one-hot.pptx.pdf, p. 3.


### Conceptos clave · extractos del PDF


Red Neuronal

Fuente: 16.1 Implementando una Red Neuronal y codificacion one-hot.pptx.pdf, p. 1.


Red Neuronal

Fuente: 16.1 Implementando una Red Neuronal y codificacion one-hot.pptx.pdf, p. 3.


## Neurona simple


### Resumen · extractos del PDF


modelo_simple = tf.keras.Sequential([
 tf.keras.layers.Dense(units=1, input_shape=[1]) # solo una neurona
])

Fuente: 16.1 Implementando una Red Neuronal y codificacion one-hot.pptx.pdf, p. 2.


### Conceptos clave · extractos del PDF


Neurona simple

Fuente: 16.1 Implementando una Red Neuronal y codificacion one-hot.pptx.pdf, p. 2.


### Fórmulas o comandos · extractos del PDF


modelo_simple = tf.keras.Sequential([
 tf.keras.layers.Dense(units=1, input_shape=[1]) # solo una neurona
])

Fuente: 16.1 Implementando una Red Neuronal y codificacion one-hot.pptx.pdf, p. 2.


## Red neuronal simple


### Resumen · extractos del PDF


Entrada
 1
 Entrada SalidaRed neuronal simple 2 1
 Entrada
 3
 • 3 capas
 • Capa de entrada: n variables (depende de la cantidad de columnas, supongamos 3 columnas)
 • input_shape=[X.shape[0]] #cantidad de filas
 • input_shape=[X.shape[1] ] #cantidad de columnas
 • Cantidad de entradas: X.shape #dataframe: X, shape: dimensión
 • Si X tiene 4 columnas: input_shape =4
 • Capa oculta
 • 3 neuronas

Fuente: 16.1 Implementando una Red Neuronal y codificacion one-hot.pptx.pdf, p. 4.


model = tf.keras.Sequential([
 tf.keras.layers.Dense(units=3, input_shape=[X.shape[1]]),
 tf.keras.layers.Dense(units=1)
])

Fuente: 16.1 Implementando una Red Neuronal y codificacion one-hot.pptx.pdf, p. 4.


Entrada
 1
 Entrada SalidaRed neuronal simple 2 1
 Entrada
 3
• 3 capas
 • Capa de entrada: n variables (depende de la cantidad de columnas, supongamos 3
 columnas)
 • input_shape=[X.shape[0] #cantidad de filas
 • input_shape=[X.shape[1] #cantidad de columnas
 • Cantidad de entradas: X.shape #dataframe: X, shape: dimensión
 • Si X tiene 4 columnas: input_shape =[4]
 • Capa oculta
 • 3 neuronas
 • Capa de salida: 1 neurona

Fuente: 16.1 Implementando una Red Neuronal y codificacion one-hot.pptx.pdf, p. 5.


Entrada
 1
 Entrada SalidaRed neuronal simple 2 1
 Entrada
 3
• 3 capas
 • Capa de entrada: n variables (depende de la cantidad de columnas, supongamos 3
 columnas)
 • input_shape=[X.shape[0] #cantidad de filas
 • input_shape=[X.shape[1] #cantidad de columnas
 • Capa oculta
 • 3 neuronas
 • Cantidad de entradas: X.shape #dataframe: X, shape: dimensión
 • Si X tiene 4 columnas: input_shape =[4]
 • Capa de salida: 1 neurona

Fuente: 16.1 Implementando una Red Neuronal y codificacion one-hot.pptx.pdf, p. 6.


### Conceptos clave · extractos del PDF


Red neuronal simple

Fuente: 16.1 Implementando una Red Neuronal y codificacion one-hot.pptx.pdf, p. 4.


Red neuronal simple

Fuente: 16.1 Implementando una Red Neuronal y codificacion one-hot.pptx.pdf, p. 5.


Red neuronal simple

Fuente: 16.1 Implementando una Red Neuronal y codificacion one-hot.pptx.pdf, p. 6.


### Ejemplos · extractos del PDF


Entrada
 1
 Entrada SalidaRed neuronal simple 2 1
 Entrada
 3
 • 3 capas
 • Capa de entrada: n variables (depende de la cantidad de columnas, supongamos 3 columnas)
 • input_shape=[X.shape[0]] #cantidad de filas
 • input_shape=[X.shape[1] ] #cantidad de columnas
 • Cantidad de entradas: X.shape #dataframe: X, shape: dimensión
 • Si X tiene 4 columnas: input_shape =4
 • Capa oculta
 • 3 neuronas

Fuente: 16.1 Implementando una Red Neuronal y codificacion one-hot.pptx.pdf, p. 4.


Entrada
 1
 Entrada SalidaRed neuronal simple 2 1
 Entrada
 3
• 3 capas
 • Capa de entrada: n variables (depende de la cantidad de columnas, supongamos 3
 columnas)
 • input_shape=[X.shape[0] #cantidad de filas
 • input_shape=[X.shape[1] #cantidad de columnas
 • Cantidad de entradas: X.shape #dataframe: X, shape: dimensión
 • Si X tiene 4 columnas: input_shape =[4]
 • Capa oculta
 • 3 neuronas
 • Capa de salida: 1 neurona

Fuente: 16.1 Implementando una Red Neuronal y codificacion one-hot.pptx.pdf, p. 5.


Entrada
 1
 Entrada SalidaRed neuronal simple 2 1
 Entrada
 3
• 3 capas
 • Capa de entrada: n variables (depende de la cantidad de columnas, supongamos 3
 columnas)
 • input_shape=[X.shape[0] #cantidad de filas
 • input_shape=[X.shape[1] #cantidad de columnas
 • Capa oculta
 • 3 neuronas
 • Cantidad de entradas: X.shape #dataframe: X, shape: dimensión
 • Si X tiene 4 columnas: input_shape =[4]
 • Capa de salida: 1 neurona

Fuente: 16.1 Implementando una Red Neuronal y codificacion one-hot.pptx.pdf, p. 6.


### Fórmulas o comandos · extractos del PDF


Entrada
 1
 Entrada SalidaRed neuronal simple 2 1
 Entrada
 3
 • 3 capas
 • Capa de entrada: n variables (depende de la cantidad de columnas, supongamos 3 columnas)
 • input_shape=[X.shape[0]] #cantidad de filas
 • input_shape=[X.shape[1] ] #cantidad de columnas
 • Cantidad de entradas: X.shape #dataframe: X, shape: dimensión
 • Si X tiene 4 columnas: input_shape =4
 • Capa oculta
 • 3 neuronas

Fuente: 16.1 Implementando una Red Neuronal y codificacion one-hot.pptx.pdf, p. 4.


model = tf.keras.Sequential([
 tf.keras.layers.Dense(units=3, input_shape=[X.shape[1]]),
 tf.keras.layers.Dense(units=1)
])

Fuente: 16.1 Implementando una Red Neuronal y codificacion one-hot.pptx.pdf, p. 4.


Entrada
 1
 Entrada SalidaRed neuronal simple 2 1
 Entrada
 3
• 3 capas
 • Capa de entrada: n variables (depende de la cantidad de columnas, supongamos 3
 columnas)
 • input_shape=[X.shape[0] #cantidad de filas
 • input_shape=[X.shape[1] #cantidad de columnas
 • Cantidad de entradas: X.shape #dataframe: X, shape: dimensión
 • Si X tiene 4 columnas: input_shape =[4]
 • Capa oculta
 • 3 neuronas
 • Capa de salida: 1 neurona

Fuente: 16.1 Implementando una Red Neuronal y codificacion one-hot.pptx.pdf, p. 5.


Entrada
 1
 Entrada SalidaRed neuronal simple 2 1
 Entrada
 3
• 3 capas
 • Capa de entrada: n variables (depende de la cantidad de columnas, supongamos 3
 columnas)
 • input_shape=[X.shape[0] #cantidad de filas
 • input_shape=[X.shape[1] #cantidad de columnas
 • Capa oculta
 • 3 neuronas
 • Cantidad de entradas: X.shape #dataframe: X, shape: dimensión
 • Si X tiene 4 columnas: input_shape =[4]
 • Capa de salida: 1 neurona

Fuente: 16.1 Implementando una Red Neuronal y codificacion one-hot.pptx.pdf, p. 6.


## Conversión de valores texto a numérico


### Resumen · extractos del PDF


Conversión de valores texto a numérico

Fuente: 16.1 Implementando una Red Neuronal y codificacion one-hot.pptx.pdf, p. 7.


●Las redes neuronales trabajan con números debido a que
 internamente son un modelo matemático, no con texto.

Fuente: 16.1 Implementando una Red Neuronal y codificacion one-hot.pptx.pdf, p. 7.


○Variables categóricas
 ■ "Soleado", "Nublado", "Lluvioso"
 ■ "Alto", "Medio", "Bajo"
 ■ "Masculino", "Femenino"
 ○Texto libre
 ■ "La película estuvo muy buena"
 ■ "El clima hoy es terrible"

Fuente: 16.1 Implementando una Red Neuronal y codificacion one-hot.pptx.pdf, p. 7.


### Conceptos clave · extractos del PDF


Conversión de valores texto a numérico

Fuente: 16.1 Implementando una Red Neuronal y codificacion one-hot.pptx.pdf, p. 7.


### Definiciones · extractos del PDF


●Las redes neuronales trabajan con números debido a que
 internamente son un modelo matemático, no con texto.

Fuente: 16.1 Implementando una Red Neuronal y codificacion one-hot.pptx.pdf, p. 7.


○Variables categóricas
 ■ "Soleado", "Nublado", "Lluvioso"
 ■ "Alto", "Medio", "Bajo"
 ■ "Masculino", "Femenino"
 ○Texto libre
 ■ "La película estuvo muy buena"
 ■ "El clima hoy es terrible"

Fuente: 16.1 Implementando una Red Neuronal y codificacion one-hot.pptx.pdf, p. 7.


## Conversión de Texto a números


### Resumen · extractos del PDF


Bag of Words Cuenta cuántas veces aparece cada palabra

Fuente: 16.1 Implementando una Red Neuronal y codificacion one-hot.pptx.pdf, p. 8.


TF-IDF Similar pero penaliza palabras muy comunes

Fuente: 16.1 Implementando una Red Neuronal y codificacion one-hot.pptx.pdf, p. 8.


Word2Vec Convierte cada palabra en un vector numérico con significado semántico

Fuente: 16.1 Implementando una Red Neuronal y codificacion one-hot.pptx.pdf, p. 8.


Embeddings (BERT, GPT) Representaciones profundas que entienden contexto

Fuente: 16.1 Implementando una Red Neuronal y codificacion one-hot.pptx.pdf, p. 8.


LLMs Tokenizar, Codificar tokens, Embedding (vectorizar), Positional (posición
 token)

Fuente: 16.1 Implementando una Red Neuronal y codificacion one-hot.pptx.pdf, p. 8.


### Conceptos clave · extractos del PDF


Conversión de Texto a números

Fuente: 16.1 Implementando una Red Neuronal y codificacion one-hot.pptx.pdf, p. 8.


## Codiﬁcación one-hot


### Resumen · extractos del PDF


• La codificación One-Hot (One-Hot Encoding) es una técnica
 para convertir datos categóricos (texto o categorías) en
 números en un dataset/dataframe.

Fuente: 16.1 Implementando una Red Neuronal y codificacion one-hot.pptx.pdf, p. 9.


### Conceptos clave · extractos del PDF


Codiﬁcación one-hot

Fuente: 16.1 Implementando una Red Neuronal y codificacion one-hot.pptx.pdf, p. 9.


### Definiciones · extractos del PDF


• La codificación One-Hot (One-Hot Encoding) es una técnica
 para convertir datos categóricos (texto o categorías) en
 números en un dataset/dataframe.

Fuente: 16.1 Implementando una Red Neuronal y codificacion one-hot.pptx.pdf, p. 9.


## one-hot


### Resumen · extractos del PDF


one-hot
encoding

Fuente: 16.1 Implementando una Red Neuronal y codificacion one-hot.pptx.pdf, p. 10.


### Conceptos clave · extractos del PDF


one-hot

Fuente: 16.1 Implementando una Red Neuronal y codificacion one-hot.pptx.pdf, p. 10.


## 16.1 Implementando una Red Neuronal y codificacion one-hot.pptx


### Resumen · extractos del PDF


• Tiene tres categorías para color: rojo, azul y verde.

Fuente: 16.1 Implementando una Red Neuronal y codificacion one-hot.pptx.pdf, p. 11.


Predicción del precio de una habitación de hotel

Fuente: 16.1 Implementando una Red Neuronal y codificacion one-hot.pptx.pdf, p. 14.


Una pequeña empresa desea predecir el precio de una habitación de hotel según tres factores:

Fuente: 16.1 Implementando una Red Neuronal y codificacion one-hot.pptx.pdf, p. 14.


Temporada Noches Personas Precio (QTZ)

Fuente: 16.1 Implementando una Red Neuronal y codificacion one-hot.pptx.pdf, p. 14.


• Aplicar one-hot encoding a “Temporada”.

Fuente: 16.1 Implementando una Red Neuronal y codificacion one-hot.pptx.pdf, p. 14.


• Normalizar todas las variables con MinMaxScaler.

Fuente: 16.1 Implementando una Red Neuronal y codificacion one-hot.pptx.pdf, p. 14.


• Entrenar una red neuronal con 3 capas:
 • Capa de entrada: 5 entradas #despues de aplicar one-hot enconding
 • Capa oculta con 3 neuronas.

Fuente: 16.1 Implementando una Red Neuronal y codificacion one-hot.pptx.pdf, p. 14.


### Conceptos clave · extractos del PDF


16.1 Implementando una Red Neuronal y codificacion one-hot.pptx

Fuente: 16.1 Implementando una Red Neuronal y codificacion one-hot.pptx.pdf, p. 11.


16.1 Implementando una Red Neuronal y codificacion one-hot.pptx

Fuente: 16.1 Implementando una Red Neuronal y codificacion one-hot.pptx.pdf, p. 14.


### Comprender y practicar · extractos del PDF


• Aplicar one-hot encoding a “Temporada”.

Fuente: 16.1 Implementando una Red Neuronal y codificacion one-hot.pptx.pdf, p. 14.


• Entrenar una red neuronal con 3 capas:
 • Capa de entrada: 5 entradas #despues de aplicar one-hot enconding
 • Capa oculta con 3 neuronas.

Fuente: 16.1 Implementando una Red Neuronal y codificacion one-hot.pptx.pdf, p. 14.


## No es recomendable asignar números


### Resumen · extractos del PDF


El modelo podría creer que: (como si hubiese un orden
 matemático)
 Rojo > Azul > Verde

Fuente: 16.1 Implementando una Red Neuronal y codificacion one-hot.pptx.pdf, p. 12.


### Conceptos clave · extractos del PDF


No es recomendable asignar números

Fuente: 16.1 Implementando una Red Neuronal y codificacion one-hot.pptx.pdf, p. 12.


## Integer encoding


### Resumen · extractos del PDF


Integer encoding
Labelencoder

Fuente: 16.1 Implementando una Red Neuronal y codificacion one-hot.pptx.pdf, p. 13.


### Conceptos clave · extractos del PDF


Integer encoding

Fuente: 16.1 Implementando una Red Neuronal y codificacion one-hot.pptx.pdf, p. 13.


## Función de activación


### Resumen · extractos del PDF


Función de activación

 Redes neuronales

Fuente: 17.1 Función de activación.pptx.pdf, p. 1.


### Conceptos clave · extractos del PDF


Función de activación

Fuente: 17.1 Función de activación.pptx.pdf, p. 1.


## Qué son las funciones de activación?


### Resumen · extractos del PDF


Qué son las funciones de activación?

Fuente: 17.1 Función de activación.pptx.pdf, p. 2.


•Es una función utilizada para introducir el fenómeno de no
 linealidad en el sistema de una red neuronal (NN).

Fuente: 17.1 Función de activación.pptx.pdf, p. 2.


Esta
 propiedad permitirá que la red aprenda patrones más
 complejos.

Fuente: 17.1 Función de activación.pptx.pdf, p. 2.


•Sin funciones de activación una red neuronal es un modelo
 lineal
 • Los datos en el mundo real son no lineales.

Fuente: 17.1 Función de activación.pptx.pdf, p. 2.


• Las funciones de activación permiten aprender relaciones complejas
 no lineales.

Fuente: 17.1 Función de activación.pptx.pdf, p. 2.


•Transforman la señal de entrada de un nodo de una red
 neuronal en una señal de salida con el fin de aprender mapeos
 complejos entre entradas y salidas.

Fuente: 17.1 Función de activación.pptx.pdf, p. 3.


•En un modelo lineal no se realiza ninguna transformación a los
 datos.

Fuente: 17.1 Función de activación.pptx.pdf, p. 3.


### Conceptos clave · extractos del PDF


Qué son las funciones de activación?

Fuente: 17.1 Función de activación.pptx.pdf, p. 2.


Qué son las funciones de activación?

Fuente: 17.1 Función de activación.pptx.pdf, p. 3.


### Definiciones · extractos del PDF


Qué son las funciones de activación?

Fuente: 17.1 Función de activación.pptx.pdf, p. 2.


•Es una función utilizada para introducir el fenómeno de no
 linealidad en el sistema de una red neuronal (NN).

Fuente: 17.1 Función de activación.pptx.pdf, p. 2.


•Sin funciones de activación una red neuronal es un modelo
 lineal
 • Los datos en el mundo real son no lineales.

Fuente: 17.1 Función de activación.pptx.pdf, p. 2.


## Tipos de funciones de activación


### Resumen · extractos del PDF


•Cada función de activación tiene sus propias propiedades y es
 adecuada para determinados casos de uso.

Fuente: 17.1 Función de activación.pptx.pdf, p. 4.


• ReLU – Redes profundas y problemas de regresión
 • Sigmoid – clasificación binaria
 • Softmax – Clasificación multiclase
 • Linear – Modelo lineal

Fuente: 17.1 Función de activación.pptx.pdf, p. 4.


### Conceptos clave · extractos del PDF


Tipos de funciones de activación

Fuente: 17.1 Función de activación.pptx.pdf, p. 4.


### Definiciones · extractos del PDF


•Cada función de activación tiene sus propias propiedades y es
 adecuada para determinados casos de uso.

Fuente: 17.1 Función de activación.pptx.pdf, p. 4.


### Ejemplos · extractos del PDF


•Cada función de activación tiene sus propias propiedades y es
 adecuada para determinados casos de uso.

Fuente: 17.1 Función de activación.pptx.pdf, p. 4.


## ReLU


### Resumen · extractos del PDF


• Devuelve 0 para números
 negativos y para valores
 positivos actúa como una
 función lineal
• Esto significa que no
 modifica la escala de las
 entradas positivas y
 permite que el gradiente
 pase sin cambios durante
 la retropropagación
• Mas común para datos
 complejos

Fuente: 17.1 Función de activación.pptx.pdf, p. 5.


### Conceptos clave · extractos del PDF


ReLU

Fuente: 17.1 Función de activación.pptx.pdf, p. 5.


## Función de


### Resumen · extractos del PDF


• Para una entrada de
 números
 negativos/positivos
 producirá una salida entre
 0 y 1

Fuente: 17.1 Función de activación.pptx.pdf, p. 6.


• A medida que los valores
 de entrada se vuelven
 significativamente
 positivos o negativos, la
 función se satura en 0 o 1

Fuente: 17.1 Función de activación.pptx.pdf, p. 6.


• Ideal para clasificación
 binaria en la capa de
 salida.

Fuente: 17.1 Función de activación.pptx.pdf, p. 6.


### Conceptos clave · extractos del PDF


Función de

Fuente: 17.1 Función de activación.pptx.pdf, p. 6.


## Softmax


### Resumen · extractos del PDF


• Útil para problemas de
 clasificación multiclase

Fuente: 17.1 Función de activación.pptx.pdf, p. 7.


• Opera sobre un vector
 denominado logits que
 representa las distribuciones
 probabilísticas de cada clase
 cuya suma es 1.

Fuente: 17.1 Función de activación.pptx.pdf, p. 7.


### Conceptos clave · extractos del PDF


Softmax

Fuente: 17.1 Función de activación.pptx.pdf, p. 7.


### Definiciones · extractos del PDF


• Opera sobre un vector
 denominado logits que
 representa las distribuciones
 probabilísticas de cada clase
 cuya suma es 1.

Fuente: 17.1 Función de activación.pptx.pdf, p. 7.


## Elección de


### Resumen · extractos del PDF


• Activación sigmoide en la capa de salida.

Fuente: 17.1 Función de activación.pptx.pdf, p. 8.


Reducirá las salidas
 a un valor entre 0 y 1, que representa las probabilidades de las
 dos clases.

Fuente: 17.1 Función de activación.pptx.pdf, p. 8.


Para la clasificación multiclase:la función de
 • Función de activación softmax en la capa de salida.

Fuente: 17.1 Función de activación.pptx.pdf, p. 8.


Dará como
 resultado distribuciones de probabilidad sobre todas las clases.

Fuente: 17.1 Función de activación.pptx.pdf, p. 8.


activación
 adecuada Predicción con datos no lineales:

Fuente: 17.1 Función de activación.pptx.pdf, p. 8.


• Función de activación ReLU en las capas ocultas.

Fuente: 17.1 Función de activación.pptx.pdf, p. 8.


ReLU es la
 función de activación predeterminada más común y suele ser
 una buena elección.

Fuente: 17.1 Función de activación.pptx.pdf, p. 8.


### Conceptos clave · extractos del PDF


Elección de

Fuente: 17.1 Función de activación.pptx.pdf, p. 8.


### Definiciones · extractos del PDF


ReLU es la
 función de activación predeterminada más común y suele ser
 una buena elección.

Fuente: 17.1 Función de activación.pptx.pdf, p. 8.


## Tensorﬂow playground


### Resumen · extractos del PDF


Tensorﬂow playground

 https://playground.tensorflow.org/

Fuente: 17.1 Función de activación.pptx.pdf, p. 9.


### Conceptos clave · extractos del PDF


Tensorﬂow playground

Fuente: 17.1 Función de activación.pptx.pdf, p. 9.


## Conﬁguración en TP


### Resumen · extractos del PDF


•DATA: Circle/Exclusive OR/Espiral
•Función de activación: Linear
•FEATURES: Activa solo x1 y x2 (entradas lineales crudas)
•HIDDEN LAYERS: 4 capas ocultas con 4 neuronas cada una
 (una red profunda estándar)
•LEARNING RATE: 0.03.

Fuente: 17.1 Función de activación.pptx.pdf, p. 10.


•Resultado a observar: La red solo trazará una línea recta
 fija en el mapa.

Fuente: 17.1 Función de activación.pptx.pdf, p. 10.


### Conceptos clave · extractos del PDF


Conﬁguración en TP

Fuente: 17.1 Función de activación.pptx.pdf, p. 10.


## Learning rate


### Resumen · extractos del PDF


•Valor alto estándar: 0.01
•Learning rate alto: El modelo aprende rápidamente, pero corre
 el riesgo de dar "pasos demasiado grandes", saltarse el punto
 óptimo y no lograr estabilizarse (oscilando o empeorando).

Fuente: 17.1 Función de activación.pptx.pdf, p. 11.


• 1.0 – 10.0
•Learning rate bajo: El avance es seguro y preciso, pero el
 entrenamiento puede volverse extremadamente lento o
 quedarse estancado en mínimos locales.

Fuente: 17.1 Función de activación.pptx.pdf, p. 11.


### Conceptos clave · extractos del PDF


Learning rate

Fuente: 17.1 Función de activación.pptx.pdf, p. 11.


### Definiciones · extractos del PDF


• 1.0 – 10.0
•Learning rate bajo: El avance es seguro y preciso, pero el
 entrenamiento puede volverse extremadamente lento o
 quedarse estancado en mínimos locales.

Fuente: 17.1 Función de activación.pptx.pdf, p. 11.


## Demo 2


### Resumen · extractos del PDF


•Cambiar a función de activación sigmoide
•Resultado a observar: La red tarda mucho en aprender, las
 neuronas de la última capa oculta empiezan a cambiar de color,
 pero las de la primera capa (las más cercanas a la entrada) se
 quedan casi transparentes o estáticas por cientos de épocas.

Fuente: 17.1 Función de activación.pptx.pdf, p. 12.


### Conceptos clave · extractos del PDF


Demo 2

Fuente: 17.1 Función de activación.pptx.pdf, p. 12.


## Demo 3


### Resumen · extractos del PDF


•Cambiar a ReLU
•Resultado a observar: En cuestión de menos de 100-200
 épocas, observara cómo el fondo blanco empieza a retorcerse
 de forma agresiva, adaptándose perfectamente a la forma de la
 espiral.

Fuente: 17.1 Función de activación.pptx.pdf, p. 13.


### Conceptos clave · extractos del PDF


Demo 3

Fuente: 17.1 Función de activación.pptx.pdf, p. 13.


## 17.1 Función de activación.pptx


### Resumen · extractos del PDF


Ejemplo

Fuente: 17.1 Función de activación.pptx.pdf, p. 14.


### Conceptos clave · extractos del PDF


17.1 Función de activación.pptx

Fuente: 17.1 Función de activación.pptx.pdf, p. 14.


### Ejemplos · extractos del PDF


Ejemplo

Fuente: 17.1 Función de activación.pptx.pdf, p. 14.


## Clasificación


### Resumen · extractos del PDF


Clasificación

 binaria y multiclase

Fuente: 18.1 Clasificación.pptx.pdf, p. 1.


### Conceptos clave · extractos del PDF


Clasificación

Fuente: 18.1 Clasificación.pptx.pdf, p. 1.


## Introducción


### Resumen · extractos del PDF


• Regresión → predice un valor numérico
 • Ejemplo: precio de una casa = Q350,000

Fuente: 18.1 Clasificación.pptx.pdf, p. 2.


• Clasificación binaria → predice entre 2 clases, Ejemplo:
 • Spam / No Spam
 • Enfermo / No enfermo
 • Compra / No compra

Fuente: 18.1 Clasificación.pptx.pdf, p. 2.


• Clasificación multiclase → predice entre varias clases, Ejemplo:
 • Tipo de flor: Rosa / Tulipán / Margarita
 • IDS: DOS, DDOS, 0-day
 • Dígito: 0 al 9

Fuente: 18.1 Clasificación.pptx.pdf, p. 2.


### Conceptos clave · extractos del PDF


Introducción

Fuente: 18.1 Clasificación.pptx.pdf, p. 2.


### Ejemplos · extractos del PDF


• Regresión → predice un valor numérico
 • Ejemplo: precio de una casa = Q350,000

Fuente: 18.1 Clasificación.pptx.pdf, p. 2.


• Clasificación binaria → predice entre 2 clases, Ejemplo:
 • Spam / No Spam
 • Enfermo / No enfermo
 • Compra / No compra

Fuente: 18.1 Clasificación.pptx.pdf, p. 2.


• Clasificación multiclase → predice entre varias clases, Ejemplo:
 • Tipo de flor: Rosa / Tulipán / Margarita
 • IDS: DOS, DDOS, 0-day
 • Dígito: 0 al 9

Fuente: 18.1 Clasificación.pptx.pdf, p. 2.


### Fórmulas o comandos · extractos del PDF


• Regresión → predice un valor numérico
 • Ejemplo: precio de una casa = Q350,000

Fuente: 18.1 Clasificación.pptx.pdf, p. 2.


## Clasificación binaria


### Resumen · extractos del PDF


•Función de activación: Sigmoid
 • Produce valores entre 0 y 1
 • Se interpreta como probabilidad
 • Umbral de decisión: (threshold)
 • Si salida >= 0.5 → clase 1
 Si salida < 0.5 → clase 0
•Función de perdida: Binary crossentropy
 • Ya no se utiliza: mse

Fuente: 18.1 Clasificación.pptx.pdf, p. 3.


### Conceptos clave · extractos del PDF


Clasificación binaria

Fuente: 18.1 Clasificación.pptx.pdf, p. 3.


### Fórmulas o comandos · extractos del PDF


•Función de activación: Sigmoid
 • Produce valores entre 0 y 1
 • Se interpreta como probabilidad
 • Umbral de decisión: (threshold)
 • Si salida >= 0.5 → clase 1
 Si salida < 0.5 → clase 0
•Función de perdida: Binary crossentropy
 • Ya no se utiliza: mse

Fuente: 18.1 Clasificación.pptx.pdf, p. 3.


## Métricas de clasificación


### Resumen · extractos del PDF


•Son medidas que nos permiten evaluar qué tan bien está funcionando
 un modelo cuando predice categorías o clases.

Fuente: 18.1 Clasificación.pptx.pdf, p. 4.


•Responder preguntas como:
 • ¿Cuántas veces acertó?

Fuente: 18.1 Clasificación.pptx.pdf, p. 4.


• ¿Qué tipo de errores está cometiendo?

Fuente: 18.1 Clasificación.pptx.pdf, p. 4.


• ¿Está confundiendo una clase con otra?

Fuente: 18.1 Clasificación.pptx.pdf, p. 4.


• ¿Es bueno detectando los casos importantes?

Fuente: 18.1 Clasificación.pptx.pdf, p. 4.


### Conceptos clave · extractos del PDF


Métricas de clasificación

Fuente: 18.1 Clasificación.pptx.pdf, p. 4.


### Definiciones · extractos del PDF


•Son medidas que nos permiten evaluar qué tan bien está funcionando
 un modelo cuando predice categorías o clases.

Fuente: 18.1 Clasificación.pptx.pdf, p. 4.


• ¿Es bueno detectando los casos importantes?

Fuente: 18.1 Clasificación.pptx.pdf, p. 4.


### Ejemplos · extractos del PDF


• ¿Es bueno detectando los casos importantes?

Fuente: 18.1 Clasificación.pptx.pdf, p. 4.


### Fórmulas o comandos · extractos del PDF


• ¿Es bueno detectando los casos importantes?

Fuente: 18.1 Clasificación.pptx.pdf, p. 4.


## Accuracy (exactitud)


### Resumen · extractos del PDF


•De todas las clasificaciones cuantas fueron correctas

Fuente: 18.1 Clasificación.pptx.pdf, p. 5.


Caso Real Predicho•Ejemplo:
 1 Sí Sí
 2 No No
 3 Sí Sí
 4 No Sí

Fuente: 18.1 Clasificación.pptx.pdf, p. 5.


• Correctos: 3
 • Total: 4
 • Accuracy: 75%

Fuente: 18.1 Clasificación.pptx.pdf, p. 5.


### Conceptos clave · extractos del PDF


Accuracy (exactitud)

Fuente: 18.1 Clasificación.pptx.pdf, p. 5.


### Ejemplos · extractos del PDF


Caso Real Predicho•Ejemplo:
 1 Sí Sí
 2 No No
 3 Sí Sí
 4 No Sí

Fuente: 18.1 Clasificación.pptx.pdf, p. 5.


## Problema del accuracy


### Resumen · extractos del PDF


• Detector de fraude:
 • 95 transacciones normales
 • 5 fraudulentas

Fuente: 18.1 Clasificación.pptx.pdf, p. 6.


• El modelo predice: Todo es normal

Fuente: 18.1 Clasificación.pptx.pdf, p. 6.


• Con accuracy:
 • Acierta 95
 • Falla 5

Fuente: 18.1 Clasificación.pptx.pdf, p. 6.


• Parece excelente… pero no detectó ningún fraude.

Fuente: 18.1 Clasificación.pptx.pdf, p. 6.


### Conceptos clave · extractos del PDF


Problema del accuracy

Fuente: 18.1 Clasificación.pptx.pdf, p. 6.


### Definiciones · extractos del PDF


• El modelo predice: Todo es normal

Fuente: 18.1 Clasificación.pptx.pdf, p. 6.


## Matriz de confusión


### Resumen · extractos del PDF


•Aquí se comparan:
 • Lo que realmente era
 • Lo que el modelo dijo

Fuente: 18.1 Clasificación.pptx.pdf, p. 7.


Predijo Sí Predijo No
 TP (True Positive): FN (False Negative):
 Real Sí Positivo y lo detecto No era positivo, pero
 bien dijo que sí.

Fuente: 18.1 Clasificación.pptx.pdf, p. 7.


FP (False Positive): Sí
 TN (True Negative):
 Real No era positivo, pero dijo Era negativo y acertó.

Fuente: 18.1 Clasificación.pptx.pdf, p. 7.


### Conceptos clave · extractos del PDF


Matriz de confusión

Fuente: 18.1 Clasificación.pptx.pdf, p. 7.


### Comparaciones · extractos del PDF


•Aquí se comparan:
 • Lo que realmente era
 • Lo que el modelo dijo

Fuente: 18.1 Clasificación.pptx.pdf, p. 7.


## Precision


### Resumen · extractos del PDF


• De todos los que el modelo dijo que eran positivos… ¿cuántos realmente lo
 eran?

Fuente: 18.1 Clasificación.pptx.pdf, p. 8.


• Ejemplo
• Modelo detectó 10 correos como spam:
 • 8 sí eran spam
 • 2 no eran spam

Fuente: 18.1 Clasificación.pptx.pdf, p. 8.


• Entonces:
 • Precision = 8 / 10 = 80%

Fuente: 18.1 Clasificación.pptx.pdf, p. 8.


### Conceptos clave · extractos del PDF


Precision

Fuente: 18.1 Clasificación.pptx.pdf, p. 8.


### Ejemplos · extractos del PDF


• Ejemplo
• Modelo detectó 10 correos como spam:
 • 8 sí eran spam
 • 2 no eran spam

Fuente: 18.1 Clasificación.pptx.pdf, p. 8.


### Fórmulas o comandos · extractos del PDF


• Entonces:
 • Precision = 8 / 10 = 80%

Fuente: 18.1 Clasificación.pptx.pdf, p. 8.


## Contextos donde cada métrica importa mas


### Resumen · extractos del PDF


Contextos donde cada métrica importa mas

Fuente: 18.1 Clasificación.pptx.pdf, p. 9.


### Conceptos clave · extractos del PDF


Contextos donde cada métrica importa mas

Fuente: 18.1 Clasificación.pptx.pdf, p. 9.


### Fórmulas o comandos · extractos del PDF


Contextos donde cada métrica importa mas

Fuente: 18.1 Clasificación.pptx.pdf, p. 9.


## Clasiﬁcación de imágenes


### Resumen · extractos del PDF


Clasiﬁcación de imágenes

Fuente: 19.1 Clasificación de imagenes.pptx.pdf, p. 1.


### Conceptos clave · extractos del PDF


Clasiﬁcación de imágenes

Fuente: 19.1 Clasificación de imagenes.pptx.pdf, p. 1.


## Visión


### Resumen · extractos del PDF


Visión
 Aprendizaje supervisado:computarizad
 Se utilizan datos de
 entrenamiento etiquetados a

Fuente: 19.1 Clasificación de imagenes.pptx.pdf, p. 2.


### Conceptos clave · extractos del PDF


Visión

Fuente: 19.1 Clasificación de imagenes.pptx.pdf, p. 2.


## MNIST dataset


### Resumen · extractos del PDF


• Utilizaremos el conjunto de datos MNIST

Fuente: 19.1 Clasificación de imagenes.pptx.pdf, p. 3.


• El NIST produjo la base de datos Fashion
 MNIST, es una gran base de datos de
 imágenes de ropa utilizados para entrenar
 sistemas de procesamiento de imágenes.

Fuente: 19.1 Clasificación de imagenes.pptx.pdf, p. 3.


• MNIST esta incluido en Tensorflow

Fuente: 19.1 Clasificación de imagenes.pptx.pdf, p. 3.


### Conceptos clave · extractos del PDF


MNIST dataset

Fuente: 19.1 Clasificación de imagenes.pptx.pdf, p. 3.


### Definiciones · extractos del PDF


• El NIST produjo la base de datos Fashion
 MNIST, es una gran base de datos de
 imágenes de ropa utilizados para entrenar
 sistemas de procesamiento de imágenes.

Fuente: 19.1 Clasificación de imagenes.pptx.pdf, p. 3.


### Comprender y practicar · extractos del PDF


• El NIST produjo la base de datos Fashion
 MNIST, es una gran base de datos de
 imágenes de ropa utilizados para entrenar
 sistemas de procesamiento de imágenes.

Fuente: 19.1 Clasificación de imagenes.pptx.pdf, p. 3.


## Fashion MNIST


### Resumen · extractos del PDF


• Es una BD que posee 70,000 imágenes
 (60,000 entrenamiento y 10,000 test)

Fuente: 19.1 Clasificación de imagenes.pptx.pdf, p. 4.


• Es decir que existen 7,000 ejemplos de
 cada categoría incluidos zapatos.

Fuente: 19.1 Clasificación de imagenes.pptx.pdf, p. 4.


### Conceptos clave · extractos del PDF


Fashion MNIST

Fuente: 19.1 Clasificación de imagenes.pptx.pdf, p. 4.


### Definiciones · extractos del PDF


• Es una BD que posee 70,000 imágenes
 (60,000 entrenamiento y 10,000 test)

Fuente: 19.1 Clasificación de imagenes.pptx.pdf, p. 4.


• Es decir que existen 7,000 ejemplos de
 cada categoría incluidos zapatos.

Fuente: 19.1 Clasificación de imagenes.pptx.pdf, p. 4.


### Ejemplos · extractos del PDF


• Es decir que existen 7,000 ejemplos de
 cada categoría incluidos zapatos.

Fuente: 19.1 Clasificación de imagenes.pptx.pdf, p. 4.


## Formato de cada


### Resumen · extractos del PDF


•Las imágenes de MNIST son
 imágenes de 28x28 pixeles
•Imágenes pequeñas serán
 procesadas por una
 computadora (neurona
 artificial) mas rápido
•Cada pixel puede ser
 representado en valores desde
 cero hasta 250 (1 byte por
 pixel).

Fuente: 19.1 Clasificación de imagenes.pptx.pdf, p. 5.


### Conceptos clave · extractos del PDF


Formato de cada

Fuente: 19.1 Clasificación de imagenes.pptx.pdf, p. 5.


### Definiciones · extractos del PDF


•Las imágenes de MNIST son
 imágenes de 28x28 pixeles
•Imágenes pequeñas serán
 procesadas por una
 computadora (neurona
 artificial) mas rápido
•Cada pixel puede ser
 representado en valores desde
 cero hasta 250 (1 byte por
 pixel).

Fuente: 19.1 Clasificación de imagenes.pptx.pdf, p. 5.


## Entrenamiento


### Resumen · extractos del PDF


• Se utilizara la función de perdida
 parse_categorical_crossentropy para
 clasificacion de imagenes y la funcion de
 activacion: Softmax

Fuente: 19.1 Clasificación de imagenes.pptx.pdf, p. 7.


### Conceptos clave · extractos del PDF


Entrenamiento

Fuente: 19.1 Clasificación de imagenes.pptx.pdf, p. 7.


## Objetivo


### Resumen · extractos del PDF


LABORATORIO
Análisis de una CNN
Prof.

Fuente: 19.3 Laboratorio analisis de una CNN.doc.pdf, p. 1.


Objetivo
Comprender las imágenes generadas en una estructura neuronal CNN, y como cada capa
convolucional transforma la imagen de entrada, como se observan los mapas de características
(feature maps) y su tamaño a medida que se avanza en la red.

Fuente: 19.3 Laboratorio analisis de una CNN.doc.pdf, p. 1.


Actividad 1: Mapas de características
Ejecutar el código que se encuentran en el sitio del curso denominado como: 1.

Fuente: 19.3 Laboratorio analisis de una CNN.doc.pdf, p. 1.


mapa de
características bloque de primera convolución

Fuente: 19.3 Laboratorio analisis de una CNN.doc.pdf, p. 1.


●​ El primer código muestra los mapas de características del primer bloque convolucional
 ●​ El segundo código muestra los mapas de características del segundo bloque
 convolucional

Fuente: 19.3 Laboratorio analisis de una CNN.doc.pdf, p. 1.


1.​ Para el primer código cambie la cantidad de mapas generados, utilice los siguientes
 valores: 32, 64, 128, 256 en la siguiente linea de codigo:
 x = layers.Conv2D(32, (5, 5), activation='relu', name='conv_1')(inputs)
 #LINEA A MODIFICAR VALORES

Fuente: 19.3 Laboratorio analisis de una CNN.doc.pdf, p. 1.


2.​ Responda: a) Que cantidad de imágenes son generadas en cada caso, b) describa que
 observa en el cambio de las imágenes
 3.​ Utilice 32 mapas generados y a continuación modifique los valores de (5,5) a los
 siguientes valores: (4,4) – (3,3) – (2,2) – (1,1) y explique que cambios observa en las
 imágenes generadas.

Fuente: 19.3 Laboratorio analisis de una CNN.doc.pdf, p. 1.


### Conceptos clave · extractos del PDF


Objetivo

Fuente: 19.3 Laboratorio analisis de una CNN.doc.pdf, p. 1.


Objetivo

Fuente: 20.4 Ejercicio de repaso redes neuronales.docx.pdf, p. 1.


### Definiciones · extractos del PDF


2.​ Responda: a) Que cantidad de imágenes son generadas en cada caso, b) describa que
 observa en el cambio de las imágenes
 3.​ Utilice 32 mapas generados y a continuación modifique los valores de (5,5) a los
 siguientes valores: (4,4) – (3,3) – (2,2) – (1,1) y explique que cambios observa en las
 imágenes generadas.

Fuente: 19.3 Laboratorio analisis de una CNN.doc.pdf, p. 1.


Actividad 2: model.summary
1.​ El método model.summary en Keras de Tensorflow es una función que imprime un resumen
 de la arquitectura de la red neuronal definida.

Fuente: 19.3 Laboratorio analisis de una CNN.doc.pdf, p. 1.


Investigue a que se refiere la columna Param
 #

Fuente: 19.3 Laboratorio analisis de una CNN.doc.pdf, p. 1.


Actividad 1: Responder las siguientes preguntas
 1.​ Estructura neuronal básica con Keras: ¿Cómo se define y configura una arquitectura
 secuencial utilizando tf.keras.Sequential y capas Dense, y qué parámetros clave deben
 establecerse al especificar la dimensión de entrada (input_shape) y el número de
 neuronas por capa?

Fuente: 20.4 Ejercicio de repaso redes neuronales.docx.pdf, p. 1.


3.​ Predicción (Regresión numérica): Al diseñar una red neuronal orientada a la estimación
 de valores numéricos continuos, ¿qué configuración particular debe llevar la capa de
 salida (número de neuronas y activación) y qué función de pérdida es la adecuada para
 medir el margen de error?

Fuente: 20.4 Ejercicio de repaso redes neuronales.docx.pdf, p. 1.


4.​ Clasificación binaria: ¿Por qué en un problema de clasificación binaria es estándar
 utilizar la función de activación Sigmoid en la neurona de salida junto con la función de
 pérdida binary_crossentropy, y cómo se interpreta la probabilidad emitida por el
 modelo?

Fuente: 20.4 Ejercicio de repaso redes neuronales.docx.pdf, p. 1.


7.​ Codificación one-hot (one-hot encoding): ¿En qué consiste la técnica de codificación
 one-hot para representar etiquetas categóricas, qué métodos ofrece TensorFlow/Keras
 para aplicarla y en qué casos es preferible frente a un esquema de enteros?

Fuente: 20.4 Ejercicio de repaso redes neuronales.docx.pdf, p. 1.


### Procedimientos · extractos del PDF


1.​ Para el primer código cambie la cantidad de mapas generados, utilice los siguientes
 valores: 32, 64, 128, 256 en la siguiente linea de codigo:
 x = layers.Conv2D(32, (5, 5), activation='relu', name='conv_1')(inputs)
 #LINEA A MODIFICAR VALORES

Fuente: 19.3 Laboratorio analisis de una CNN.doc.pdf, p. 1.


2.​ Responda: a) Que cantidad de imágenes son generadas en cada caso, b) describa que
 observa en el cambio de las imágenes
 3.​ Utilice 32 mapas generados y a continuación modifique los valores de (5,5) a los
 siguientes valores: (4,4) – (3,3) – (2,2) – (1,1) y explique que cambios observa en las
 imágenes generadas.

Fuente: 19.3 Laboratorio analisis de una CNN.doc.pdf, p. 1.


Utilice la misma línea de código indicada en el paso 1.

Fuente: 19.3 Laboratorio analisis de una CNN.doc.pdf, p. 1.


4.​ Las imágenes generadas corresponden a la salida de la primera convolución,

Fuente: 19.3 Laboratorio analisis de una CNN.doc.pdf, p. 1.


Actividad 2: model.summary
1.​ El método model.summary en Keras de Tensorflow es una función que imprime un resumen
 de la arquitectura de la red neuronal definida.

Fuente: 19.3 Laboratorio analisis de una CNN.doc.pdf, p. 1.


2.​ Explique que hace la siguiente línea de código:
 layers.MaxPooling2D((2, 2))

Fuente: 19.3 Laboratorio analisis de una CNN.doc.pdf, p. 1.


2.​ Funciones de activación en capas ocultas: ¿De qué manera influye la elección de una
 función de activación (como ReLU, Leaky ReLU o Tanh) en las capas internas sobre la
 capacidad del modelo para aprender relaciones no lineales y evitar el desvanecimiento
 del gradiente?

Fuente: 20.4 Ejercicio de repaso redes neuronales.docx.pdf, p. 1.


### Ejemplos · extractos del PDF


2.​ Responda: a) Que cantidad de imágenes son generadas en cada caso, b) describa que
 observa en el cambio de las imágenes
 3.​ Utilice 32 mapas generados y a continuación modifique los valores de (5,5) a los
 siguientes valores: (4,4) – (3,3) – (2,2) – (1,1) y explique que cambios observa en las
 imágenes generadas.

Fuente: 19.3 Laboratorio analisis de una CNN.doc.pdf, p. 1.


7.​ Codificación one-hot (one-hot encoding): ¿En qué consiste la técnica de codificación
 one-hot para representar etiquetas categóricas, qué métodos ofrece TensorFlow/Keras
 para aplicarla y en qué casos es preferible frente a un esquema de enteros?

Fuente: 20.4 Ejercicio de repaso redes neuronales.docx.pdf, p. 1.


### Fórmulas o comandos · extractos del PDF


1.​ Para el primer código cambie la cantidad de mapas generados, utilice los siguientes
 valores: 32, 64, 128, 256 en la siguiente linea de codigo:
 x = layers.Conv2D(32, (5, 5), activation='relu', name='conv_1')(inputs)
 #LINEA A MODIFICAR VALORES

Fuente: 19.3 Laboratorio analisis de una CNN.doc.pdf, p. 1.


Actividad 4: Segunda convolucion
 1.​ Explique que hace la siguiente línea de código:
 layers.Conv2D(64, (1, 1), activation='relu')

Fuente: 19.3 Laboratorio analisis de una CNN.doc.pdf, p. 1.


## Redes neuronales


### Resumen · extractos del PDF


Redes neuronales
 convolucionales

Fuente: 20.2 Redes neuronales convolucionales.pptx.pdf, p. 1.


### Conceptos clave · extractos del PDF


Redes neuronales

Fuente: 20.2 Redes neuronales convolucionales.pptx.pdf, p. 1.


## CIFAR Dataset


### Resumen · extractos del PDF


Contiene:
•60,000 imágenes (50k training)
•tamaño: 32×32 píxeles
 (32,32,3)
•imágenes a color (3 canales)
 • rojo, verde, azul
•10 clases
•6,000 imágenes por clase

Fuente: 20.2 Redes neuronales convolucionales.pptx.pdf, p. 2.


### Conceptos clave · extractos del PDF


CIFAR Dataset

Fuente: 20.2 Redes neuronales convolucionales.pptx.pdf, p. 2.


## Tipos de redes neuronales


### Resumen · extractos del PDF


•Redes neuronales artificiales básicas (ANN)
 • Predicción de precios y clasificación
•Redes neuronales convolucionales (CNN)
 • Clasificación de imágenes
•Redes neuronales recurrentes (RNN)
 • Texto y audio
•Transformer
 • GPT-4.0, deepseek-R1, etc

Fuente: 20.2 Redes neuronales convolucionales.pptx.pdf, p. 3.


### Conceptos clave · extractos del PDF


Tipos de redes neuronales

Fuente: 20.2 Redes neuronales convolucionales.pptx.pdf, p. 3.


## Redes neuronales convolucionales (CNN)


### Resumen · extractos del PDF


Redes neuronales convolucionales (CNN)

Fuente: 20.2 Redes neuronales convolucionales.pptx.pdf, p. 4.


•Modelo de Deep Learning ideal para datos visuales tales como
 imágenes o videos, y algunas veces audios.

Fuente: 20.2 Redes neuronales convolucionales.pptx.pdf, p. 4.


•Diseñadas para procesar datos con una estructura en forma de
 cuadricula como las imágenes.

Fuente: 20.2 Redes neuronales convolucionales.pptx.pdf, p. 4.


•Permiten extraer características relevantes como bordes,
 texturas o formas.

Fuente: 20.2 Redes neuronales convolucionales.pptx.pdf, p. 4.


• Un grupo de pixeles puede representar parte de un borde o forma.

Fuente: 20.2 Redes neuronales convolucionales.pptx.pdf, p. 4.


• Las redes neuronales tradicionales tratan cada pixel como una
 característica independiente.

Fuente: 20.2 Redes neuronales convolucionales.pptx.pdf, p. 4.


Una convolución es una operación matemática usada para detectar patrones en datos,
especialmente imágenes.

Fuente: 20.2 Redes neuronales convolucionales.pptx.pdf, p. 5.


### Conceptos clave · extractos del PDF


Redes neuronales convolucionales (CNN)

Fuente: 20.2 Redes neuronales convolucionales.pptx.pdf, p. 4.


Redes neuronales convolucionales (CNN)

Fuente: 20.2 Redes neuronales convolucionales.pptx.pdf, p. 5.


Redes neuronales convolucionales (CNN)

Fuente: Preguntas basicas redes neuronales convolucionales.pdf, p. 1.


### Definiciones · extractos del PDF


Una convolución es una operación matemática usada para detectar patrones en datos,
especialmente imágenes.

Fuente: 20.2 Redes neuronales convolucionales.pptx.pdf, p. 5.


La idea simple es:
• Tomar una pequeña matriz llamada kernel o filtro.

Fuente: 20.2 Redes neuronales convolucionales.pptx.pdf, p. 5.


¿Qué es una red neuronal convolucional y para qué se utiliza

Fuente: Preguntas basicas redes neuronales convolucionales.pdf, p. 1.


Es un tipo de inteligencia artificial que aprende a reconocer imágenes.

Fuente: Preguntas basicas redes neuronales convolucionales.pdf, p. 1.


los números 2, 5, 8 y 3, selecciona el 8 porque es el mayor.

Fuente: Preguntas basicas redes neuronales convolucionales.pdf, p. 1.


### Ejemplos · extractos del PDF


Por ejemplo, un filtro puede detectar:
• bordes
• líneas
• texturas
• esquinas

Fuente: 20.2 Redes neuronales convolucionales.pptx.pdf, p. 5.


### Fórmulas o comandos · extractos del PDF


Analiza una imagen por partes para encontrar detalles importantes, como líneas, bordes,

Fuente: Preguntas basicas redes neuronales convolucionales.pdf, p. 1.


sin perder los detalles más importantes.

Fuente: Preguntas basicas redes neuronales convolucionales.pdf, p. 1.


## Componentes


### Resumen · extractos del PDF


Capa completamente conectada
 (fully connected)
 5.

Fuente: 20.2 Redes neuronales convolucionales.pptx.pdf, p. 6.


Posee dos fases: Extracción de características y
 clasificación

Fuente: 20.2 Redes neuronales convolucionales.pptx.pdf, p. 6.


Capa de activación
 • Introduce no linealidad, normalmente ReLU

Fuente: 20.2 Redes neuronales convolucionales.pptx.pdf, p. 14.


Capa completamente conectada (fully connected)
 • Conecta las características extraídas en capas anteriores con las
 salidas finales
 • Aquí se toma la decisión de clasificación

Fuente: 20.2 Redes neuronales convolucionales.pptx.pdf, p. 14.


Capa de salida
 • Utiliza funciones Softmax para convertir las activaciones en
 probabilidades de pertenencia a cada clase.

Fuente: 20.2 Redes neuronales convolucionales.pptx.pdf, p. 14.


Componentes

Fuente: 20.2 Redes neuronales convolucionales.pptx.pdf, p. 15.


### Conceptos clave · extractos del PDF


Componentes

Fuente: 20.2 Redes neuronales convolucionales.pptx.pdf, p. 6.


Componentes

Fuente: 20.2 Redes neuronales convolucionales.pptx.pdf, p. 14.


Componentes

Fuente: 20.2 Redes neuronales convolucionales.pptx.pdf, p. 15.


## Componentes CNN


### Resumen · extractos del PDF


Capa convolucional
 • Núcleo de la CNN
 • Aplica filtros que generan un mapa de características para resaltar un
 tipo especifico de patrón visual como borde, textura, forma, etc)

Fuente: 20.2 Redes neuronales convolucionales.pptx.pdf, p. 7.


Capa de agrupamiento (pooling)
 • Reduce el tamaño de los mapas disminuyendo el numero de
 parámetros para evitar sobreajuste.

Fuente: 20.2 Redes neuronales convolucionales.pptx.pdf, p. 11.


### Conceptos clave · extractos del PDF


Componentes CNN

Fuente: 20.2 Redes neuronales convolucionales.pptx.pdf, p. 7.


Componentes CNN

Fuente: 20.2 Redes neuronales convolucionales.pptx.pdf, p. 11.


## Capa convolucional


### Resumen · extractos del PDF


Conv2D(32) → Conv2D(64) → Conv2D(64)
model = models.Sequential([ • 32 filtros para captar caracteristicas basicas, generando
 32 mapas de caracteristicas basicas.

Fuente: 20.2 Redes neuronales convolucionales.pptx.pdf, p. 8.


# Bloque 1
 • 64 filtros para detectar combinaciones de rasgos (por
 layers.Conv2D(32, (3, 3), activation='relu', input_shape=(32, 32, ejemplo: formas y ojos)
3)), • 64 filtros para refinar y detectar patrones mas complejos

Fuente: 20.2 Redes neuronales convolucionales.pptx.pdf, p. 8.


layers.MaxPooling2D((2, 2)),
 Consideraciones:

Fuente: 20.2 Redes neuronales convolucionales.pptx.pdf, p. 8.


• Más filtros = más capacidad de aprendizaje,
 # Bloque 2 • (pero) también más parámetros y más tiempo de entrenamiento.

Fuente: 20.2 Redes neuronales convolucionales.pptx.pdf, p. 8.


layers.Conv2D(64, (3, 3), activation='relu'),
 • Demasiados filtros pueden provocar sobreajuste,
 layers.MaxPooling2D((2, 2)), especialmente si el dataset es pequeño.

Fuente: 20.2 Redes neuronales convolucionales.pptx.pdf, p. 8.


• Pocos filtros pueden hacer que la red no capture suficiente
 # Bloque 3 información visual.

Fuente: 20.2 Redes neuronales convolucionales.pptx.pdf, p. 8.


layers.Conv2D(64, (3, 3), activation='relu'),
 • En la práctica se eligen valores potencias de 2 (16, 32, 64,
 128, …) por eficiencia en GPU.

Fuente: 20.2 Redes neuronales convolucionales.pptx.pdf, p. 8.


### Conceptos clave · extractos del PDF


Capa convolucional

Fuente: 20.2 Redes neuronales convolucionales.pptx.pdf, p. 8.


### Definiciones · extractos del PDF


layers.Conv2D(64, (3, 3), activation='relu'),
 • Demasiados filtros pueden provocar sobreajuste,
 layers.MaxPooling2D((2, 2)), especialmente si el dataset es pequeño.

Fuente: 20.2 Redes neuronales convolucionales.pptx.pdf, p. 8.


### Procedimientos · extractos del PDF


# Bloque 1
 • 64 filtros para detectar combinaciones de rasgos (por
 layers.Conv2D(32, (3, 3), activation='relu', input_shape=(32, 32, ejemplo: formas y ojos)
3)), • 64 filtros para refinar y detectar patrones mas complejos

Fuente: 20.2 Redes neuronales convolucionales.pptx.pdf, p. 8.


### Ejemplos · extractos del PDF


# Bloque 1
 • 64 filtros para detectar combinaciones de rasgos (por
 layers.Conv2D(32, (3, 3), activation='relu', input_shape=(32, 32, ejemplo: formas y ojos)
3)), • 64 filtros para refinar y detectar patrones mas complejos

Fuente: 20.2 Redes neuronales convolucionales.pptx.pdf, p. 8.


### Fórmulas o comandos · extractos del PDF


Conv2D(32) → Conv2D(64) → Conv2D(64)
model = models.Sequential([ • 32 filtros para captar caracteristicas basicas, generando
 32 mapas de caracteristicas basicas.

Fuente: 20.2 Redes neuronales convolucionales.pptx.pdf, p. 8.


# Bloque 1
 • 64 filtros para detectar combinaciones de rasgos (por
 layers.Conv2D(32, (3, 3), activation='relu', input_shape=(32, 32, ejemplo: formas y ojos)
3)), • 64 filtros para refinar y detectar patrones mas complejos

Fuente: 20.2 Redes neuronales convolucionales.pptx.pdf, p. 8.


• Más filtros = más capacidad de aprendizaje,
 # Bloque 2 • (pero) también más parámetros y más tiempo de entrenamiento.

Fuente: 20.2 Redes neuronales convolucionales.pptx.pdf, p. 8.


layers.Conv2D(64, (3, 3), activation='relu'),
 • Demasiados filtros pueden provocar sobreajuste,
 layers.MaxPooling2D((2, 2)), especialmente si el dataset es pequeño.

Fuente: 20.2 Redes neuronales convolucionales.pptx.pdf, p. 8.


layers.Conv2D(64, (3, 3), activation='relu'),
 • En la práctica se eligen valores potencias de 2 (16, 32, 64,
 128, …) por eficiencia en GPU.

Fuente: 20.2 Redes neuronales convolucionales.pptx.pdf, p. 8.


## Ejemplo de la salida del bloque uno, que


### Resumen · extractos del PDF


Ejemplo de la salida del bloque uno, que
crea 32 mapas de características

Fuente: 20.2 Redes neuronales convolucionales.pptx.pdf, p. 9.


### Conceptos clave · extractos del PDF


Ejemplo de la salida del bloque uno, que

Fuente: 20.2 Redes neuronales convolucionales.pptx.pdf, p. 9.


### Ejemplos · extractos del PDF


Ejemplo de la salida del bloque uno, que
crea 32 mapas de características

Fuente: 20.2 Redes neuronales convolucionales.pptx.pdf, p. 9.


## Como decidir cuantos ﬁltros utilizar


### Resumen · extractos del PDF


Como decidir cuantos ﬁltros utilizar

Fuente: 20.2 Redes neuronales convolucionales.pptx.pdf, p. 10.


Filtros
 Capa Propósito Observación
 típicos

Fuente: 20.2 Redes neuronales convolucionales.pptx.pdf, p. 10.


bordes, formas Primer nivel de 1ª capa 16–32Detectar
 simples detalle

Fuente: 20.2 Redes neuronales convolucionales.pptx.pdf, p. 10.


patrones más 2ª capa 32–64Detectar Más abstracción
 complejos (ojos, texturas)

Fuente: 20.2 Redes neuronales convolucionales.pptx.pdf, p. 10.


combinaciones de Aumenta la 3ª capa 64–128Detectar
 patrones (rostros, objetos) profundidad
 Detectar estructuras
 Solo útil en
 4ª o más 128–512 completas (perro, auto,
 redes grandes
 avión)

Fuente: 20.2 Redes neuronales convolucionales.pptx.pdf, p. 10.


### Conceptos clave · extractos del PDF


Como decidir cuantos ﬁltros utilizar

Fuente: 20.2 Redes neuronales convolucionales.pptx.pdf, p. 10.


## Ejemplo capa de


### Resumen · extractos del PDF


Ejemplo capa de
 agrupamiento
 (pooling)

Fuente: 20.2 Redes neuronales convolucionales.pptx.pdf, p. 12.


### Conceptos clave · extractos del PDF


Ejemplo capa de

Fuente: 20.2 Redes neuronales convolucionales.pptx.pdf, p. 12.


### Ejemplos · extractos del PDF


Ejemplo capa de
 agrupamiento
 (pooling)

Fuente: 20.2 Redes neuronales convolucionales.pptx.pdf, p. 12.


## Tipos de pooling


### Resumen · extractos del PDF


• Max Pooling
 • Toma el valor máximo de cada ventana (2,2)
 • Conserva la característica mas intensa, hace que la red enfatice bordes,
 rasgos mas distintivos y patrones muy marcados.

Fuente: 20.2 Redes neuronales convolucionales.pptx.pdf, p. 13.


• Average Pooling
 • Calcula el valor promedio de la ventana
 • Matiene el contexto global de la imagen, sin enfatizar puntos fuertes, útil al
 analizar imágenes medicas, donde las diferencias son muy sutiles
• Min Pooling
 • Toma el valor mínimo
 • No es común utilizarlo, solo en casos especiales donde el valor mas bajo
 tiene importancia (detección de sombras o regiones oscuras)

Fuente: 20.2 Redes neuronales convolucionales.pptx.pdf, p. 13.


### Conceptos clave · extractos del PDF


Tipos de pooling

Fuente: 20.2 Redes neuronales convolucionales.pptx.pdf, p. 13.


### Definiciones · extractos del PDF


• Average Pooling
 • Calcula el valor promedio de la ventana
 • Matiene el contexto global de la imagen, sin enfatizar puntos fuertes, útil al
 analizar imágenes medicas, donde las diferencias son muy sutiles
• Min Pooling
 • Toma el valor mínimo
 • No es común utilizarlo, solo en casos especiales donde el valor mas bajo
 tiene importancia (detección de sombras o regiones oscuras)

Fuente: 20.2 Redes neuronales convolucionales.pptx.pdf, p. 13.


### Ejemplos · extractos del PDF


• Average Pooling
 • Calcula el valor promedio de la ventana
 • Matiene el contexto global de la imagen, sin enfatizar puntos fuertes, útil al
 analizar imágenes medicas, donde las diferencias son muy sutiles
• Min Pooling
 • Toma el valor mínimo
 • No es común utilizarlo, solo en casos especiales donde el valor mas bajo
 tiene importancia (detección de sombras o regiones oscuras)

Fuente: 20.2 Redes neuronales convolucionales.pptx.pdf, p. 13.


### Comparaciones · extractos del PDF


• Average Pooling
 • Calcula el valor promedio de la ventana
 • Matiene el contexto global de la imagen, sin enfatizar puntos fuertes, útil al
 analizar imágenes medicas, donde las diferencias son muy sutiles
• Min Pooling
 • Toma el valor mínimo
 • No es común utilizarlo, solo en casos especiales donde el valor mas bajo
 tiene importancia (detección de sombras o regiones oscuras)

Fuente: 20.2 Redes neuronales convolucionales.pptx.pdf, p. 13.


### Fórmulas o comandos · extractos del PDF


• Average Pooling
 • Calcula el valor promedio de la ventana
 • Matiene el contexto global de la imagen, sin enfatizar puntos fuertes, útil al
 analizar imágenes medicas, donde las diferencias son muy sutiles
• Min Pooling
 • Toma el valor mínimo
 • No es común utilizarlo, solo en casos especiales donde el valor mas bajo
 tiene importancia (detección de sombras o regiones oscuras)

Fuente: 20.2 Redes neuronales convolucionales.pptx.pdf, p. 13.


### Comprender y practicar · extractos del PDF


• Average Pooling
 • Calcula el valor promedio de la ventana
 • Matiene el contexto global de la imagen, sin enfatizar puntos fuertes, útil al
 analizar imágenes medicas, donde las diferencias son muy sutiles
• Min Pooling
 • Toma el valor mínimo
 • No es común utilizarlo, solo en casos especiales donde el valor mas bajo
 tiene importancia (detección de sombras o regiones oscuras)

Fuente: 20.2 Redes neuronales convolucionales.pptx.pdf, p. 13.


## Ventajas


### Resumen · extractos del PDF


•Reducción del numero de parámetros gracias al uso de filtros
 compartidos
•Aprendizaje automático de características
•Excelente rendimiento en tareas de clasificación, detección y
 segmentación de imágenes.

Fuente: 20.2 Redes neuronales convolucionales.pptx.pdf, p. 16.


•Realización ante pequeñas variaciones.

Fuente: 20.2 Redes neuronales convolucionales.pptx.pdf, p. 16.


### Conceptos clave · extractos del PDF


Ventajas

Fuente: 20.2 Redes neuronales convolucionales.pptx.pdf, p. 16.


### Comparaciones · extractos del PDF


•Reducción del numero de parámetros gracias al uso de filtros
 compartidos
•Aprendizaje automático de características
•Excelente rendimiento en tareas de clasificación, detección y
 segmentación de imágenes.

Fuente: 20.2 Redes neuronales convolucionales.pptx.pdf, p. 16.


## Usos comunes


### Resumen · extractos del PDF


•Clasificación de imágenes
•Reconocimiento facial
•Detección de objetivos dinámicos/estáticos vehículos
 autónomos
•Diagnostico medico asistido por imágenes
•Reconocimiento de escritura o digitos

Fuente: 20.2 Redes neuronales convolucionales.pptx.pdf, p. 17.


### Conceptos clave · extractos del PDF


Usos comunes

Fuente: 20.2 Redes neuronales convolucionales.pptx.pdf, p. 17.


## Actividad 2: Suba sus respuestas al sitio del curso.


### Resumen · extractos del PDF


LABORATORIO
Análisis de una CNN
Prof.

Fuente: 20.4 Ejercicio de repaso redes neuronales.docx.pdf, p. 2.


Franz Polanco
 procedimientos se requieren para gestionar la persistencia de datos y el
 almacenamiento de modelos entrenados?

Fuente: 20.4 Ejercicio de repaso redes neuronales.docx.pdf, p. 2.


11.​ Evaluación y diagnóstico del rendimiento: Tras finalizar el entrenamiento, ¿de qué forma
 se evalúa la capacidad de generalización del modelo mediante model.evaluate() y
 model.predict(), y cómo se analizan las curvas de pérdida y exactitud (accuracy) para
 detectar sobreajuste (overfitting) o subajuste (underfitting)?

Fuente: 20.4 Ejercicio de repaso redes neuronales.docx.pdf, p. 2.


Actividad 2: Suba sus respuestas al sitio del curso.

Fuente: 20.4 Ejercicio de repaso redes neuronales.docx.pdf, p. 2.


### Conceptos clave · extractos del PDF


Actividad 2: Suba sus respuestas al sitio del curso.

Fuente: 20.4 Ejercicio de repaso redes neuronales.docx.pdf, p. 2.


### Procedimientos · extractos del PDF


11.​ Evaluación y diagnóstico del rendimiento: Tras finalizar el entrenamiento, ¿de qué forma
 se evalúa la capacidad de generalización del modelo mediante model.evaluate() y
 model.predict(), y cómo se analizan las curvas de pérdida y exactitud (accuracy) para
 detectar sobreajuste (overfitting) o subajuste (underfitting)?

Fuente: 20.4 Ejercicio de repaso redes neuronales.docx.pdf, p. 2.


## Informe comparativo: cantidad de neuronas en la


### Resumen · extractos del PDF


Informe comparativo: cantidad de neuronas en la
 clasificación de imágenes

Fuente: Informe_Neuronas_Clasificacion_Imagenes.pdf, p. 1.


Se realizaron siete entrenamientos de una red neuronal en TensorFlow y Keras, variando la

Fuente: Informe_Neuronas_Clasificacion_Imagenes.pdf, p. 1.


cantidad de neuronas de la capa oculta: 1, 8, 16, 32, 64, 128 y 256.

Fuente: Informe_Neuronas_Clasificacion_Imagenes.pdf, p. 1.


cómo afecta esta configuración a la precisión (accuracy), la pérdida (loss) y el tiempo requerido

Fuente: Informe_Neuronas_Clasificacion_Imagenes.pdf, p. 1.


para entrenar un clasificador de imágenes.

Fuente: Informe_Neuronas_Clasificacion_Imagenes.pdf, p. 1.


Cada modelo fue configurado para 15 épocas.

Fuente: Informe_Neuronas_Clasificacion_Imagenes.pdf, p. 1.


Los valores corresponden a la última época legible en las capturas proporcionadas.

Fuente: Informe_Neuronas_Clasificacion_Imagenes.pdf, p. 1.


### Conceptos clave · extractos del PDF


Informe comparativo: cantidad de neuronas en la

Fuente: Informe_Neuronas_Clasificacion_Imagenes.pdf, p. 1.


### Definiciones · extractos del PDF


En algunos casos, no es
visible el resultado final de la época 15.

Fuente: Informe_Neuronas_Clasificacion_Imagenes.pdf, p. 1.


valores son compatibles con un desempeño similar al azar en una tarea de diez clases, lo que

Fuente: Informe_Neuronas_Clasificacion_Imagenes.pdf, p. 1.


### Ejemplos · extractos del PDF


En algunos casos, no es
visible el resultado final de la época 15.

Fuente: Informe_Neuronas_Clasificacion_Imagenes.pdf, p. 1.


### Comparaciones · extractos del PDF


Informe comparativo: cantidad de neuronas en la
 clasificación de imágenes

Fuente: Informe_Neuronas_Clasificacion_Imagenes.pdf, p. 1.


### Comprender y practicar · extractos del PDF


para entrenar un clasificador de imágenes.

Fuente: Informe_Neuronas_Clasificacion_Imagenes.pdf, p. 1.


## Conclusiones


### Resumen · extractos del PDF


8 y 16 neuronas: la precisión aumentó hasta 86.04 % y 87.94 %, respectivamente.

Fuente: Informe_Neuronas_Clasificacion_Imagenes.pdf, p. 2.


neuronas permitió representar mejor los patrones de las imágenes.

Fuente: Informe_Neuronas_Clasificacion_Imagenes.pdf, p. 2.


32 y 64 neuronas: se alcanzaron precisiones de 89.92 % y 91.38 %, con una pérdida cada vez

Fuente: Informe_Neuronas_Clasificacion_Imagenes.pdf, p. 2.


Estas configuraciones mostraron un equilibrio favorable entre capacidad de aprendizaje y

Fuente: Informe_Neuronas_Clasificacion_Imagenes.pdf, p. 2.


128 y 256 neuronas: se registraron las mejores precisiones de entrenamiento, 92.03 % y 92.87 %.

Fuente: Informe_Neuronas_Clasificacion_Imagenes.pdf, p. 2.


Sin embargo, las mejoras adicionales fueron relativamente pequeñas, mientras que las capturas

Fuente: Informe_Neuronas_Clasificacion_Imagenes.pdf, p. 2.


muestran un aumento en el tiempo por época para los modelos más grandes.

Fuente: Informe_Neuronas_Clasificacion_Imagenes.pdf, p. 2.


### Conceptos clave · extractos del PDF


Conclusiones

Fuente: Informe_Neuronas_Clasificacion_Imagenes.pdf, p. 2.


### Definiciones · extractos del PDF


sobreajuste, es necesario comparar también la precisión y la pérdida en un conjunto de validación

Fuente: Informe_Neuronas_Clasificacion_Imagenes.pdf, p. 2.


### Comparaciones · extractos del PDF


Sin embargo, las mejoras adicionales fueron relativamente pequeñas, mientras que las capturas

Fuente: Informe_Neuronas_Clasificacion_Imagenes.pdf, p. 2.


Una sola neurona resultó insuficiente, mientras que el aumento gradual de

Fuente: Informe_Neuronas_Clasificacion_Imagenes.pdf, p. 2.


sobreajuste, es necesario comparar también la precisión y la pérdida en un conjunto de validación

Fuente: Informe_Neuronas_Clasificacion_Imagenes.pdf, p. 2.


## Redes neuronales básicas


### Resumen · extractos del PDF


Estructura neuronal básica con Keras: ¿Cómo se define y configura una

Fuente: RedesNeuronalesBasicas.pdf, p. 1.


arquitectura secuencial utilizando tf.keras.Sequential y capas Dense, y

Fuente: RedesNeuronalesBasicas.pdf, p. 1.


qué parámetros clave deben establecerse al especificar la dimensión de

Fuente: RedesNeuronalesBasicas.pdf, p. 1.


entrada (input_shape) y el número de neuronas por capa?

Fuente: RedesNeuronalesBasicas.pdf, p. 1.


Se crea con tf.keras.Sequential y se agregan capas Dense una después de otra.

Fuente: RedesNeuronalesBasicas.pdf, p. 1.


input_shape indica cuántos datos recibe la red;

Fuente: RedesNeuronalesBasicas.pdf, p. 1.


por ejemplo, (4,) significa cuatro valores

Fuente: RedesNeuronalesBasicas.pdf, p. 1.


### Conceptos clave · extractos del PDF


Redes neuronales básicas

Fuente: RedesNeuronalesBasicas.pdf, p. 1.


### Definiciones · extractos del PDF


Estructura neuronal básica con Keras: ¿Cómo se define y configura una

Fuente: RedesNeuronalesBasicas.pdf, p. 1.


el valor es negativo, y Tanh produce valores entre -1 y 1.

Fuente: RedesNeuronalesBasicas.pdf, p. 1.


y qué función de pérdida es la adecuada para medir el margen de error?

Fuente: RedesNeuronalesBasicas.pdf, p. 1.


Clasificación binaria: ¿Por qué en un problema de clasificación binaria es

Fuente: RedesNeuronalesBasicas.pdf, p. 1.


### Procedimientos · extractos del PDF


Se crea con tf.keras.Sequential y se agregan capas Dense una después de otra.

Fuente: RedesNeuronalesBasicas.pdf, p. 1.


### Ejemplos · extractos del PDF


por ejemplo, (4,) significa cuatro valores

Fuente: RedesNeuronalesBasicas.pdf, p. 1.


Por ejemplo, una salida de 0.8 indica un 80 % de probabilidad para la clase

Fuente: RedesNeuronalesBasicas.pdf, p. 1.


## Clasificación multiclase: ¿Cómo transforma la función de activación


### Resumen · extractos del PDF


Clasificación multiclase: ¿Cómo transforma la función de activación

Fuente: RedesNeuronalesBasicas.pdf, p. 2.


Softmax las salidas (logits) de la red en una distribución de probabilidad

Fuente: RedesNeuronalesBasicas.pdf, p. 2.


para múltiples clases, y qué criterio determina si se debe compilar el

Fuente: RedesNeuronalesBasicas.pdf, p. 2.


modelo con categorical_crossentropy o sparse_categorical_crossentropy?

Fuente: RedesNeuronalesBasicas.pdf, p. 2.


Softmax convierte los resultados de la red en probabilidades para todas las clases;

Fuente: RedesNeuronalesBasicas.pdf, p. 2.


Se usa categorical_crossentropy si las etiquetas están en formato

Fuente: RedesNeuronalesBasicas.pdf, p. 2.


one-hot, por ejemplo [0, 1, 0], y sparse_categorical_crossentropy si son números

Fuente: RedesNeuronalesBasicas.pdf, p. 2.


### Conceptos clave · extractos del PDF


Clasificación multiclase: ¿Cómo transforma la función de activación

Fuente: RedesNeuronalesBasicas.pdf, p. 2.


### Definiciones · extractos del PDF


one-hot, por ejemplo [0, 1, 0], y sparse_categorical_crossentropy si son números

Fuente: RedesNeuronalesBasicas.pdf, p. 2.


Normalizar consiste en poner los datos en escalas parecidas, por ejemplo entre 0 y 1.

Fuente: RedesNeuronalesBasicas.pdf, p. 2.


Codificación one-hot (one-hot encoding): ¿En qué consiste la técnica de

Fuente: RedesNeuronalesBasicas.pdf, p. 2.


ofrece TensorFlow/Keras para aplicarla y en qué casos es preferible frente

Fuente: RedesNeuronalesBasicas.pdf, p. 2.


Es útil si se utiliza categorical_crossentropy;

Fuente: RedesNeuronalesBasicas.pdf, p. 2.


etiquetas son enteros, sparse_categorical_crossentropy evita convertirlas.

Fuente: RedesNeuronalesBasicas.pdf, p. 2.


durante el aprendizaje y cuáles son las consecuencias de seleccionar una

Fuente: RedesNeuronalesBasicas.pdf, p. 2.


### Ejemplos · extractos del PDF


one-hot, por ejemplo [0, 1, 0], y sparse_categorical_crossentropy si son números

Fuente: RedesNeuronalesBasicas.pdf, p. 2.


Normalizar consiste en poner los datos en escalas parecidas, por ejemplo entre 0 y 1.

Fuente: RedesNeuronalesBasicas.pdf, p. 2.


ofrece TensorFlow/Keras para aplicarla y en qué casos es preferible frente

Fuente: RedesNeuronalesBasicas.pdf, p. 2.


## Fase de entrenamiento (model.fit): ¿Investigar qué secuencia de pasos


### Resumen · extractos del PDF


Fase de entrenamiento (model.fit): ¿Investigar qué secuencia de pasos

Fuente: RedesNeuronalesBasicas.pdf, p. 3.


matemáticos e internos (propagación hacia adelante, cálculo del error y

Fuente: RedesNeuronalesBasicas.pdf, p. 3.


retropropagación o backpropagation) ocurren durante cada época (epoch)

Fuente: RedesNeuronalesBasicas.pdf, p. 3.


de entrenamiento dentro del método model.fit()?

Fuente: RedesNeuronalesBasicas.pdf, p. 3.


Primero, la red recibe los datos y produce una predicción (propagación hacia adelante).

Fuente: RedesNeuronalesBasicas.pdf, p. 3.


Luego calcula el error con la función de pérdida.

Fuente: RedesNeuronalesBasicas.pdf, p. 3.


Después, la retropropagación calcula

Fuente: RedesNeuronalesBasicas.pdf, p. 3.


### Conceptos clave · extractos del PDF


Fase de entrenamiento (model.fit): ¿Investigar qué secuencia de pasos

Fuente: RedesNeuronalesBasicas.pdf, p. 3.


### Definiciones · extractos del PDF


Como sus sesiones son temporales, conviene conectar Google Drive para

Fuente: RedesNeuronalesBasicas.pdf, p. 3.


### Procedimientos · extractos del PDF


Primero, la red recibe los datos y produce una predicción (propagación hacia adelante).

Fuente: RedesNeuronalesBasicas.pdf, p. 3.


Luego calcula el error con la función de pérdida.

Fuente: RedesNeuronalesBasicas.pdf, p. 3.


Después, la retropropagación calcula

Fuente: RedesNeuronalesBasicas.pdf, p. 3.


### Ejemplos · extractos del PDF


guardar los datos y guardar el modelo con model.save(), por ejemplo en formato .keras.

Fuente: RedesNeuronalesBasicas.pdf, p. 3.


### Comparaciones · extractos del PDF


mientras que model.predict() genera predicciones.

Fuente: RedesNeuronalesBasicas.pdf, p. 3.


### Comprender y practicar · extractos del PDF


model.evaluate() mide el error y las métricas con datos que no se usaron para entrenar,

Fuente: RedesNeuronalesBasicas.pdf, p. 3.