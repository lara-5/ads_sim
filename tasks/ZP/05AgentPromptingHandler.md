# Agent Prompting Handler

- Deciding which agents to show the ad to and sending formatted prompts.

### Objectives and research question

Implement the logic that queries the prediction model, selects agents based on group probabilities, and formats/sends prompts to LLM agents for their response.

### Detailed specs

#### Functional requirements
- Query prediction model for ad
- Filter groups with probability > 30%
- Distribute ad displays proportionally to probabilities
- Randomly select agents from chosen groups
- Format prompts with ad features + agent history
- Send prompts to LLM (GPT-4-mini)

#### Technical requirements
- Python functions in `world/simulator.py`
- API client for prediction endpoint
- LLM API integration (OpenAI)
- Prompt template management
- Located in simulation orchestration module

#### Subtasks
1. **Create a function to query the model** - API client for prediction endpoint
- Define the function that queryies the model for the prediction 
- tbd., exact endpoint is not defined yet
2. **Create a function to randomly select agents for reacting** - Implement proportional selection algorithm
model will return the array 
3. **Create a function to format and send prompts** - LLM prompt generation and API calls

#### Dependencies
- Task 11: Exposing Model as Endpoint (requires prediction API)
- Task 5: Interaction History Management System (requires history retrieval)
- Task 6: Agent Template Creation (requires agent structure)

#### Input data
- Ad to be shown
- Prediction model endpoint
- All agents with current groupings
- Agent interaction history

#### Output
- Agent selection functions in `world/simulator.py`
- Prompt formatting utilities
- LLM interaction handler
- Usage documentation

#### How to test
- Test with sample ad and verify selection distribution
- Validate prompt format with sample agent
- Test LLM API integration with mock responses
- Verify agents from correct groups are selected
- Check proportional distribution matches probabilities
- Test edge cases (single group, all groups filtered)

## Workflow, algorithms and procedures

## Issues and challenges

## Results and conclusions

## Notes
