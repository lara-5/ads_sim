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
- create a dataframe that assigns each row with id, combines features, how to combine them is explained in dataset's README
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
- `data/users.json` - 100 agent descriptions
- Agent creation script
- Initial grouping results
- Documentation of feature extraction and generation process

#### How to test
- Verify 100 agents created
- Check feature completeness for all agents
- Validate propensity features are in [0,100] range
- Test grouping produces reasonable clusters
- Verify JSON structure matches specification

## Workflow, algorithms and procedures

## Issues and challenges

## Results and conclusions

## Notes
