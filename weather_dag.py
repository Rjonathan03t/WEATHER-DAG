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

# Define the tasks
extract_data = PythonOperator(
    task_id='extract_data',
    python_callable=extract_data,
    dag=dag,
)

transform = PythonOperator(
    task_id='transform_data',
    python_callable=transform_data,
    dag=dag,
)

load = PythonOperator(
    task_id='load_data',
    python_callable=load_data,
    dag=dag,
)

# Set the task dependencies
[extract_data] >> transform >> load
