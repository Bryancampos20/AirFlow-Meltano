## Apache Airflow Project for Meltano Pipeline

This project uses Apache Airflow to automate the execution of a Meltano pipeline consisting of CSV extractors and loaders. The main goal is to streamline the scheduling and execution of this workflow efficiently.

## Requirements

- Python 3.x installed on your system.
- Apache Airflow installed in your environment.
- Meltano installed in your environment.

## Before running 

1. On `/meltano/files_def.json` please add the path where the csv file is. In this project is located in `/meltano/input/CSV-Template1.csv`
2. On `/dags/meltano_pipeline.py` please add the path where `meltano` is located.
3. Please keep in mind that this is a local project thats why we have to set the paths

## Execution

1. Run the following command to execute the project in the local environment

```bash
airflowctl start 
```

## Results

1. This is the dashboard where you can see the DAG before it is executed.

![Screenshot (160)](https://github.com/Bryancampos20/AirFlow-Meltano/blob/main/results/dashboard.png)

2. This is the graphical view where we can see that it executed successfully.

![Screenshot (160)](https://github.com/Bryancampos20/AirFlow-Meltano/blob/main/results/graph.png)

3. Here are the logs

![Screenshot (160)](https://github.com/Bryancampos20/AirFlow-Meltano/blob/main/results/logs.png)

4. This is the output after executing the pipeline

![Screenshot (160)](https://github.com/Bryancampos20/AirFlow-Meltano/blob/main/results/csv.png)

This is a basic example of how we can run a Meltano command in Apache Airflow.

Happy coding! 🚀
