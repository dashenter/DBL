# DBL

This repository has been created to fulfill the requirements of the JBG030 course at the Technical University of Eindhoven.

## Overview 

This repository contains multiple Jupyter Notebooks, CSV files and databases, each serving a specific purpose.

### DataBases

- `dbl10.db`: This is the main database used throughout the project. Initially, the table name was set to "nikitas," but it was later changed to "tweets" during the sentiment analysis phase. If any code cells fail to execute due to this change, you can simply modify the table name in the SQL queries accordingly.
  
- `map.db`: DataBase used for the creation of the Geographical Analysis with sentiment for the United States of America.

- `sankey.db`: This is the one used for the Sankey diagrams displayed in the poster.

### CSV Files

-  `csv_files_per_airline` folder: This folder contains all the CSV files created using the `ConversationMining.ipynb` notebook.

-  `cb_2018_us_state_500k` folder: This folder contains files used for plotting the maps for the United States of America. 

- Other CSV files: These additional CSV files were generated for the demonstration during the third presentation. Due to time constraints, we created these files to ensure the smooth execution of the `DemoGroup10.ipynb` notebook.

### Jupyter Notebooks

- `FinalDatabase.ipynb`: This Jupyter Notebook contains the code for creating the 'dbl_10' database, which is approximately 6.6 GB in size.

- `ConversationMining.ipynb`: This notebook is designed to mine and analyze conversations from the dataset. It provides functions to extract conversations from CSV files, with each file representing a different airline. Various statistics for the selected airline can be explored using this notebook.
  
- `Initial_ComparisonAmericanAirAirFrance.ipynb`: This notebook was used for an initial comparison between American Airlines and Air France. It was created after the first presentation to assess our progress. You may ignore this notebook as it contains graphs that are misleading based on our final definition of conversations.
- `SentimentAnalysis.ipynb`: In this notebook, sentiment analysis is performed on all the tweets in the database using the Vader sentiment analysis tool accessed via NLTK. The notebook creates four new columns for each tweet: 'pos', 'neu', 'neg', and 'compound'. Please note that the sentiment analysis process may take a significant amount of time due to the size of the dataset.

- `SentimentAnalysisOnConversations.ipynb`: In this notebook, the function for mining conversations is indluded and we then do another sentiment analysis on only the conversations using the csv files that were created with the previous file named `ConversationMining.ipynb`. It also contains graphs that were used in the second presentation.
- 
- `SentimentAnalysis_French&Spanish.ipynb`: This notebook focuses on sentiment analysis of Spanish and French tweets (identified by the 'lang' column) for the customer AmericanAir and the competitor AirFrance. It explores the potential of responding to Spanish tweets as a strategy to expand the customer base.

- `VisualsForPresentations.ipynb`: This file contains all of the visuals used for presentations (1&2), including additional representations that were not used in the final presentation.

- `DemoGroup10.ipynb`: This notebook was used for the demonstration during the final presentation, the teacher that graded us explictly asked for September, thus the current notebook is for September only.




