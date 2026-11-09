# Redes neuronales · Explica y practica

Una sola página local con **13 temas explicados y 52 preguntas** basados en los PDF de esta carpeta. Elige un tema en el índice, lee la explicación y contesta las preguntas que aparecen debajo.

## Abrir

Haz doble clic en **Iniciar.cmd**. Se abre **http://127.0.0.1:8501** en tu navegador. Mantén abierta la ventana de inicio; para detener el servidor pulsa Ctrl+C.

Necesita Python 3.11 o posterior. **No requiere Streamlit, Ollama, modelos, cuentas, internet ni paquetes adicionales.** Si la página ya está ejecutándose, el lanzador abre la misma instancia.

También puedes usar `python run_local.py`.

## Contenido

- Red neuronal, entradas, pesos y capas.
- Normalización, Min-Max y estandarización.
- One-hot y representación de categorías.
- Activaciones: ReLU, Sigmoid, Softmax, Tanh y Leaky ReLU.
- Salidas, tipos de predicción y funciones de pérdida.
- Entrenamiento, épocas, lotes, gradientes y learning rate.
- Accuracy, precision, recall y matriz de confusión.
- Imágenes, canales, MNIST, Fashion MNIST y CIFAR-10.
- Convolución, filtros, dimensiones y parámetros.
- Pooling y sus diferencias con la convolución.
- Arquitectura completa de una CNN.
- Validación, sobreajuste y análisis del informe de neuronas.
- Interpretación de código con Keras.

Las explicaciones están redactadas y disponibles desde el inicio; no hay que generarlas. Los ejemplos numéricos desarrollan los conceptos de los apuntes. Las aclaraciones señalan errores del material, como la confusión entre falsos positivos y negativos y el rango de píxeles de 8 bits.

Cada tema contiene tres preguntas de selección y una abierta. Las de selección se corrigen con una explicación. En la abierta, primero escribes tu respuesta y después se muestra una respuesta de referencia y las ideas que debes haber mencionado; no se inventa una nota automática. Puedes volver a intentarlas.

En «Ver las páginas del material» puedes abrir los PDF originales en otra pestaña. La numeración corresponde a páginas físicas comenzando en 1.

Las respuestas se conservan en el almacenamiento local de ese navegador. No se envían al servidor. Si borras los datos del sitio, se borran esos intentos. La página solo sirve archivos locales, escucha en 127.0.0.1 y bloquea recursos de terceros mediante una política de contenido. No hay telemetría ni búsquedas web.

Los documentos originales y la base de datos de la versión anterior permanecen intactos. La interfaz anterior y sus funciones administrativas ya no se utilizan.

## Archivos y comprobaciones

- `public/index.html`, `styles.css`, `app.js`: página y preguntas interactivas.
- `course_content.py`: explicaciones, respuestas y referencias redactadas para el curso.
- `build_course.py`: prepara `public/course.js` después de editar los contenidos.
- `run_local.py`: servidor local, sin dependencias externas.

Para regenerar el contenido ejecuta `python build_course.py`.

Para comprobar el funcionamiento:

```powershell
python -m unittest discover -s tests -v
node tests/test_page.js
```

Node solo se necesita para la comprobación del código JavaScript; la página no lo necesita para ejecutarse.
