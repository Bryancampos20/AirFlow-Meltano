from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.operators.bash_operator import BashOperator
import subprocess

dag_id = 'meltano_pipeline'

default_args = {
    "owner": "airflow",
    "start_date": datetime(2023, 10, 3),
    "retry_delay": timedelta(seconds=10),
}

dag = DAG(
    dag_id,
    default_args=default_args,
    description='Ejecutar Meltano Pipeline v3',
)

meltano_directory = 'MELTANO_DIRECTORY'

meltano_command = f'cd {meltano_directory} && meltano run tap-csv target-csv'

run_meltano_task = BashOperator(
    task_id='run_meltano',
    bash_command=meltano_command,
    dag=dag,
)