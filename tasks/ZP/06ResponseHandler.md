# Response Handler

- Store interaction information, handle sharing actions, and trigger model updates.

### Objectives and research question

Process agent responses from LLM, validate and store interactions, handle share propagation to other agents, and trigger daily model retraining.

### Detailed specs

#### Functional requirements
- Parse LLM responses (ignore, click, like, dislike, share)
- Validate action compatibility
- Store interactions in database
- Handle share action (propagate to another agent)
- Trigger daily model retraining
- Update ad interaction rates
- Deactivate ads below threshold

#### Technical requirements
- Python functions in `world/simulator.py` and `world/logger.py`
- Database write operations
- Event listener for daily updates
- Interaction rate calculation: `[(click + share + 2·like) - (2·dislike + ignore)] / N`

#### Subtasks
1. **Create a function to store interaction history and call agent prompting when sharing occurs** - Handle response processing and share propagation
2. **Create an event listener for daily model updates** - Implement daily retraining trigger

#### Dependencies
- Task 5: Interaction History Management System (requires database)
- Task 8: TPPM (requires retraining capability)
- Task 12: Agent Prompting Handler (for share propagation)

#### Input data
- LLM response strings/JSON
- Agent ID and ad ID
- Current ad interaction rates

#### Output
- Response processing functions in `world/simulator.py`
- Interaction logging in `world/logger.py`
- Daily update scheduler
- Ad lifecycle management functions

#### How to test
- Test with various response formats
- Verify action compatibility validation
- Check database storage of interactions
- Test share propagation (agent B receives ad)
- Validate interaction rate calculations
- Test ad deactivation when threshold reached
- Verify daily retraining triggers correctly

## Workflow, algorithms and procedures

## Issues and challenges

## Results and conclusions

## Notes
