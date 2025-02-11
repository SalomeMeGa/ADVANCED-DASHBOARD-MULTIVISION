from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from datetime import datetime

# Argumentos predeterminados para el DAG
default_args = {
    'owner': 'airflow',
    'start_date': datetime(2025, 1, 1),  # Fecha de inicio del DAG
    'retries': 2  # Número de intentos si una tarea falla
}

# Definir el DAG
dag = DAG(
    'simple_dag',  # Nombre único del DAG
    default_args=default_args,  # Argumentos predeterminados
    description='Un simple DAG',  # Descripción del DAG
    schedule_interval='@daily',  # Intervalo de programación (en este caso, diario)
)

# Crear una tarea Dummy que no hace nada, solo sirve para la demostración
start_task = DummyOperator(
    task_id='start',  # Identificador único de la tarea
    dag=dag,  # DAG al que pertenece la tarea
)

# Configura la secuencia de ejecución de las tareas (en este caso, solo tenemos una tarea)
start_task
