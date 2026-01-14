import marimo

__generated_with = "0.19.2"
app = marimo.App()


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell
def _():
    import json
    import random
    import pandas as pd
    import yaml
    import copy
    import numpy as np
    return copy, json, np, pd, random, yaml


@app.cell
def _(mo):
    mo.md(r"""
    # World Definition & Ad Creation
    """)
    return


@app.cell
def _(copy, yaml):
    # 01.1 Create world boundaries and specifications
    with open("context/simulation_config.yaml", "r") as f:
        config_str = f.read()

    _loaded_config = yaml.safe_load(config_str)

    config = copy.deepcopy(_loaded_config)
    return (config,)


@app.cell
def _(config):
    config
    return


@app.cell
def _(yaml):
    # 01.2 Load simulation state
    STATE_FILE = "context/simulation_state.yaml"

    def load_state():
        with open(STATE_FILE, "r") as f:
            return yaml.safe_load(f)

    def save_state(state):
        with open(STATE_FILE, "w") as f:
            yaml.safe_dump(state, f)

    state = load_state()
    return (state,)


@app.cell
def _(state):
    state
    return


@app.cell
def _(pd):
    # 01.3 Create ad templates
    ads_features_df = pd.read_csv("data/ads_features.csv")
    ads_features_df
    return (ads_features_df,)


@app.cell
def _(config, json):
    class Ad:
        def __init__(
            self,
            ad_id,
            group,
            emotion_label,
            message_type,
            visual_style,
            num_people,
            people_present,
            people_area_ratio,
            product_present,
            product_area_ratio,
            object_count,
            object_list,
            dominant_element,
            text_present,
            text_area_ratio,
            avg_font_size_proxy,
            dominant_colors,
            brightness_category,
            saturation_category,
            hue_category,
            visual_impact,
        ):
            self.ad_id = ad_id
            self.group = group
            self.emotion_label = emotion_label
            self.message_type = message_type
            self.visual_style = visual_style
            self.num_people = num_people
            self.people_present = people_present
            self.people_area_ratio = people_area_ratio
            self.product_present = product_present
            self.product_area_ratio = product_area_ratio
            self.object_count = object_count
            self.object_list = object_list
            self.dominant_element = dominant_element
            self.text_present = text_present
            self.text_area_ratio = text_area_ratio
            self.avg_font_size_proxy = avg_font_size_proxy
            self.dominant_colors = dominant_colors
            self.brightness_category = brightness_category
            self.saturation_category = saturation_category
            self.hue_category = hue_category
            self.visual_impact = visual_impact

            self.day_of_entry = None
            self.interaction_rate = 0
            self.is_active = False

        def update_interaction_rate(self, click, share, like, dislike, ignore):
            self.interaction_rate += (click + share + 2 * like) - (
                2 * dislike + ignore
            )
            if self.interaction_rate < config["ad_deactivation_threshold"]:
                self.is_active = False

        def to_message_format(self):
            return json.dumps(self.__dict__)
    return (Ad,)


@app.cell
def _(random):
    # 01.4 Create the ads instances
    def day_of_entry_assignment(all_ads, config):
        days_ads_can_enter = config["days_ads_can_enter"]
        new_ads_per_day = config["new_ads_per_day"]

        ad_ids = [ad.ad_id for ad in all_ads]
        random.shuffle(ad_ids)

        schedule = {day: [] for day in days_ads_can_enter}
        day_index = 0

        for ad_id in ad_ids:
            if day_index >= len(days_ads_can_enter):
                schedule[days_ads_can_enter[0]].append(ad_id)
                continue

            day = days_ads_can_enter[day_index]

            if len(schedule[day]) < new_ads_per_day:
                schedule[day].append(ad_id)
            else:
                day_index += 1
                if day_index < len(days_ads_can_enter):
                    next_day = days_ads_can_enter[day_index]
                    schedule[next_day].append(ad_id)
                else:
                    schedule[days_ads_can_enter[0]].append(ad_id)

        return schedule
    return (day_of_entry_assignment,)


@app.cell
def _(Ad, ads_features_df, config, day_of_entry_assignment):
    all_ads = []

    for _, row in ads_features_df.iterrows():
        ad = Ad(**row.to_dict())
        all_ads.append(ad)

    ads_entering_schedule = day_of_entry_assignment(all_ads, config)

    for ad in all_ads:
        for day, ad_ids in ads_entering_schedule.items():
            if ad.ad_id in ad_ids:
                ad.day_of_entry = day
                break

    print("len(all_ads)")
    print(len(all_ads))
    return (all_ads,)


@app.cell
def _(all_ads):
    all_ads[0].to_message_format()
    return


@app.cell
def _(config, random):
    def schedule_for_day(current_day, ads_entering_schedule, all_ads):
        if current_day in ads_entering_schedule:
            for ad_id in ads_entering_schedule[current_day]:
                for ad in all_ads:
                    if ad.ad_id == ad_id:
                        ad.is_active = True
                        ad.day_of_entry = current_day

        active_ads = [ad for ad in all_ads if ad.is_active]

        if len(active_ads) > config["max_ads_shown_per_day"]:
            return random.sample(active_ads, config["max_ads_shown_per_day"])

        return active_ads
    return


@app.cell
def _(mo):
    mo.md(r"""
    # Agent Template Creation
    """)
    return


@app.cell
def _(json, np):
    class User:
        def __init__(self, user_id, gender, age, profession, hobby, family):
            self.user_id = user_id
            self.gender = gender
            self.age = age
            self.profession = profession
            self.hobby = hobby
            self.family = family
            self.friend_list = []
            self.assign_propensity_features()
            self.emotional_state = {
                "acute_irritation": 0,
                "acute_interest": 0,
                "acute_arousal": 0,
                "bias_irritation": 0,
                "bias_trust": 0,
                "bias_fatigue": 0,
            }

        def assign_propensity_features(self):
            self.activity_level = np.random.normal(50, 15)
            self.risk_tolerance = np.random.normal(50, 15)
            self.social_engagement = np.random.normal(50, 15)

        def add_friend(self, user_id):
            self.friend_list.append(user_id)

        def to_message_format(self):
            return json.dumps(
                {
                    "user_id": self.user_id,
                    "gender": self.gender,
                    "age": self.age,
                    "profession": self.profession,
                    "hobby": self.hobby,
                    "family": self.family,
                    "activity_level": self.activity_level,
                    "risk_tolerance": self.risk_tolerance,
                    "social_engagement": self.social_engagement,
                    "emotional_state": self.emotional_state,
                }
            )
    return (User,)


@app.cell
def _(np):
    def calculate_similarity(user1, user2, users):
        age_similarity = np.exp(-abs(user1.age - user2.age) / 15)
        family_similarity = 1 if user1.family == user2.family else 0
        gender_similarity = 1 if user1.gender == user2.gender else 0

        hobbies1 = set(eval(user1.hobby))
        hobbies2 = set(eval(user2.hobby))
        hobby_similarity = len(hobbies1.intersection(hobbies2)) / len(hobbies1.union(hobbies2)) if len(hobbies1.union(hobbies2)) > 0 else 0

        professions1 = set(eval(user1.profession))
        professions2 = set(eval(user2.profession))
        profession_similarity = 1 if professions1 == professions2 else 0

        activity_similarity = 1 - abs(user1.activity_level - user2.activity_level) / 100
        risk_similarity = 1 - abs(user1.risk_tolerance - user2.risk_tolerance) / 100
        social_similarity = 1 - abs(user1.social_engagement - user2.social_engagement) / 100

        mutual_friends = len(set(user1.friend_list).intersection(set(user2.friend_list)))
        friend_of_friend = 0.1 * mutual_friends

        compatibility = (
            0.03 * age_similarity
            + 0.02 * family_similarity
            + 0.005 * gender_similarity
            + 0.08 * hobby_similarity
            + 0.04 * profession_similarity
            + 0.05 * activity_similarity
            + 0.04 * risk_similarity
            + 0.03 * social_similarity
            + 0.05 * friend_of_friend
        )

        return compatibility
    return (calculate_similarity,)


@app.cell
def _(calculate_similarity, np):
    def friendship_simulation(users, friendship_threshold):
        for i in range(len(users)):
            for j in range(i + 1, len(users)):
                user1 = users[i]
                user2 = users[j]

                compatibility = calculate_similarity(user1, user2, users)
                random_noise = np.random.uniform(0, 1)

                p_friendship = 0.7 * compatibility + 0.3 * random_noise

                if p_friendship > friendship_threshold:
                    user1.add_friend(user2.user_id)
                    user2.add_friend(user1.user_id)

    return (friendship_simulation,)


@app.cell
def _(User, config, friendship_simulation, pd):
    users_df = pd.read_csv("data/users_features.csv")
    all_users = [User(**row.to_dict()) for _, row in users_df.iterrows()]
    friendship_simulation(all_users, config["friendship_threshold"])
    return (all_users,)


@app.cell
def _(all_users):
    for u in all_users:
        print(u.friend_list)
        print(len(u.friend_list))
    return


@app.cell
def _():
    return


@app.cell
def _():
    return


@app.cell
def _():
    return


@app.cell
def _():
    return


@app.cell
def _():
    return


@app.cell
def _():
    return


@app.cell
def _():
    return


@app.cell
def _():
    return


@app.cell
def _():
    return


@app.cell
def _():
    return


@app.cell
def _():
    return


@app.cell
def _():
    return


@app.cell
def _():
    return


@app.cell
def _():
    return


@app.cell
def _():
    return


@app.cell
def _():
    return


@app.cell
def _():
    return


@app.cell
def _():
    return


@app.cell
def _():
    return


@app.cell
def _():
    return


@app.cell
def _():
    return


@app.cell
def _():
    return


@app.cell
def _():
    return


@app.cell
def _():
    return


@app.cell
def _():
    return


@app.cell
def _():
    return


@app.cell
def _():
    return


@app.cell
def _():
    return


@app.cell
def _():
    return


@app.cell
def _():
    return


@app.cell
def _():
    return


@app.cell
def _():
    return


@app.cell
def _():
    return


@app.cell
def _():
    return


@app.cell
def _():
    return


@app.cell
def _():
    return


@app.cell
def _():
    return


@app.cell
def _():
    return


@app.cell
def _():
    return


@app.cell
def _():
    return


@app.cell
def _():
    return


@app.cell
def _():
    return


@app.cell
def _():
    return


@app.cell
def _():
    return


@app.cell
def _():
    return


@app.cell
def _():
    return


@app.cell
def _():
    return


@app.cell
def _():
    return


@app.cell
def _():
    return


@app.cell
def _():
    return


@app.cell
def _():
    return


@app.cell
def _():
    return


@app.cell
def _():
    return


@app.cell
def _():
    return


@app.cell
def _():
    return


@app.cell
def _():
    return


@app.cell
def _():
    return


@app.cell
def _():
    return


@app.cell
def _():
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
