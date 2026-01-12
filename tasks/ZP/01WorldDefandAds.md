# World Definition & Ad Creation

- Defining the simulation environment, creating ad templates, and generating ad objects.

## Objectives and research question

Establish the simulation environment parameters, create structured ad templates, and generate ad objects that will be dynamically introduced into the simulation over time.

## Detailed specs

### Functional requirements
- Define world boundaries and specifications 
- Create function to determine daily ad display schedule
- Design ad template structure
- Generate a list of ad objects with entry timing

### Technical requirements
- YAML configuration file
- Python classes for Ad objects
- Ad scheduling algorithm

### Subtasks
1. **Create world boundaries and specifications** - Define simulation parameters in config file
2. **State file** - Create a file that will store global states
- Create a file that will store states needed for simulation
- states needed:
    - current_simulation_day: default 0
    ads_entering_schedule: empty dict
3. **Create ad templates** - Design Ad class structure
- features in Ad class: 
    - descriptive features - from world_sim/data/ads_features.csv, that includes features: id,group,emotion_label,message_type,visual_style,num_people,people_present,people_area_ratio,product_present,product_area_ratio,object_count,object_list,dominant_element,text_present,text_area_ratio,avg_font_size_proxy,dominant_colors,brightness_category,saturation_category,hue_category,visual_impact
        - id should be renamed to ad_id
    - function features 
        - day of entry into simulation - will be assigned using day_of_entry_asignment function
        - interaction_rate which is initialy set to 0
        - is_active which is boolean info if the ad is active, false by default
- methods in Ad class:
    - update_interaction_rate - function that is called after each interaction with ad, it calculates the interaction rate using 
    ```interaction_rate = previous_interaction_rate + [(click + share + 2·like) - (2·dislike + ignore)]```, where every reaction value is 1 if it occured in last step, and 0 if it didn't
    and check if it is below ad_deactivation_threshold and should be deactivated, i.e. is_active set to false
    - to_massage_format - returns the descriptive features of ad in json-like string format that will be used in prompt

4. **Create the ads instances** - Instantiate ad objects with features and entry days
- Create ads using Ad class and these functions, add thema all to all_ads list 
- create a day_of_entry_asignment function - iteartes trough days_ads_can_enter days and randomly asign new_ads_per_day number of ads for each day in list, without repeating, then assign the rest to the 1st day of the list, the output is stored in the dict, whose keys are entering days and values the list of ad ids
- call that function and save it's output in state in ads_entering_schedule dict
4. **Create a function that determines which ads will be shown each day** - Implement ad scheduling logic in main program logic
- create a function schedule_for_day that:
    - checks if any ads are entering the simulation that day, sets their is_active to true
    - if the number of ads is greater than max_ads_shown_per_day number, randomly selects exactly that number ads whose is_active is true, if the number is smaller schedules every active ad

### Dependencies
- Ad Selection

### Input data
- `data/ads_features.csv` - ads features
- Simulation parameters (days, agents_count, etc.)

### Output
- `config/simulation_config.yaml` - Complete simulation configuration
- in `world/simulator.ipynb` - Ad class, Ad instances array, scheduling function
- Ad class definition in appropriate module
- Documentation

## Workflow, algorithms and procedures

## Issues and challenges
- setting the config pramethers so that the simulation has enough interactions, but not more than doable in this project
## Results and conclusions

## Notes
- exacly 10 ads each day is not natural, the number should vary from day to day, and also during the day