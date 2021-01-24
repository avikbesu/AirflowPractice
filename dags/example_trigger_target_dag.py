"""
Example usage of the TriggerDagRunOperator. This example holds 2 DAGs:
1. 1st DAG (example_trigger_controller_dag) holds a TriggerDagRunOperator, which will trigger the 2nd DAG
2. 2nd DAG (example_trigger_target_dag) which will be triggered by the TriggerDagRunOperator in the 1st DAG
"""

from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator
from airflow.utils.dates import days_ago


def run_this_func(**context):
    """
    Print the payload "message" passed to the DagRun conf attribute.
    :param context: The execution context
    :type context: dict
    """
    print("I am here")
    print(context)
    #print(f"Remotely received value of {context['dag_run'].conf['message']} for key=message")


with DAG(
    dag_id="example_trigger_target_dag",
    default_args={"owner": "airflow"},
    start_date=days_ago(2),
    schedule_interval=None,
    tags=['example'],
) as dag:

    run_this = PythonOperator(task_id="run_this", python_callable=run_this_func)

    bash_task = BashOperator(
        task_id="bash_task",
        bash_command='echo "Here is the message: $message"',
        env={'message': '{{ dag_run.conf["message"] if dag_run else "" }}'},
    )