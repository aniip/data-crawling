from airflow import DAGS
from airflow.oeprators.python import PythonOperator

# script to crawl
# script to insert 

with DAGS(
    "dags_scraping",
    description="Scraping data...",
    schedule="*/5 * * * *"
) as dag:    
    task = PythonOperator(
        task_id="",
        python_callable=None
    )
    
    # task1 > task2