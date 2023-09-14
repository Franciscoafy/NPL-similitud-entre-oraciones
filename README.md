Proyecto de Análisis de Similitud de Oraciones con DistilRoBERTa

Este proyecto utiliza el modelo preentrenado DistilRoBERTa-base para analizar la similitud entre una serie de oraciones. El objetivo principal es determinar si dos oraciones son sinónimos o no.

Descripción del Proyecto

Uso del Model

El modelo DistilRoBERTa-base se utiliza para calcular la similitud entre dos oraciones proporcionadas como entrada. Utilizamos este modelo para obtener una puntuación que indica cuán similares son las oraciones. Cuanto más alta sea la puntuación, mayor será la similitud entre las oraciones.

Datos de Entrenamiento

Los datos de entrenamiento se obtuvieron del conjunto de datos GLUE (General Language Understanding Evaluation) al seleccionar el subconjunto MRPC (Microsoft Research Paraphrase Corpus). Estos datos se utilizaron para entrenar el modelo en la tarea de detección de similitud de oraciones.

Métricas del Modelo

El modelo entrenado ha demostrado un buen rendimiento en la tarea de detección de similitud de oraciones. A continuación se presentan las métricas obtenidas:

Loss: 0.7184
Accuracy: 0.8456
F1 Score: 0.8869
Estas métricas indican que el modelo tiene una alta precisión y capacidad para identificar oraciones sinónimas.

Conclusiones

El proyecto muestra cómo utilizar el modelo preentrenado DistilRoBERTa-base para analizar la similitud de oraciones. Con las métricas de rendimiento obtenidas, podemos confiar en que el modelo es capaz de identificar eficazmente si dos oraciones son sinónimas o no.