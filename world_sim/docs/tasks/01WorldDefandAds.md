# World Definition & Ad Creation

- Defining the simulation environment, creating ad templates, and generating ad objects.

### Objectives and research question

Establish the simulation environment parameters, create structured ad templates, and generate ad objects that will be dynamically introduced into the simulation over time.

### Detailed specs

#### Functional requirements
- Define world boundaries and specifications in `config/simulation_config.yaml`
- Create function to determine daily ad display schedule
- Design ad template structure
- Generate ad objects with entry timing

#### Technical requirements
- YAML configuration file
- Python classes for Ad objects
- Ad scheduling algorithm
- Integration with ads.json data

#### Subtasks
1. **Create world boundaries and specifications** - Define all simulation parameters in config file
2. **Create ad templates** - Design Ad class structure
3. **Create the ads** - Instantiate ad objects with features and entry days
4. **Create a function that determines which ads will be shown each day** - Implement ad scheduling logic

#### Dependencies
- Task 3: EDA and Ad Selection (requires final ads.json)

#### Input data
- `data/ads.json` - 50 selected advertisements
- Simulation parameters (days, agents_count, etc.)

#### Output
- `config/simulation_config.yaml` - Complete simulation configuration
- `world/simulator.py` - Ad scheduling functions
- Ad class definition in appropriate module
- Documentation of ad lifecycle management

#### How to test
- Validate YAML configuration completeness
- Test ad scheduling function with various parameters
- Verify ads are distributed across simulation days
- Check ad template instantiation with sample data

## Workflow, algorithms and procedures

## Issues and challenges

## Results and conclusions

## Notes
