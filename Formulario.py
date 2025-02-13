conda install -c conda-forge openpyxl
import streamlit as st
import openpyxl
import os

# Archivo donde se guardarán los datos
archivo = "empleados.xlsx"

def guardar_datos(nombre, edad, puesto, salario):
    """Guarda los datos ingresados en un archivo Excel."""
    if os.path.exists(archivo):
        wb = openpyxl.load_workbook(archivo)
        ws = wb.active
    else:
        wb = openpyxl.Workbook()
        ws = wb.active
        ws.append(["Nombre", "Edad", "Puesto", "Salario"])  # Encabezados

    ws.append([nombre, edad, puesto, salario])
    wb.save(archivo)

    st.success("✅ Datos guardados correctamente en empleados.xlsx")

# Crear la interfaz en Streamlit
st.title("📋 Formulario de Empleados")

nombre = st.text_input("Nombre")
edad = st.number_input("Edad", min_value=18, max_value=100, step=1)
puesto = st.text_input("Puesto")
salario = st.number_input("Salario", min_value=0.0, step=0.01)

if st.button("Guardar"):
    if nombre and edad and puesto and salario:
        guardar_datos(nombre, edad, puesto, salario)
    else:
        st.error("⚠️ Todos los campos son obligatorios")
