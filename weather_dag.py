from airflow import DAG
from airflow.operators.python_operator import PythonOperator # type: ignore
from airflow.utils.dates import days_ago

# Importing the task functions
from script.extract import extract_data
from script.transform import transform_data
from script.load import load_data

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
}

dag = DAG(
    'weather',
    default_args=default_args,
    description='daily weather data',
    schedule_interval='@daily',
    start_date=days_ago(1),
    catchup=False,
)

# Define the path to your file
file_path = '/home/artiana/airflow/WEATHER-DAG/data/raw/Geographic_Data.csv'

# Define the tasks with arguments
extract_data_task = PythonOperator(
    task_id='extract_data',
    python_callable=extract_data,
    op_args=[file_path],  # Pass the file path argument here
    dag=dag,
)

transform_task = PythonOperator(
    task_id='transform_data',
    python_callable=transform_data,
    dag=dag,
)

load_task = PythonOperator(
    task_id='load_data',
    python_callable=load_data,
    dag=dag,
)

# Set the task dependencies
extract_data_task >> transform_task >> load_task
