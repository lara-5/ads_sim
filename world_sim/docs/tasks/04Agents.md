# Agent Creation

- Extracting agent features from dataset and creating agent instances.

### Objectives and research question

Process the RedDust dataset to extract personal features, generate propensity features, and create the full set of agent instances that will participate in the simulation.

### Detailed specs

#### Functional requirements
- Extract personal features from RedDust dataset
- Generate random propensity features (0-100%)
- Create 100 agent instances
- Implement initial agent grouping
- Store agents in `data/users.json`

#### Technical requirements
- Data processing pipeline for RedDust dataset
- Random number generation with seed control
- Agent instantiation using template from Task 6
- Initial clustering algorithm (K-Means or similar)

#### Subtasks
1. **Extract features from dataset** - Process RedDust dataset to extract personal features
2. **Generate random features** - Create propensity features (activity_level, risk_tolerance, social_engagement)
3. **Create agents using the agent template** - Instantiate 100 agents with all features
4. **Create a model to group agents** - Initial clustering based on features

#### Dependencies
- Task 6: Agent Template Creation (requires Agent class)

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
