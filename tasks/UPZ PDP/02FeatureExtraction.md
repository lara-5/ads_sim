# Task 2: Ads Feature Extraction

Extracting features from ad images using machine learning models.

## Objectives and research question

Automatically extract descriptive features from advertisement images that will be used to characterize each ad in the simulation. Features should capture theme, color tone, rhetorical approach, and text content.

## Detailed specs

### Functional requirements

- Extract main feature categories: color tone, rhetorical triangle, text amount, main elements
- Create a ML model for feature "group" prediction
- Use pretrained computer vision models
- Process all collected images
- Handle various image formats and sizes

### Technical requirements

- Python environment with CV libraries (OpenCV, PIL)
- Pretrained models (e.g., ResNet, CLIP, OCR models)
- GPU acceleration recommended for batch processing
- Feature output in structured format (JSON/CSV)

### Subtasks

1. **Choose the appropriate model for each feature type** - Explore potential models, and theirs pros and cons in these specific usage. Choose the appropriate model for each feature type. 
color tone, rhetorical triangle, text amount, main elements
2. **Extract color tone using pretrained models** - Apply choosen CV model to extract color tone from each image. Add the extracted feature in dataframe. 

3. **Extract rhetorical triangle using pretrained models** - Apply choosen CV model to extract dominant element of rhetorical triangle from each image. Add the extracted feature in dataframe. 

4. **Extract text amount using pretrained models** - Apply choosen CV model to extract text amount from each image. Add the extracted feature in dataframe. 

5. **Extract main elements using pretrained models** - Apply choosen CV model to extract the list of main elements from each image. Add the extracted feature in dataframe. 

6. **Create a ML model for group prediction** - Choose the appropriate model for predicting which group thoes the picture belongs to. Split the dataset in train, validation and test set. Applay the model, validate it.

### Dependencies

- Task 1: Collecting Ad Images (requires collected images)

### Input data

- 200 advertisement images from Task 1
- Pretrained ML models

### Output

- Structured dataset (CSV/JSON) with extracted features for each image:
  - `image_id`, `theme`, `color_tone`, `rhetorical_triangle`, `text_amount`
- Feature extraction script
- Documentation of models used and extraction methodology

### How to test

- Verify all images have been processed
- Manually validate a sample (10-20 images) for accuracy
- Verify output format matches specification

## Workflow, algorithms and procedures

## Issues and challenges

## Results and conclusions

## Notes


