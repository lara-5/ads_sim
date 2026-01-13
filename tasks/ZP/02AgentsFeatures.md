# Agent Features extraction

- Extracting agent features from dataset.

### Objectives and research question

Process the RedDust dataset to extract personal features and generate propensity features that will participate in the simulation.

### Detailed specs

#### Functional requirements
- Extract personal features from RedDust dataset
- Generate random propensity features (0-100%)

#### Technical requirements
- Data processing pipeline for RedDust dataset
- Random number generation with seed control

#### Subtasks
1. **Extract features from dataset** - Process RedDust dataset to extract personal features
- fetch data using Zendo endpoint: https://zenodo.org/api/records/3541657 
- create a dataframe that assigns each row with user_id, combines features, how to combine them is explained in dataset's README
2. **EDA analysis** - do a quick EDA on dataframe
- remove any missing rows
- visualise distributions and correlations
3. **Choose agents** - choose which lines of dataframe to keep 
- decide which agents_count number of lines to keep to maintain as much diversity as posible by analysing the visualisations above
- save dataframe in world_sim/data/users_features.csv

#### Dependencies

#### Input data
- RedDust dataset
- Simulation config (number of agents, seed)

#### Output
- `user_feature_extraction/user_feature_extraction.ipynb` - user feature extraction script 
- `data/users.csv` - agent descriptions

## Workflow, algorithms and procedures
1. **Data Fetching**: The script starts by fetching metadata from the Zenodo API endpoint for the RedDust dataset. It extracts the download links for `dataset.csv` and `documentation.csv`.
2. **Data Loading**: Using the obtained links, the script downloads the CSV files and loads them into pandas DataFrames.
3. **Data Processing**: A `user_id` is assigned to each row in the dataset, effectively treating each row as a unique user. The script also loads the documentation to provide context for the features.
4. **Exploratory Data Analysis (EDA)**: The script performs basic EDA by checking for missing values and removing them. It then visualizes the distributions of key demographic and personality features (age, gender, openness, agreeableness, conscientiousness, extraversion) and calculates a correlation matrix to understand the relationships between features.
5. **Agent Selection**: To create a manageable and diverse set of agents for the simulation, a random sample of 1000 users is selected from the processed dataset. A fixed random state is used for reproducibility.
6. **Data Saving**: The final DataFrame containing the selected agents and their features is saved to `data/users_features.csv`.

## Issues and challenges
- The dataset documentation (`documentation.csv`) did not contain clear instructions on how to combine features. For this task, we assumed a one-to-one mapping between rows in `dataset.csv` and individual users.
- The selection of agents is random. For a more targeted simulation, a more sophisticated sampling method like stratified sampling or clustering could be used to ensure the representation of specific user profiles.

## Results and conclusions
- A Marimo-based Python script (`user_feature_extraction/user_feature_extraction.py`) was created to automate the process of fetching, cleaning, analyzing, and selecting user features.
- An EDA was performed, revealing the basic statistical properties and distributions of the user features.
- A dataset of 1000 users with diverse features was generated and saved to `data/users_features.csv`, ready to be used in the simulation. This provides a solid foundation for the agent-based modeling part of the project.

## Notes
