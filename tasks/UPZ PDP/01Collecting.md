# Task 1: Collecting Ad Images

Finding the optimal source for ad images and collecting double the amount needed for simulation.

## Objectives and research question

Identify and collect a sufficient dataset of advertisement images that will serve as the foundation for the simulation system. The goal is to obtain diverse, high-quality ad images that can be processed for feature extraction.

## Detailed specs

### Functional requirements
- Explore at least 3 different data sources (Kaggle datasets, web scraping, social media APIs)
- Collect at least 200 advertisement images (double the 100 needed for simulation)
- Images must contain visual content suitable for feature extraction
- Images should represent diverse themes (sport, fashion, technology, etc.)

### Technical requirements

- Images in standard formats (JPG, PNG)
- Minimum resolution: 512x512 pixels
- Organized file structure with metadata
- Legal compliance for image usage

### Subtasks

1. **Explore existing datasets** - Search Kaggle and other platforms for ad image datasets
2. **Explore alternative solutions** - Investigate web scraping and unofficial social media APIs
3. **Collect images** - Download and organize double the required amount (200 images)

### Dependencies

- None (initial task)

### Input data

- Pictures of ads

### Output

- Folder containing 200 advertisement images
- Metadata file (CSV/JSON) with source information and basic descriptions
- Documentation of data sources and collection methodology

### How to test

- Verify image count (200 images)
- Check image quality and format compatibility
- Ensure diversity across different ad themes
- Validate metadata completeness

## Workflow, algorithms and procedures

### Workflow

1. web search - searched trough existing datasets questioning weater they are suitable for the task 
- most didn't have images, some didn't have enough images
- only satisfying dataset:
@misc{
    containt-x1bwp_dataset,
    title = { contAInt Dataset },
    type = { Open Source Dataset },
    author = { ContAInt },
    howpublished = { \url{ https://universe.roboflow.com/containt/containt-x1bwp } },
    url = { https://universe.roboflow.com/containt/containt-x1bwp },
    journal = { Roboflow Universe },
    publisher = { Roboflow },
    year = { 2022 },
    month = { dec },
    note = { visited on 2025-12-08 },
}

2. alternative solutions exploration - searched trough alternatives such as API-s and scraping
- meta has API almost perfect for this project, but does not allow public exposing of pictures and removing, extracting features and than deleteing the images is the reasonable choice, may be used in future stages of project
- scraping violates policies in every possible source

3. image downloading using random sampling
- i
## Issues and challenges
- policies
    - meta's policy of removing the images - solution: feature extraction and deleteing the images later 
    - policies against scraping - solution: not using this tehnique
- dataset doesn't have random selector, importing every picture is't optimal - solution: importing url of every image, than randomly selecting 200 urls to import 

## Results and conclusions

## Notes
