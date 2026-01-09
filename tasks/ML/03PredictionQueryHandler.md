# Prediction Query Handler Function

- A function that receives an advertisement, predicts engagement for each agent using the TPPM model across all GAM groups, and computes group averages.

## Objectives and research question

- **Objective:** Implement a function that combines outputs from TPPM and GAM to provide group-level engagement predictions.  
- **Research question:** How can individual agent predictions be aggregated to produce accurate group-level engagement metrics?

## Detailed specs

### Functional requirements
- Accept an advertisement as input.  
- For each agent in each GAM group:  
  - Use TPPM to predict individual engagement.  
  - Compute the average engagement for the group.  
- Return a summary of group-level engagement predictions.  

### Technical requirements
- Programming language: Python.  
- Dependencies: TPPM model, GAM groupings.  
- Data handling: pandas or NumPy for aggregation and computations.  

### Subtasks
**Prediction query handler function** - Use created models to create the response

### Dependencies
- Trained TPPM model.  
- Defined GAM groupings.  
- Python environment with data processing libraries installed.  

### Input data
- Advertisement data to predict engagement on.  
- Agent grouping information from GAM.  

### Output
- Average engagement predictions for each agent group.  
- Optionally, detailed individual agent predictions.  

### How to test
- Provide a sample advertisement.  
- Verify that the function correctly predicts engagement for each agent via TPPM.  
- Check that group averages are computed accurately.  
- Compare outputs against manual calculations or a small test dataset to ensure correctness.

## Workflow, algorithms and procedures

## Issues and challenges

## Results and conclusions

## Notes


