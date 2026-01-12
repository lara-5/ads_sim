# Model Mocker Creation

- Creation of lightweight mock models and placeholder logic to enable early integration and testing before full model availability.

## Objectives and research question

- **Objective:** Enable system development and integration by providing mock implementations of core models and lifecycle hooks.  
- **Research question:** How can simplified mock models best simulate expected behavior while keeping implementation minimal and flexible?

## Detailed specs

### Functional requirements
- Provide a mock version of the Target Public Prediction Model (TPPM).  
- Implement a simple and fast user grouping model based on K-means clustering.  
- Define a placeholder function triggered when the model is updated.  
- Persist mock models to storage for reuse across sessions.  

### Technical requirements
- Programming language: Python.  
- ML libraries: scikit-learn (for K-means), NumPy, pandas.  
- File storage: local filesystem or object storage.  

### Subtasks
1. **TPPM mocker** - Implement a mock version of the Target Public Prediction Model (TPPM)
- Create a function that will randomly assign each agent with a number that will represent the model's prediction of should the ad be shown to user
2. **Simple grouping model** - Implement a lightweight K-means-based user grouping model
- Create a K-means grouping algorithm, based only on personal, propensity and frend_list user features(without history), that will group the users only once
- save it in DuckDB in grouping table
3. **Prediction query handler** - Create a main function that will recieve an ad description, run the TPPM mocker model for each user and calculate the average for each group of users, scale it so that the sum of each group is equal to agents_exposed_to_ad, so that it represents the number of people.
4. **Save** - Save and load mock models for reuse
- save the model using joblib

### Dependencies
- Defined interfaces for TPPM and grouping models.  
- Agreement on expected input/output formats for mocked components.  

### Input data

### Output
- `models/mocks/mock_model.ipynb` - Mock TPPM, grouping model
- `models/mocks/mock_model.joblib` - Saved mock model artifacts.  

## Workflow, algorithms and procedures

## Issues and challenges
- the real model will not be available, so mocking model output is the easiest solution
## Results and conclusions

## Notes
