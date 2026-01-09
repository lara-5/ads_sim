# Exposing the Model as Endpoint

- Deploy the predictive model as an API endpoint to enable easy querying and integration with other systems.

## Objectives and research question

- **Objective:** Make the model accessible through a RESTful or similar API for external applications.  
- **Research question:** What deployment method provides the most reliable, scalable, and low-latency access to the model?

## Detailed specs

### Functional requirements
- Provide an endpoint to submit ad data and receive predictions.  
- Handle requests for individual agents or entire GAM groups.  
- Return predictions in a structured format (JSON).  
- Ensure response times are acceptable for intended use cases.  

### Technical requirements
- Programming language: Python.  
- API frameworks: FastAPI, Flask, or similar.  
- Hosting options: Cloud platforms (AWS, GCP, Azure), local server, or containerized deployment (Docker).  
- Security: Basic authentication or API key for endpoint access.  

### Subtasks
1. **Explore possible model hosting options**
2. **Expose the model as an API endpoint **

### Dependencies
- Trained model ready for inference (TPPM, GAM integration).  
- Python environment with API framework installed.  
- Hosting infrastructure (cloud or local server).  

### Input data
- Advertisement data submitted via API request.  
- Optionally, specify agent group or individual agents.  

### Output
- Predicted engagement for specified agents or groups in JSON format.  
- Optional metadata such as request timestamp or model version.  

### How to test
- Send test requests with sample ad data.  
- Verify that predictions are returned correctly and in expected format.  
- Measure response times and check reliability under multiple requests.  
- Test authentication and error handling.


## Workflow, algorithms and procedures

## Issues and challenges

## Results and conclusions

## Notes


