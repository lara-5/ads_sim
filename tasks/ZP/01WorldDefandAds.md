# World Definition & Ad Creation

- Defining the simulation environment, creating ad templates, and generating ad objects.

### Objectives and research question

Establish the simulation environment parameters, create structured ad templates, and generate ad objects that will be dynamically introduced into the simulation over time.

### Detailed specs

#### Functional requirements
- Define world boundaries and specifications in `config/simulation_config.yaml`
- Create function to determine daily ad display schedule
- Design ad template structure
- Generate ad objects with entry timing

#### Technical requirements
- YAML configuration file
- Python classes for Ad objects
- Ad scheduling algorithm
- Integration with ads.json data

#### Subtasks
1. **Create world boundaries and specifications** - Define simulation parameters in config file
2. **Create ad templates** - Design Ad class structure
- features in Ad class: 
    - descriptive features - from world_sim/data/ads_features.csv, that includes features: id,group,emotion_label,message_type,visual_style,num_people,people_present,people_area_ratio,product_present,product_area_ratio,object_count,object_list,dominant_element,text_present,text_area_ratio,avg_font_size_proxy,dominant_colors,brightness_category,saturation_category,hue_category,visual_impact
    - function features 
        - day of entry into simulation - will be assigned using day_of_entry_asignment function
        - interaction_rate which is initialy set to 0
        - is_active which is boolean info if the ad is active, false by default
- methods in Ad class:
    - update_interaction_rate - function that is called after each interaction with ad, it calculates the interaction rate using 
    ```interaction_rate = [(click + share + 2·like) - (2·dislike + ignore)] / N``` 
    and checks if the ad should be deactivated, i.e. is_active set to false
    - to_massage_format - returns the descriptive features of ad in json-like string format that will be used in prompt

3. **Create the ads instances** - Instantiate ad objects with features and entry days
- create a day_of_entry_asignment function - assigned randomly, with respect for the fact that each day gets exactly new_ads_per_day, the number red from world_sim/config/simulation_config.yaml
- Create ads using Ad class and these functions
4. **Create a function that determines which ads will be shown each day** - Implement ad scheduling logic
- create a function schedule_for_day that:
    - checks which ads are entering the simulation that day, sets their is_active to true
    - defines ads_shown_per_day number of ads that will be shown that day by randomly selecting ads whose is_active is true
    - keeps that list of selected ads globaly visible

#### Dependencies
- Task 3: EDA and Ad Selection (requires final ads.json)

#### Input data
- `data/ads.json` - 50 selected advertisements
- Simulation parameters (days, agents_count, etc.)

#### Output
- `config/simulation_config.yaml` - Complete simulation configuration
- `world/simulator.py` - Ad scheduling functions
- Ad class definition in appropriate module
- Documentation of ad lifecycle management

#### How to test
- Validate YAML configuration completeness
- Test ad scheduling function with various parameters
- Verify ads are distributed across simulation days
- Check ad template instantiation with sample data

## Workflow, algorithms and procedures

## Issues and challenges

## Results and conclusions

## Notes
- exacly 10 ads each day is not natural, the number should vary from day to day, and also during the day