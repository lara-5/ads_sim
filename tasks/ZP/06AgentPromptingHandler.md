# Agent Prompting Handler

- Deciding which agents to show the ad to and sending formatted prompts.

## Objectives and research question

Implement the logic that queries the prediction model, selects agents based on group probabilities, and formats/sends prompts to LLM agents for their response.

## Detailed specs

### Functional requirements
- Query prediction model for ad
- Distribute ad displays proportionally to probabilities
- Randomly select agents from chosen groups
- Format prompts
- Send prompts to LLM 

### Technical requirements
- Python functions in `world/simulator.py`
- API client for prediction endpoint
- LLM API integration
- Prompt template management
- Located in simulation orchestration module

### Subtasks
1. **Create a function to query the model** - API client for prediction endpoint
- Define the function that queryies the model for the prediction 
- tbd., exact endpoint is not defined yet
2. **Create a function to randomly select agents for reacting** - Implement proportional selection algorithm
- model will return the array of groups of users and probability they will like that. 
- the grouping model will return which angent is in which group
- the scheduling algorithm will iterate trough the array of predictions, and randomly select as much users from that group as the model predicted 
3. **LLM model setup** - Download local model and set it up
4. **Create a function to format and send prompts** - LLM prompt generation and API calls
- the function should send the query to local model
- response format:
```json
    ignore - boolean
    click - boolean
    like - boolean
    dislike - boolean
    share - agent_id, number
    reaction_description - text
    acute_irritation_change - number in [1, 100]
    acute_interest_change - number in [1, 100]
    acute_arousal_change - number in [1, 100]
    bias_irritation_change - number in [1, 100]
    bias_trust_change - number in [1, 100]
    bias_fatigue_change - number in [1, 100]

    ```
- query consists of:
    - User description: "You are a social media user with folowing features -insert json features-" 
    - Task description: "You are shown an ad and you need to react to it folowing the certain rules. The response should be in this exact format: -insert format-. These are the meanings of each item in that response: 
        ignore - Indicates that the ad did not trigger relevant interest, emotion, or motivation for engagement, leading the user to consciously or automatically pass without interacting.
        click - Indicates that the ad generated sufficient curiosity or perceived usefulness for the user to explore further, without implying emotional approval or purchase intent.
        like - Indicates a light positive emotional resonance with the ad, where the user expresses approval or affinity with minimal cognitive or effort investment.
        dislike - Indicates an active negative reaction to an ad that causes irritation, disagreement, or discomfort, with the intent to signal reduced preference for similar content.
        share - Indicates that the user perceives any kind social, informational, or identity value in sharing the ad with exactly one friend.
        reaction_description - A structured 40–60 word explanation that explicitly describes the agent’s emotional response, intention, and reaction type, causally linking the ad content to the chosen interaction.
        acute_irritation_change - Quantifies the immediate, short-term change in irritation caused by the ad, ranging from tension reduction to increased frustration or resistance.
        acute_interest_change -  Quantifies the immediate change in attention, curiosity, or perceived relevance triggered by the ad, independent of trust or emotional approval.
        acute_arousal_change - Quantifies the change in emotional activation or intensity, such as excitement, stress, surprise, or calming effects.
        bias_irritation_change - Represents a small, long-term shift in the user’s baseline tendency to feel irritated by similar ads or advertising in general.
        bias_trust_change - Represents a gradual change in long-term trust toward ads, brands, or the platform based on perceived transparency and credibility.
        bias_fatigue_change - Represents a slow change in baseline mental and emotional exhaustion related to ad exposure and perceived cognitive effort."
    - Ad description: "This is the ad you are reacting to: -insert ad json- "

### Dependencies
- ...

### Input data
- Ad to be shown
- Prediction model endpoint
- All agents with current groupings
- Agent interaction history

### Output
- Agent selection functions in `world/simulator.py`
- Prompt formatting utilities
- LLM interaction handler
- Usage documentation

## Workflow, algorithms and procedures

## Issues and challenges
- token limit per prompt
- prompt modeling
- common ground for meaning of interactions
## Results and conclusions

## Notes
- repeating instructions and lack of common ground for reaction meanings is a challenge that is complex and important thing to explore, but can't be right now
