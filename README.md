# Data Skills Exhibition - Chess Performance Analysis
## Project Overview
This project showcases many of my skills that are applicable to a data science role. The goal of this project is to transform chess improvement from intuition-based experimentation to data-driven, purposeful training. By systematically analyzing data from thousands of Chess.com games, I am able to uncover patterns in opening choice, move accuracy, time management, and tactical errors for players seeking to train more effectively. Using these insights, I am able to provide trustworthy direction to the areas in a player's game with the highest potential for rating improvement. 
## Introduction
Every move played between public Chess.com accounts generates game data which is saved to archives pointing to each competitor. Metadata, move choices, and time management data lay dormant in these archives, rich with untapped improvement potential, but is effectively unreadable to the human eye. This project extracts and processes that data, applies machine learning techniques to uncover hidden patterns in player behavior, and generates reports that illustrate concrete improvement opportunities invisible through casual analysis.
## Directory Structure
### `Data/`
Stores all raw, intermediate, and polished data files.
Example contents:
* PGN game files (raw data)
* CSV exports of move and metadata dataframes
* DuckDB databases of cleaned metadata and movedata
This folder is mounted as a volume in docker