# Grouping Agents ML Model (GAM)

- A machine learning model designed to group agents based on their interaction history. Optionally, a representative agent can be manually selected as the group’s starting center.

## Objectives and research question

- **Objective:** Develop a model that automatically groups agents based on interaction patterns.  
- **Research question:** Which unsupervised machine learning techniques best cluster agents, and how does initializing with a representative agent affect grouping?

## Detailed specs

### Functional requirements
- Implement multiple unsupervised machine learning models.  
- Evaluate and compare models using appropriate clustering metrics.  
- Handle limited historical interaction data.  
- Optionally allow manual selection of a representative agent as the initial group center.

### Technical requirements
- Programming language: Python (preferred).  
- ML libraries: scikit-learn, SciPy, or similar.  
- Data handling: pandas, NumPy.  
- Model evaluation: silhouette score, Davies–Bouldin index, or other suitable clustering metrics.  

### Subtasks

1. **Select unsupervised ML models and implement them** - Select which model best suits the problem and implement it
2. **Choose evaluation metrics** - Choose appropriate metrics for model
3. **Evaluate models considering limited initial data** - Evaluate all models using choosen metrics and considering limited initial data

### Dependencies
- Access to historical interaction data for all agents.  
- Computational resources capable of training clustering models.  
- Python environment with necessary ML and data processing libraries installed.  

### Input data
- Historical agent interaction data, including:  
  - Interaction frequencies or patterns  
  - Agent characteristics (optional)  
  - Previous grouping information (if available)  

### Output
- Agent clusters/groups based on interaction history.  
- Evaluation report comparing models and metrics.  

### How to test
- Apply clustering models to historical interaction data.  
- Evaluate clusters using selected metrics.  
- Compare performance and select the most effective clustering model(s).  
- Optionally test how initializing clusters with a representative agent affects results.


## Workflow, algorithms and procedures

## Issues and challenges

## Results and conclusions

## Notes


