from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.utils import dates
from airflow.operators import MyFirstOperator

default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "start_date": dates.days_ago(2),
}

dag = DAG('Parent_dag', default_args=default_args, schedule_interval=timedelta(days=1))

leave_work = MyFirstOperator(
	my_operator_param='leave_work...',
    task_id='leave_work', 
    dag=dag,
)
cook_dinner = MyFirstOperator(
	my_operator_param='cook_dinner!!!',
    task_id='cook_dinner',
    dag=dag,
)

leave_work >> cook_dinner