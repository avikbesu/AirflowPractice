# Airflow on docker

[![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/avikbesu/AirflowPractice)](#)
[![GitHub issues](https://img.shields.io/github/issues-raw/avikbesu/AirflowPractice)](#)
[![GitHub commit activity](https://img.shields.io/github/commit-activity/m/avikbesu/AirflowPractice)](#)

### How to start airflow on docker

##### *Airflow 1.10.14*
For airflow 1.10.14, go to `airflow_v1` folder and execute this command: `docker-compose -f docker-compose.yml up`

**Ref**: https://towardsdatascience.com/apache-airflow-and-postgresql-with-docker-and-docker-compose-5651766dfa96

##### *Airflow 2.0.0*
For airflow 2, go to `airflow_v2` folder and execute this command: `docker-compose -f docker-compose.yml up`

**Ref**: https://github.com/apache/airflow/blob/master/docs/apache-airflow/start/docker-compose.yaml

------

### What is Airflow ?

Airflow is a platform to programmatically author, schedule and monitor workflows.

Airflow is not a data streaming solution. Tasks do not move data from one to the other (though tasks can exchange metadata!). Airflow is not in the `Spark Streaming` or `Storm` space, it is more comparable to `Oozie` or `Azkaban`.

### Basic Architecture

![arch](https://airflow.apache.org/docs/apache-airflow/2.0.0/_images/arch-diag-basic.png)

There are a few components to note:

**Metadata Database**: Airflow uses a SQL database to store metadata about the data pipelines being run. In the diagram above, this is represented as Postgres which is extremely popular with Airflow. Alternate databases supported with Airflow include MySQL.

**Web Server** and **Scheduler**: The Airflow web server and Scheduler are separate processes run (in this case) on the local machine and interact with the database mentioned above.

The **Executor** is shown separately above, since it is commonly discussed within Airflow and in the documentation, but in reality it is NOT a separate process, but run within the Scheduler.

The **Worker(s)** are separate processes which also interact with the other components of the Airflow architecture and the metadata repository.

***airflow.cfg*** is the Airflow configuration file which is accessed by the Web Server, Scheduler, and Workers.

DAGs refers to the DAG files containing Python code, representing the data pipelines to be run by Airflow. The location of these files is specified in the Airflow configuration file, but they need to be accessible by the Web Server, Scheduler, and Workers.

---



### LINKS

#### Tutorials

 - https://github.com/jghoman/awesome-apache-airflow

 - https://airflow.apache.org/docs/apache-airflow/stable/tutorial.html

#### Sample Codes

##### job triggering sample

 - https://stackoverflow.com/questions/61514887/how-to-trigger-a-dag-on-the-success-of-a-another-dag-in-airflow-using-python

 - https://stackoverflow.com/questions/47103160/run-another-dag-with-triggerdagrunoperator-multiple-times

 - https://kuanbutts.com/2020/05/31/airflow-dags-trigger-external-with-context/

 - https://stackoverflow.com/questions/45271532/in-airflow-is-there-a-good-way-to-call-another-dags-task **[Working]**

##### custom operator

 - https://michal.karzynski.pl/blog/2017/03/19/developing-workflows-with-apache-airflow/ **[Working]**

 
