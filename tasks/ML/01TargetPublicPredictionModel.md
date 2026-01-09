# Ad Target Public Prediction Model (TPPM)

- A machine learning model designed to predict how different groups of agents will respond to a given advertisement.

## Objectives and research question

- **Objective:** Develop a predictive model to estimate the response of agent groups to specific ads.  
- **Research question:** Which machine learning models and features can most accurately predict group-level ad engagement with limited initial data?

## Detailed specs

### Functional requirements
- Implement multiple supervised machine learning models.  
- Evaluate and compare models using appropriate metrics.  
- Handle limited training data effectively.  
- Produce predictions of agent group responses for new ads.

### Technical requirements
- Programming language: Python (preferred).  
- ML libraries: scikit-learn, XGBoost, LightGBM, or similar.  
- Data handling: pandas, NumPy.  
- Model evaluation: accuracy, F1-score, AUC, or other suitable metrics.  

### Subtasks
1. **Select several supervised ML models and implement them** - Select models which will get better as more data gets in the model

- The models will proggres in 4 steps:
  1. random selection
  - the model will randomly assign each 
2. **Choose evaluation metrics** - Choose appropriate metrics for each model

3. **Evaluate models** - Evaluate all models using choosen metrics and considering limited initial data


### Dependencies
- Access to historical ad response data by agent groups.  
- Computational resources capable of training selected ML models.  
- Python environment with necessary ML and data processing libraries installed.  

### Input data
- Historical ad campaigns data, including:  
  - Ad features (e.g., format, length, target audience)  
  - Agent group characteristics  
  - Observed responses (clicks, engagement, conversions)  

### Output
- Predicted responses of agent groups to new advertisements.  
- Evaluation report comparing models and metrics.  

### How to test
- Split data into training and test sets (or use cross-validation).  
- Train models on training data and generate predictions on test data.  
- Evaluate predictions using selected metrics.  
- Compare performance and select the most accurate and robust model(s).


## Workflow, algorithms and procedures

## Issues and challenges

## Results and conclusions

## Notes


