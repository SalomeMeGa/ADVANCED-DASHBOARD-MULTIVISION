import streamlit as st

# Título del Dashboard
st.title("Dashboard de Multivisión")

# Texto de bienvenida
st.write("Bienvenido al Dashboard de monitoreo de datos.")

# Agregar un gráfico de ejemplo
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Crear datos de ejemplo
data = pd.DataFrame(np.random.randn(20, 3), columns=['A', 'B', 'C'])

# Mostrar datos
st.write("Datos de muestra:", data)

# Crear gráfico de líneas
st.line_chart(data)

