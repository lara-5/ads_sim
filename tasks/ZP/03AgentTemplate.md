# Agent Template Creation

- Creating a template for agents that describes features, history access, and possible actions and creating agents.

## Objectives and research question

Design the Agent class structure that encapsulates user characteristics and agent skills that define available actions with compatibility rules.

## Detailed specs

### Functional requirements
- Define all agent features (personal + propensity)
- Define 5 possible actions with compatibility matrix

### Technical requirements
- User class
- Friendship simulator
- Action compatibility enforcement

### Subtasks

1. **Create user templates** - Design User class structure
- features in User class: 
    - personal features - from world_sim/data/users_features.csv, that includes features: user_id, age, family, gender, hobbys, profession
    - propensity features - defined from assign_propensity_features class method, that includes features: activity_level, risk_tolerance and social_engagement
    - emotional state features - acute_irritation, acute_interest, acute_arousal, bias_irritation, bias_trust, bias_fatigue, with initial value 0
    - frend_list feature - initialy empty array, will be added later
- class method in User class: 
    - assign_propensity_features that assigns features activity_level, risk_tolerance, social_engagement by randomly assigning a precantage, with vaguely normal distribution (the closer to average the more chance it is to be assigned)
    - add_friend - appends the friend_list with recieved user id 
    - to_massage_format - returns the descriptive features of user in json-like string format that will be used in prompt
2. **Add frendship relations** - Define friend list for each agent
- calculate and scale the features that will be used in frendship simulator:
    - age_similarity = exp(-|age_i - age_j| / 15)
    - family_similarity = 1 if same_status else 0
    - gender_similarity = 1 if same_gender else 0
    - hobby_similarity = |hobbies_i ∩ hobbies_j| / |hobbies_i ∪ hobbies_j|
    - profession_similarity = 1 if same_profession else 0
    - activity_similarity = 1 - |activity_i - activity_j| / 100
    - risk_similarity = 1 - |risk_i - risk_j| / 100
    - social_similarity = 1 - |social_i - social_j| / 100
    - friend_of_friend - 0.1 * number of mutual friends 
- calculate the  final similarity:
```
compatibility =
  0.03 * age_similarity +
  0.02 * family_similarity +
  0.005 * gender_similarity +
  0.08 * hobby_similarity +
  0.04 * profession_similarity +
  0.05 * activity_similarity +
  0.04 * risk_similarity +
  0.03 * social_similarity +
  0.05 * friend_of_friend
```
- define the random noise that simulates the chance of meeting: random_noise = uniform(0, 1)
- define the chance of friendship:
```
P(friendship) = 0.7 * normalize(compatibility)+ 0.3 * random_noise
```
- if P(friendship) is above friendship_threshold (simulation_config.yaml), append each of user's frend_list list with each other using User class method add_friend
3. **Create the user instances** - Instantiate user objects with features and entry days
- Create users instances using world_sim/data/users_features.csv data, User class and functions

### Dependencies
- Agent features

### Input data
- Agent feature specifications
- Action compatibility rules from specification

## Output
- in `world/simulator.ipynb` - User class implementation, friendships relations, user list 

## Workflow, algorithms and procedures

## Issues and challenges

## Results and conclusions

## Notes
