# Data-pipelines-project

## Overview
This project forms part of Udacity's data Engineering Nanodegree

A music streaming company, Sparkify, has decided that it is time to introduce more automation and 
monitoring to their data warehouse ETL pipelines and come to the conclusion that the best tool to 
achieve this is Apache Airflow.

This project aims to create a high grade data pipeline that is dynamic and built from reusable tasks, 
can be monitored, and allows for easy backfills. Data quality plays a big part when analyses are 
executed on top the data warehouse and so tests should be run against the datasets after the ETL steps 
have been executed to catch any discrepancies in the datasets.

The source data resides in S3 and needs to be processed in Sparkify's data warehouse in Amazon Redshift. 
The source datasets consist of JSON logs that tell about user activity in the application and JSON 
metadata about the songs the users listen to.

## Datasets

The source data can be find in S3 under the following links:

1. Log data: s3://udacity-dend/log_data
2. Song data: s3://udacity-dend/song_data

## Files

1. etl.dag: contains all the imports, tasks and task dependecies to run the pipeline
2. state_redshift.py: operator which stages the song and events tables
3. load_fact.py: operator to load data into the fact (songplays) table
4. load_dimension.py: operator to load data into the dimension tables (users, artists, songs and time)
5. data_quality.py: operator to perform quality checks on output tables


