# README 

## ANALYSIS DATA
this folder includes file analysis_data.csv, which is the result of running the script from CommandFiles\Preprocessing.ipynb

## COMMAND FILES
this folder contains only one file - Preprocessing.ipynb. That file contains all code used to prepare original data for analysis.

## DOCUMENTS
in this catalogue you will find data_appendix that provides information about processed data - Analysis Data

## ORIGINAL DATA 
this folder contains all original data and subfolder MetaData that includes metadata guide, which provides information about original data

## HOW TO REPLICATE STUDY
to replicate results the user must only run script written in CommandFiles\Preprocessing.ipynb, 
script requires access to data file - earthquake_data.csv. 
After running Preprocessing.ipynb the result should be the creation of analysis_data.csv, 
which should contain table consisting of respondents age, gender and answer to question "Do you think the "Big One" will occur in your lifetime?"

The study was conducted using Jupyter running on Python 3.8.3 (64-bit) (conda) kernel with installed packages: 'pandas' and 'matplotlib'. Operational system used was Windows 10 Home.