Práctica 1: Aprendizaje Automático - Clasificación Bancaria y Despliegue

Este repositorio contiene la solución a la Práctica 1 de la asignatura Aprendizaje Automático de la Universidad Carlos III de Madrid (UC3M).

El objetivo principal de este proyecto es realizar un Análisis Exploratorio de Datos (EDA), preprocesar un conjunto de datos del ámbito bancario, entrenar y evaluar modelos de aprendizaje automático supervisado, y desplegar la solución final mediante una aplicación web interactiva.

Estructura del Repositorio

notebook_principal.ipynb: Notebook de Jupyter que contiene todo el flujo de trabajo: Análisis Exploratorio de Datos (EDA), preprocesamiento, selección e ingeniería de características, e higiene de datos, así como el entrenamiento y validación de los modelos.

notebook_predicciones.ipynb: Notebook enfocado exclusivamente en cargar el modelo entrenado y generar las predicciones sobre el conjunto de test/competición.

bank_15.pkl y bank_competition.pkl: Datasets guardados en formato pickle utilizados para el desarrollo, validación y prueba del modelo.

modelo_final.pkl y modelo_final.joblib: Archivos con el modelo predictivo final serializado para su reutilización inmediata en producción o inferencia.

predicciones.csv: Fichero resultante con la versión final de las predicciones generadas para el conjunto de competición.

mystreamlit.py: Aplicación desarrollada en Streamlit para ofrecer una interfaz interactiva e intuitiva con el modelo predictivo.

README.md: Fichero de documentación del repositorio.

Metodología y Flujo de Trabajo

El proyecto sigue un pipeline completo de Ciencia de Datos:

Análisis Exploratorio de Datos (EDA): Identificación de patrones, distribuciones, relaciones entre variables y tratamiento de valores nulos o atípicos.

Preprocesamiento: Escalado de variables numéricas, codificación de variables categóricas y balanceo de datos en caso de ser necesario.

Modelado y Evaluación: Entrenamiento de distintos clasificadores supervisados, optimización de hiperparámetros y selección del modelo con mejor rendimiento.

Inferencia: Carga del modelo optimizado desde archivo serializado y generación del archivo predicciones.csv.

Despliegue: Creación de una aplicación web ligera mediante Streamlit que permite realizar predicciones interactivas en tiempo real.

Requisitos e Instalación

Para ejecutar los notebooks de Jupyter o lanzar la aplicación web localmente, asegúrate de instalar las dependencias necesarias:

pip install pandas numpy scikit-learn joblib matplotlib seaborn streamlit


Despliegue de la Aplicación (Streamlit)

Para lanzar la interfaz gráfica desarrollada con Streamlit, abre la terminal en la raíz del repositorio y ejecuta:

streamlit run mystreamlit.py
