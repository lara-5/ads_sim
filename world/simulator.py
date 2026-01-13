import marimo

__generated_with = "0.19.2"
app = marimo.App()


@app.cell
def _():
    import json
    import random
    import pandas as pd
    import yaml
    import context.simulation_state as simulation_state
    return json, pd, random, yaml, simulation_state


@app.cell
def _(yaml):
    # 01.1 Create world boundaries and specifications
    with open("context/simulation_config.yaml", "r") as f:
        config_str = f.read()

    # YAML ne podržava list comprehension → evaluiramo ručno
    config_str = config_str.replace(
        "[for day in range(1, 86) if day % 5 != 0]",
        str([day for day in range(1, 86) if day % 5 != 0]),
    )

    config = yaml.safe_load(config_str)
    return (config,)


@app.cell
def _():
    # 01.2 State file
    import context.simulation_state as simulation_state
    state = simulation_state

    return state, simulation_state


@app.cell
def _(pd):
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
def _(config, random):
    def day_of_entry_assignment(all_ads):
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
                    schedule[days_ads_can_enter[day_index]].append(ad_id)

        return schedule

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
    return day_of_entry_assignment, schedule_for_day


@app.cell
def _(Ad, ads_features_df):
    all_ads = []

    for _, row in ads_features_df.iterrows():
        ad = Ad(**row.to_dict())
        all_ads.append(ad)

    len(all_ads)
    return (all_ads,)


@app.cell
def _(all_ads, day_of_entry_assignment):
    ads_entering_schedule = day_of_entry_assignment(all_ads)

    with open("world/simulation_state.py", "w") as f:
        f.write("current_simulation_day = 0\n")
        f.write(f"ads_entering_schedule = {ads_entering_schedule}\n")

    ads_entering_schedule
    return (ads_entering_schedule,)


@app.cell
def _(ads_entering_schedule, all_ads, mo, pd, schedule_for_day):
    current_day = mo.ui.slider(1, 85, value=1, label="Simulation day")

    scheduled_ads = schedule_for_day(current_day.value, ads_entering_schedule, all_ads)
    ads_df = pd.DataFrame([ad.__dict__ for ad in scheduled_ads])

    mo.vstack(
        [
            current_day,
            mo.ui.table(ads_df),
        ]
    )
    return


if __name__ == "__main__":
    app.run()
