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

## Issues and challenges

## Results and conclusions

## Notes
