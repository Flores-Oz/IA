"""Explicaciones preparadas para los PDF de este curso; sin generación en ejecución."""
NORMAL = "15.1.0 Normalización.pptx.pdf"
ONEHOT = "16.1 Implementando una Red Neuronal y codificacion one-hot.pptx.pdf"
ACT = "17.1 Función de activación.pptx.pdf"
CLASS = "18.1 Clasificación.pptx.pdf"
IMAGE = "19.1 Clasificación de imagenes.pptx.pdf"
CNN = "20.2 Redes neuronales convolucionales.pptx.pdf"
BASIC = "RedesNeuronalesBasicas.pdf"
REVIEW = "20.4 Ejercicio de repaso redes neuronales.docx.pdf"
CNN_Q = "Preguntas basicas redes neuronales convolucionales.pdf"
REPORT = "Informe_Neuronas_Clasificacion_Imagenes.pdf"
LAB = "19.3 Laboratorio analisis de una CNN.doc.pdf"


def section(title, *paragraphs, **extra):
    return {"title": title, "paragraphs": list(paragraphs), **extra}


def choice(prompt, options, answer, explanation, tag="COMPRENSIÓN"):
    return {"kind": "choice", "prompt": prompt, "options": options, "answer": answer,
            "explanation": explanation, "tag": tag}


def open_question(prompt, answer, explanation, criteria):
    return {"kind": "open", "prompt": prompt, "answer": answer, "explanation": explanation, "criteria": criteria}


def source(document, *pages):
    return {"document": document, "pages": list(pages)}


LESSONS = [
    {
        "id": "red-neuronal", "shortTitle": "La red neuronal", "title": "¿Qué aprende una red neuronal?",
        "intro": "Una red recibe números, los transforma y produce una predicción. Aprender significa ajustar esas transformaciones para equivocarse menos.",
        "sections": [
            section("Empieza por una neurona", "Una neurona combina sus entradas mediante **pesos** y suma un **sesgo**. Los pesos determinan cuánto influye cada entrada y con qué signo; el sesgo desplaza el resultado. Después se aplica una función de activación.",
                    "Piensa en predecir un precio con antigüedad y kilometraje. Cada dato aporta una parte al cálculo. La red no recibe reglas escritas como «resta Q1,000 por año»: aprende valores de los pesos a partir de ejemplos.",
                    formula="z = x₁·w₁ + x₂·w₂ + … + b\nsalida = activación(z)"),
            section("Cómo se organizan las capas", "La **entrada** contiene las características de un ejemplo. Las **capas ocultas** combinan esas características. La **salida** representa lo que quieres predecir.",
                    "En una capa `Dense`, cada neurona se conecta con todas las salidas de la capa anterior. `units=3` crea tres neuronas; no significa tres datos ni tres clases necesariamente. La función de la última capa depende del problema.",
                    "Si tu tabla tiene 100 filas y 4 columnas de entrada, cada ejemplo contiene 4 características. La forma de entrada es `(4,)`; las 100 filas son ejemplos diferentes y no 100 entradas de una misma neurona."),
            section("Un cálculo pequeño", "Con entradas 2 y 3, pesos 0.4 y −0.2 y sesgo 0.1, la combinación vale 0.3. Si usas ReLU, la salida sigue siendo 0.3. Durante el entrenamiento cambiarán los pesos y el sesgo; las entradas del ejemplo son los datos que observas.",
                    type="example", formula="z = 2·0.4 + 3·(−0.2) + 0.1 = 0.3"),
            section("La idea que debes conservar", "Más neuronas dan más capacidad para representar patrones, pero no garantizan mejores predicciones con datos nuevos. Lo comprobarás al estudiar sobreajuste.", type="note"),
        ],
        "sources": [source(ONEHOT, 2, 4, 5, 6), source(BASIC, 1)],
        "questions": [
            choice("Una tabla tiene 200 ejemplos y 5 características por ejemplo. ¿Cuál es la forma de entrada de cada ejemplo?", ["(200,)", "(5,)", "(205,)", "(1,), porque solo hay un modelo"], 1, "Las columnas de entrada describen cada ejemplo. La cantidad de filas determina cuántos ejemplos tienes, no cuántas características contiene uno.", "APLICACIÓN"),
            choice("¿Qué cambia principalmente una red durante el entrenamiento?", ["Los datos originales para que coincidan con la predicción", "El nombre de las clases", "Los pesos y sesgos", "El número de filas del conjunto de prueba"], 2, "El entrenamiento ajusta parámetros. No cambia la respuesta real de un ejemplo para hacerla coincidir con la predicción."),
            choice("Una neurona recibe x=4, tiene peso 0.5 y sesgo −1. Antes de la activación, ¿qué resultado produce?", ["1", "2", "3", "−2"], 0, "La combinación es z=4×0.5−1=1. Después se aplica la función de activación que se haya elegido.", "CÁLCULO"),
            open_question("Explica la diferencia entre características, neuronas ocultas y clases de salida.", "Las características son los datos que describen un ejemplo. Las neuronas ocultas transforman esos datos y aprenden representaciones. Las clases de salida son las categorías que queremos predecir; solo en ciertos problemas coinciden con el número de neuronas de la última capa.", "Una entrada, una neurona y una clase son conceptos distintos. Por ejemplo, puedes tener 4 características, 16 neuronas ocultas y 3 clases.", ["datos de entrada", "transformación interna", "objetivo de la predicción"]),
        ],
    },
    {
        "id": "normalizacion", "shortTitle": "Normalización", "title": "Normalizar: cambiar la escala, no el significado",
        "intro": "Si una entrada está entre 0 y 20 y otra entre 10,000 y 100,000, sus magnitudes pueden dificultar el entrenamiento. Escalarlas ayuda a trabajar con números comparables.",
        "sections": [
            section("Qué problema resuelve", "En los apuntes aparece el ejemplo de antigüedad y precio original de un vehículo. El precio tiene números mucho mayores. Eso puede desbalancear las magnitudes de los cálculos y gradientes durante el entrenamiento.",
                    "**Normalizar no decide qué variable es más importante.** Hace más manejables sus escalas para que la red pueda aprender. Tampoco garantiza por sí sola una buena precisión."),
            section("Min-Max, paso a paso", "Primero encuentras el mínimo y el máximo de una característica. Luego restas el mínimo al valor y divides por la diferencia entre máximo y mínimo. Si usas el rango [0,1], el mínimo se convierte en 0 y el máximo en 1.",
                    "Por ejemplo, en los valores 0, 10, 20, 30 y 40, dividir entre 40 produce 0, 0.25, 0.5, 0.75 y 1. Se conserva el orden y la relación de las distancias en esa escala.",
                    formula="x_escalado = (x − mínimo) / (máximo − mínimo)\nx_original = x_escalado·(máximo − mínimo) + mínimo"),
            section("Ejemplo para entenderlo", "La antigüedad de entrenamiento va de 0 a 20 años. Un vehículo de 5 años se representa como 5/20=0.25. Si una salida escalada de precio es 0.6 y los precios usados para ajustar el escalador van de Q100 a Q500, el precio original es 0.6×400+100=Q340.", type="example"),
            section("Estandarizar es otra opción", "La estandarización resta la media y divide por la desviación estándar. Produce valores centrados alrededor de 0; **no los limita al intervalo [0,1]**. No elimina los valores atípicos ni es inmune a ellos.",
                    "En `MinMaxScaler`, `fit` aprende mínimo y máximo, `transform` aplica esa escala e `inverse_transform` vuelve a la unidad original. Como regla de uso, ajusta el escalador con entrenamiento y aplica ese mismo ajuste a validación y prueba; así no utilizas información de los conjuntos reservados.",
                    formula="z = (x − media) / desviación_estándar"),
            section("Dos detalles que evitan errores", "Si máximo=mínimo, la fórmula escrita divide entre cero: esa característica es constante y necesita un tratamiento adecuado. Además, un dato nuevo fuera del rango de entrenamiento puede quedar por debajo de 0 o por encima de 1 con Min-Max.", type="note"),
        ],
        "sources": [source(NORMAL, 2, 3, 4, 5, 6), source(BASIC, 2)],
        "questions": [
            choice("Con mínimo 10 y máximo 50, ¿cuánto vale 30 después de aplicar Min-Max al rango [0,1]?", ["0.25", "0.5", "0.6", "30"], 1, "(30−10)/(50−10)=20/40=0.5. Debes restar el mínimo antes de dividir.", "CÁLCULO"),
            choice("¿Qué afirmación describe correctamente la estandarización?", ["Siempre produce números entre 0 y 1", "Convierte todas las categorías a vectores", "Centra los datos usando su media y desviación estándar", "Borra los valores atípicos"], 2, "Estandarizar usa (x−media)/desviación. Puede producir números negativos y valores mayores que 1."),
            choice("El escalador de precios usó mínimo Q100 y máximo Q500. Una predicción escalada es 0.75. ¿Cuál es el precio?", ["Q300", "Q375", "Q500", "Q400"], 3, "Desnormalizas con 0.75×(500−100)+100=Q400. Multiplicar solo por el máximo sería incorrecto.", "APLICACIÓN"),
            open_question("¿Por qué no basta con decir que normalizar hace que todas las entradas sean igual de importantes?", "Porque normalizar modifica sus escalas, no la relevancia real de cada variable. Los pesos aprendidos y los datos determinan cómo se usan las entradas. El escalado puede facilitar un entrenamiento más estable, pero no impone igual importancia ni asegura buenas predicciones.", "La expresión de los apuntes busca explicar el problema de magnitudes. Evita interpretarla como una regla sobre la importancia de las características.", ["escala numérica", "pesos aprendidos", "no garantiza precisión"]),
        ],
    },
    {
        "id": "one-hot", "shortTitle": "Categorías y one-hot", "title": "¿Cómo conviertes categorías en números?",
        "intro": "Una red calcula con números. Debes representar las categorías sin introducir relaciones que no existen en los datos.",
        "sections": [
            section("El problema de poner rojo=1, azul=2 y verde=3", "Si usas esos números como una característica numérica normal, el modelo puede tratar la diferencia entre 1 y 3 como una distancia con significado. Pero los colores no tienen ese orden ni esa separación numérica.",
                    "**One-hot** crea una posición por categoría: un 1 señala cuál está presente y las demás posiciones contienen 0. El orden de las columnas se fija una vez y se conserva al entrenar y predecir.",
                    table=[["Categoría", "Rojo", "Azul", "Verde"], ["Rojo", "1", "0", "0"], ["Azul", "0", "1", "0"], ["Verde", "0", "0", "1"]]),
            section("Cuenta las entradas después de codificar", "El ejercicio del hotel tiene temporada, noches y personas. Si temporada contiene tres categorías y se conserva una columna por categoría, esa variable se transforma en tres entradas. Al añadir noches y personas tienes **cinco características**, no tres.",
                    "Ejemplo de entrada: temporada alta, 2 noches y 2 personas → `[1,0,0,2,2]`, usando el orden alta, media, baja. Después puedes escalar las variables numéricas según corresponda.", type="example"),
            section("Cuándo puedes mantener etiquetas enteras", "Distingue entre una categoría de **entrada** y una **etiqueta de salida**. En clasificación multiclase puedes guardar las respuestas correctas como 0, 1 y 2 si utilizas `sparse_categorical_crossentropy`. La pérdida las interpreta como identificadores de clase, no como una cantidad continua.",
                    "Con etiquetas one-hot utilizas `categorical_crossentropy`. Puedes crear one-hot con `tf.one_hot()` o `tf.keras.utils.to_categorical()`. La decisión debe ser consistente con el formato de las etiquetas."),
            section("Texto libre es un problema diferente", "Para frases completas, los apuntes mencionan Bag of Words, TF-IDF y embeddings. Bag of Words cuenta palabras; TF-IDF pondera las palabras según su frecuencia en los documentos; los embeddings representan elementos del texto mediante vectores. No confundas codificar tres colores con representar el significado de una oración."),
        ],
        "sources": [source(ONEHOT, 7, 8, 9, 11, 12, 14), source(BASIC, 2)],
        "questions": [
            choice("El orden de categorías es rojo, azul, verde. ¿Cuál es la representación one-hot de azul?", ["[0,1,0]", "[1,0,0]", "[0,0,1]", "[1,2,3]"], 0, "El 1 ocupa la posición asignada a azul. Los otros dos valores son 0."),
            choice("Tienes cuatro categorías de temporada y dos variables numéricas. Si mantienes todas las columnas one-hot, ¿cuántas entradas quedan?", ["3", "4", "5", "6"], 3, "La temporada se convierte en cuatro columnas; al sumar las otras dos características quedan seis.", "APLICACIÓN"),
            choice("Tus etiquetas de salida son enteros 0, 1 y 2 para tres clases excluyentes. Con salida Softmax, ¿qué pérdida corresponde al formato?", ["mean_squared_error", "sparse_categorical_crossentropy", "binary_crossentropy", "categorical_crossentropy con esas etiquetas sin convertir"], 1, "Sparse categorical crossentropy recibe el índice entero de la clase. Categorical crossentropy espera el vector de etiquetas en este esquema."),
            open_question("¿Por qué pueden ser problemáticos los enteros al codificar colores de entrada, pero válidos al guardar etiquetas de salida?", "Como entrada numérica ordinaria, 1, 2 y 3 pueden introducir un orden y distancias artificiales entre colores. Como etiquetas de salida usadas con una pérdida sparse, son índices que identifican clases. Su interpretación depende de cómo los consume el modelo.", "No memorices «los enteros siempre están mal». El contexto y la función de pérdida cambian el significado de la representación.", ["orden artificial en entradas", "índices de clase", "pérdida compatible"]),
        ],
    },
    {
        "id": "activaciones", "shortTitle": "Funciones de activación", "title": "La activación permite aprender relaciones complejas",
        "intro": "Una combinación de transformaciones lineales sigue siendo lineal. Las activaciones no lineales permiten que las capas representen patrones más complejos.",
        "sections": [
            section("Qué cambia una activación", "La neurona primero calcula una combinación de entradas. La activación transforma ese resultado. Sin activaciones no lineales entre capas, aumentar la profundidad no basta para representar relaciones no lineales.",
                    "No elijas la activación solo por costumbre. Una cosa es la activación de las capas ocultas y otra la de salida: la última debe expresar el tipo de predicción que necesitas."),
            section("Las funciones que debes distinguir", table=[["Función", "Qué hace", "Uso habitual en este curso"], ["ReLU", "Devuelve max(0,z): negativos → 0; positivos → el mismo valor.", "Capas ocultas y bloques convolucionales."], ["Leaky ReLU", "Deja una pequeña pendiente para valores negativos.", "Alternativa para evitar que la rama negativa quede totalmente bloqueada."], ["Tanh", "Produce valores entre −1 y 1; puede saturarse.", "Activación no lineal en capas ocultas."], ["Sigmoid", "Produce un valor entre 0 y 1.", "Una salida para clasificación binaria."], ["Softmax", "Transforma un vector en valores que suman 1.", "Salida multiclase excluyente."], ["Lineal", "No restringe el resultado por una no linealidad.", "Salida de una regresión numérica simple."]]),
            section("ReLU con números", "Para las entradas −3, 0 y 4, ReLU devuelve 0, 0 y 4. Que dé cero a números negativos no significa que toda la red deje de aprender; significa que esa rama local no transmite gradiente para esos valores. Leaky ReLU conserva una pendiente pequeña en esa zona.", type="example", formula="ReLU(z) = max(0,z)"),
            section("Saturación y gradientes pequeños", "Sigmoid y Tanh se aplanan para entradas de gran magnitud. En esas regiones sus derivadas son pequeñas. Al encadenar muchas capas, la señal que se usa para ajustar las primeras puede hacerse muy débil: es el **desvanecimiento del gradiente**.",
                    "ReLU suele facilitar el entrenamiento en capas ocultas, pero no es una solución universal. En salida, Sigmoid o Softmax siguen siendo apropiadas si la tarea pide probabilidades."),
            section("Probabilidad no significa certeza", "Una salida 0.8 de Sigmoid se interpreta como la probabilidad estimada por el modelo para la clase 1. No significa que esa predicción esté garantizada ni que la red tenga 80 % de exactitud general.", type="note"),
        ],
        "sources": [source(ACT, 2, 3, 4, 5, 6, 7, 8, 12), source(BASIC, 1)],
        "questions": [
            choice("¿Qué devuelve ReLU para −5 y 3, respectivamente?", ["−5 y 3", "0 y 1", "0 y 3", "5 y 3"], 2, "ReLU sustituye los valores negativos por 0 y deja iguales los positivos.", "CÁLCULO"),
            choice("¿Por qué varias capas sin activaciones no lineales siguen siendo limitadas?", ["Porque su composición sigue siendo una transformación lineal o afín", "Porque siempre producen exactamente cero", "Porque no admiten más de una entrada", "Porque no pueden almacenar pesos"], 0, "Encadenar transformaciones lineales o afines puede resumirse en otra transformación del mismo tipo. La no linealidad es lo que amplía la representación."),
            choice("Una red muy profunda con Sigmoid en sus capas ocultas aprende muy lentamente en las primeras capas. ¿Qué explicación es razonable?", ["Softmax está normalizando mal las imágenes", "Le faltan obligatoriamente más clases", "Todas las derivadas valen exactamente uno", "La saturación puede hacer pequeños los gradientes"], 3, "Las derivadas pequeñas pueden multiplicarse a través de las capas y debilitar la señal que llega a las primeras. Es una posible causa, no un diagnóstico automático.", "RAZONAMIENTO"),
            open_question("¿Por qué usarías ReLU en capas ocultas y Softmax en la salida de un clasificador de diez clases?", "ReLU aporta no linealidad para aprender patrones en las capas ocultas. Softmax transforma las diez salidas en una distribución de probabilidades que suma 1 y permite elegir entre diez clases excluyentes.", "Cada activación responde a una función diferente dentro de la misma red. No necesitas usar la misma en todas las capas.", ["no linealidad interna", "diez salidas", "probabilidades que suman 1"]),
        ],
    },
]

LESSONS += [
    {
        "id": "salida-y-perdida", "shortTitle": "Salida y función de pérdida", "title": "El problema decide la salida y la pérdida",
        "intro": "Antes de construir la red, define qué significa su respuesta: un número, una de dos clases o una de varias clases.",
        "sections": [
            section("Tres problemas diferentes", "**Regresión** predice una cantidad continua, como precio o temperatura. **Clasificación binaria** distingue dos clases, como spam/no spam. **Clasificación multiclase** elige una categoría entre varias, como uno de diez dígitos.",
                    "La capa de salida debe representar esa respuesta. No se elige por el número de columnas de entrada ni por la cantidad de ejemplos del conjunto de entrenamiento.",
                    table=[["Tarea", "Salida típica", "Pérdida compatible"], ["Un número continuo", "1 neurona lineal", "MSE o MAE"], ["Dos clases", "1 neurona Sigmoid", "binary_crossentropy"], ["Una de K clases; etiqueta one-hot", "K neuronas Softmax", "categorical_crossentropy"], ["Una de K clases; etiqueta entera", "K neuronas Softmax", "sparse_categorical_crossentropy"]]),
            section("Qué hace la pérdida", "La función de pérdida **cuantifica el error** entre la predicción y la respuesta correcta. Durante el entrenamiento se calcula cómo cambiar los parámetros para reducirla. Una métrica como accuracy describe el rendimiento, pero no reemplaza necesariamente la función usada para optimizar.",
                    "Para un precio real de Q100 y una predicción de Q80, el error absoluto es 20 y el error cuadrado es 400. MAE promedia errores absolutos; MSE promedia errores cuadrados. El cuadrado da más peso a los errores grandes.",
                    formula="MAE = promedio(|valor_real − predicción|)\nMSE = promedio((valor_real − predicción)²)"),
            section("Interpreta la clasificación", "Con Sigmoid y umbral 0.5, una salida 0.8 se asigna a la clase 1 y una salida 0.3 a la clase 0. El umbral es una regla de decisión; no es la función de pérdida.",
                    "Con tres clases ordenadas como gato, perro y ave, la salida Softmax `[0.1,0.7,0.2]` selecciona perro. Los valores suman 1 y el mayor identifica la clase elegida. Las tres neuronas representan clases, no tres predicciones numéricas independientes.", type="example"),
            section("No confundas etiquetas con logits", "La tabla supone que la última capa ya aplica Sigmoid o Softmax. Si trabajas con salidas crudas o logits, la pérdida debe configurarse de forma consistente. Para los ejercicios del curso, conserva las combinaciones de la tabla.",
                    "También se supone una sola clase correcta por ejemplo. Un problema donde una imagen puede ser simultáneamente «perro» y «exterior» es multietiqueta y requiere otro planteamiento.", type="note"),
        ],
        "sources": [source(CLASS, 2, 3), source(ACT, 6, 7, 8), source(BASIC, 1, 2)],
        "questions": [
            choice("Quieres estimar el precio de una habitación. ¿Qué salida corresponde a esta tarea?", ["Una neurona lineal", "Diez neuronas Softmax", "Una neurona Sigmoid para limitar todo precio a Q1", "Una neurona por fila de entrenamiento"], 0, "Es una regresión de un solo valor continuo. La salida típica es una neurona lineal, con una pérdida como MSE.", "APLICACIÓN"),
            choice("Tienes 10 clases excluyentes y etiquetas one-hot. ¿Qué combinación es consistente?", ["1 salida lineal y binary_crossentropy", "10 salidas ReLU y MAE como clasificador estándar", "10 salidas Softmax y categorical_crossentropy", "1 salida Sigmoid y sparse_categorical_crossentropy"], 2, "La salida tiene una posición por clase y Softmax produce una distribución. Categorical crossentropy compara esa distribución con la etiqueta one-hot."),
            choice("El valor real es 10 y la predicción es 7. ¿Cuál es el error cuadrado de este ejemplo?", ["3", "9", "17", "49"], 1, "El error es 10−7=3 y su cuadrado es 9. Para obtener MSE debes promediar los errores cuadrados de los ejemplos.", "CÁLCULO"),
            open_question("Distingue pérdida, accuracy y umbral de decisión usando un clasificador binario.", "La pérdida mide el error de las probabilidades y guía el ajuste de los pesos. Accuracy cuenta qué proporción de decisiones de clase resultó correcta. El umbral transforma una probabilidad en clase, por ejemplo usando 0.5.", "Una red puede mejorar la pérdida sin cambiar de inmediato sus decisiones de clase. Por eso pérdida y accuracy no son la misma medida.", ["error para optimizar", "proporción de aciertos", "regla para decidir la clase"]),
        ],
    },
    {
        "id": "entrenamiento", "shortTitle": "Cómo aprende: entrenamiento", "title": "Lo que ocurre dentro de model.fit()",
        "intro": "El entrenamiento repite un ciclo: predecir, medir el error, calcular gradientes y actualizar los parámetros.",
        "sections": [
            section("El ciclo completo", "**1. Propagación hacia adelante:** un grupo de ejemplos atraviesa las capas y produce predicciones. **2. Pérdida:** se comparan esas predicciones con sus respuestas correctas.",
                    "**3. Retropropagación:** se calculan las derivadas de la pérdida respecto a los parámetros. El gradiente indica cómo influye un cambio de cada parámetro en el error. **4. Optimizador:** usa esos gradientes para actualizar pesos y sesgos.",
                    "Retropropagar no significa invertir la predicción ni cambiar las etiquetas. Es calcular cómo contribuye cada parámetro a la pérdida."),
            section("Batch, época y actualización", "Un **batch** es un grupo de ejemplos procesado en una iteración. Una **época** es un recorrido completo por el conjunto de entrenamiento. Normalmente hay muchas actualizaciones dentro de una época.",
                    "Si tienes 1,000 ejemplos y `batch_size=100`, hay 10 lotes por época. Con 5 épocas se recorren esos datos cinco veces y se realizan 50 actualizaciones, suponiendo una actualización por lote.", type="example"),
            section("La tasa de aprendizaje", "La **learning rate** controla el tamaño del paso que da el optimizador. Si es demasiado alta, el entrenamiento puede oscilar o empeorar. Si es demasiado baja, puede avanzar muy lentamente. No hay un valor universal adecuado para todos los problemas.",
                    "En el descenso de gradiente más sencillo, si un peso vale 0.5, su gradiente es 2 y la tasa es 0.1, el nuevo peso vale 0.3. Se resta el gradiente multiplicado por la tasa. Optimizadores como Adam incorporan ajustes adicionales.",
                    formula="peso_nuevo = peso_actual − tasa·gradiente\n0.5 − 0.1·2 = 0.3"),
            section("Entrenar más no siempre mejora el resultado", "Que la pérdida de entrenamiento siga bajando no demuestra que el modelo generalice mejor. Debes observar validación. Si la red empieza a memorizar particularidades de entrenamiento, más épocas pueden empeorar su respuesta a ejemplos nuevos.", type="note"),
        ],
        "sources": [source(BASIC, 2, 3), source(ACT, 11, 12, 13), source(REVIEW, 1)],
        "questions": [
            choice("¿Qué orden describe una actualización de entrenamiento?", ["Actualizar pesos → inventar etiquetas → predecir", "Predecir → calcular pérdida → retropropagar → actualizar parámetros", "Calcular accuracy → borrar datos → cambiar clases", "Normalizar salidas → terminar la época sin calcular error"], 1, "Primero necesitas una predicción y su error; después puedes calcular gradientes y aplicar una actualización."),
            choice("Tienes 600 ejemplos, lotes de 100 y 4 épocas. Sin pasos adicionales, ¿cuántas actualizaciones hay si haces una por lote?", ["4", "6", "600", "24"], 3, "Hay 600/100=6 lotes por época. Cuatro épocas producen 6×4=24 actualizaciones.", "CÁLCULO"),
            choice("La pérdida oscila mucho al subir considerablemente la tasa de aprendizaje. ¿Qué interpretación es razonable?", ["Los pasos pueden ser demasiado grandes y saltar zonas de menor error", "La red ha garantizado una mejor generalización", "La cantidad de clases se duplicó", "El batch dejó de contener ejemplos"], 0, "Una tasa excesiva puede hacer inestable la optimización. Debes probar un ajuste y observar las curvas, no asumir que más velocidad significa mejor aprendizaje.", "RAZONAMIENTO"),
            open_question("Explica por qué una época no equivale necesariamente a una sola actualización de pesos.", "Una época recorre todos los ejemplos, pero los datos suelen dividirse en lotes. La red calcula gradientes y actualiza parámetros después de cada lote; por eso puede haber varias actualizaciones dentro de una época.", "Relaciona el número de actualizaciones con el número de lotes, no solo con la cantidad de épocas.", ["recorrido completo", "división en lotes", "actualización por lote"]),
        ],
    },
    {
        "id": "metricas", "shortTitle": "Accuracy y matriz de confusión", "title": "Acertar mucho no siempre significa detectar lo importante",
        "intro": "Accuracy cuenta aciertos generales. La matriz de confusión te permite distinguir qué clases y qué tipos de errores están detrás de ese número.",
        "sections": [
            section("Accuracy y el engaño del desbalance", "Accuracy es el número de clasificaciones correctas dividido entre el total. Si aciertas 3 de 4, tienes 75 %.",
                    "El ejemplo de los PDF contiene 95 transacciones normales y 5 fraudulentas. Un modelo que diga «normal» para todas obtiene 95 % de accuracy, pero detecta **cero fraudes**. El resultado general oculta el fracaso en la clase que te interesa."),
            section("Define primero la clase positiva", "Si «fraude» es positivo, la matriz se interpreta así. Lo real determina si el caso es positivo o negativo; la predicción determina si el modelo acertó o se equivocó.",
                    table=[["", "Predijo positivo", "Predijo negativo"], ["Realmente positivo", "TP: detectó un positivo real", "FN: dejó escapar un positivo real"], ["Realmente negativo", "FP: dio una alarma falsa", "TN: reconoció un negativo real"]]),
            section("Precision y recall responden preguntas distintas", "**Precision:** de los casos marcados como positivos, ¿cuántos sí lo eran? Se reduce cuando hay falsas alarmas. **Recall o sensibilidad:** de todos los positivos reales, ¿cuántos detectaste? Se reduce cuando dejas positivos sin detectar.",
                    "Los apuntes desarrollan precision; recall completa la comparación para comprender los falsos negativos. F1 combina precision y recall mediante una media armónica, útil para observar ambas juntas.",
                    formula="Accuracy = (TP + TN) / total\nPrecision = TP / (TP + FP)\nRecall = TP / (TP + FN)\nF1 = 2·Precision·Recall / (Precision + Recall)"),
            section("Un ejemplo completo", "Hay 10 fraudes reales. El sistema marca 8 casos como fraude: 6 lo son y 2 son falsas alarmas. Entonces TP=6, FP=2 y FN=4. Precision=6/8=75 %, mientras recall=6/10=60 %. Detectó bastantes casos, pero todavía dejó escapar cuatro fraudes.", type="example"),
            section("Aclaración del material", "En la diapositiva de matriz de confusión, las descripciones escritas de FP y FN están cruzadas. Usa las definiciones de esta tabla: **FP es una alarma falsa; FN es un positivo que no detectaste**. Para calcular cualquier métrica, verifica también qué clase elegiste como positiva.", type="note"),
        ],
        "sources": [source(CLASS, 4, 5, 6, 7, 8), source(BASIC, 3)],
        "questions": [
            choice("Un detector llama normal a las 100 transacciones: 95 son normales y 5 fraudulentas. ¿Qué ocurre?", ["Accuracy=0 % y detectó 5 fraudes", "Accuracy=100 % y no tiene errores", "Accuracy=95 % y no detectó ningún fraude", "Precision=95 % necesariamente"], 2, "Acierta las 95 normales, pero sus cinco fraudes son falsos negativos. Accuracy alta no asegura detectar la clase minoritaria.", "APLICACIÓN"),
            choice("La clase positiva es enfermedad. Una persona enferma recibe un resultado negativo. ¿Qué caso es?", ["Falso negativo", "Falso positivo", "Verdadero negativo", "Verdadero positivo"], 0, "El caso era positivo, pero el modelo predijo negativo. Es un positivo real que no se detectó."),
            choice("El modelo marca 10 correos como spam: 8 son spam y 2 no. ¿Cuál es su precision para spam?", ["20 %", "80 %", "No se puede calcular sin saber todos los correos spam que escaparon", "100 %"], 1, "Precision=TP/(TP+FP)=8/(8+2)=80 %. Los spam no detectados hacen falta para recall, no para esta precision.", "CÁLCULO"),
            open_question("En un detector de una enfermedad, ¿por qué conviene revisar los falsos negativos además de la accuracy?", "Un falso negativo deja sin detectar a una persona enferma. Si hay pocos enfermos, el modelo puede tener accuracy alta acertando muchos sanos aunque pierda casi todos los positivos. Recall ayuda a medir cuántos enfermos reales detecta.", "La importancia de un error depende del contexto. No basta con maximizar un porcentaje general sin mirar qué casos se pierden.", ["enfermos no detectados", "desbalance de clases", "recall"]),
        ],
    },
    {
        "id": "imagenes", "shortTitle": "Imágenes como datos", "title": "Una imagen es una matriz de números",
        "intro": "Para una red, una fotografía es un conjunto ordenado de valores de píxeles. Su forma y escala son parte de la entrada del modelo.",
        "sections": [
            section("Alto, ancho y canales", "Una imagen en escala de grises puede representarse con alto×ancho valores. Para una capa Conv2D, se suele hacer explícito el canal: una imagen de 28×28 queda como `(28,28,1)`.",
                    "Una imagen RGB tiene tres canales: rojo, verde y azul. Una entrada `(32,32,3)` contiene 32×32×3=3,072 valores. El 3 no significa tres imágenes ni tres clases; describe canales por píxel."),
            section("Los conjuntos que aparecen en el curso", table=[["Conjunto", "Qué representa", "Forma habitual de una imagen", "Clases"], ["MNIST", "Dígitos manuscritos", "28×28; escala de grises", "10"], ["Fashion MNIST", "Prendas de vestir y accesorios", "28×28; escala de grises", "10"], ["CIFAR-10", "Objetos de distintas categorías", "32×32×3; color", "10"]]),
            section("Prepara los valores antes de entrenar", "Cuando los píxeles están almacenados como enteros de 8 bits sin signo, sus valores van de **0 a 255**. Dividir por 255 los lleva a [0,1]. Un píxel con valor 128 pasa a 128/255≈0.502.",
                    "En una red densa, `Flatten` transforma la imagen en una lista: 28×28 se convierte en 784 entradas. Una CNN mantiene la organización espacial al aplicar convoluciones: eso ayuda a reconocer patrones locales como bordes.",
                    formula="Imagen gris: 28×28 = 784 valores\nImagen RGB: 32×32×3 = 3,072 valores\nEscalado de un píxel de 8 bits: valor / 255"),
            section("Separar ejemplos de entrenamiento y prueba", "Las imágenes necesitan etiquetas correctas para aprendizaje supervisado. Los ejemplos de entrenamiento sirven para ajustar parámetros; los de prueba reservados sirven para evaluar el comportamiento con datos no usados para entrenar. No conviertas las imágenes de prueba en más ejemplos de entrenamiento si después pretendes medir con ellas."),
            section("Dos aclaraciones de las diapositivas", "MNIST de dígitos y Fashion MNIST de ropa son conjuntos distintos. Además, donde la diapositiva menciona un máximo de 250 para un byte, la referencia correcta para enteros de 8 bits sin signo es **255**. Por eso en estos ejemplos se divide entre 255.", type="note"),
        ],
        "sources": [source(IMAGE, 2, 3, 4, 5, 7), source(CNN, 2)],
        "questions": [
            choice("¿Qué significa el último 3 en una imagen con forma (32,32,3)?", ["Tres canales de color", "Tres clases posibles", "Tres ejemplos de entrenamiento", "Tres capas ocultas obligatorias"], 0, "En esta representación RGB hay tres valores de canal por cada posición de píxel."),
            choice("Al aplanar una imagen gris de 28×28, ¿cuántos valores quedan?", ["56", "28", "784", "2,352 obligatoriamente"], 2, "28×28=784. El resultado de 2,352 correspondería a multiplicar por tres canales, que no se indican aquí.", "CÁLCULO"),
            choice("Si un píxel de 8 bits vale 255, ¿qué obtiene al dividirlo entre 255?", ["0", "0.5", "255", "1"], 3, "El máximo de ese rango se transforma en 1. Un valor de 0 se transforma en 0.", "CÁLCULO"),
            open_question("¿Qué cambia entre aplanar una imagen para una capa Dense y procesarla con una CNN?", "Flatten transforma la imagen en un vector para conectarlo con capas densas. Una CNN aplica filtros a regiones de la imagen conservando su organización espacial durante las convoluciones, lo que permite extraer patrones locales.", "Aplanar no cambia el número de valores de la imagen, pero deja de representar explícitamente sus dos dimensiones espaciales en esa entrada.", ["vector con Flatten", "regiones locales", "estructura espacial"]),
        ],
    },
    {
        "id": "convolucion", "shortTitle": "Convolución y filtros", "title": "La CNN aprende a buscar patrones locales",
        "intro": "Una capa convolucional recorre la imagen con pequeños filtros. Cada filtro produce un mapa que indica dónde aparece el patrón que ha aprendido a detectar.",
        "sections": [
            section("Qué hace un filtro", "Un filtro o **kernel** es una pequeña matriz de pesos. Se coloca sobre una región de la imagen, multiplica valores correspondientes y suma los resultados. Al desplazarse, repite el cálculo y construye un **mapa de características**.",
                    "El mismo conjunto de pesos se usa en diferentes posiciones: no se necesita aprender un filtro diferente para cada esquina de la imagen. Los filtros no tienen que diseñarse manualmente; durante el entrenamiento se ajustan para ayudar a resolver la tarea."),
            section("Qué significa Conv2D(32, (3,3))", "La capa aprende **32 filtros**, cada uno con un tamaño espacial de 3×3, y produce 32 canales o mapas de características. No significa 32 clases ni una imagen de 32×32.",
                    "Si la entrada tiene tres canales, cada filtro abarca también esos tres canales: usa 3×3×3 pesos. En una configuración con un sesgo por filtro, la capa tiene `(3×3×3+1)×32=896` parámetros.",
                    formula="Parámetros = (alto_kernel·ancho_kernel·canales_entrada + 1)·filtros"),
            section("Ejemplo pequeño de convolución", "Para entender las multiplicaciones, imagina una región `[1,2;3,4]` y un filtro `[1,0;0,−1]`. El resultado de esa posición, antes del sesgo y la activación, es 1×1+2×0+3×0+4×(−1)=−3. Con ReLU se transforma en 0. En una red real los valores del filtro se aprenden.", type="example"),
            section("Tamaño de salida: padding y stride", "El **stride** indica cuántas posiciones avanza el filtro. El **padding** añade borde para controlar las dimensiones de salida. Con stride 1 y sin padding (`valid`), una imagen de 32×32 y un kernel 3×3 produce un mapa de 30×30. Con `same` y stride 1 conserva 32×32.",
                    "La cuenta de dimensiones y parámetros desarrolla el ejemplo de las diapositivas; estos cálculos se incluyen para que entiendas la arquitectura y no solo memorices sus capas.",
                    formula="Sin padding y stride 1: tamaño_salida = tamaño_entrada − tamaño_kernel + 1\n32 − 3 + 1 = 30"),
            section("Más filtros: capacidad y costo", "Las primeras capas suelen aprender rasgos sencillos y las siguientes combinaciones más complejas. Aumentar filtros puede ayudar a representar más patrones, pero también aumenta parámetros, tiempo y riesgo de sobreajuste. «Más filtros» no equivale automáticamente a «mejor modelo».", type="note"),
        ],
        "sources": [source(CNN, 4, 5, 7, 8, 9, 10, 16), source(CNN_Q, 1)],
        "questions": [
            choice("Una capa Conv2D usa 32 filtros. ¿Cuántos mapas de características produce para cada imagen?", ["3", "9", "32", "La misma cantidad que clases"], 2, "Cada filtro produce un canal de salida. Su cantidad no define por sí sola el número de clases."),
            choice("Una entrada de 32×32 pasa por un kernel 3×3, stride 1 y padding valid. ¿Cuál es la dimensión espacial de salida?", ["30×30", "32×32", "16×16", "3×3"], 0, "Sin borde agregado, cada dimensión queda en 32−3+1=30.", "CÁLCULO"),
            choice("¿Por qué compartir los pesos de un filtro entre posiciones es útil?", ["Obliga a que todas las imágenes sean idénticas", "Evita calcular una función de pérdida", "Convierte todos los píxeles en etiquetas", "Permite buscar el mismo patrón en distintos lugares con los mismos parámetros"], 3, "Un detector local aprendido puede aplicarse en toda la imagen, en lugar de aprender pesos independientes para cada posición.", "RAZONAMIENTO"),
            open_question("Una CNN mejora su accuracy de entrenamiento al duplicar filtros. ¿Eso demuestra que detectará mejor imágenes nuevas?", "No. Más filtros aumentan capacidad, pero el resultado de entrenamiento no demuestra generalización. Debes comparar métricas de validación o prueba y observar si aumentó el costo o el sobreajuste.", "Separa la capacidad de ajustar ejemplos conocidos de la capacidad de resolver casos nuevos.", ["capacidad del modelo", "validación o prueba", "sobreajuste y costo"]),
        ],
    },
]

LESSONS += [
    {
        "id": "pooling", "shortTitle": "Pooling", "title": "Pooling: resumir una región de la imagen",
        "intro": "Después de extraer características, puedes reducir el tamaño de sus mapas. Pooling resume pequeños grupos de valores; no aprende filtros nuevos.",
        "sections": [
            section("Max, average y min", "**Max pooling** conserva el máximo de cada ventana. Resalta la respuesta más intensa que ya encontró una capa. **Average pooling** conserva el promedio y resume la actividad de la región. **Min pooling** conserva el mínimo y es menos habitual.",
                    "Una ventana 2×2 con valores 2, 5, 8 y 3 se transforma en 8 con max pooling, 4.5 con average pooling y 2 con min pooling. No se suman todos los valores para obtener el máximo.",
                    table=[["Región 2×2", "Max", "Average", "Min"], ["2, 5 / 8, 3", "8", "(2+5+8+3)/4 = 4.5", "2"]]),
            section("Cuánto se reduce", "Con `MaxPooling2D((2,2))`, stride 2 y dimensiones compatibles, cada bloque espacial de cuatro valores se resume en uno. Un mapa de 28×28 se convierte en 14×14.",
                    "Si la entrada tiene 32 canales, la salida sigue teniendo 32: el pooling habitual actúa sobre las dimensiones espaciales de cada canal. Por eso `(28,28,32)` pasa a `(14,14,32)` en este ejemplo.", type="example"),
            section("Qué gana y qué pierde", "Reducir mapas disminuye la cantidad de operaciones de capas posteriores y conserva una representación más compacta. También elimina parte del detalle espacial. No puedes recuperar la ubicación exacta de cada valor original solo mirando el máximo.",
                    "El pooling estándar no tiene pesos entrenables. Puede reducir indirectamente el número de parámetros de capas densas posteriores, al entregarles menos valores. No debe confundirse con una convolución: la convolución aprende filtros; el pooling aplica una regla fija de resumen."),
            section("No hay un pooling ganador para todo", "Max destaca respuestas fuertes y average conserva información promedio. Los apuntes proponen comparar ambos. Elige según el resultado de validación de la tarea; no supongas que average siempre es mejor para imágenes médicas ni que max siempre obtiene más precisión.", type="note"),
        ],
        "sources": [source(CNN, 11, 12, 13, 19), source(CNN_Q, 1)],
        "questions": [
            choice("Una ventana contiene 1, 7, 3 y 5. ¿Qué devuelve max pooling?", ["4", "1", "16", "7"], 3, "Max pooling toma el valor mayor: 7. El promedio sería 4.", "CÁLCULO"),
            choice("Una entrada (20,20,16) pasa por pooling 2×2 con stride 2. ¿Qué forma resulta?", ["(10,10,8)", "(10,10,16)", "(20,20,2)", "(40,40,16)"], 1, "Se divide por dos alto y ancho, pero la cantidad de canales permanece en 16.", "APLICACIÓN"),
            choice("¿Qué diferencia esencial hay entre Conv2D y max pooling estándar?", ["Conv2D aprende pesos de filtros; max pooling aplica una regla fija", "Max pooling aprende más filtros que Conv2D", "Conv2D solo sirve para tomar máximos", "Max pooling cambia las etiquetas reales"], 0, "Los filtros de convolución se entrenan. La operación máximo no requiere aprender parámetros."),
            open_question("¿Por qué reducir los mapas puede ser útil y, al mismo tiempo, perder información?", "Reduce las dimensiones y el trabajo de capas posteriores, pero reemplaza varios valores por un resumen. Esto descarta parte de sus detalles y posiciones exactas. La reducción debe conservar suficiente información para la tarea.", "Un resumen útil no es una copia sin pérdidas. Debes relacionar eficiencia y detalle espacial.", ["menos valores", "menor costo posterior", "pérdida de detalle"]),
        ],
    },
    {
        "id": "arquitectura-cnn", "shortTitle": "La CNN completa", "title": "De una imagen a la clase predicha",
        "intro": "Una CNN combina dos trabajos: extraer características visuales y usar esas características para decidir una categoría.",
        "sections": [
            section("Recorre la arquitectura", "**Conv2D** detecta patrones locales mediante filtros aprendidos. **ReLU** introduce no linealidad. **Pooling** reduce los mapas. Puedes repetir bloques para construir representaciones cada vez más elaboradas.",
                    "Después, **Flatten** convierte los mapas en un vector. Una capa **Dense** combina la información extraída y la capa final genera la salida. Para diez clases excluyentes, diez neuronas con Softmax producen las probabilidades por clase.",
                    formula="Imagen → Conv2D + ReLU → Pooling → Conv2D + ReLU → Pooling\n       → Flatten → Dense → Softmax"),
            section("Sigue las dimensiones del ejemplo", "Para el ejemplo de 32×32×3, usa kernels 3×3 con stride 1 y padding valid, y pooling 2×2 con stride 2. Cada convolución reduce dos posiciones espaciales; cada pooling divide por dos en estos tamaños.",
                    table=[["Paso", "Forma sin contar el lote"], ["Entrada", "32×32×3"], ["Conv2D: 32 filtros 3×3", "30×30×32"], ["MaxPooling 2×2", "15×15×32"], ["Conv2D: 64 filtros 3×3", "13×13×64"], ["MaxPooling 2×2", "6×6×64"], ["Conv2D: 64 filtros 3×3", "4×4×64"], ["Flatten", "1,024 valores"], ["Dense final con 10 salidas", "10 probabilidades"]]),
            section("No confundas la extracción con la decisión", "Los 32 o 64 filtros no significan 32 o 64 clases. Son detectores de características intermedias. La cantidad de categorías se refleja en la última capa del clasificador multiclase.",
                    "Flatten tampoco clasifica ni aprende pesos: reorganiza los valores. La interpretación como gato, automóvil o cualquier clase definida por el conjunto de datos aparece en la salida del modelo."),
            section("Un ejemplo de código para leer", "Aquí interesa que puedas explicar cada capa. El código es una ilustración de la arquitectura del material, no se ejecuta en esta página ni descarga conjuntos de imágenes.",
                    code="model = tf.keras.Sequential([\n    tf.keras.Input(shape=(32, 32, 3)),\n    tf.keras.layers.Conv2D(32, (3, 3), activation='relu'),\n    tf.keras.layers.MaxPooling2D((2, 2)),\n    tf.keras.layers.Conv2D(64, (3, 3), activation='relu'),\n    tf.keras.layers.MaxPooling2D((2, 2)),\n    tf.keras.layers.Conv2D(64, (3, 3), activation='relu'),\n    tf.keras.layers.Flatten(),\n    tf.keras.layers.Dense(64, activation='relu'),\n    tf.keras.layers.Dense(10, activation='softmax')\n])"),
        ],
        "sources": [source(CNN, 6, 8, 14), source(LAB, 1), source(CNN_Q, 1)],
        "questions": [
            choice("¿Qué parte convierte los mapas de características en un vector sin aprender pesos?", ["Softmax", "Flatten", "La función de pérdida", "La etiqueta de clase"], 1, "Flatten reorganiza los valores para que puedan alimentar capas densas. No crea filtros ni decide la clase."),
            choice("El último mapa antes de Flatten mide 4×4×64. ¿Cuántos valores tendrá el vector?", ["72", "256", "1,024", "4,096"], 2, "Multiplica las tres dimensiones: 4×4×64=1,024.", "CÁLCULO"),
            choice("Una CNN tiene 64 filtros en la última convolución y debe clasificar 10 categorías excluyentes. ¿Cuántas salidas Softmax necesita?", ["10", "64", "640", "1 obligatoriamente"], 0, "Los filtros representan características; las salidas Softmax representan las clases de esta tarea.", "APLICACIÓN"),
            open_question("Explica el recorrido de una imagen hasta convertirse en una predicción de clase.", "Las convoluciones extraen patrones locales, las activaciones permiten combinaciones no lineales y el pooling reduce mapas. Flatten los convierte en un vector, las capas densas combinan sus características y la salida Softmax produce las probabilidades de clase.", "La idea central es separar extracción de características y decisión final, sin atribuir a Flatten o pooling una clasificación que no realizan por sí solos.", ["extracción visual", "reducción y vector", "decisión por clases"]),
        ],
    },
    {
        "id": "generalizacion", "shortTitle": "Sobreajuste y evaluación", "title": "Aprender los ejemplos no es lo mismo que generalizar",
        "intro": "El objetivo es predecir bien datos nuevos. Un resultado excelente en entrenamiento puede esconder un modelo que solo memoriza.",
        "sections": [
            section("Entrenamiento, validación y prueba", "**Entrenamiento** ajusta los pesos. **Validación** ayuda a comparar configuraciones y vigilar lo que ocurre mientras entrenas. **Prueba** se reserva para estimar el desempeño final en ejemplos no usados para ajustar el modelo ni elegir continuamente sus parámetros.",
                    "`model.evaluate()` calcula pérdida y métricas sobre los datos que le entregues. Solo es una evaluación con datos nuevos si tú le pasas un conjunto reservado. `model.predict()` produce predicciones; no calcula por sí solo todos los aciertos sin compararlos con las etiquetas."),
            section("Dos problemas diferentes", "**Subajuste:** el modelo no representa suficientemente bien el problema. Su rendimiento en entrenamiento y validación sigue siendo malo. Puede deberse a capacidad insuficiente, poco entrenamiento u otras dificultades del proceso.",
                    "**Sobreajuste:** sigue mejorando en entrenamiento mientras empeora o se distancia su rendimiento de validación. Ha aprendido particularidades de los ejemplos conocidos que no se transfieren bien.",
                    table=[["Situación observada", "Qué debes investigar"], ["Pérdidas altas en entrenamiento y validación", "Subajuste u otro problema de datos/optimización"], ["Pérdida de entrenamiento baja; validación sube", "Posible sobreajuste"], ["Ambas pérdidas bajan de manera consistente", "Aprendizaje que por ahora parece generalizar mejor"]]),
            section("Qué demuestra el informe de neuronas", "El informe compara 1, 8, 16, 32, 64, 128 y 256 neuronas ocultas. En sus resultados observados, 256 alcanza 92.87 % de accuracy de entrenamiento y pérdida 0.1909. Una neurona se queda cerca del 10 %.",
                    "Eso muestra que la capacidad influyó en esos entrenamientos. **No demuestra que 256 sea la mejor elección para imágenes nuevas**. El propio informe aclara que faltan métricas de validación o prueba y que algunas capturas corresponden a épocas diferentes.", type="example"),
            section("Qué decisiones puedes probar", "Si hay subajuste, revisa datos, escalado, optimización y capacidad. Si hay sobreajuste, puedes evaluar menor capacidad, regularización, más datos adecuados o detener el entrenamiento según validación. Son posibilidades para contrastar, no una receta que siempre funcione.",
                    "Al comparar configuraciones, usa las mismas divisiones de datos y condiciones tanto como sea posible. Cambiar neuronas, épocas y datos simultáneamente impide atribuir con claridad el resultado a una sola decisión.", type="note"),
        ],
        "sources": [source(REPORT, 1, 2), source(BASIC, 3), source(CNN, 8, 19)],
        "questions": [
            choice("La pérdida de entrenamiento baja, pero la de validación sube durante varias épocas. ¿Qué debes sospechar?", ["Que ya no necesitas datos de prueba", "Que hay garantía de generalización", "Que Softmax dejó de sumar 1", "Posible sobreajuste"], 3, "La divergencia indica que mejorar los ejemplos conocidos puede estar perjudicando el desempeño sobre los reservados. Revisa la tendencia y las condiciones.", "DIAGNÓSTICO"),
            choice("¿Qué garantiza por sí solo llamar model.evaluate()?", ["Que los datos nunca se usaron para entrenar", "Que se calcularán pérdida y métricas sobre los datos entregados", "Que el modelo entrenará más épocas", "Que ya no puede haber sobreajuste"], 1, "El método no decide por ti qué datos están reservados. Si le pasas entrenamiento, evalúa entrenamiento."),
            choice("El modelo A obtiene 99 % en entrenamiento y 70 % en validación. B obtiene 92 % y 89 %. ¿Cuál parece generalizar mejor en esa validación?", ["A, porque 99 es el mayor número", "Ambos son iguales", "B, por su mejor resultado en validación", "No se puede observar ningún indicio"], 2, "En esos datos reservados, B tiene mejor rendimiento. La prueba final y una comparación controlada permiten evaluar con más confianza.", "APLICACIÓN"),
            open_question("¿Por qué el informe de 256 neuronas no permite afirmar que ese modelo sea siempre el mejor?", "Porque presenta principalmente métricas de entrenamiento, no el desempeño final sobre imágenes nuevas. Además, no todas las capturas muestran la misma época. Debe compararse validación o prueba bajo condiciones consistentes, considerando también el costo y el sobreajuste.", "Un número mayor de neuronas y una mejor métrica de entrenamiento no constituyen una garantía fuera de esos ejemplos.", ["métricas de entrenamiento", "condiciones comparables", "datos reservados"]),
        ],
    },
    {
        "id": "keras", "shortTitle": "Leer el código de Keras", "title": "Qué hace cada instrucción del modelo",
        "intro": "No necesitas memorizar un bloque de código sin entenderlo. Relaciona cada instrucción con una etapa: construir, preparar, entrenar y usar.",
        "sections": [
            section("Construir y compilar", "`Sequential` organiza capas que se aplican una detrás de otra. Una forma de entrada como `(4,)` indica cuatro características por ejemplo. `Dense(8, activation='relu')` crea una capa de ocho neuronas con ReLU.",
                    "`compile()` configura cómo se entrenará: optimizador, pérdida y métricas. Todavía no ajusta los pesos con tus ejemplos. Para tres clases con etiquetas enteras, puedes combinar tres salidas Softmax con sparse categorical crossentropy."),
            section("Un ejemplo completo para interpretar", code="model = tf.keras.Sequential([\n    tf.keras.Input(shape=(4,)),\n    tf.keras.layers.Dense(8, activation='relu'),\n    tf.keras.layers.Dense(3, activation='softmax')\n])\n\nmodel.compile(\n    optimizer='adam',\n    loss='sparse_categorical_crossentropy',\n    metrics=['accuracy']\n)\n\nhistory = model.fit(\n    X_train, y_train,\n    epochs=10, batch_size=32,\n    validation_data=(X_val, y_val)\n)\n\nloss, accuracy = model.evaluate(X_test, y_test)\nprobabilidades = model.predict(X_new)\nmodel.save('modelo.keras')"),
            section("Entrenar, evaluar y predecir", "`fit()` recorre ejemplos, calcula errores y actualiza parámetros. Su historial permite revisar pérdidas y métricas por época. Validación mide el rendimiento en el conjunto indicado sin usarlo para actualizar los pesos en esos pasos.",
                    "`evaluate()` calcula pérdida y métricas usando entradas y etiquetas. `predict()` genera salidas para las nuevas entradas; en este ejemplo devuelve tres probabilidades por fila. Para seleccionar la clase eliges la posición del valor mayor.",
                    "`save()` conserva el modelo en un archivo para volver a usarlo. Guardar un modelo no equivale a exportar solo sus predicciones."),
            section("Cómo se relaciona con el ejercicio de Colab", "El cuestionario de tus PDF menciona Colab como entorno de cuadernos que puede ofrecer aceleración de hardware. La idea evaluable es que una sesión de ejecución no debe confundirse con almacenamiento permanente: tienes que conservar los datos y guardar el modelo si quieres recuperarlos después.",
                    "Esta página no utiliza Colab ni conecta servicios. El código se muestra únicamente como material de estudio; no se ejecuta ni descarga datos desde aquí.", type="note"),
        ],
        "sources": [source(BASIC, 1, 2, 3), source(ONEHOT, 4), source(REVIEW, 1, 2)],
        "questions": [
            choice("¿Qué instrucción actualiza los parámetros a partir de los ejemplos de entrenamiento?", ["model.compile()", "model.predict()", "model.fit()", "model.save()"], 2, "Fit realiza el ciclo de aprendizaje. Compile configura ese ciclo, predict genera salidas y save guarda el modelo."),
            choice("Un clasificador con tres salidas Softmax recibe cinco ejemplos en predict(). ¿Qué estructura esperas?", ["Cinco filas con tres probabilidades cada una", "Tres archivos PDF", "Una sola probabilidad total para todo el conjunto", "Cinco etiquetas reales conocidas automáticamente"], 0, "Cada ejemplo produce su propio vector de tres probabilidades. Las etiquetas reales no aparecen automáticamente en predict().", "APLICACIÓN"),
            choice("¿Cuál es el propósito de validation_data dentro de fit()?", ["Duplicar el entrenamiento con las mismas etiquetas", "Guardar el modelo en la nube", "Cambiar automáticamente el número de clases", "Observar el desempeño en datos reservados durante el entrenamiento"], 3, "Se usa para monitorear cómo responde el modelo a ejemplos que no forman parte de las actualizaciones de entrenamiento."),
            open_question("Explica con tus palabras la diferencia entre compile, fit, evaluate y predict.", "Compile define cómo se entrenará, incluyendo optimizador y pérdida. Fit ajusta pesos usando ejemplos y etiquetas. Evaluate mide pérdida y métricas en los datos entregados. Predict genera salidas del modelo para las entradas que recibe.", "Una buena explicación distingue configuración, aprendizaje, medición y uso de la red. No todos esos métodos entrenan.", ["configurar", "ajustar parámetros", "medir con etiquetas", "generar predicciones"]),
        ],
    },
]
