# Data Skills Exhibition - Chess Performance Analysis
## Project Overview
This project showcases many of my skills that are applicable to a data science role. The goal of this project is to transform chess improvement from intuition-based experimentation to data-driven, purposeful training. By systematically analyzing data from thousands of Chess.com games, I am able to uncover patterns in opening choice, move accuracy, time management, and tactical errors for players seeking to train more effectively. Using these insights, I am able to provide trustworthy direction to the areas in a player's game with the highest potential for rating improvement.
## Skill Exibition
### Python
* Utilizing Python to automate the ingestion, synthesis, and cleaning of data through a web API
* Demonstrating object oriented programming for data preparation
* Experience with pandas, NumPy, and matplotlib libraries
### PostgreSQL
* Designed and managed Dockerized PostgreSQL databases for analytics pipielines
* Created user-specific databases and tables using SQLAlchemy and Python
* Migrated Pandas dataframes into Postgres for queryable storage
* Tested database connectivity and handled credentials/configuration within containers
### SQL
* Advanced querying techiques to investigate patterns in data
* Utilizing SQLAlchemy for Object-Relational Mapping
* PostgreSQL connection for future scalability
### Machine Learning
* Used linear regression to predict favorable areas of improvement
* Experience with scikit-learn library
### GitHub
* Using Git version control to organize updates
* Using GitHub to publish the project and encourage collaboration
* Using `git branch` to test functionality and merge features
* Using `git reset` to default to previous commit hashes
### Docker
* Using Docker to guaruntee reproducibility
* Mounting volumes for data persistence
## Introduction
Every move played between public Chess.com accounts generates game data which is saved to archives pointing to each competitor. Metadata, move choices, and time management data lay dormant in these archives, rich with untapped improvement potential, but is effectively unreadable to the human eye. This project extracts and processes that data, applies machine learning techniques to uncover hidden patterns in player behavior, and generates reports that illustrate concrete improvement opportunities invisible through casual analysis.
## Directory Structure
### `Ingestion/`
Files for online data ingestion and initial formating
Example contents:
* download_pgn.py: ingests user data from Chess.com archives
* metadata.py, movedata.py: formatting classes
### `Processing/`
Files for data cleaning and evaluation
Example contents:
* cleanmeta.py: removal of unecessary table columns
* add_eval: Stockfish evaluation of position data
### `Data/`
A backup for all raw, intermediate, and polished data files during the preparation process
Example contents:
* PGN game files (raw data)
* CSV exports of move and metadata dataframes
* CSV exports of cleaned data
This folder is mounted into the container viea a Docker volume
### `Analysis/`
Data inspection and database management
Example contents:
* Pipeline testing scripts
* User performance metrics calculations
## More Information
### Stockfish Engine
This project uses a locked Stockfish version for reproducibility:
* Stockfish 17.1 (Linux x64, AVX2 build)
* Installed at image build time (not user-provided)
* Fixed engine configuration (threads and hash size)