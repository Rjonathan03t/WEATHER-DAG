from datetime import timedelta
from airflow.utils.task_group import TaskGroup
from airflow import DAG
from airflow.operators.python_operator import PythonOperator # type: ignore
from airflow.utils.dates import days_ago

from script.extract import extract_demographic
from script.extract import extract_geographic
from script.transform import merge_pollution_to_demographic
from script.transform import merge_pollution_to_geographic
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
    schedule_interval=timedelta(hours=2),
    start_date=days_ago(1),
    catchup=False,
)


with TaskGroup("extract_tasks", dag=dag) as extract_tasks:
    extract_demographic = PythonOperator(
        task_id='extract_demographic',
        python_callable=extract_demographic,
    )

    extract_geographic = PythonOperator(
        task_id='extract_geographic',
        python_callable=extract_geographic,
    )


with TaskGroup("transformation_tasks" , dag=dag) as transformation_tasks:
    merge_pollution_to_geographic = PythonOperator(
    task_id='merge_pollution_to_geographic',
    python_callable=merge_pollution_to_geographic,
    dag=dag,
)
    merge_pollution_to_demographic = PythonOperator(
        task_id='merge_pollution_to_demographic',
        python_callable=merge_pollution_to_demographic,
        dag=dag
    )


load_task = PythonOperator(
    task_id='load_data',
    python_callable=load_data,
    dag=dag,
)

extract_tasks >> transformation_tasks >> load_task