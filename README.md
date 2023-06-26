# DBL

This repository has been created to fulfill the requirements of the JBG030 course at the Technical University of Eindhoven.

## Overview

This repository contains multiple files, each serving a specific purpose.

- `DataBaseCreation.ipynb`: This Jupyter Notebook contains the code to create the 'dbl_10' database. The database size is approximately 6.6 GB.

- `ConversationMining.ipynb`: This file is designed to mine and analyze conversations from the dataset. It provides functions to extract conversations from CSV files, with each file representing a different airline. You can explore various statistics for the selected airline.

- `SentimentAnalysis.ipynb`: In this notebook, sentiment analysis is performed on all the tweets in the database using the Vader sentiment analysis tool accessed via NLTK. The notebook creates four new columns for each tweet: 'pos', 'neu', 'neg', and 'compound'. Please note that the sentiment analysis process may take a significant amount of time due to the size of the dataset.

- `SentimentAnalysis_French&Spanish.ipynb`: This notebook focuses on sentiment analysis of Spanish and French tweets (identified by the 'lang' column) for the customer AmericanAir and the competitor AirFrance. It explores the potential of responding to Spanish tweets as a strategy to expand the customer base.

- `VisualsForPresentations.ipynb`: This file contains visuals used for presentations, including additional representations that were not utilized in the final presentation.

- `DEMO.ipynb`: This notebook was used for the demonstration during the final presentation.



