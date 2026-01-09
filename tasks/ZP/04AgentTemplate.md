# Agent Template Creation

- Creating a template for agents that describes features, history access, and possible actions and creating agents.

### Objectives and research question

Design the Agent class structure that encapsulates user characteristics and agent skills that define available actions with compatibility rules.

### Detailed specs

#### Functional requirements
- Define all agent features (personal + propensity)
- Define 5 possible actions with compatibility matrix
- Implement action validation logic
- Use agent skills to describe actions

#### Technical requirements
- Python class definition in `agents/agent.py`
- JSON serialization support
- Action compatibility enforcement

#### Subtasks

1. **Create user templates** - Design User class structure
- features in User class: 
    - personal features - from world_sim/data/users_features.csv, that includes features: id, age, family, gender, hobbys, profession
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
    - activity_similarity = 1 - |activity_i - activity_j|
    - risk_similarity = 1 - |risk_i - risk_j|
    - social_similarity = 1 - |social_i - social_j|
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
  0.03 * social_similarity
  0.05 * friend_of_friend
```
- define the random noise that simulates the chance of meeting: random_noise = uniform(0, 1)
- define the chance of friendship:
```
P(friendship) = 0.7 * normalize(compatibility)+ 0.3 * random_noise
```
- if P(friendship) is above friendship_threshold (simulation_config.yaml), append each of user's frend_list list with each other using User class method add_friend
2. **Create the user instances** - Instantiate user objects with features and entry days
- Create users instances using world_sim/data/users_features.csv data, User class and functions
3. **Create agent skills** - Define the skills agents will need to interact in this simulation
- responding skill
    - define the skill that describes the format and basic guidelines how the response should be
    - the response should be in this exact format:
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
    - agent should folow these rules when deciding how to react: 
        - **ignore** - true if the ad does not capture user's interest and user has no motivation to engage with it in any way
            - When to use:
                - The ad is irrelevant to your interests or current needs
                - The topic feels neutral, boring, or mildly annoying
                - You scroll past without emotional involvement
                - No curiosity or emotional response is triggered
            - Important:
                - Ignoring does not imply a strong negative reaction
                - Ignore is the default reaction for low relevance
            - Typical emotional effect:
                - Minimal or no emotional shift
                - Slight fatigue or indifference possible
        - **click** - true if the ad generates curiosity or informational interest, and user want to learn more about the offer
            - When to use:
                - The ad aligns partially or strongly with your interests
                - The message raises questions you want answered
                - You are evaluating whether the offer is useful or relevant
                - You have sufficient attention and motivation to explore further
            - Important:
                - Clicking does not imply approval, liking, or intent to purchase
                - Click reflects exploration, not endorsement
            - Typical emotional effect:
                - Increased engagement
                - Mild positive arousal or curiosity
        - **like** - true if the ad creates a positive emotional response and user approve of or resonate with its content
            - When to use:
                - The ad matches your values, interests, or aesthetic preferences
                - You feel positive, amused, inspired, or satisfied by the content
                - You want to express light, low-effort positive feedback
            - Important:
                - Liking does not require clicking
                - Like is a passive positive signal, not a strong commitment
            - Typical emotional effect:
                - Positive valence
                - Slight mood improvement
        - **dislike** - if the ad evokes a negative emotional reaction and user want to express disapproval or annoyance.
            - When to use:
                - The ad feels irritating, inappropriate, misleading, or offensive
                - The topic strongly conflicts with your preferences or values
                - You want to signal “show me less of this”
            - Important:
                - Dislike implies active negative feedback, not just lack of interest
                - Use dislike only when a clear negative reaction is present
            - Typical emotional effect:
                - Increased irritation or frustration
                - Negative valence
        - **share** - if the ad is interesting, meaningful, or entertaining enough that you want others in your network to see it, user can share one ad to only one user with whom user is friends(their id is in user's friend_list)
            - When to use:
                - The content is relevant to your friends or social circle
                - The ad supports your identity, values, or humor
                - You expect social value from sharing (discussion, signaling, usefulness)
            - Important:
                - Sharing implies strong positive or provocative engagement
                - Share may occur even without liking or clicking, but is higher effort
            - Typical emotional effect:
                - Elevated engagement
                - Social activation and reinforcement

        - **reaction compatibility** - reaction should respect reaction compatibility:
        ```json
        {
        "ignore": ["share"],
        "click": ["like", "dislike", "share"],
        "like": ["click", "share"],
        "dislike": ["click", "share"],
        "share": ["like", "dislike", "click"]
        }
        ```
        - **reaction_description** should explain emotions, intentions, nature and the reason for such interaction. It is not a narrative or comment, but a structured explanatory signal that captures why a specific reaction occurred and what internal state it reflects.
            - it shoul be 40 to 60 words long 
            Its role is to:
            - make the agent’s internal emotional response explicit
            - explain the intention behind the interaction choice
            - describe the nature of the reaction (impulsive, deliberate, avoidant, social)
            - provide a causal link between the ad content and the chosen reaction
            - This description must be detailed enough to allow downstream emotional modeling or numerical state updates.
        - **emotional state** - this applies to all 6 variables:
            -The following variables represent incremental changes (deltas) to the user’s emotional state resulting from a single ad interaction.They do not describe the current emotional state and must never be interpreted as absolute values. Each value reflects how one specific interaction shifted the emotional state relative.All changes should be small, bounded, and proportional to the perceived impact of the interaction.
            - Important:
                - Values represent change, not final state
                - Values are in [-100, 100]
                - Positive values indicate an increase, negative values indicate a decrease
                - 0 means that the interaction had no meaningful effect on that dimension
                - Agent must not not attempt to infer or restate previous emotional values
                - Agent should estimate changes based only on: the current interaction, the emotional reaction described and the agent’s personality and sensitivity
            - Acute vs Bias Distinction - very important
                - Acute variables represent short-term, immediate emotional reactions. They are fast-changing, high sensitivity, decaying quickly over time
                - Bias variables represent slow-moving, accumulated attitudes. They change gradually, reflect repeated exposure, persist across sessions and days
                - acute changes may contribute to bias changes, but they are not equivalent.
                - Bias changes should be smaller in magnitude than acute changes
                - Strong reactions may affect both, but asymmetrically
            - Agents task
        - **acute_irritation_change**- represents the immediate increase or decrease in irritation caused by this ad exposure
            - When to increase:
                - the ad feels annoying, intrusive, repetitive, or irrelevant
                - The tone conflicts with the user’s preferences or emotional state
                - The user experiences frustration or resistance
            - When to decrease:
                - The ad unexpectedly reduces tension
                - The content feels calming, reassuring, or relieving
            -Interpretation:
                - This reflects short-term emotional friction, not long-term dislike.
        - **acute_interest_change** - represents the immediate change in curiosity, relevance perception, or cognitive engagement
        - When to increase:
            - The ad aligns with current interests or needs
            - The message sparks curiosity or perceived usefulness
            - The user wants to learn more or explore the offer
        -When to decrease:
            - The ad actively disengages the user
            - The content feels boring, redundant, or mentally draining
        -Interpretation:
            - Interest is about attention and relevance, not approval or trust.
        - **acute_arousal_change** - represents the change in emotional activation or alertness triggered by the ad.
            - When to increase:
                - The ad is emotionally charged, surprising, exciting, or stressful
                - The content creates urgency or strong stimulation
            - When to decrease:
                - The ad feels dull, monotonous, or calming
                - The interaction lowers emotional intensity
            - Interpretation:
                - Arousal is emotional intensity, independent of positive or negative valence.
        - **bias_irritation_change** - represents a gradual shift in the user’s baseline tendency to feel irritated by similar content or advertising in general 
            - When to increase:
                - The interaction reinforces existing annoyance
                - The ad contributes to cumulative frustration or saturation
                - The user perceives a pattern of unwanted content
            - When to decrease:
                - The interaction slightly restores tolerance
                - The ad breaks a negative pattern with relevance or respectfulness
            - Interpretation:
                - This is long-term sensitivity, not a momentary reaction.
        - **bias_trust_change** - represents a slow change in baseline trust toward ads, brands, or the platform.
            - When to increase:
                - The ad feels transparent, credible, or respectful
                - The message aligns with expectations and values
                - The interaction reinforces reliability
            When to decrease:
                - The ad feels misleading, manipulative, or inappropriate
                - The user perceives hidden intent or exaggeration
            Interpretation:
                - Trust evolves gradually and should change less frequently and less intensely than acute emotions.
        - **bias_fatigue_change** - represents a gradual change in baseline mental and emotional exhaustion related to ads
            - When to increase:
                - The ad contributes to overload or repetition
                - The interaction requires unwanted cognitive effort
                - The user feels “worn down” by exposure
            - When to decrease:
                - The ad feels lightweight, refreshing, or unusually relevant
                - The interaction reduces perceived effort or noise
            - Interpretation:
                - Fatigue reflects capacity depletion, not emotional valence.
    - while forming the reaction, agent should reflect on it's features
        - personal features - describes the user’s stable identity and life context, such as age, family situation, gender, hobbies, and profession.
            - How they influence the reaction:
                - They frame how relevant or meaningful the ad topic is to the user
                - They shape value alignment, life-stage appropriateness, and contextual fit
                - They influence interpretation of tone, messaging, and intent
            - Interpretation:
                -Personal features define who the user is, not how active or emotional they are. They provide semantic context rather than behavioral force.
        - propensity features - represent the user’s baseline behavioral tendencies, independent of the current emotional moment
            - Includes:
                - activity_level
                - risk_tolerance
                - social_engagement
            - How they influence the reaction:
                - They bias the likelihood of engagement versus ignoring
                - They affect willingness to explore uncertain or unfamiliar offers
                - They influence preference for low-effort vs. high-effort actions
                - They modulate likelihood of social actions (like, share)
            - Interpretation:
                - Propensity features define how the user tends to behave in general.
                - They adjust probabilities and thresholds, but do not determine outcomes on their own.
        - emotional state features - describe the user’s current and accumulated emotional context at the time of interaction.
        - Includes:
            Acute emotions (short-term reactivity)
            Bias emotions (long-term attitudinal drift)
        - How they influence the reaction:
            - Acute emotions modulate immediacy, intensity, and impulsiveness
            - Bias emotions adjust long-term tolerance, trust, and fatigue thresholds
            - Emotional state can amplify or suppress personality-driven tendencies
        - Interpretation:
            - Emotional state reflects how the user feels right now and over time, not who they are.
            - It shapes momentary responsiveness and accumulated sensitivity to ads.
        -During reaction formation, the reaction emerges from the combined influence of:
            - identity-based interpretation (personal features)
            - baseline behavioral tendencies (propensity features)
            - momentary and accumulated emotional modulation (emotional state features)
            - No single feature group is sufficient to explain the reaction on its own.

#### Dependencies
- Task 5: Interaction History Management System (requires memory manager)

#### Input data
- Agent feature specifications
- Action compatibility rules from specification

#### Output
- `agents/agent.py` - Complete Agent class
- Agent feature validation functions
- Action compatibility validator
- Unit tests for agent behavior

#### How to test
- Instantiate agents with various feature combinations
- Test history retrieval for agents with sample interactions
- Validate action compatibility rules (e.g., ignore + share should fail)
- Test JSON serialization/deserialization

## Workflow, algorithms and procedures

## Issues and challenges

## Results and conclusions

## Notes
