"""
### Tutorial Documentation
Documentation that goes along with the Airflow tutorial located
[here](https://airflow.apache.org/tutorial.html)
"""
# [START tutorial]
# [START import_module]
from datetime import timedelta
from textwrap import dedent

# The DAG object; we'll need this to instantiate a DAG
from airflow import DAG

# Operators; we need this to operate!
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from airflow.utils.dates import days_ago
from airflow.models import Variable

import helper

# [END import_module]

# [START default_args]
# These args will get passed on to each operator
# You can override them on a per-task basis during operator initialization
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email': ['airflow@example.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
    # 'queue': 'bash_queue',
    # 'pool': 'backfill',
    # 'priority_weight': 10,
    # 'end_date': datetime(2016, 1, 1),
    # 'wait_for_downstream': False,
    # 'dag': dag,
    # 'sla': timedelta(hours=2),
    # 'execution_timeout': timedelta(seconds=300),
    # 'on_failure_callback': some_function,
    # 'on_success_callback': some_other_function,
    # 'on_retry_callback': another_function,
    # 'sla_miss_callback': yet_another_function,
    # 'trigger_rule': 'all_success'
}
# [END default_args]

# [START instantiate_dag]
with DAG(
    'mytutorial',
    default_args=default_args,
    description='A simple tutorial DAG',
    schedule_interval=timedelta(days=1),
    start_date=days_ago(2),
    tags=['avikm'],
) as dag:
    # [END instantiate_dag]

    # t1, t2 and t3 are examples of tasks created by instantiating operators
    # [START basic_task]
    t1 = BashOperator(
        task_id='print_date',
        bash_command='date',
    )

    t2 = BashOperator(
        task_id='sleep',
        depends_on_past=False,
        bash_command='sleep 5',
        retries=3,
    )
    # [END basic_task]

    # [START documentation]
    t1.doc_md = __doc__

    dag.doc_md = dedent(
        """\
    #### Task Documentation
    You can document your task using the attributes `doc_md` (markdown),
    `doc` (plain text), `doc_rst`, `doc_json`, `doc_yaml` which gets
    rendered in the UI's Task Instance Details page.
    ![img](http://montcs.bloomu.edu/~bobmon/Semesters/2012-01/491/import%20soul.png)
    """
    )
    # [END documentation]

    # [START jinja_template]
    templated_command = dedent(
        """
    {% for i in range(5) %}
        echo "{{ ds }}"
        echo "{{ macros.ds_add(ds, i)}}"
        echo "{{ params.my_param }}"
    {% endfor %}
    echo "{{ dag_run.conf }}"
    """
    )

    t3 = BashOperator(
        task_id='templated',
        depends_on_past=False,
        bash_command=templated_command,
        params={'my_param': 'Parameter I passed in'},
    )
    # [END jinja_template]

    # [START python_task]
    # def print_context(ds, **kwargs):
    #     """Print the Airflow context and ds variable from the context."""
    #     print(kwargs)
    #     print(ds)
    #     return 'Whatever you return gets printed in the logs'

    t4 = PythonOperator(
        task_id='print_the_context',
        python_callable=helper.print_context,
        dag=dag,
    )
    # [END python_task]

    # [START python variable]
    #hello = context['dag_run'].conf['key'] #"Hello User"
    t5 = BashOperator(
        task_id="bash_task",
        bash_command='echo "here is the message: \'$message\'"',
        env={'message': '{{ dag_run.conf["message"] if dag_run else "" }}'},
    )

    t6 = PythonOperator(
        task_id='python_task',
        provide_context=True,
        python_callable=helper.get_message,
        dag=dag,
    )

    message = Variable.get('stupid')

    t7 = BashOperator(
        task_id="print_variable",
        bash_command='echo "$message is stupid"',
    )

    # [END python variable]

    t1 >> [t2, t3] >> t4 >> [t5, t6, t7]
# [END tutorial]