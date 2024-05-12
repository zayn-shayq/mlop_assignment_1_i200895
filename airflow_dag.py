from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2023, 1, 1),
    'retries': 2,
    'retry_delay': timedelta(minutes=5),
    'email_on_failure': False,
    'email_on_retry': False
}

dag = DAG('article_extraction_pipeline',
          default_args=default_args,
          schedule_interval='@daily',
          catchup=False)

def extract_transform_save():
    from data_extraction import extract_data
    from data_storage import save_data
    # Assuming the transformation is a separate module or function
    # from data_transformation import transform_data

    dawn_articles = extract_data('https://www.dawn.com')
    bbc_articles = extract_data('https://www.bbc.com')
    # Transform data if necessary (not shown here)
    # transformed_dawn = transform_data(dawn_articles)
    # transformed_bbc = transform_data(bbc_articles)
    save_data(dawn_articles, 'dawn_data.csv')
    save_data(bbc_articles, 'bbc_data.csv')

task1 = PythonOperator(
    task_id='extract_transform_save',
    python_callable=extract_transform_save,
    dag=dag
)

if __name__ == "__main__":
    from airflow.utils.state import State
    dag.clear(dag_run_state=State.NONE)
    dag.run()
