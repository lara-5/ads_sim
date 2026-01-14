# Response Handler

- Store interaction information, handle sharing actions.

## Objectives and research question

Process agent responses from LLM, validate and store interactions, handle share propagation to other agents.

## Detailed specs

### Functional requirements
- Parse LLM responses 
- Validate action compatibility
- Store interactions in database
- Handle share action (propagate to another agent)
- Deactivate ads below threshold

### Technical requirements
- Python functions in `world/simulator.py` and `world/logger.py`
- Database write operations
- Interaction rate calculation: `[(click + share + 2·like) - (2·dislike + ignore)] / N`

### Subtasks
1. **Create a function to store interaction history and call agent prompting when sharing occurs** - Handle response processing and share propagation
- create a function that stores the interaction in database with respect to database's structure
- create a function that additionaly queries the user to interact with the ad if the ad was shared with them
2. **Users emotional state update** - create a function that updates user's emotional state
- Create and call the function that uses User class method to update user's emotional state
3. **Day simulation loop** - Create a loop that will call all the necessary functions for sending and processing the prompt
- create a bach of code that:
    - checks which day it is in curent day state
    - calls the ad scheduling function
    - iterates trough that scheduled ads list
    - for each ad:
        - creates and sends the promt
        - process the result
        - updates agent's emotional state 
### Dependencies
- ...

### Input data
-...

### Output
- Response processing functions in `world/simulator.py`

## Workflow, algorithms and procedures

## Issues and challenges

## Results and conclusions

## Notes
