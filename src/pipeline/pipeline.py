from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

# Define Task 1
def preprocess_data():
    print("Preprocessing data___")

## Define Task 2
def train_model():
    print("Train Model___")

## Define Task 3
def evaluate_model():
    print("Evaluate Modle____")

## Define the DAG

with DAG(
    'dynamic_price_model',
    start_date = datetime(2025,4,1),
    schedule_interval = '@weekly'
) as dag:
    
    ## Define the task
    preprocess = PythonOperator(task_id="preprocess_task",python_callable=preprocess_data)
    train = PythonOperator(task_id="train_task",python_callable=train_model)
    evaluate = PythonOperator(task_id="evaluate_task",python_callable=evaluate_model)

    ## Set the Order at which it will be executed (Dependencies)
    preprocess >> train >> evaluate