# Task 3: EDA and Ad Selection

Exploring extracted features and cleaning the data to select final ads for simulation.

## Objectives and research question

Perform exploratory data analysis on extracted features, clean the dataset, and hand-pick the optimal set of 100 advertisements that provide diverse representation across all feature dimensions.

## Detailed specs

### Functional requirements

- Analyze distribution of each feature type
- Identify and remove invalid/low-quality entries
- Select 100 ads ensuring balanced representation
- Store final ads in accessible format

### Technical requirements

- Python data analysis stack (pandas, matplotlib, seaborn)
- Jupyter notebook for EDA documentation
- Final dataset in JSON format matching specification

### Subtasks

1. **Explore extracted features** - Create visualizations and statistics for each feature
2. **Remove invalid rows** - Filter out corrupted or incomplete entries
3. **Hand-pick a defined number of ads** - Select 100 ads with balanced feature distribution
4. **Store ads in accessible format** - Save final dataset as `data/ads.json`

### Dependencies

- Task 2: Ads Feature Extraction (requires extracted features)

### Input data

- Unclean ads features dataset

### Output

- `data/ads.json` - Final 100 advertisements with all features
- Data clearing script
- EDA notebook with visualizations and analysis
- Data quality report documenting cleaning decisions

### How to test

- Verify exactly 100 ads in final dataset
- Check feature distribution balance
- Validate JSON structure matches specification
- Ensure all selected ads have corresponding images

## Workflow, algorithms and procedures

## Issues and challenges

## Results and conclusions

## Notes


