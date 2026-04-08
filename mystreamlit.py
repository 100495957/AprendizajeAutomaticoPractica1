# Usamos IA generativa para el desarollo de este fichero debido a que no logramos entender como se implementaba de forma correcta el streamlit y a la hora de ejecutar nuestro 
# codigo nos daba errores que no eramos capaces de solucionar. Por ello, decidimos pedir ayuda a la IA para que nos generara un código funcional y que se ajustara a lo
#  que queríamos hacer, que era crear una aplicación web con streamlit para predecir si un cliente suscribirá un depósito a plazo en función de sus características 
# y datos de contacto.


import streamlit as st
import pandas as pd
import numpy as np
import joblib
from sklearn.preprocessing import FunctionTransformer

#funciones auxiliares del pipeline
def transform_pdays(X):
    vals = np.array(X).flatten()
    no_previo = (vals == -1).astype(int)
    dias = np.where(vals == -1, 0, vals)
    return np.column_stack((no_previo, dias))

def get_pdays_names(transformer, feature_names):
    return ['pdays_no_previo', 'pdays_dias']

#carga del modelo
@st.cache_resource
def cargar_modelo():
    return joblib.load('modelo_final.joblib')

modelo = cargar_modelo()

#configuración de la página
st.set_page_config(
    page_title="Predicción Depósito Bancario",
    page_icon="🏦",
    layout="centered"
)

st.title("🏦 Predicción de Subscripción a Depósito")
st.markdown(
    "Introduce los datos del cliente para predecir si suscribirá un depósito a plazo."
)
st.divider()

#formulario
st.subheader("Datos del cliente")

col1, col2 = st.columns(2)

with col1:
    st.markdown("**Perfil personal**")
    age = st.number_input("Edad", min_value=18, max_value=95, value=41)
    job = st.selectbox("Tipo de trabajo", [
        'admin.', 'blue-collar', 'entrepreneur', 'housemaid',
        'management', 'retired', 'self-employed', 'services',
        'student', 'technician', 'unemployed', 'unknown'
    ])
    marital = st.selectbox("Estado civil", ['married', 'single', 'divorced'])
    education = st.selectbox("Nivel de educación", ['secondary', 'tertiary', 'primary', 'unknown'])
    default = st.selectbox("¿Tiene crédito impagado?", ['no', 'yes'])
    balance = st.number_input("Balance anual medio (€)", min_value=-6847, max_value=81204, value=1529)
    housing = st.selectbox("¿Tiene hipoteca?", ['yes', 'no'])
    loan = st.selectbox("¿Tiene préstamo personal?", ['no', 'yes'])

with col2:
    st.markdown("**Datos del contacto**")
    contact = st.selectbox("Tipo de contacto", ['cellular', 'telephone', 'unknown'])
    day = st.number_input("Día del mes del último contacto", min_value=1, max_value=31, value=16)
    month = st.selectbox("Mes del último contacto", [
        'jan', 'feb', 'mar', 'apr', 'may', 'jun',
        'jul', 'aug', 'sep', 'oct', 'nov', 'dec'
    ])
    duration = st.number_input("Duración del último contacto (segundos)", min_value=0, max_value=3881, value=372)
    campaign = st.number_input("Nº contactos esta campaña", min_value=1, max_value=63, value=2)

    st.markdown("**Campaña anterior**")
    pdays = st.number_input(
        "Días desde último contacto previo (-1 = sin contacto)",
        min_value=-1, max_value=854, value=-1
    )
    previous = st.number_input("Nº contactos campañas anteriores", min_value=0, max_value=58, value=0)
    poutcome = st.selectbox("Resultado campaña anterior", ['unknown', 'failure', 'other', 'success'])

st.divider()

#predicción
if st.button("🔍 Predecir", use_container_width=True, type="primary"):

    input_data = pd.DataFrame([{
        'age': age,
        'job': job,
        'marital': marital,
        'education': education,
        'default': default,
        'balance': balance,
        'housing': housing,
        'loan': loan,
        'contact': contact,
        'day': day,
        'month': month,
        'duration': duration,
        'campaign': campaign,
        'pdays': pdays,
        'previous': previous,
        'poutcome': poutcome
    }])

    prediccion = modelo.predict(input_data)[0]
    probabilidad = modelo.predict_proba(input_data)[0][1]

    st.subheader("Resultado de la predicción")

    if prediccion == 1:
        st.success(f"✅ **El cliente SÍ suscribirá el depósito**")
    else:
        st.error(f"❌ **El cliente NO suscribirá el depósito**")

    st.metric(
        label="Probabilidad de suscripción",
        value=f"{probabilidad * 100:.1f}%"
    )

    st.progress(float(probabilidad))

    with st.expander("Ver datos introducidos"):
        st.dataframe(input_data.T.rename(columns={0: 'Valor'}))
