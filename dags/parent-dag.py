# from datetime import datetime, timedelta
# from airflow import DAG
# from airflow.operators.dummy_operator import DummyOperator
# from airflow.utils import dates

# default_args = {
#     "owner": "airflow",
#     "depends_on_past": False,
#     "start_date": dates.days_ago(1),
# }

# dag = DAG('Parent_dag', default_args=default_args, schedule_interval=timedelta(minutes=5))

# leave_work = DummyOperator(
#     task_id='leave_work',
#     dag=dag,
# )
# cook_dinner = DummyOperator(
#     task_id='cook_dinner',
#     dag=dag,
# )

# leave_work >> cook_dinner