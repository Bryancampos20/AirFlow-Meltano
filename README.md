## Apache Airflow Project for Meltano Pipeline

This project uses Apache Airflow to automate the execution of a Meltano pipeline consisting of CSV extractors and loaders. The main goal is to streamline the scheduling and execution of this workflow efficiently.

## Requirements

- Python 3.x installed on your system.
- Apache Airflow installed in your environment.
- Meltano installed in your environment.

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
