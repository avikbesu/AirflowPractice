# Airflow on docker

[![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/avikbesu/AirflowPractice)](#)
[![GitHub issues](https://img.shields.io/github/issues-raw/avikbesu/AirflowPractice)](#)
[![GitHub commit activity](https://img.shields.io/github/commit-activity/m/avikbesu/AirflowPractice)](#)

### How to start airflow on docker

##### *Airflow 1.10.14*
For airflow 1.10.14, go to `airflow_v1` folder and execute this command: `docker-compose -f docker-compose.yml up`.

**Ref**: https://towardsdatascience.com/apache-airflow-and-postgresql-with-docker-and-docker-compose-5651766dfa96

##### *Airflow 2.0.0*
For airflow 2, go to `airflow_v2` folder and execute this command: `docker-compose -f docker-compose.yml up`.

**Ref**: https://github.com/apache/airflow/blob/master/docs/apache-airflow/start/docker-compose.yaml

### tutorials

 - https://github.com/jghoman/awesome-apache-airflow

 - https://airflow.apache.org/docs/apache-airflow/1.10.14/tutorial.html

### Sample codes

##### job triggering sample

 - https://stackoverflow.com/questions/61514887/how-to-trigger-a-dag-on-the-success-of-a-another-dag-in-airflow-using-python

 - https://stackoverflow.com/questions/47103160/run-another-dag-with-triggerdagrunoperator-multiple-times

 - https://kuanbutts.com/2020/05/31/airflow-dags-trigger-external-with-context/

 - https://stackoverflow.com/questions/45271532/in-airflow-is-there-a-good-way-to-call-another-dags-task **[Working]**

##### custom operator

 - https://michal.karzynski.pl/blog/2017/03/19/developing-workflows-with-apache-airflow/ **[Working]**

 
