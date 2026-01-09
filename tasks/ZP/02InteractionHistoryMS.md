# Interaction History Management System

- Creating a system to store interaction history and determine optimal agent data compression.

### Objectives and research question

Design and implement a robust system for storing all agent-ad interactions in DuckDB, and develop multiple schemes for compressing agent history data to optimize LLM context usage. Research question: Which compression method best balances information retention with context efficiency?

### Detailed specs

#### Functional requirements
- Store all interactions (user_id, ad_id, timestamp, actions, metadata)
- Implement 3 compression schemes: vector embeddings, full history, aggregated metrics
- Create retrieval functions for each scheme
- Measure effectiveness of each approach

#### Technical requirements
- DuckDB database (`data/interactions.db`)
- Python database interface
- Embedding model for vector representation (if applicable)
- Memory manager module (`agents/memory_manager.py`)

#### Subtasks
1. **Create an interaction history management system that stores each interaction** - Design database schema and storage functions
2. **Select the best compression system** - Evaluate possibilities
- vector emotional model with acute and bias emotional effects is estimated to be the best fit, with open posibility for changing the model if major flaws in this model appears during implementation or simulation
- the system will describe agent's shift in emotion, and it will describe acute emotional effects which will be short therm reaction to ad and will decay fast and completely reset at the end of the day and bias which will show longer-therm consenquences of the interaction and will decay slower over time
3. **Create the compression system** - Define where and how will this system be implemented (not to be implemented yet)
- the system will be implemented in User class
- each user will be given the the emotional state features: acute_irritation, acute_interest, acute_arousal, bias_irritation, bias_trust, bias_fatigue
- agent will respond with emotionional state shifts for each feature
#### Dependencies
- None (foundational infrastructure)

#### Input data
- Interaction data format specification
- Sample interaction data for testing

#### Output
- `data/interactions.db` - DuckDB database with schema
- `agents/memory_manager.py` - Memory management module
- `world/logger.py` - Interaction logging functions
- Comparison document evaluating compression schemes

#### How to test
- Insert sample interactions and verify storage
- Test each compression scheme with sample agent history
- Measure context size for each scheme
- Validate data integrity after compression/retrieval
- Test concurrent access patterns

## Workflow, algorithms and procedures

## Issues and challenges

## Results and conclusions

## Notes
